# Pokedex 3D Models & Animations

Private asset storage for [Pokedex 3D Max](https://github.com/Unborne-Fetus/Pokedex-3D-Max).

The model repository contains converted **regular Pokémon** GLB files organized by National Pokédex number:

```text
0001/regular.glb
0002/regular.glb
...
```

A GLB normally includes its material textures and animation clips; those do not need separate folders.

## No-billing model catalog

GitHub Actions is **not required** and has been removed from this repository.

There are two no-command options:

1. Open the updated `Pokedex-3D-Max/index.html` in Chrome/Edge.
2. Click **Open Switch model folder** and select the local folder containing the converted `switch/0001/regular.glb` files.
3. The browser checks the model structures, texture bindings, animations, and idle clips on your computer.
4. Click **Export model catalog**. The browser downloads `switch-manifest.json`.
5. In this private GitHub repository, use **Add file → Upload files** to upload that JSON using the GitHub website. Make sure the listed model files have also been uploaded.

The uploaded JSON is only a structural catalog; it cannot guarantee visually correct Switch shader colors, transparency, or legal redistribution rights. The previously committed `uploaded-model-inventory.json` lists existing uploaded filenames without claiming they passed material inspection.

The optional `scripts/build_model_manifest.py` remains for developers with a local Python environment, but no command-line tools or paid build service are needed for the browser workflow.

## GitHub Pages website (no billing)

The standalone 3D Pokédex is already at the **repository root** as `index.html`
and `web/`. All 756 numbered GLBs also live at the root, so GitHub Pages
can serve the website and models from the same HTTPS origin without exposing
credentials or fetching assets from another site.

To make the site available, on GitHub open:
**Settings → Pages → Build and deployment → Source: Deploy from a branch →
Branch: main → Folder: / (root) → Save**.

After GitHub has finished the Pages deployment, its expected URL is:

https://unborne-fetus.github.io/Pokedex-3D-Models-Animations/

No commands, payment information, GitHub Actions workflow, installer, or local
folder selection is needed for visitors. The website includes a bundled local copy of the model-viewer JavaScript
library. It discovers the public file inventory automatically and downloads
each selected GLB from the same GitHub Pages site. Before rendering, it checks
that the file has embedded base-color textures and an identifiable idle
animation.

**Current coverage:** 756 uploaded regular GLBs. The original 903-model local
import had more models. The website does not invent replacements for gaps.

GitHub raw-file hosting is convenient for a prototype, but it is not a
guaranteed high-bandwidth CDN; GitHub can rate-limit or change delivery
behavior. If public traffic increases, authorized static model hosting may
be needed. Original shader color/transparency defects cannot be fixed by
the website's structural checks.

Before redistributing Nintendo Switch game assets, make sure you have the
appropriate rights; changing repository visibility to public does not grant
permission.
