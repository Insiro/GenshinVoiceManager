from typing import TypedDict


class TabLocale(TypedDict):
    home: str
    gen_mod: str
    config: str


class ModsLocale(TypedDict):
    source_select: str
    mod_base: str
    input_mod_name: str
    gen_success: str
    pack_failed: str
    pack: str
    packing: str
    preparing: str


class AlertLocale(TypedDict):
    responbility: str
    hide: str
    argree: str
    cancel: str


class SettingLocale(TypedDict):
    locale: str
    voice: str
    path: str
    genshin: str
    source: str
    resouece: str
    temp: str
    backup: str


class MainLocale(TypedDict):
    restore: str
    select_mod: str
    backup_fail: str
    apply_mod: str
    link: str
    move: str
    backup: str
    removed: str
    activated: str
    no_backup: str
    original: str


class Locale(TypedDict):
    tab: TabLocale
    mods: ModsLocale
    main: MainLocale
    alert: AlertLocale
    setting: SettingLocale
    apply: str
    refresh: str
    success: str
    failed: str
