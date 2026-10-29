"""Generate static publication HTML from the research bibliography."""
import html
import json
from pathlib import Path

root = Path(__file__).resolve().parent
pubs = json.loads((root / 'data/publications.json').read_text())
selected, more = [], []
for p in pubs:
    title = html.escape(p['title'])
    if p['url']:
        title = f'<a href="{html.escape(p["url"], quote=True)}">{title}<span class="paper-arrow" aria-hidden="true">↗</span></a>'
    authors = html.escape(p['authors']).replace('Prateek Kumar Rajput', '<strong>Prateek Kumar Rajput</strong>').replace('Prateek Rajput', '<strong>Prateek Rajput</strong>')
    row = f'<li class="publication"><div class="pub-year">{p["year"]}</div><div><h3>{title}</h3><p class="authors">{authors}</p><p class="venue">{html.escape(p["venue"])}</p></div></li>'
    (selected if p.get('selected') else more).append(row)
template = (root / 'index.template.html').read_text()
page = template.replace('<!-- SELECTED_PUBLICATIONS -->', '\n'.join(selected))
page = page.replace('<!-- MORE_PUBLICATIONS -->', '\n'.join(more))
page = page.replace('<!-- MORE_COUNT -->', str(len(more)))
page = page.replace('<!-- MORE_START -->', str(len(selected) + 1))
(root / 'index.html').write_text(page)
print(f'Built index.html with {len(selected)} selected and {len(more)} additional publications.')
