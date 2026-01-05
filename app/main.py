from fastapi import FastAPI
from . import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="CRUD API Project")

app.include_router(routes.router)
