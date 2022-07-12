from fastapi import FastAPI
from fastapi.responses import FileResponse
import pdf417
import PIL

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{string}")
async def encode(string: str):
    codes = pdf417.encode(string)
    image = pdf417.render_image(codes)
    image.save("image.png")
    # FileResponse("image.png", media_type="image/png")
    return FileResponse("image.png")
