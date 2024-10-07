# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from db import SimCard, SessionLocal

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Activate SIM card
@app.post("/activate")
def activate_sim(sim_number: str, db: Session = Depends(get_db)):
    sim_card = db.query(SimCard).filter(SimCard.sim_number == sim_number).first()
    
    if sim_card is None:
        raise HTTPException(status_code=404, detail="SIM card not found")
    
    if sim_card.status == 'active':
        raise HTTPException(status_code=400, detail="SIM card is already active")
    
    sim_card.status = 'active'
    sim_card.activation_date = datetime.now()
    db.commit()
    db.refresh(sim_card)
    
    return {"message": "SIM card activated successfully", "sim_details": sim_card}

# Deactivate SIM card
@app.post("/deactivate")
def deactivate_sim(sim_number: str, db: Session = Depends(get_db)):
    sim_card = db.query(SimCard).filter(SimCard.sim_number == sim_number).first()
    
    if sim_card is None:
        raise HTTPException(status_code=404, detail="SIM card not found")
    
    if sim_card.status == 'inactive':
        raise HTTPException(status_code=400, detail="SIM card is already inactive")
    
    sim_card.status = 'inactive'
    sim_card.activation_date = None
    db.commit()
    db.refresh(sim_card)
    
    return {"message": "SIM card deactivated successfully", "sim_details": sim_card}

# Get SIM details
@app.get("/sim-details/{sim_number}")
def get_sim_details(sim_number: str, db: Session = Depends(get_db)):
    sim_card = db.query(SimCard).filter(SimCard.sim_number == sim_number).first()
    
    if sim_card is None:
        raise HTTPException(status_code=404, detail="SIM card not found")
    
    return sim_card
