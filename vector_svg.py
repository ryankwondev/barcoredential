from fastapi import FastAPI
from fastapi.responses import FileResponse
import pdf417

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{string}")
async def encode(string: str):
    codes = pdf417.encode(string)
    image = pdf417.render_svg(codes)
    image.write("image.svg")
    return FileResponse("image.svg")
