#!/usr/bin/env python3
"""Build experimental background-only NXThemes, in ZIP format (installer 3+)."""
from pathlib import Path
import hashlib, json, zipfile
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PARTS = {'home':'Home Menu','lock':'Lock Screen','apps':'All Applications','set':'Settings','user':'User Profile','news':'News','psl':'Player Selection'}
for part, title in PARTS.items():
    source = ROOT/'artwork'/('sonic-green-hill-source.png' if part in ('home','lock') else 'sonic-team-source.png')
    img = ImageOps.fit(Image.open(source).convert('RGB'), (1280,720), method=Image.Resampling.LANCZOS)
    bg = ROOT/'backgrounds'/f'{part}.jpg'
    bg.parent.mkdir(exist_ok=True)
    img.save(bg, 'JPEG', quality=94, subsampling=0, progressive=False)
    meta = {'Version':17,'Target':part,'Author':'Amir Saeid Dehghan','ThemeName':'Sonic Green Hill — '+title,'Id':hashlib.sha256(('sonic-green-hill-'+part).encode()).hexdigest()[:8]}
    dest = ROOT/'packages'/f'sonic-{part}.nxtheme'
    dest.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(dest, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr('info.json',json.dumps(meta,ensure_ascii=False,indent=2))
        z.write(bg,'image.jpg')
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == {'info.json','image.jpg'}
        assert json.loads(z.read('info.json')) == meta
        from io import BytesIO
        check=Image.open(BytesIO(z.read('image.jpg')))
        assert check.size == (1280,720) and not check.info.get('progressive')
    print(f'{dest.name}: structure and baseline JPEG checks passed')
