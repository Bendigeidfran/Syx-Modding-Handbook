# audio/mono

This folder holds the game's sound effects: short recordings such as the sounds of work, animal calls, sword blows and button clicks. Which recording plays for what is set in [audio/config/mono](02-config/03-mono.md), and the main menu's button sounds in [audio/config/Menu.txt](02-config/02-Menu.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/audio/mono/`, and any sub-folders you make |
| **Files** | `.wav` files: mono, 8-bit or 16-bit, at most 10 seconds long |
| **Name** | A [sound path](00-audio.md#sound-paths) relative to this folder, such as `impact->Axe*` |
| **Adding new files** | Yes |
| **Volume slider** | Effects |

## The files

The game checks each file when it loads it, and stops with an error if the file:

- isn't a `.wav` file,
- has two channels ("stereo sounds can't be sound effects"), or more,
- uses a sample size other than 8 or 16 bits, or
- is longer than 10 seconds.

Convert stereo recordings to mono before adding them.

Vanilla sorts its effects into folders such as `animal`, `battle`, `gore`, `gui`, `human`, `impact`, `misc`, `swing` and `work`, and keeps similar recordings together with numbered names (`Axe_000`, `Axe_001`, …) so that a `*` path like `impact->Axe*` picks them all up. The folders are only for keeping things tidy: a new file can go anywhere in `assets/audio/mono/`, as long as the path in the config file matches.

## How effects are played

Sounds in your settlement, such as work, fighting and animal calls, are played at their place on the map. Each time, the game picks a random recording from the entry. Most are played at a slightly random pitch (between 0.7 and 1.3 times normal) and volume (80% to 100%). They don't play while the world map is open.

Interface sounds, such as button clicks, play at normal pitch and volume.

## Related

- [audio](00-audio.md)
- [audio/config/mono](02-config/03-mono.md)
- [audio/config/Menu.txt](02-config/02-Menu.md)
