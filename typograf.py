import re


NBSP = '\u00A0'

PATTERS = [
    (r"""(['"])(.*)(\1)""", r'«\2»', 'handle quotes'),
    (r'(—)', '-', 'hyphen to dash'),
    (r'( - )', ' — ', 'dash to hyphen when spaces are around'),
    (r'(\d+)[\s+|*?](\w+)', r'\1{}\2'.format(
        NBSP), 'join words with digit by nbsp'),
    (r'(\b[а-яА-Яa-zA-Z]{1,2}\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)',
     r'\1{0}\3'.format(NBSP), 'link word with no break space'),
    (r'\r\n', r'\n', 'remove win-like newlines'),
    (r'(\d+)-(\d+)-(\d+)-(\d+)-(\d+)',
     r'\1–\2–\3–\4–\5', 'ndash in phone number'),
    (r'\n{2,}', r'\n', 'replace extra newlines'),
    (r'\t', r' ', 'remove tabs'),
    (r'[ ]{2,}', r' ', 'remove extra spaces')
]


def typografy_text(text):
    for patter, replacement, _ in PATTERS:
        text = re.sub(patter, replacement, text)
        return text
000