from .abs_locale import Locale, MainLocale, ModsLocale, TabLocale


mod_locale = ModsLocale(
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
)
tab_locale = TabLocale(home="메인", gen_mod="모드 생성", config="설정")
locale_map = Locale(
    tab=tab_locale,
    mods=mod_locale,
    main=main_locale,
    refresh="다시 불려오기",
    apply="적용",
    success="성공",
    failed="실패",
)
