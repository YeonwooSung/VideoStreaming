from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .api import rtsp, video, nlp


app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")
templates = Jinja2Templates(directory="views")

#-------------------------------------------------------------
# Include routers
api_list = [rtsp, video, nlp]
for api in api_list:
    app.include_router(api.router)
#-------------------------------------------------------------


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("item.html")

@app.get("/")
async def root():
    return {"message": "Hello World"}


def run_app(run_on_localhost : bool = False, port : int = 8000, access_log : bool = False):
    import uvicorn
    if run_on_localhost:
        uvicorn.run(app, host="localhost", port=port, access_log=access_log)
    else:
        uvicorn.run(app, host="0.0.0.0", port=port, access_log=access_log)
