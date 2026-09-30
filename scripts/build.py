"""Build the self-contained browser application; Python standard library only."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
parts=[]
for name,path in [('POSITIONS','data/positions.json'),('PROVENANCE','data/provenance.json'),('PIECES','vendor/pieces.json')]:
 data=json.loads((ROOT/path).read_text(encoding='utf-8'))
 parts.append('const TABIA_'+name+'='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';')
for path in ['src/app.js','vendor/chess-1.4.0.js','src/chessdb.js']:
 parts.append((ROOT/path).read_text(encoding='utf-8'))
script='\n'.join(parts).replace('</script','<\\/script')
page=(ROOT/'src/template.html').read_text(encoding='utf-8').replace('<!-- TABIASCOUT_SCRIPTS -->','<script>'+script+'</script>')
(ROOT/'index.html').write_text(page,encoding='utf-8')
print('Built index.html')
