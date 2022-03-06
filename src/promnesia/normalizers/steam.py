import re

from promnesia.cannon import CanonifyException
from .Site import Site


class SteamStore(Site):
    URL_RE = r'(?:https?://)?store\.steampowered\.com/app/(\d+)(?:/.*)?'

    @classmethod
    def supports(cls, url):
        return re.match(cls.URL_RE, url)

    @classmethod
    def canonify(cls, url):
        m = re.match(cls.URL_RE, url)
        if not m:
            raise CanonifyException('Unsupported URL: {!r}'.format(url))
        return 'store.steampowered.com/app/{}'.format(m.group(1))
