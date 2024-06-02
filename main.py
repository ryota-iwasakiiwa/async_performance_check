
import asyncio
import time

from fastapi import FastAPI

app = FastAPI()

async def async_sleep(second: int = 3):
    await asyncio.sleep(second)

def sleep(second: int = 3):
    time.sleep(second)

@app.get("/async_await")
async def async_await():
    await async_sleep()
    return "Finish"

@app.get("/async_no_await")
async def async_no_await():
    sleep()
    return "Finish"

# This will not work
@app.get("/no_async_await")
def no_async_await():
    async_sleep()
    return "Finish"

@app.get("/no_async_no_await")
def no_async_no_await():
    sleep()
    return "Finish"

