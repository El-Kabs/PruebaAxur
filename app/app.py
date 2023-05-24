#!/usr/bin/env python3

import uvicorn
import requests
from fastapi import FastAPI, Request
# from fastapi.security import HTTPBearer
# from splunk_otel.tracing import start_tracing
# from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from fastapi.responses import RedirectResponse

app = FastAPI()
PATH = "/api/fast-api-test/v1/"

# start_tracing()
peticiones = []

@app.get(PATH + "health")
async def health(request: Request):
    return "Hello World"
#steven.johnston1640@quartzotech.com
@app.get(PATH + "axur")
async def axur(request: Request):
    secret = "z&4gAqHw!bX9C7O#h*4au779k1r"
    return secret

@app.post(PATH + "test")
async def test(request: Request):
    body = await request.json()
    url = body["url"]
    secret = body["secret"]

    if secret != "z&4gAqHw!bX9C7O#h*4au779k1r":
        return 0

    activeDirectoryUsersRequest = requests.get(url)
    return activeDirectoryUsersRequest.text

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)
