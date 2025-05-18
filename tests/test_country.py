from pythonuef_github_lib_template import get_by_alpha2, get_by_name

def test_get_by_alpha2():
    cz = get_by_alpha2("CZ")
    assert cz is not None
    assert cz.name == "Czechia"
    assert cz.emoji == "🇨🇿"

def test_get_by_name():
    cz = get_by_name("Czechia")
    assert cz is not None
    assert cz.alpha2 == "CZ"
