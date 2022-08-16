from .endpoints import rtsp, stream, video


def set_routers_v1(app):
    app.include_router(rtsp.router)
    app.include_router(stream.router)
    app.include_router(video.router)
