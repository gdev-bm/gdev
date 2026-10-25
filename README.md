# gdev

The [gdev.bm](https://gdev.bm) site: a static Astro site showcasing projects.

```sh
npm install
npm run dev      # http://localhost:4321
npm run build    # static site in dist/
```

## Adding a project

Each project is one Markdown file in `src/content/projects/`, with its fields defined in `src/content.config.ts`. Images go in `src/assets/projects/<slug>/` and are optimised at build time. Looping videos go in `public/media/<slug>/` as `loop.mp4` (H.264, 720p, no audio) with a `poster.jpg` beside it.

Featured projects (`featured: true`) get a large video card on the home page; the rest appear under "Earlier work", in `order`.
