from fastapi import APIRouter, status
from fastapi.responses import StreamingResponse
from imutils.video import VideoStream

import threading
import imutils
import time
import cv2
import uvicorn
from multiprocessing import Process, Queue
import subprocess
import numpy as np


lock = threading.Lock()
router = APIRouter()
manager = None
count_keep_alive = 0
url_rtsp = 'rtsp://localhost:8123/ds-test'


def start_stream(url_rtsp, manager, width : int = 1280, height : int = 720):
    vs = VideoStream(url_rtsp).start()
    while True:
        time.sleep(0.2)

        frame = vs.read()
        frame = imutils.resize(frame, width=680)
        output_frame = frame.copy()

        if output_frame is None:
            continue
        (flag, encodedImage) = cv2.imencode(".jpg", output_frame)
        if not flag:
            continue
        manager.put(encodedImage)


def streamer():
    try:
        while manager:
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                   bytearray(manager.get()) + b'\r\n')
    except GeneratorExit:
        print("cancelled")


def manager_keep_alive(p):
    global count_keep_alive
    global manager
    while count_keep_alive:
        time.sleep(1)
        print(count_keep_alive)
        count_keep_alive -= 1
    p.kill()
    time.sleep(.5)
    p.close()
    manager.close()
    manager = None


@router.get("/rtsp")
async def video_feed():
    return StreamingResponse(streamer(), media_type="multipart/x-mixed-replace;boundary=frame")

@router.get("/rtsp/stream")
async def stream():
    global manager
    global count_keep_alive
    if manager is None:
        manager = Queue(maxsize=1)
        p = Process(target=start_stream, args=(url_rtsp, manager))
        p.start()
        count_keep_alive += 1
        p.join()
        count_keep_alive -= 1
        p.terminate()
        p.join()
        p.close()
        manager.close()
        manager = None
    return StreamingResponse(streamer(), status_code=status.HTTP_200_OK)
