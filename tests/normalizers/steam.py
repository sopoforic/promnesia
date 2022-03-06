import pytest

from promnesia.cannon import canonify, CanonifyException

param = pytest.mark.parametrize

@param('url,expected', [
    ('https://store.steampowered.com/app/546560/HalfLife_Alyx?snr=1_7_15__13',
     'store.steampowered.com/app/546560'),
])
def test_steam_store(url, expected):
    assert canonify(url) == expected
