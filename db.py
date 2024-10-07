# db.py (Database configuration) ##
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://username:password@localhost/simdb" ##enter your local host link here

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model ##
class SimCard(Base):
    __tablename__ = 'sim_cards'
    
    sim_number = Column(String, primary_key=True, index=True)
    phone_number = Column(String)
    status = Column(String, default='inactive')
    activation_date = Column(DateTime, nullable=True)

Base.metadata.create_all(bind=engine)
