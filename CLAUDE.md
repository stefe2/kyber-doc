# CLAUDE.md

Documentation du **Kyber Controller** (système de contrôle pour droïdes R2 / astromech), publiée avec MkDocs + Material sur GitHub Pages : <https://stefe2.github.io/kyber-doc/>

Le contenu des pages est **en anglais** ; les messages de commit sont souvent en français.

## Commandes

```bash
pip install mkdocs mkdocs-material   # mkdocs 1.6.1, Python 3.13 installés localement
mkdocs serve                          # aperçu local sur http://127.0.0.1:8000
mkdocs build --strict                 # vérifier liens cassés / avertissements
mkdocs gh-deploy                      # build + push sur la branche gh-pages (publication)
```

Pas de CI : la publication se fait manuellement via `mkdocs gh-deploy`. Le dossier `site/` est un artefact de build ignoré par git.

## Structure

- `mkdocs.yml` — config du thème, **navigation (`nav`) explicite** : toute nouvelle page doit y être ajoutée, sinon elle n'apparaît pas dans le menu.
- `docs/index.md`, `docs/about.md` — accueil et à propos.
- `docs/manual/` — le manuel principal :
  - `hardware/` (carte principale, contrôleurs Maestro, servos, câblage)
  - `software/` (installation, configuration, interface web, Kyberpad)
  - `usage/` (contrôles de base, fonctions avancées, sons)
  - `troubleshooting.md`
- `docs/faq/` — base de connaissances générée à partir des questions du groupe Facebook *Kyber Control Systems* (index + 6 catégories). Format : blocs repliables `??? question "..."` avec réponses de la communauté en citations.
- `docs/assets/` — images par section (`kyberpad/`, `web_interface/`, `Installation/`, `hardware/`, `maestros/`, `transmitters/`, `wiring/`, `misc/`, `originals/`), plus `stylesheets/extra.css` et `javascripts/simple-lightbox.js` (clic sur une image = agrandissement).
- `docpdf/docs/` — source Markdown + PDF du manuel V3 (génération via Pandoc/LaTeX, voir `README_MANUAL_GENERATION.md`). Hors du site MkDocs.

### Fichiers orphelins (hors `nav`, à ne pas confondre avec le contenu actif)

`docs/faq.md` (ancien FAQ placeholder, remplacé par `docs/faq/`), `docs/guide/*` (gabarit initial), `docs/includes/image-grid.md` (vide), `docs/manual/software/web-inferface-backup.md` (sauvegarde).

## Conventions de rédaction

- Images en chemins relatifs depuis la page, ex. depuis `docs/manual/software/` : `![Alt](../../assets/kyberpad/kyberpad_main.png)`.
- Utiliser les admonitions Material (`!!! info`, `!!! note`, `!!! warning`, `??? question` repliable) — indentation de 4 espaces pour le contenu.
- Extensions activées : admonition, attr_list, def_list, footnotes, md_in_html, tables, toc, pymdownx (highlight, inlinehilite, superfences, details, snippets).
- `theme.custom_dir: docs` — les overrides de templates éventuels vivraient directement dans `docs/`.

## Points d'attention

- `pymdownx.emoji` **n'est pas activé** : les icônes `:material-...:` utilisées dans `docs/faq/index.md` s'affichent en texte brut. Pour les activer, ajouter dans `markdown_extensions` :

  ```yaml
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  ```

- `extra.css` définit une classe `.grid` (flex) qui peut entrer en conflit avec les `grid cards` de Material utilisées dans `docs/faq/index.md`.
- Le `README.md` est encore celui du gabarit (« ma-doc »).
- Le Kyberpad est un script LUA pour radios FrSky ETHOS (X18/X20/Twin X…) ; le logiciel est distribué par courriel par Stéphane Beaulieu, pas via ce dépôt.
