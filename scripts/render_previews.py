#!/usr/bin/env python3
"""Draw illustrative previews from the packaged backgrounds (not console screenshots)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(size,bold=False): return ImageFont.truetype(BOLD if bold else FONT,size)
def label(d, xy, text, size=20, color='white', bold=False): d.text(xy,text,font=font(size,bold),fill=color)
def pill(d,box,color=(10,25,53,205),radius=18):d.rounded_rectangle(box,radius,fill=color)
parts={'home':'HOME MENU','lock':'LOCK SCREEN','apps':'ALL APPLICATIONS','set':'SYSTEM SETTINGS','user':'USER PROFILE','news':'NEWS','psl':'PLAYER SELECTION'}
out=ROOT/'previews';out.mkdir(exist_ok=True)
for part,title in parts.items():
    image=Image.open(ROOT/'backgrounds'/f'{part}.jpg').convert('RGBA'); overlay=Image.new('RGBA',image.size);d=ImageDraw.Draw(overlay)
    # This overlay is schematic; only the underlying image is included in the theme.
    d.rectangle((0,0,1280,82),fill=(4,15,35,155));d.rectangle((0,649,1280,720),fill=(4,15,35,190))
    label(d,(40,28),'SONIC  /  '+title,18,bold=True);label(d,(1007,30),'PREVIEW',15,(255,214,93),True)
    label(d,(43,672),'ILLUSTRATIVE PREVIEW  •  NOT A CONSOLE CAPTURE',15,(224,233,247),True)
    if part=='home':
        label(d,(48,104),'Recently played',21,bold=True)
        for i in range(4):
            x=48+i*151; pill(d,(x,155,x+134,289),(7,20,48,220),13)
            d.rounded_rectangle((x+4,159,x+130,285),10,outline=(105,201,255,210),width=2)
            label(d,(x+21,207),f'GAME {i+1:02}',16,(230,240,255),True)
        label(d,(48,320),'Select a game to play',20)
        for i,name in enumerate(['news','shop','album','controller','settings','power']):
            x=70+i*82;d.ellipse((x,493,x+57,550),fill=(6,23,48,230),outline=(251,216,107),width=2)
            icon=Image.open(ROOT/'icons'/f'{name}.png').convert('RGBA').resize((48,42));overlay.alpha_composite(icon,(x+5,500))
    elif part=='lock':
        label(d,(50,140),'10:08',62,bold=True);label(d,(55,228),'Wednesday, October 28',23)
        pill(d,(48,493,558,567));label(d,(75,511),'Press the same button three times',21,bold=True)
    elif part=='apps':
        label(d,(48,106),'All Software',28,bold=True)
        for i in range(8):
            x=48+(i%4)*145;y=160+(i//4)*158
            pill(d,(x,y,x+130,y+130),(9,25,54,225),12);label(d,(x+20,y+53),f'GAME {i+1:02}',15,(223,239,255),True)
    elif part=='set':
        pill(d,(35,110,650,613),(5,17,40,220),20);label(d,(60,132),'System Settings',30,bold=True)
        for i,t in enumerate(['Airplane Mode','Notifications','Sleep Mode','Controllers and Sensors','System']):
            y=201+i*71
            if i==0: d.rounded_rectangle((53,y-8,631,y+49),10,fill=(15,111,160,220),outline=(112,224,255),width=2)
            label(d,(75,y),t,20)
    elif part=='user':
        pill(d,(35,115,650,612),(5,17,40,220));d.ellipse((65,150,155,240),fill=(0,135,212),outline=(250,217,101),width=3)
        label(d,(87,177),'S',34,bold=True);label(d,(180,160),'Player',31,bold=True);label(d,(180,207),'Profile',20)
        for i,t in enumerate(['Profile','Friend List','Add Friend','User Settings']):label(d,(75,292+i*66),t,22,bold=(i==0))
    elif part=='news':
        pill(d,(36,110,695,600),(5,17,40,215));label(d,(62,136),'News',30,bold=True)
        for i,t in enumerate(['Latest updates','Featured stories','More from your games']):
            y=207+i*118;d.rounded_rectangle((62,y,665,y+92),12,fill=(17,52,88,230));label(d,(89,y+29),t,21,bold=True)
    else:
        pill(d,(50,158,720,560),(5,17,40,220));label(d,(79,188),'Select a user',30,bold=True)
        for i in range(3):
            x=85+i*175;d.ellipse((x,270,x+115,385),fill=(0,112+i*25,190),outline=(255,218,108),width=3);label(d,(x+38,309),str(i+1),32,bold=True)
    Image.alpha_composite(image,overlay).convert('RGB').save(out/f'{part}.jpg',quality=92,subsampling=0)
# contact sheet uses the actual generated previews
thumbs=[]
for part in parts:
    im=Image.open(out/f'{part}.jpg'); im.thumbnail((512,288)); thumbs.append(im)
board=Image.new('RGB',(1600,1010),(4,15,36));d=ImageDraw.Draw(board)
label(d,(44,32),'SONIC  /  THEME OVERVIEW',32,bold=True);label(d,(46,80),'Illustrative previews — not console screenshots',18,(157,199,229))
for i,im in enumerate(thumbs): board.paste(im,(32+(i%3)*524,122+(i//3)*292))
board.save(out/'overview.jpg',quality=92,subsampling=0)
