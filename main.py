import uvicorn
from fastapi import FastAPI, Form
from starlette.middleware.cors import CORSMiddleware
import slots

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def clear():
    slots.already = {
        "MON": {},
        "TUE": {},
        "WED": {},
        "THU": {},
        "FRI": {}
    }


@app.get("/")
async def testing():
    """Check if server is working"""
    return "Ok! Working!"


@app.post("/fetch/")
async def get_timetable(request: str = Form(...)):
    data = slots.fetch_info(request)
    clear()
    return data

if __name__ == "__main__":
    uvicorn.run(app)
