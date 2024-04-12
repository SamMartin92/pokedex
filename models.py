import requests
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

association_table = Table(
    'association', Base.metadata,
    Column('trainer_id', Integer, ForeignKey('trainers.id')),
    Column('pokemon_id', Integer, ForeignKey('pokemons.id'))
)

class Trainer(Base):
    __tablename__ = "trainers"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    pokemon = relationship('Pokemon', secondary=association_table, back_populates='trainers')

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Trainer Name: {self.name}"


class Pokemon(Base):
    __tablename__= "pokemons"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, unique=True)
    description1 = Column("description1", Text)
    description2 = Column("description2", Text)
    height = Column("height", Integer)
    weight = Column("weight", Integer)
    type1 = Column("type1", String)
    type2 = Column("type2", String)
    trainers= relationship('Trainer', secondary=association_table, back_populates='pokemons')

    def __init__(self, id, name, description1, description2,  height, weight, type1, type2):
        self.id = id
        self.name = name
        self.description1 = description1
        self.description2 = description2
        self.height = height
        self.weight = weight
        self.type1 = type1
        self.type2 = type2

    def __repr__(self):
        return f"{self.id}: {self.name}"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# add all pokemon to db
# for i in range(1,152):
#     species_response = requests.get(
#             f"https://pokeapi.co/api/v2/pokemon-species/{i}/")
#     pokemon_species_api_response = species_response.json()
#     response = requests.get(
#             f"https://pokeapi.co/api/v2/pokemon/{i}/")
#     pokemon_api_response = response.json()
#     name = pokemon_api_response["name"]
#     description = pokemon_species_api_response["flavor_text_entries"]
#     description1 = f"{description[1]['flavor_text'].replace('↑', ' ')}"
#     if description[1]['flavor_text'] == description[2]['flavor_text']:
#         description2 = f"{description[5]['flavor_text'].replace('↑', ' ')}"
#     else:
#         description2 = f"{description[2]['flavor_text'].replace('↑', ' ')}"
#     height = pokemon_api_response["height"]
#     weight = pokemon_api_response["weight"]
#     pokemon_types = pokemon_api_response['types']
#     type1 = pokemon_types[0]['type']['name']
#     if len(pokemon_types) > 1:
#         type2 = pokemon_types[1]['type']['name']

#     pokemon = Pokemon(id=i, name=name, description1=description1, description2=description2, height=height, weight=weight, type1=type1, type2=type2)
#     session.add(pokemon)

    

# session.commit()
session.close()
