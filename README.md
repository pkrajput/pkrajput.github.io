# Prateek Kumar Rajput

Static personal research website for GitHub Pages.

## Edit and preview

- Edit `index.template.html` for the compact biography, logo row, supervisors, and research grants.
- Edit `data/publications.json` for publication details. Entries with `selected: true` appear by default and the rest are in the native “More publications” disclosure.
- Run `python3 build.py` to regenerate `index.html`.
- Run `python3 -m http.server 8873 --bind 127.0.0.1` to preview locally.

The site uses HTML and CSS only, with system fonts and no external font requests or JavaScript dependencies. Publication links remain available through the native disclosure without JavaScript. Layouts support mobile screens, keyboard focus, and reduced motion.

The website intentionally has no CV download or hosted CV PDF. Keep CV files outside this repository. Program Bindings Inside Code Models links to the prepared author PDF in `assets/` until a public arXiv URL is available. Do not add its review venue to public content.

GitHub Pages serves the repository root. Run the static build and review changes before pushing to `main`.

## Logo sources

- University of Luxembourg logo: https://commons.wikimedia.org/wiki/File:University_of_Luxembourg_logo_(fr).svg (university-authored vector extracted from its official material).
- Huawei logo: https://www.huawei.com/-/media/hcomponent-header/1.0.1.20260908162100/component/img/huawei_logo.png
- OxML uses the text wordmark displayed on https://www.oxfordml.school/ (OxML by AI4GG), rendered as HTML rather than a substituted university crest.
