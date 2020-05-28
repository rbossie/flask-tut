from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from trie.database import db

class Spelers(db.Model):
    __tablename__ = 'spelers'
    id = Column(Integer, primary_key=True)
    voornaam = Column(String(250), nullable=False)
    achternaam = Column(String(250), nullable=False)
    rugnummer = Column(Integer, nullable=False)


    def __init__(self, voornaam, achternaam, rugnummer):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.rugnummer = rugnummer