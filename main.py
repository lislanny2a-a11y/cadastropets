from fastapi import FastAPI
from controllers import usuario_controller
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Usuários")
app.include_router(usuario_controller.router)
