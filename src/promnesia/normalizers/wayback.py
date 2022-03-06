import re

from promnesia.cannon import CanonifyException
from .Site import Site


class WaybackURL(Site):
    URL_RE = r'(?:https?://)?web.archive.org/web/(?P<timestamp>\d+)/(?P<rest>.*)'

    @classmethod
    def supports(cls, url):
        return re.fullmatch(cls.URL_RE, url)

    @classmethod
    def canonify(cls, url):
        m = re.fullmatch(cls.URL_RE, url)
        if not m:
            raise CanonifyException('Unsupported URL: {!r}'.format(url))
        return Site.canonify(m.group('rest'))
