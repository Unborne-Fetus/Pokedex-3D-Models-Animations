# Pokedex 3D Models & Animations

Private asset storage for [Pokedex 3D Max](https://github.com/Unborne-Fetus/Pokedex-3D-Max).

The model repository contains converted **regular Pokémon** GLB files organized by National Pokédex number:

```text
0001/regular.glb
0002/regular.glb
...
```

A GLB normally includes its material textures and animation clips; those do not need separate folders.

## Verified model catalog

A GitHub Actions workflow scans the GLB headers, mesh/material texture links, and idle animation clips and maintains `switch-manifest.json` automatically. It does **not** modify any model files, convert assets, or restore missing original files. A model is only added to the manifest if it passes those structural checks. Visual fidelity still requires an in-browser inspection.

The existing files may include some models with incorrect shader colors/transparency, which structural validation alone cannot detect. Keep the original import files until those problems are resolved.

## How the website will connect

The website at `Pokedex-3D-Max` can consume a verified manifest and its hosted GLB files **when those resources are reachable by ordinary site visitors and have suitable redistribution rights**.

This repository is intentionally **private**. Public visitors cannot load its assets directly through raw GitHub file URLs without credentials. **Never put a GitHub access token in a website, index.html, or repository.** We can connect the website to a separately authorized public asset host later without changing this storage layout.

Do not upload original Nintendo Switch game archives or distribute Nintendo game models publicly without appropriate permission.
