from pygments.formatters import HtmlFormatter
from markdown.extensions.codehilite import CodeHiliteExtension


class CustomHtmlFormatter(HtmlFormatter):
    def __init__(self, lang_str='', **options):
        super().__init__(**options)
        # lang_str has the value {lang_prefix}{lang}
        # specified by the CodeHilite's options
        self.lang_str = lang_str

    def _wrap_code(self, source):
        yield 0, f'<code class="{self.lang_str}">'
        yield from source
        yield 0, '</code>'


md_extension_configs = {
    'extra': {
        'footnotes': {
            'UNIQUE_IDS': True
        },
        'fenced_code': {
            'lang_prefix': 'lang-'
        }
    },
    'toc': {
        'permalink': True
    }
}

md_extensions = ['extra', 'toc',
                 CodeHiliteExtension(pygments_formatter=CustomHtmlFormatter)]
