# MagicForge Studio — Official Site

Futuristic single-page studio profile for **MagicForge Studio**, makers of **MagicMath** and **Star Saviours**.
Self-contained `index.html` (no build step, no dependencies) — ready for GitHub Pages.

## Deploy to GitHub Pages

1. Create a new public repo on GitHub, e.g. `magicforge-studio`.
2. From this folder:
   ```bash
   git init
   git add .
   git commit -m "MagicForge Studio site"
   git branch -M main
   git remote add origin https://github.com/komzakdroid/magicforge-studio.git
   git push -u origin main
   ```
3. GitHub → repo → **Settings → Pages** → Source: `main` / `/ (root)` → Save.
4. Live in ~1 min at: `https://komzakdroid.github.io/magicforge-studio/`

Put that URL in the Google Play payment profile **"Веб-сайт"** field.

## Games featured

- **Star Saviors** (`com.komzak.starsaviors`) — pixel-art cosmic platformer, 300 levels, 5 heroes, 5 worlds.
- **MagicMath** (`com.komzak.magicmath`) — cross-math puzzle, 5 modes, 120 levels, 3 languages.

Real Play Store key art, icons and screenshots live in `assets/` (copied from each game's `play-store-assets`).

## ⚠️ Before going public — verify the Play Store links

Both store links point to:
`https://play.google.com/store/apps/details?id=<package>`

If a game is **not yet live** (still in review / draft), that link 404s. Options:
- Wait until the listing is published, **or**
- Temporarily change the button to "Coming soon" (in `index.html`, search the `gp-btn` / `pricepill` near each game).

## Customize

- **Stats** — edit the `.stats` block in the hero (honest figures, no fake download counts).
- **Game copy / tags / features** — edit the `<article class="game">` blocks.
- **Screenshots** — replace files in `assets/` (keep the same names) or add more `<img>` to `.shots`.
- **Colors** — all design tokens live in `:root { ... }` at the top of `<style>`.
- **Studio fact sheet** — edit the `.factsheet` rows in the Studio section.

## Stack

Plain HTML + CSS + vanilla JS. Fonts: Space Grotesk + Sora (Google Fonts). Canvas ember-particle background, scroll-reveal via IntersectionObserver. Fully responsive, dark, SEO + Open Graph tags included.
