from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .api import users


app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")
templates = Jinja2Templates(directory="views")

#-------------------------------------------------------------
# Include routers
app.include_router(users.router)
#-------------------------------------------------------------


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("item.html")

@app.get("/")
async def root():
    return {"message": "Hello World"}
