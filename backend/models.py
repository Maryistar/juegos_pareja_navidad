from sqlalchemy import Column, Integer, String
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    real_name = Column(String, unique=True)      # ❗ no se repite
    assigned_name = Column(String, unique=True)  # ❗ no se repite
