# How to Use This Handbook

> **Website and PDF:** this handbook is available as a website at <https://bendigeidfran.github.io/syx-modding-handbook/> and as a PDF. Both are built from the same pages, so they always contain the same information.
>
> If you found the PDF on Google Drive, download it and open it in your web browser (or any PDF reader) rather than reading it in Drive's preview. Drive's preview doesn't support links within the document, so the contents page and the page titles, which link to each other, won't work there.

## How it's organised

The handbook has three main parts.

**Getting Started** walks you through setting up a mod from scratch: where mods live, how the game identifies them, and how a mod's folders are laid out. It's meant to be read in order, and by the end you'll have a mod set up that the game recognises, ready for you to fill with content.

**Your First Mod** is a step-by-step walkthrough that builds a complete mod, a new playable race, using what Getting Started covers.

**The Modding Compendium** covers the game's moddable files one area at a time. Its structure mirrors the game's own `assets` folder, so if you know where a file sits in the game, you know where to find it in the handbook. Each entry explains what the file controls, what its tags do, and how it relates to other files.

## Suggested reading path

If you're new to modding, read Getting Started from beginning to end before doing anything else. The concepts it introduces, especially how the game finds and loads your files, come up throughout the rest of the handbook. Then work through Your First Mod to put them into practice.

After that, use the Modding Compendium as you need it. There's no need to read it cover to cover. Look up the files that relate to whatever you're making, and follow the links to related entries as they come up.

## Conventions

A few conventions are used throughout:

- **File and folder paths** are written in code formatting, for example `assets/init/race`. Paths are relative to the game's data folder or your mod's folder, depending on context, and the text will say which.
- **Tags and values** from game files are also written in code formatting, for example `SPRITE` or `1.0`.
- **Longer excerpts** from game files appear in code blocks:

  ```text
  NAME: "My Mod",
  ```

- **Spelling is reproduced exactly.** Tag names, file names and values are copied as the game writes them, including any unusual spelling or capitalisation. The game reads these literally, so a "corrected" spelling won't work.
- **Names are case sensitive.** `Race.txt` and `RACE.txt` are different files as far as the game is concerned. When in doubt, match the capitalisation of the game's own files.

## A note on versions

Songs of Syx is still in active development, and its modding system changes between versions. Everything in this handbook was checked against **v0.71.44**.

Game versions are written as `0.MAJOR.MINOR`. In v0.71.44, the major version is `71` and the minor version is `44`. The major version matters most to modders: a mod's files are stored in a folder named after the major version they were made for, and the launcher marks a mod as outdated if it wasn't made for the major version you're running. Outdated mods can still be enabled, but they often fail to load or cause errors, because files and tags change between major versions. Getting Started covers this in detail.

If you're using a different version of the game, most of what's here will still apply in broad terms, but specific files and tags may differ. When the handbook and the game disagree, the game's own files are the final authority.

## Licence

This handbook is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). You're free to share and adapt it, as long as you credit the author and release your adapted version under the same licence.
