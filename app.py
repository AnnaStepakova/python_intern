#!/usr/bin/python3
import requests
import uvicorn
import os
from fastapi import FastAPI

app = FastAPI()


def is_alive_host(hostname):
    try:
        page = requests.get("http://" + hostname)
        return 100 <= page.status_code < 400
    except requests.exceptions.ConnectionError:
        return False


@app.get("/healthz")
async def root(hostname: str):
    return {"status": "up" if is_alive_host(hostname) else "down"}


if __name__ == "__main__":
    port = os.getenv('PORT')
    uvicorn.run(app, host="0.0.0.0", port=(port if port is not None else 8000))

