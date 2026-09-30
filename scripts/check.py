"""Check the packaged data and reproducibility without external dependencies."""
import json,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/positions.json').read_text());p=json.loads((root/'data/provenance.json').read_text())
assert len(rows)==5820 and len({r['epd'] for r in rows})==len(rows)
assert all(r['count']>=20 and len(r['steps'])==6 and len(r['fens'])==7 for r in rows)
assert all(sum(r['results'].values())==r['count'] for r in rows)
assert all(rows[i]['count']>=rows[i+1]['count'] for i in range(len(rows)-1))
assert sum(m['stats']['counted_games'] for m in p['months'])==3433977
assert rows[0]['count']==133091
before=(root/'index.html').read_bytes();subprocess.run([sys.executable,str(root/'scripts/build.py')],check=True);assert (root/'index.html').read_bytes()==before
print('OK: 5820 positions, counts, provenance and reproducible HTML build')
