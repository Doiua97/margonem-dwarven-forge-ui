from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import random, math

ROOT=Path("assets/gui/v03")
ROOT.mkdir(parents=True,exist_ok=True)

C={
"void":"#070808","black":"#0c0e0e","iron":"#171918","iron2":"#262a28","iron3":"#3b403d",
"edge":"#686f69","copper":"#6a3d22","copper2":"#a3602f","bronze":"#b87b36","gold":"#d79b43",
"gold2":"#f0bf68","warm":"#2a1b13"
}
def rgb(h):
    h=h.lstrip("#"); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def noise(size,base,seed=1,amount=7):
    w,h=size; b=rgb(C[base]); rnd=random.Random(seed); im=Image.new("RGBA",size); px=im.load()
    for y in range(h):
        for x in range(w):
            n=rnd.randint(-amount,amount)+((x*5+y*3+seed)%5-2)
            px[x,y]=tuple(max(0,min(255,c+n)) for c in b)+(255,)
    return im.filter(ImageFilter.GaussianBlur(.18))
def rivet(d,x,y,r=2):
    d.ellipse((x-r,y-r,x+r,y+r),fill=C["bronze"],outline=C["void"])
    if r>1: d.point((x-1,y-1),fill=C["gold2"])
def save(im,name):
    p=ROOT/name; p.parent.mkdir(parents=True,exist_ok=True); im.save(p)
def bevel(d,box,outer="void",edge="edge",inner="copper2",w=1):
    x0,y0,x1,y1=box
    d.rectangle(box,outline=C[outer],width=2)
    if x1-x0>4 and y1-y0>4:d.rectangle((x0+2,y0+2,x1-2,y1-2),outline=C[edge],width=1)
    if x1-x0>8 and y1-y0>8:d.rectangle((x0+4,y0+4,x1-4,y1-4),outline=C[inner],width=1)

im=noise((128,128),"iron",11,5); d=ImageDraw.Draw(im)
for y in range(0,128,32): d.line((0,y,127,y),fill=(0,0,0,35),width=1)
for x in range(0,128,64): d.line((x,0,x,127),fill=(255,255,255,10),width=1)
save(im,"surface.png")

im=noise((128,128),"warm",12,5); d=ImageDraw.Draw(im)
for y in range(8,128,24): d.line((0,y,127,y),fill=rgb(C["copper"])+(55,),width=1)
save(im,"surface-warm.png")

w,h=96,96
im=Image.new("RGBA",(w,h),(0,0,0,0)); base=noise((w,h),"iron2",13,5); im.alpha_composite(base); d=ImageDraw.Draw(im)
bevel(d,(0,0,w-1,h-1)); d.rectangle((17,17,w-18,h-18),fill=(0,0,0,0))
for pts in [[(3,3),(31,3),(22,12),(12,22),(3,31)],[(w-4,3),(w-32,3),(w-23,12),(w-13,22),(w-4,31)],[(3,h-4),(31,h-4),(22,h-13),(12,h-23),(3,h-32)],[(w-4,h-4),(w-32,h-4),(w-23,h-13),(w-13,h-23),(w-4,h-32)]]:
    d.polygon(pts,fill=C["iron3"],outline=C["copper2"])
for x,y in [(9,9),(w-10,9),(9,h-10),(w-10,h-10)]:rivet(d,x,y,2)
d.line((18,5,w-19,5),fill=C["gold"],width=1); d.line((18,h-6,w-19,h-6),fill=C["copper2"],width=1)
d.line((5,18,5,h-19),fill=C["copper2"],width=1); d.line((w-6,18,w-6,h-19),fill=C["copper2"],width=1)
save(im,"window-frame.png")

im=noise((256,32),"iron2",14,5); d=ImageDraw.Draw(im); bevel(d,(0,0,255,31)); d.line((8,3,247,3),fill=C["gold"],width=1); d.line((8,27,247,27),fill=C["copper"],width=2)
for x in (9,246):rivet(d,x,16,2)
save(im,"header.png")

im=noise((256,40),"iron2",15,5); d=ImageDraw.Draw(im); bevel(d,(0,0,255,39)); d.line((0,4,255,4),fill=C["copper2"],width=2); d.line((0,36,255,36),fill=C["void"],width=2)
for x in (9,246):rivet(d,x,20,2)
save(im,"bottom-bar.png")

im=noise((33,33),"black",16,3); d=ImageDraw.Draw(im); d.rectangle((0,0,32,32),outline=C["void"]); d.rectangle((1,1,31,31),outline=C["edge"]); d.rectangle((3,3,29,29),outline=C["copper"]); d.line((4,4,28,4),fill=C["gold"],width=1)
for x,y in [(4,4),(28,4),(4,28),(28,28)]:rivet(d,x,y,1)
save(im,"slot.png")

im=noise((13,64),"black",17,3); d=ImageDraw.Draw(im); d.rectangle((0,0,12,63),outline=C["void"]); d.line((2,0,2,63),fill=C["copper"]); d.line((10,0,10,63),fill=C["edge"]); save(im,"scrollbar-bg.png")
im=noise((13,48),"copper",18,3); d=ImageDraw.Draw(im); d.rectangle((0,0,12,47),outline=C["void"]); d.rectangle((2,2,10,45),outline=C["gold"])
for y in (10,24,38):d.line((4,y,8,y),fill=C["gold2"])
save(im,"scrollbar-handle.png")

im=Image.new("RGBA",(342,65),(0,0,0,0)); d=ImageDraw.Draw(im); d.rounded_rectangle((0,0,341,64),8,fill=C["iron"],outline=C["void"],width=2); d.rounded_rectangle((3,3,338,61),6,outline=C["copper2"],width=1); d.rectangle((30,9,219,51),fill=(10,12,12,210),outline=C["edge"]); d.rectangle((225,9,332,51),fill=(10,12,12,210),outline=C["copper"]); d.line((14,4,328,4),fill=C["gold"],width=1)
for x,y in [(9,9),(332,9),(9,55),(332,55)]:rivet(d,x,y,2)
save(im,"hud-frame.png")

im=Image.new("RGBA",(590,100),(0,0,0,0)); d=ImageDraw.Draw(im); d.rounded_rectangle((0,9,589,99),11,fill=C["iron"],outline=C["void"],width=2); d.rounded_rectangle((3,12,586,96),8,outline=C["copper2"],width=1); d.line((25,15,565,15),fill=C["gold"],width=1); d.ellipse((246,-3,344,95),fill=(0,0,0,0),outline=C["copper2"],width=2)
for x,y in [(10,22),(579,22),(10,88),(579,88)]:rivet(d,x,y,2)
save(im,"bottom-panel.png")

im=Image.new("RGBA",(96,96),(0,0,0,0)); base=noise((96,96),"iron2",19,5); im.alpha_composite(base); d=ImageDraw.Draw(im); bevel(d,(0,0,95,95)); d.rectangle((13,13,82,82),fill=(0,0,0,0))
for x,y in [(7,7),(88,7),(7,88),(88,88)]:rivet(d,x,y,2)
save(im,"map-frame.png")

im=Image.new("RGBA",(48,48),(0,0,0,0)); d=ImageDraw.Draw(im); d.rectangle((0,0,47,47),fill=C["iron"],outline=C["void"],width=2); d.rectangle((2,2,45,45),outline=C["gold"],width=1); d.rectangle((5,5,42,42),fill=(0,0,0,0))
for x,y in [(4,4),(43,4),(4,43),(43,43)]:rivet(d,x,y,1)
save(im,"tooltip-frame.png")

im=noise((160,28),"warm",20,4); d=ImageDraw.Draw(im); bevel(d,(0,0,159,27)); d.line((6,3,153,3),fill=C["gold"],width=1); save(im,"answer.png")
