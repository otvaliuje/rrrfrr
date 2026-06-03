import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
templates = Jinja2Templates(directory="templates")

mongo_uri = os.getenv("MONGO_BAGLANTISI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["anket_veritabani"]
koleksiyon = db["yanitlar"]

@app.get("/", response_class=HTMLResponse)
async def formu_goster(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/gonder")
async def veriyi_kaydet(
    ad: str = Form(...), 
    dogum_tarihi: str = Form(...), 
    hobiler: str = Form(...)
):
    yeni_kayit = {
        "ad": ad,
        "dogum_tarihi": dogum_tarihi,
        "hobiler": hobiler
    }
    koleksiyon.insert_one(yeni_kayit)
    return {"mesaj": "Harika! Anket başarıyla kaydedildi."}