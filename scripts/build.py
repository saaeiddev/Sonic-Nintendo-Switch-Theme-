#!/usr/bin/env python3
"""Build experimental background-only NXThemes, in ZIP format (installer 3+)."""
from pathlib import Path
import hashlib, json, zipfile
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PARTS = {'home':'Home Menu','lock':'Lock Screen','apps':'All Applications','set':'Settings','user':'User Profile','news':'News','psl':'Player Selection'}
for part, title in PARTS.items():
    source_name = {'home':'sonic-green-hill-source.png','lock':'shadow-green-hill-source.png','apps':'sonic-team-source.png','set':'tails-green-hill-source.png','user':'shadow-green-hill-source.png','news':'tails-green-hill-source.png','psl':'sonic-team-source.png'}[part]
    source = ROOT/'artwork'/source_name
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
        if part == 'home':
            for name in ('news','shop','album','controller','settings','power'):
                z.write(ROOT/'icons'/f'{name}.png',f'{name}.png')
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
        expected = {'info.json','image.jpg'} | ({n+'.png' for n in ('news','shop','album','controller','settings','power')} if part == 'home' else set())
        assert set(z.namelist()) == expected
        if part == 'home':
            from io import BytesIO
            for n in expected - {'info.json','image.jpg'}:
                icon=Image.open(BytesIO(z.read(n)))
                assert icon.size == (64,56) and icon.format == 'PNG'
        assert json.loads(z.read('info.json')) == meta
        from io import BytesIO
        check=Image.open(BytesIO(z.read('image.jpg')))
        assert check.size == (1280,720) and not check.info.get('progressive')
    print(f'{dest.name}: structure and baseline JPEG checks passed')
