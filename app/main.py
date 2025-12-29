from fastapi import FastAPI

from app.db.session import init_db
from app.api.users import router as users_router
from app.api.auth.login import router as auth_router
from app.api.tasks import router as tasks_router


app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "API funcionando"}
