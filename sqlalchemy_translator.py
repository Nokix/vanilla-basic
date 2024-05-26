from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import func

# Erstelle eine SQLite-Datenbankverbindung zur neuen Datenbank
engine = create_engine('sqlite:///pokemon.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    english_name = Column(String)
    translation = Column(String)
    language = Column(String)


def translate_to_eng(name):
    """
    Gibt den englischen Namen eines Pokémon zurück, basierend auf einem beliebigen Namen in einer unterstützten Sprache.

    Args:
        name (str): Der Name des Pokémon in einer beliebigen unterstützten Sprache.

    Returns:
        str: Der englische Name des Pokémon, wenn gefunden, sonst None.

    Examples:
        >>> translate_to_eng('フシギダネ')
        'Bulbasaur'
        >>> translate_to_eng('Bisasam')
        'Bulbasaur'
        >>> translate_to_eng('Bulbizarre')
        'Bulbasaur'
    """
    session = Session()
    name = name.lower()
    result = session.query(Pokemon.english_name).filter(
        Pokemon.translation == name
    ).first()

    session.close()

    return result.english_name if result else None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
