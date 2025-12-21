from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import Base, engine, SessionLocal
from models import Player
import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

class PlayerRequest(BaseModel):
    real_name: str

AVAILABLE_NAMES = [
    "katherine", "aledanis", "yennis", "zharick", "maryis",
    "keithlyn", "gregoris", "maycol", "gerald", "brayan", "jorge"
]

@app.post("/jugar")
def jugar(data: PlayerRequest):
    db = SessionLocal()
    nombre = data.real_name.strip().lower()

    # 1️⃣ Verificar si ya jugó
    if db.query(Player).filter(Player.real_name == nombre).first():
        raise HTTPException(
            status_code=400,
            detail="Ya jugaste, no puedes volver a participar"
        )

    # 2️⃣ Obtener nombres ya usados
    usados = [p.assigned_name for p in db.query(Player).all()]
    disponibles = list(set(AVAILABLE_NAMES) - set(usados))

    # 3️⃣ Verificar si quedan nombres
    if not disponibles:
        raise HTTPException(
            status_code=400,
            detail="Ya no hay nombres disponibles"
        )

    # 4️⃣ Asignar nombre
    asignado = random.choice(disponibles)

    jugador = Player(
        real_name=nombre,
        assigned_name=asignado
    )

    db.add(jugador)
    db.commit()

    return {
        "tu_nombre": data.real_name,
        "pareja": asignado
    }
