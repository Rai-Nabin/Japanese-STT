def validate_label(label):
    punctuations = [
        "。",
        "、",
        "・",
        ".",
        '"',
        "?",
        "!",
        ";",
        ":",
        "-",
        "{",
        "}",
        "[",
        "]",
        "(",
        ")",
        "゠",
        "＝",
        "！",
        "「",
        "」",
        "【",
        "】",
        "『",
        "』",
        "⟨",
        "⟩",
        "“",
        "…",
        "‘",
        "‥",
        "〝",
        "〝",
        "〜",
        "♪",
        "?",
        "〇",
        "〆",
        "ー",
        "゛",
        "゜",
        "・",
        "々",
        "ヽ",
        "ヾ",
        "ゝ",
        "ゞ",
        "〃",
        "〽",
        "﹅",
        "〻",
        "〵",
        "〴",
        "？",
        "&",
        ",",
        "/",
        "–",
        "—",
        "―",
        "｢",
        "｣",
        "･",
    ]

    for punct in punctuations:
        label = label.replace(punct, "")
    label = label.replace("'", "")
    label = label.lower()

    return label if label else None