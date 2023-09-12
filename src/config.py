from os import path
import json

output_path = "../temp/output_pck/"
original_path = ""
# D:\Game\Genshin Impact game\GenshinImpact_Data\StreamingAssets\AudioAssets\Korean


class Config:
    temp_path: str
    resource_path: str
    genshin_path: str  # Path to Genshin Path, audio path will replaced as Symbolic Link
    mods_path: str  # path to Origianl Mod Source Files Saved
    language: str

    @staticmethod
    def __assign(
        temp_path: str,
        resource_path: str,
        genshin_path: str,
        mods_path: str,
        language: str,
    ):
        config = Config()
        config.temp_path = temp_path
        config.resource_path = resource_path
        config.genshin_path = genshin_path
        config.mods_path = mods_path
        config.language = language
        return config

    @property
    def wem_path(self) -> str:
        return path.join(self.temp_path, "wem")

    @property
    def output_pck_path(self) -> str:
        return path.join(self.temp_path, "output_pck")

    @property
    def backup_path(self) -> str:  # Path to Original Sound Backup Directory
        return path.join(self.resource_path, "backup")

    @property
    def applied_mods_path(self) -> str:  # Path to Mod Applied Path
        return path.join(self.resource_path, "applied")

    @property
    def sym_path(self) -> str:
        sym = path.join(
            self.genshin_path,
            "GenshinImpact_Data\\StreamingAssets\\AudioAssets",
            self.language,
        )
        return sym

    @staticmethod
    def load():
        if path.isfile("config.json"):
            with open("config.json", "r") as fp:
                return Config.__assign(**json.load(fp))
        return Config.__assign(
            temp_path="..\\temp",
            mods_path=".\\resources\\mods",
            resource_path=".\\resources",
            genshin_path="C:\\Program Files\\Genshin Impact\\Genshin Impact game",
            language="Korean",
        )

    def save(self):
        with open("config.json", "w") as fp:
            print(json.dump(self.__dict__, fp, indent=2))