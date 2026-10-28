#!/usr/bin/env python3
"""Create 64×56 transparent home applet icons using vector-like Pillow drawing."""
from PIL import Image,ImageDraw
from pathlib import Path
root=Path(__file__).resolve().parents[1]/'icons';root.mkdir(exist_ok=True)
S=4
for name in ('news','shop','album','controller','settings','power'):
 im=Image.new('RGBA',(64*S,56*S));d=ImageDraw.Draw(im)
 def line(points,fill='#FFFFFF',width=3):d.line([(int(x*S),int(y*S)) for x,y in points],fill=fill,width=width*S,joint='curve')
 def ellipse(box,fill=None,outline=None,width=1):d.ellipse(tuple(int(v*S) for v in box),fill=fill,outline=outline,width=width*S)
 def rect(box,fill=None,outline=None,width=1,radius=0):d.rounded_rectangle(tuple(int(v*S) for v in box),radius=radius*S,fill=fill,outline=outline,width=width*S)
 ellipse((9,5,55,51),outline='#FFD453',width=3); ellipse((13,9,51,47),outline='#B67516',width=1)
 if name=='news':
  d.polygon([(33*S,12*S),(22*S,29*S),(30*S,29*S),(27*S,43*S),(43*S,23*S),(34*S,23*S)],fill='#FFFFFF')
 elif name=='shop':
  rect((20,22,44,40),outline='white',width=3,radius=2);d.arc((25*S,13*S,39*S,30*S),180,360,fill='white',width=3*S)
 elif name=='album':
  rect((18,18,46,39),outline='white',width=3,radius=3);ellipse((27,23,37,33),outline='white',width=2);line([(21,17),(27,17)])
 elif name=='controller':
  rect((17,20,47,38),outline='white',width=3,radius=7);line([(22,29),(30,29)]);line([(26,25),(26,33)]);ellipse((37,25,40,28),fill='white');ellipse((41,30,44,33),fill='white')
 elif name=='settings':
  ellipse((22,18,42,38),outline='white',width=3);ellipse((29,25,35,31),fill='white')
  for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]:line([(32+dx*11,28+dy*11),(32+dx*15,28+dy*15)])
 else:
  d.arc((21*S,16*S,43*S,40*S),35,325,fill='white',width=3*S);line([(32,13),(32,29)],width=3)
 im.resize((64,56),Image.Resampling.LANCZOS).save(root/(name+'.png'))
