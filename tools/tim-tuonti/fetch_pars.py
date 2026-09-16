import pathlib, collections
from timlib import *
stats=collections.Counter(); errors=[]
for fn in sorted(pathlib.Path('timhtml').glob('*.html')):
    docid, pars = parse_page(fn)
    for p in pars:
        if p['preamble'] or p['plugin']: stats['skip']+=1; continue
        d = get_block(docid, p['id'])
        if 'error' in d: errors.append((fn.name, p['id'], d['error'], p['attrs'])); stats['err']+=1
        else: stats['ok']+=1
print(stats); print('\n'.join(map(str,errors)))
