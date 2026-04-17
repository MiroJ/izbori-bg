import re

FOOTER = """
## Допълнителни източници

- [Изборен Кодекс](https://dela.bg/Laws/%D0%98%D0%9A)
- [Документи на ЦИК](https://www.cik.bg/bg/documents/)
- [Проверка на протоколи в Excel](https://github.com/MiroJ/izbori-bg/raw/master/docs/Протокол%20-%20Проверка.xlsx?download=1)
"""


def on_page_markdown(markdown, **kwargs):
    return markdown + "\n\n" + FOOTER


def on_page_content(html, **kwargs):
    """Inject an inline counter-reset on every <ol start="N"> so the CSS
    counter used by Material for MkDocs starts at the correct number."""
    def fix_ol_start(m):
        start = int(m.group(1))
        return f'<ol start="{start}" style="counter-reset: list-item {start - 1};">'

    return re.sub(r'<ol start="(\d+)">', fix_ol_start, html)
