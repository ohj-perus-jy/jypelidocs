import re, pathlib, urllib.request, time, html
refs=set()
for f in pathlib.Path('tim').rglob('*.md'):
    refs.update(re.findall(r'/(?:images|files)/\d+/[^)\s"\]]+', f.read_text(encoding='utf-8')))
for f in pathlib.Path('timhtml').glob('*.html'):
    refs.update(html.unescape(f.read_text(encoding='utf-8')).replace('\\"','"').__str__() and re.findall(r'/(?:images|files)/\d+/[A-Za-z0-9_.\-]+', html.unescape(f.read_text(encoding='utf-8'))))
refs={r.rstrip('.') for r in refs}
dst=pathlib.Path('timfiles'); n=0
for r in sorted(refs):
    p=dst/r.lstrip('/')
    if p.exists(): continue
    p.parent.mkdir(parents=True,exist_ok=True)
    try:
        with urllib.request.urlopen('https://tim.jyu.fi'+r,timeout=120) as resp: p.write_bytes(resp.read()); n+=1
    except Exception as e: print('ERR',r,e)
print(len(refs),'refs,',n,'downloaded')
