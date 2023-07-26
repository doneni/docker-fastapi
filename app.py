from fastapi import FastAPI 
from fastapi.responses import FileResponse, RedirectResponse
import logging

app = FastAPI()

@app.get("/")
async def root():
    logging.info("GET root")
    return FileResponse('./resources/index.html')

@app.get("/doneni/")
async def doneni():
    logging.info("GET doneni")
    return FileResponse('./resources/doneni.html')

@app.get("/doneni/profile/")
async def doneni_profile():
    logging.info("GET doneni/profile")
    return FileResponse('./resources/profile.html')

@app.get("/doneni/blog/")
async def doneni_blog():
    logging.info("GET doneni/blog")
    return RedirectResponse(url="https://doneni.tistory.com")

@app.get("/doneni/portfolio/")
async def doneni_portfolio():
    logging.info("GET doneni/portfolio")
    return RedirectResponse(url="https://donenigz.notion.site/debe9fa5999d43fdbb93d6205e0475d5?pvs=4")

@app.get("/doneni/lab/")
async def doneni_lab():
    logging.info("GET doneni/lab")
    return RedirectResponse(url="https://csec.ssu.ac.kr/")
