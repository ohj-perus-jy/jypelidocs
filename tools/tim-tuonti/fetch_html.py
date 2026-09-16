import pathlib, urllib.request, time
ROOT='kurssit/jypeli/'
out=pathlib.Path('timhtml'); out.mkdir(exist_ok=True)
pages=sorted(p for p in (ROOT+str(f.relative_to('tim').with_suffix('')) for f in pathlib.Path('tim').rglob('*.md')) if p not in (ROOT+'luonti',ROOT+'ajastimet'))
# Läpsylinnun vaiheet 2-11 eivät ole wikin etusivun linkkejä (vaihe 1 on).
pages=sorted(set(pages)|{ROOT+'mallit/lapsylintu/vaihe%d'%n for n in range(2,12)})
for p in pages:
    f=out/(p[len(ROOT):].replace('/','__')+'.html')
    if f.exists() and f.stat().st_size>1000: continue
    for attempt in range(3):
        try:
            with urllib.request.urlopen(f'https://tim.jyu.fi/view/{p}',timeout=120) as r: f.write_bytes(r.read()); break
        except Exception as e: print('retry',p,e); time.sleep(2)
print(len(pages),'pages;',len(list(out.glob('*.html'))),'html files')
