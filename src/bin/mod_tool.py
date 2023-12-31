import os
from os import path
from shutil import move, rmtree
from logging import Logger

from ..repack.repack import repack
from ..utils.dir import check_mkdirs, clear_dir, copy_contents, link_contents
from ..utils.error import NotValidPathException
from .config import Config


class ModTool:
    input_path: str
    input_changed = False

    @property
    def logger(self):
        return self.__logger

    def __init__(self, config: Config, logger: Logger) -> None:
        self.config = config
        self.__logger = logger
        check_mkdirs(config.temp_path)
        check_mkdirs(config.resource_path)
        check_mkdirs(config.mod_sources_path)
        check_mkdirs(config.backup_path)
        check_mkdirs(config.packed_mods_path)

        self.reset_input_path()
        pass

    # Step 1 : backup
    def move_and_link_original(self):
        if not path.isdir(self.config.sym_path):
            raise NotValidPathException("selected language is Not installed")
        lang_backup = path.join(self.config.backup_path, self.config.voice_lang)
        if path.exists(lang_backup):
            rmtree(lang_backup)

        self.logger.info(f"backup sound files, lang : {self.config.voice_lang}")
        move(self.config.sym_path, self.config.backup_path)
        os.symlink(lang_backup, self.config.sym_path, True)

    # region Step 2 : mod source insert
    def reset_input_path(self):
        self.input_changed = False
        self.input_path = path.join(self.config.backup_path, self.config.voice_lang)

    def set_input_path(self, input_path: str):
        self.input_changed = True
        self.input_path = input_path

    def clear_mod_source(self):
        self.logger.info(f"clear inputs")
        rmtree(self.config.wem_path)

    def prepare_mod_source(self, source_path: str):
        link_contents(
            source_path,
            self.config.wem_path,
            "preparing mod files",
            lambda file: file.endswith("wem"),
        )

    # endregion

    # Step 3 : generate mod files

    def pack_mod_files(self, mod_path: str):
        clear_dir(mod_path)
        self.logger.info(f"packing mod file {mod_path}")
        repack(self.config.wem_path, self.input_path, mod_path, self.logger)
        self.logger.info("save packed mod file")

    # Step 4 : Apply Mod
    def apply(self, mod_path: str):
        self.logger.info(f"apply mod {mod_path}")

        lang_backup_path = path.join(self.config.backup_path, self.config.voice_lang)
        if self.input_changed:
            copy_contents(
                lang_backup_path,
                mod_path,
                "copying missing files",
                lambda file: file.startswith("External")
                and not path.exists(path.join(mod_path, file)),
            )

        link_contents(
            lang_backup_path,
            mod_path,
            "linking other files",
            lambda file: not path.exists(path.join(mod_path, file)),
        )
        if path.islink(self.config.sym_path):
            os.unlink(self.config.sym_path)
        os.symlink(path.abspath(mod_path), self.config.sym_path)

    def restore(self, link=True):
        os.unlink(self.config.sym_path)
        origin = path.abspath(
            path.join(self.config.backup_path, self.config.voice_lang)
        )
        sym = self.config.sym_path

        if link:
            os.symlink(origin, sym)
        else:
            move(origin, sym)
