from PIL import Image,ImageDraw
from pathlib import Path
import random,math,csv,os
R=Path('.')
P={'void':'#090A0A','bg0':'#0D0F0F','bg1':'#141616','bg2':'#1B1D1D','steel':'#373C3B','edge':'#7A817A','cu0':'#3E2416','cu':'#6A391F','cu2':'#A05B2B','bronze':'#B77A34','gold':'#D19A42','gold2':'#F0C36A','danger':'#A83A31','success':'#5D8C47','info':'#416D8B','mana':'#286A9A','energy':'#B18A2B','slot':'#111212'}
def tex(sz,base='bg1',seed=1):
 w,h=sz; b=tuple(int(P[base][i:i+2],16) for i in (1,3,5)); rnd=random.Random(seed); im=Image.new('RGBA',sz); px=im.load()
 for y in range(h):
  for x in range(w):
   n=rnd.randint(-6,6)+((x*7+y*3+seed)%5-2); px[x,y]=tuple(max(0,min(255,c+n)) for c in b)+(255,)
 return im
def riv(d,x,y,r=2):
 d.ellipse((x-r,y-r,x+r,y+r),fill=P['bronze'],outline=P['void'])
def save(im,p):
 p=R/p; p.parent.mkdir(parents=True,exist_ok=True); im.save(p)
def frame(sz,transparent=False):
 w,h=sz; im=tex(sz,'bg1',w+h); d=ImageDraw.Draw(im); d.rectangle((0,0,w-1,h-1),outline=P['void'],width=2); d.rectangle((2,2,w-3,h-3),outline=P['edge']); d.rectangle((4,4,w-5,h-5),outline=P['cu2'],width=2)
 if transparent and w>30 and h>30: d.rectangle((min(20,w//4),min(20,h//4),w-min(21,w//4),h-min(21,h//4)),fill=(0,0,0,0))
 for x,y in ((7,7),(w-8,7),(7,h-8),(w-8,h-8)):
  if 0<x<w and 0<y<h:riv(d,x,y,1)
 return im
def bar(sz,active=False):
 w,h=sz; im=tex(sz,'bg2',w+h); d=ImageDraw.Draw(im); d.rectangle((0,0,w-1,h-1),outline=P['void'],width=2); d.line((0,2,w-1,2),fill=P['edge']); d.line((0,h-3,w-1,h-3),fill=P['gold'] if active else P['cu'],width=2); return im
spec={
'ReverseButton.png':(16,16),'ReverseButtonHover.png':(16,16),'X-blackoutline.png':(15,15),'auctions/header_left.png':(80,28),'battle/summary-bottom-bar.png':(654,57),'battle/surrender.png':(32,32),'battle/toggle-less.png':(22,22),'battle/toggle-more.png':(22,22),'belka-gora-dol.png':(64,122),'bottom-panel-frame.png':(590,100),'bubble/bottom.png':(228,24),'bubble/bottom_l.png':(228,24),'bubble/left.png':(4,32),'bubble/right.png':(13,32),'bubble/top.png':(228,13),'chat-powtarzalny-podklad.png':(502,64),'close-button.png':(22,22),'close-corner.png':(51,52),'cloud_tail.png':(21,22),'direction.png':(52,26),'exit.png':(32,32),'exp-overlay-left.png':(250,18),'exp-overlay-right.png':(250,18),'friend-header.png':(52,40),'hud-frame.png':(342,65),'info-box-2.png':(96,64),'item-slot.png':(50,50),'item_frames/frames/item_frames.png':(192,32),'line-highlight-green2.png':(4,64),'line-highlight-red2.png':(4,64),'line-highlight-yellow2.png':(4,64),'match-bar.png':(56,25),'middle_graphics.png':(22,64),'o.png':(14,14),'ok-blackoutline.png':(15,15),'oneItemSlotToRepeat.png':(33,33),'progressBar/percent-blue.png':(16,14),'progressBar/percent-red.png':(16,14),'progressBar/percent-yellow.png':(16,14),'progressBar/progress-bar.png':(16,14),'quests/quest_bar.png':(80,28),'quests/tracked.png':(20,14),'search-icon.png':(16,16),'search.png':(64,32),'shop/canopy.png':(471,92),'stats-scroll-bar.png':(13,64),'table_header.png':(80,28),'triangle.png':(8,8),'width-card-button-active.png':(60,35),'width-card-button.png':(60,35),'window-frame.png':(80,96),'zoom1.png':(200,200),'zoom2.png':(200,200)}
for n,sz in spec.items(): save(frame(sz, n in {'window-frame.png','hud-frame.png','bottom-panel-frame.png','close-corner.png'}), 'assets/gui/'+n)
for n in ['auctions/header_left.png','battle/summary-bottom-bar.png','bubble/bottom.png','bubble/bottom_l.png','bubble/top.png','friend-header.png','match-bar.png','quests/quest_bar.png','table_header.png','width-card-button.png','width-card-button-active.png']:
 save(bar(spec[n], n in {'battle/summary-bottom-bar.png','quests/quest_bar.png','width-card-button.png'}),'assets/gui/'+n)
im=tex((33,33),'slot',33); d=ImageDraw.Draw(im); d.rectangle((0,0,32,32),outline=P['void']); d.rectangle((2,2,30,30),outline=P['cu']); save(im,'assets/gui/oneItemSlotToRepeat.png')
im=Image.new('RGBA',(64,122)); im.alpha_composite(bar((64,60)),(0,0)); im.alpha_composite(bar((64,60),True),(0,61)); save(im,'assets/gui/belka-gora-dol.png')
im=Image.new('RGBA',(502,64)); im.alpha_composite(tex((251,64),'bg2',501),(0,0)); im.alpha_composite(tex((251,64),'bg2',502),(251,0)); d=ImageDraw.Draw(im); d.line((4,0,4,63),fill=P['cu2'],width=2); d.line((255,0,255,63),fill=P['cu2'],width=2); save(im,'assets/gui/chat-powtarzalny-podklad.png')
colors={'line-highlight-green2.png':P['success'],'line-highlight-red2.png':P['danger'],'line-highlight-yellow2.png':P['gold']}
for n,c in colors.items(): im=Image.new('RGBA',spec[n],(0,0,0,0)); ImageDraw.Draw(im).rectangle((0,0,2,spec[n][1]-1),fill=c); save(im,'assets/gui/'+n)
for n,c in [('progressBar/percent-blue.png',P['mana']),('progressBar/percent-red.png',P['danger']),('progressBar/percent-yellow.png',P['energy'])]: im=Image.new('RGBA',spec[n],(0,0,0,0)); ImageDraw.Draw(im).rectangle((0,2,15,11),fill=c); save(im,'assets/gui/'+n)
def icon(n,drawfn):
 im=Image.new('RGBA',spec[n],(0,0,0,0)); d=ImageDraw.Draw(im); drawfn(d,*spec[n]); save(im,'assets/gui/'+n)
icon('close-button.png',lambda d,w,h:(d.rounded_rectangle((1,1,w-2,h-2),3,fill=P['bg1'],outline=P['cu2'],width=2),d.line((6,6,w-7,h-7),fill=P['danger'],width=2),d.line((w-7,6,6,h-7),fill=P['danger'],width=2)))
icon('search-icon.png',lambda d,w,h:(d.ellipse((2,2,9,9),outline=P['gold'],width=2),d.line((9,9,14,14),fill=P['gold'],width=2)))
icon('triangle.png',lambda d,w,h:d.polygon([(0,0),(w,0),(0,h)],fill=P['gold']))
icon('o.png',lambda d,w,h:d.ellipse((2,2,w-3,h-3),outline=P['gold'],width=2))
icon('quests/tracked.png',lambda d,w,h:d.line((2,h//2,7,h-2,w-2,2),fill=P['success'],width=3))
icon('battle/surrender.png',lambda d,w,h:(d.rounded_rectangle((1,1,w-2,h-2),4,fill=P['bg1'],outline=P['danger'],width=2),d.polygon([(9,7),(23,16),(9,25)],outline=P['gold2'])))
for n,down in [('battle/toggle-more.png',1),('battle/toggle-less.png',0)]: icon(n,lambda d,w,h,down=down:d.line([(5,7),(w//2,15 if down else 7),(w-5,7 if down else 15)],fill=P['gold2'],width=2))
icon('exit.png',lambda d,w,h:(d.polygon([(w//2,1),(w-2,h//2),(w//2,h-2),(1,h//2)],fill=P['bg1'],outline=P['gold']),d.line((9,9,w-10,h-10),fill=P['danger'],width=3),d.line((w-10,9,9,h-10),fill=P['danger'],width=3)))
icon('cloud_tail.png',lambda d,w,h:d.polygon([(2,2),(w-2,2),(8,h-2)],fill=P['bg2'],outline=P['cu']))
icon('direction.png',lambda d,w,h:(d.polygon([(2,h//2),(22,2),(22,h-2)],fill=P['bronze'],outline=P['gold2']),d.polygon([(w-2,h//2),(w-22,2),(w-22,h-2)],fill=P['bronze'],outline=P['gold2'])))
for n,hover in [('ReverseButton.png',0),('ReverseButtonHover.png',1)]: icon(n,lambda d,w,h,hover=hover:(d.arc((2,2,w-3,h-3),25,300,fill=P['gold2'] if hover else P['bronze'],width=2),d.polygon([(w-4,2),(w-1,5),(w-5,6)],fill=P['gold2'] if hover else P['bronze'])))
for n,plus in [('zoom1.png',0),('zoom2.png',1)]:
 im=Image.new('RGBA',(200,200),(0,0,0,0)); d=ImageDraw.Draw(im); d.ellipse((14,14,185,185),fill=P['bg1'],outline=P['cu2'],width=8); d.line((62,100,138,100),fill=P['gold2'],width=12); plus and d.line((100,62,100,138),fill=P['gold2'],width=12); save(im,'assets/gui/'+n)
im=Image.new('RGBA',(192,32),(0,0,0,0)); d=ImageDraw.Draw(im)
for i,c in enumerate(['#737975','#38B8EB','#FFFB00','#FF59AF','#FF8400','#E14046']): d.rectangle((i*32,0,i*32+31,31),outline=c,width=2)
save(im,'assets/gui/item_frames/frames/item_frames.png')
im=Image.new('RGBA',(471,92),(0,0,0,0)); d=ImageDraw.Draw(im)
for off in (0,46):
 for x in range(0,471,47): d.polygon([(x,off),(min(x+46,470),off),(min(x+41,470),off+35),(x+5,off+35)],fill=P['cu0'] if (x//47)%2==0 else P['steel'],outline=P['gold'])
save(im,'assets/gui/shop/canopy.png')
rows=[]
for n,sz in sorted(spec.items()): rows.append(['assets/gui/'+n,sz[0],sz[1],'Dwarven Forge UI replacement'])
Path('docs').mkdir(exist_ok=True)
with open('docs/asset-manifest.csv','w',newline='',encoding='utf-8-sig') as f: csv.writer(f,delimiter=';').writerows([['asset','width','height','purpose'],*rows])
Path('docs/changed-assets.md').write_text('# Changed assets\n\nThis manifest contains only assets intentionally replaced by Dwarven Forge. Original Margonem assets not modified by the theme are not stored in this repository.\n',encoding='utf-8')
