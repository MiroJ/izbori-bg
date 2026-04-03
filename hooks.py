FOOTER = """
## Допълнителни източници

- [Изборен Кодекс](https://dela.bg/Laws/%D0%98%D0%9A)
- [Документи на ЦИК](https://www.cik.bg/bg/documents/)
"""


def on_page_markdown(markdown, **kwargs):
    return markdown + "\n\n" + FOOTER
