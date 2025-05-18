from dataclasses import dataclass

@dataclass(frozen=True)
class Country:
    alpha2: str
    name: str
    emoji: str

COUNTRIES = [
    Country("AF", "Afghanistan", "🇦🇫"),
    Country("AL", "Albania", "🇦🇱"),
    Country("DZ", "Algeria", "🇩🇿"),
    Country("AS", "American Samoa", "🇦🇸"),
    Country("AD", "Andorra", "🇦🇩"),
    Country("CZ", "Czechia", "🇨🇿"),
    # ... sem přidáš všechny ostatní státy dle tvého Go balíčku
]

_COUNTRIES_BY_ALPHA2 = {c.alpha2: c for c in COUNTRIES}
_COUNTRIES_BY_NAME = {c.name.lower(): c for c in COUNTRIES}

def get_by_alpha2(code: str) -> Country | None:
    return _COUNTRIES_BY_ALPHA2.get(code.upper())

def get_by_name(name: str) -> Country | None:
    return _COUNTRIES_BY_NAME.get(name.lower())
