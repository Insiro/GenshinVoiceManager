from .abs_locale import *


genmod_locale = GenModsLocale(
    source_select="적용할 모드 소스",
    mod_base="베이스 모드",
    input_mod_name="새 모드 이름",
    gen_success="모드 생성 성공",
    pack_failed="모드 생성 실패",
    pack="모드 생성",
    packing="생성중",
    preparing="준비중",
)

main_locale = MainLocale(
    restore="복구",
    select_mod="--모드 선택--",
    backup_fail="원본언어가 옮겨졌거나 존재하지 않습니다",
    apply_mod="모드 적용",
    link="symlink 방식",
    move="이동 방식",
    backup="백업",
    original="원본",
    removed="원본을 찾을수 없음",
    activated="활성화 됨",
    no_backup="백업 해제 됨",
)
tab_locale = TabLocale(home="메인", gen_mod="모드 생성", config="설정", mod="모드 관리")

alert_locale = AlertLocale(
    responbility="본 소프트웨어를 사용함에 있어 생기는 문제에 대해 책임은 전적으로 사용자에게 있습니다",
    hide="다시 열지 않기",
    argree="동의",
    cancel="닫기",
    path="경로",
    cannotFindVoice="원신 음성 폴더를 찾을 수 없습니다.",
)
setting_locale = SettingLocale(
    locale="Locale",
    voice="음성",
    path="경로설정",
    genshin="GenshinImpact.exe 폴더",
    source="모드 소스",
    resouece="Resourcaes",
    temp="Temp",
    backup="Backup",
)
mod_locale = ModLocale(delete="삭제")


locale_map = Locale(
    mod=mod_locale,
    setting=setting_locale,
    alert=alert_locale,
    tab=tab_locale,
    genmods=genmod_locale,
    main=main_locale,
    refresh="다시 불러오기",
    apply="적용",
    success="성공",
    failed="실패",
    wrong="오류",
    selected="선택한",
    save="저장",
    item="항목",
    notselected="선택안됨",
)
