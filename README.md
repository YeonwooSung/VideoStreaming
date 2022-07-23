# Video Streaming

## Environment

Virtualenv has been used for configuring the environment.

```bash
# generate venv
$ python3 -m venv venv

# activate venv
$ source venv/bin/activate
```

For running the app, you could use either uvicorn or hypercorn. For testing and development, uvicorn was mainly used.

```bash
$ uvicorn app.main:app --reload
```

## Documents

By entering "http://localhost:8000/docs", you would be able to see the auto generated documents.

For alternative, you could look up "http://localhost:8000/redoc".
