# Video Streaming

A simple web application server that provides the video streaming and video delivering services.

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

### Auto-generated Documents

By entering "http://localhost:8000/docs", you would be able to see the auto generated documents.

For alternative, you could look up "http://localhost:8000/redoc".

Also, FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs. A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description. In this case, OpenAPI is a specification that dictates how to define a schema of your API. This schema definition includes your API paths, the possible parameters they take, etc. The term "schema" might also refer to the shape of some data, like a JSON content. In that case, it would mean the JSON attributes, and data types they have, etc. OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using JSON Schema, the standard for JSON data schemas. If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API. You can see it directly at [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json).

## Functionality

- [ ] Real-time streaming
    * [x] RTSP
    * [ ] DASH
    * [ ] HLS
- [x] Video downloading (only support MP4)
- [ ] Video search (using NLP)
- [ ] Auth
    * [ ] Log in
    * [ ] Register
