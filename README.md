# DAC7 Check (www.dac7check.eu)

Free DAC7 checker for EU resale sellers in 22 languages, by SortwellStudios.

- `src/i18n.py`, `src/i18n2.py`: all page texts, one block per language
- `src/build.py`: builds every page, the sitemap, robots.txt, Impressum and privacy page into `out/`
- `src/base.css`: shared styles
- `out/`: the finished site that Netlify publishes (see `netlify.toml`)

To change the site: edit the files in `src/`, run `python3 src/build.py`, commit `src/` and `out/` together, push to `main`. Netlify deploys automatically.
