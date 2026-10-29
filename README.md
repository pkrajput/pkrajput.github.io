# Prateek Kumar Rajput

Personal research website, published at https://pkrajput.github.io/ through GitHub Pages.

## Update content

- Edit `index.template.html` for the biography, funding, experience, and education.
- Edit `data/publications.json` for papers and their publication status.
- Run `python3 build.py` to regenerate `index.html`.
- Replace `assets/Prateek_Rajput_CV.pdf` when updating the CV.
- Preview with `python3 -m http.server 8873`.

The page is static HTML/CSS with a small progressive-enhancement script for
publication filters. All papers remain visible if JavaScript is disabled.
Styling includes mobile layouts, keyboard focus states, reduced-motion
support, and print rules. Google Fonts has system-font fallbacks.

Manuscripts are distinguished from accepted/published work. The paper
“Program Bindings Inside Code Models” has no public paper URL yet; add its
arXiv URL after announcement. Do not add its review venue to public content.

Deploy by pushing a reviewed change to `main`; GitHub Pages serves the repository root.
