"""Regenerate the static publication list; no third-party dependencies needed."""
import html
import json
from pathlib import Path
root = Path(__file__).resolve().parent
pubs = json.loads((root / 'data/publications.json').read_text())
rows = []
for p in pubs:
    title = html.escape(p['title'])
    if p['url']:
        title = f'<a href="{html.escape(p["url"], quote=True)}">{title}<span class="paper-arrow" aria-hidden="true">↗</span></a>'
    authors = html.escape(p['authors']).replace('Prateek Kumar Rajput', '<strong>Prateek Kumar Rajput</strong>').replace('Prateek Rajput', '<strong>Prateek Rajput</strong>')
    rows.append(f'<li class="publication" data-type="{p["type"]}"><div class="pub-year">{p["year"]}</div><div class="pub-body"><h3>{title}</h3><p class="authors">{authors}</p><p class="venue">{html.escape(p["venue"])}</p></div></li>')
template = (root / 'index.template.html').read_text()
(root / 'index.html').write_text(template.replace('<!-- PUBLICATIONS -->', '\n'.join(rows)))
print(f'Built index.html with {len(pubs)} publications.')
