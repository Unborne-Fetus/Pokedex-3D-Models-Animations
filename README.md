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

## How the website will connect

The website at `Pokedex-3D-Max` can consume a verified manifest and its hosted GLB files **when those resources are reachable by ordinary site visitors and have suitable redistribution rights**.

This repository is intentionally **private**. Public visitors cannot load its assets directly through raw GitHub file URLs without credentials. **Never put a GitHub access token in a website, index.html, or repository.** We can connect the website to a separately authorized public asset host later without changing this storage layout.

Do not upload original Nintendo Switch game archives or distribute Nintendo game models publicly without appropriate permission.
