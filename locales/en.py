from .abs_locale import *


genmod_locale = GenModsLocale(
    source_select="Select Mod Source",
    mod_base="Mod Base",
    input_mod_name="New Mod Name",
    gen_success="successfully Generated",
    pack_failed="Faild To Packing mod",
    pack="Pack Mod",
    packing="packing",
    preparing="preparing",
)

main_locale = MainLocale(
    restore="Restore",
    select_mod="--Select Mod--",
    backup_fail="Voice Not Installed or Already Backuped",
    apply_mod="Apply Mod",
    link="symlink mod",
    move="move mod",
    backup="Backup",
    original="Original",
    removed="Original Removed",
    activated="Activated",
    no_backup="Backup Disabled",
)

alert_locale = AlertLocale(
    responbility="You are solely responsible for any problems that arise while using this software.",
    hide="Do Not Open More",
    argree="Agree",
    cancel="Cancel",
    path="Path",
    cannotFindVoice="Cannot Find Voice Folder",
)
setting_locale = SettingLocale(
    locale="Locale",
    voice="Voice",
    path="Path",
    genshin="Genshin Game",
    source="Mod Sources",
    resouece="Resourcaes",
    temp="Temp",
    backup="Backup",
)
tab_locale = TabLocale(
    home="home", gen_mod="Mod Generate", config="config", mod="Mod Manage"
)
mod_locale = ModLocale(delete="Delete")
locale_map = Locale(
    mod=mod_locale,
    tab=tab_locale,
    alert=alert_locale,
    setting=setting_locale,
    genmods=genmod_locale,
    main=main_locale,
    refresh="Refresh",
    apply="Apply",
    success="Success",
    failed="Failed",
    wrong="Wrong",
    selected="Selected",
    save="Save",
    notselected="Not Selected",
    item="Item",
)
