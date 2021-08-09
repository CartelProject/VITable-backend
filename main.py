import uvicorn
from fastapi import FastAPI, Form
from starlette.middleware.cors import CORSMiddleware
from slots import fetch_info

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://0.0.0.0:8000",
    ],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def testing():
    """Check if server is working"""
    return "Ok! Working!"


@app.post("/fetch/")
async def get_timetable(request: str = Form(...)):
    data = fetch_info(request)
    return data


if __name__ == "__main__":
    uvicorn.run(app)
