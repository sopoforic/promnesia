import pytest

from promnesia.cannon import canonify, CanonifyException

param = pytest.mark.parametrize

@param('url,expected', [
    ('https://web.archive.org/web/20121011184646/http://www.well.com/~sjroby/lcars/1975.html',
     'well.com/~sjroby/lcars/1975.html'),
    ('https://web.archive.org/web/*/http://www.well.com/~sjroby/lcars/1975.html',
     'web.archive.org/web/%2A/http%3A//www.well.com/~sjroby/lcars/1975.html'),
])
def test_wayback(url, expected):
    assert canonify(url) == expected
