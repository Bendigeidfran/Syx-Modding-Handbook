# audio/music

This folder holds the game's music. Which tracks play is set in [audio/config/Music.txt](02-config/04-Music.md) for the game itself and [audio/config/Menu.txt](02-config/02-Menu.md) for the main menu.

## At a glance

| | |
|---|---|
| **Location** | `assets/audio/music/`, and any sub-folders you make |
| **Files** | `.ogg` files (Ogg Vorbis), mono or stereo |
| **Name** | A [sound path](00-audio.md#sound-paths) relative to this folder, such as `battle->*` |
| **Adding new files** | Yes |
| **Volume slider** | Music |

## The files

Vanilla has three folders:

| Folder | Holds | Used by |
|---|---|---|
| `normal/` | The tracks that play while you build your settlement | `NORMAL` in [Music.txt](02-config/04-Music.md), as `normal->*` |
| `battle/` | The tracks that play while enemies are in your settlement | `BATTLE` in [Music.txt](02-config/04-Music.md), as `battle->*` |
| `misc/` | The main menu's music, the sound of the menu's torches, and the music for the opening logo | [Menu.txt](02-config/02-Menu.md), by full name |

`misc/script/Tutorial.ogg` is the music for the tutorial campaign's opening scene. It's named by the scene's `MUSIC` tag, in the campaign's file in `data/campaigns` (see [text/campaign](../02-text/02-campaign.md)). Only the first file such a path names is played.

Vanilla's `misc/_Menu.ogg` and `misc/_Menu_New2.ogg` aren't named by any of vanilla's files, so they never play.

A file that isn't Ogg Vorbis stops the game with an error when it's loaded. So does one with more than two channels.

## Adding music

Because vanilla's `Music.txt` takes every file in `normal/` and `battle/`, a mod can add tracks just by putting `.ogg` files in its own `assets/audio/music/normal/` or `assets/audio/music/battle/`. They're played alongside vanilla's tracks.

To play only your own tracks, also put an `_IgnoreVanilla.txt` in that folder: see [Hiding vanilla files](../../02-Getting-Started.md#hiding-vanilla-files). Alternatively, point `Music.txt` at a folder of your own.

## Related

- [audio](00-audio.md)
- [audio/config/Music.txt](02-config/04-Music.md)
- [audio/config/Menu.txt](02-config/02-Menu.md)
