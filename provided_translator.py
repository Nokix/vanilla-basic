import doctest

"""Pokemonnamen von 10 Pokemon.
Der Key ist der Englische Name, der Value ist eine Liste von Namen in den Sprachen:
de - German
en - English
fr - French
ja - Japanese
"""
pokemonnames = {
    'Bulbasaur': ['Bisasam', 'Bulbasaur', 'Bulbizarre', 'フシギダネ'],
    'Ivysaur': ['Bisaknosp', 'Ivysaur', 'Herbizarre', 'フシギソウ'],
    'Venusaur': ['Bisaflor', 'Venusaur', 'Florizarre', 'フシギバナ'],
    'Charmander': ['Glumanda', 'Charmander', 'Salamèche', 'ヒトカゲ'],
    'Charmeleon': ['Glutexo', 'Charmeleon', 'Reptincel', 'リザード'],
    'Charizard': ['Glurak', 'Charizard', 'Dracaufeu', 'リザードン'],
    'Squirtle': ['Schiggy', 'Squirtle', 'Carapuce', 'ゼニガメ'],
    'Wartortle': ['Schillok', 'Wartortle', 'Carabaffe', 'カメール'],
    'Blastoise': ['Turtok', 'Blastoise', 'Tortank', 'カメックス'],
    'Pikachu': ['Pikachu', 'Pikachu', 'Pikachu', 'ピカチュウ']
}


def translate_to_eng(name: str):
    """Erwartet den Namen eines Pokemons in einer beliebigen Sprache und
    gibt den Namen auf Englisch zurück.

    Wenn kein passendes pokemon gefunden wurde, so wird None zurückgegben.

    >>> translate_to_eng("Bisasam")
    'Bulbasaur'

    >>> translate_to_eng("Viktor")

    """
    name = name.lower()
    for eng_name, all_names in pokemonnames.items():
        if name in [n.lower() for n in all_names]:
            return eng_name

    return None


if __name__ == '__main__':
    doctest.testmod()
