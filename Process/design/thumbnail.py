import os
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageOps
from random import choice

ZAID = [
    "Process/ImageFont/LightGreen.png",
    "Process/ImageFont/Red.png",
    "Process/ImageFont/Black.png",
    "Process/ImageFont/Blue.png",
    "Process/ImageFont/Grey.png",
    "Process/ImageFont/Green.png",
    "Process/ImageFont/Lightblue.png",
    "Process/ImageFont/Lightred.png",
    "Process/ImageFont/Purple.png",
    "Process/ImageFont/foreground.png",
]


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def thumb(thumbnail, title, userid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"search/thumb{userid}.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image = Image.open(f"search/thumb{userid}.png")
    image1 = changeImageSize(1280, 720, image)
    # Cropping circle from thubnail
    image = ImageOps.expand(image1, border=20, fill="blue")    
    
    image.save(f"final.png")
    os.remove(f"search/thumb{userid}.png")
    final = f"final.png" 
    return final
