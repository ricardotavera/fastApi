from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Delivery(BaseModel):
    receiverName: str
    phone: str
    country: str
    city: str
    zipcode: int
    destinyAddress: str
    weightKG: Optional[int] = None





#Creating api called app
app = FastAPI()

#creating list of orders

# WELCOME
@app.get("/")
async def home():
        return { "Welcome": "Delivery API" }


# GET   
#Get all
@app.get("/delivery")
async def getDeliveries():
        return orders

# Get delivery by ID
@app.get("/delivery/{id}")
async def getDelivery(id: int):
    if id not in orders:
        return {"Error_Message": f"Delivery with id {id} does not exit"}
    return orders[id]


# POST        
# Create new order
@app.post("/delivery/{id}")
async def newDelivery(id: int, delivery: Delivery):
    if id in orders:
        return {"Error_Message": f"Delivery with id {id} is alredy registered"}
    
    elif id <= 0:
        return {"Error_Message": f"Delivery id should be greater than 0"}

    orders[id] = {"receiverName": delivery.receiverName,
                  "phone": delivery.phone,
                  "country": delivery.country,
                  "city":delivery.city,
                  "zipcode": delivery.zipcode,
                  "destinyAddress": delivery.destinyAddress,
                  "weightKG": delivery.weightKG
                   }
    return {"message": "Delivery created successfully", "delivery": orders[id]}


#PUT
@app.put("/delivery/{id}")
async def updateDelivery(id: int, delivery: Delivery):
    if id not in orders:
        return {"Error_Message": f"Delivery with id {id} does not exit"}
    orders[id] = {"receiverName": delivery.receiverName,
                  "phone": delivery.phone,
                  "country": delivery.country,
                  "city":delivery.city,
                  "zipcode": delivery.zipcode,
                  "destinyAddress": delivery.destinyAddress,
                  "weightKG": delivery.weightKG
                   }
    return {"message": "Delivery updated successfully", "delivery": orders[id]}


# DELETE
@app.delete('/delivery/{id}')
async def deleteDelivery(id: int):
    if id not in orders:
        return {"Error_Message": f"Delivery with id {id} does not exit"}
    
    delivery = orders[id]
    del orders[id]
    return {"message": f"Delivery removed successfully", "delivery": delivery}



# DATA
orders = { 
    1: {
        "receiverName": "Mark Dowell",
        "phone": 3232421212,
        "country": "Colombia",
        "city": "Bucaramga",
        "zipcode": 1000001,
        "destinyAddress": "Cra 27 #9",
        "weightKG": 2
    },
    2: {
        "receiverName": "Daniel Balmer",
        "phone": 354838823,
        "country": "Colombia",
        "city": "Medellín",
        "zipcode": 100011,
        "destinyAddress": "Calle 49 #32-25",
        "weightKG": 7
    },
    3: {
        "receiverName": "Tom Walker",
        "phone": 3218326237,
        "country": "UK",
        "city": "London",
        "zipcode": 103001,
        "destinyAddress": "White Collar Factory Old Street, London EC2M, Old St",
        "weightKG": 4
    },
    4: {
        "receiverName": "Juana Pedraza",
        "phone": 343223231,
        "country": "Spain",
        "city": "Madrd",
        "zipcode": 28001,
        "destinyAddress": "Calle de Goya, 41",
        "weightKG": 2
    },
    5: {
        "receiverName": "Andrea Lincon",
        "phone": 61222212,
        "country": "US",
        "city": "Seattle",
        "zipcode": 98101,
        "destinyAddress": "440 Terry Ave N",
        "weightKG": 5
    }

}