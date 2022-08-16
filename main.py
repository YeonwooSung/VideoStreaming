from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_router_controller import Controller, ControllersTags

from .v1 import set_routers_v1


app = FastAPI(title='VideoStreaming',
    description='This is a very fancy project, with auto docs for the API and everything',
    version='0.0.1',
    docs_url=True, #TODO: add docs_url to config
    openapi_tags=ControllersTags)
app.mount("/public", StaticFiles(directory="public"), name="public")
templates = Jinja2Templates(directory="views")

#-------------------------------------------------------------
# Set up API routers
set_routers_v1(app)
#-------------------------------------------------------------
# Set up CORS
origins = ["*"]
app.add_middleware(
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
)
#-------------------------------------------------------------


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html")


@app.get("/display")
async def get_display_page(reqest: Request):
    return templates.TemplateResponse("video.html")


def run_app(run_on_localhost : bool = False, port : int = 8000, access_log : bool = False):
    import uvicorn
    if run_on_localhost:
        uvicorn.run(app, host="localhost", port=port, access_log=access_log)
    else:
        uvicorn.run(app, host="0.0.0.0", port=port, access_log=access_log)
