from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import address_book.crud as crud
import address_book.models as models
import address_book.schemas as schemas
import address_book.database as database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(database.get_db)):
    return crud.create_address(db=db, address=address)

@app.get("/addresses/", response_model=list[schemas.Address])
def read_addresses(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_addresses(db=db, skip=skip, limit=limit)

@app.delete("/addresses/{address_id}", response_model=schemas.Address)
def delete_address(address_id: int, db: Session = Depends(database.get_db)):
    db_address = crud.get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return crud.delete_address(db=db, address_id=address_id)
