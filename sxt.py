# coding: utf-8
from PIL import Image, ImageFont
from handright import Template,handwrite

text =open("date.txt",'r',encoding='utf-8').read()
template = Template(
    background=Image.new(mode="1", size=(1080, 2340), color=1),
    font=ImageFont.truetype("font.ttf", size=100),
)
images = handwrite(text, template)
for im in images:
    assert isinstance(im, Image.Image)
    im.show()