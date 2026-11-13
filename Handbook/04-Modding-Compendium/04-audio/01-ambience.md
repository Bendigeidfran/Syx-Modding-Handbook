# audio/ambience

This folder holds the recordings for ambient sound: the background of birdsong, wind, water, rain and thunder that changes with what's on screen in your settlement. Which recording plays when is set in [audio/config/ambience](02-config/01-ambience.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/audio/ambience/`, and any sub-folders you make |
| **Files** | `.ogg` files (Ogg Vorbis), mono or stereo |
| **Name** | A [sound path](00-audio.md#sound-paths) relative to this folder, such as `nature->Rain` |
| **Adding new files** | Yes |
| **Volume slider** | Ambience |

## The files

Vanilla keeps its ambient sounds in `nature/`, with the thunder claps in `nature/thunder/`. The folders are only for keeping things tidy: a new file can go anywhere in `assets/audio/ambience/`, as long as the path in the config file matches.

An ambient sound isn't looped. When a recording ends and the sound is still wanted, the game starts another file picked at random from the same entry. Each recording starts silent and fades up to its volume, by at most a second, so there's a short dip between one recording and the next.

A file that isn't Ogg Vorbis stops the game with an error when it's loaded. So does one with more than two channels.

Vanilla's `nature/Earthquake.ogg` isn't named by any of vanilla's config files, so it never plays.

## Notes

### Other users

The [`SOUND_AMBIENT`](../01-init/05-event/03-actions.md#sound_ambient) event action plays files from this folder directly, by sound path, without an entry in the config files.

## Related

- [audio](00-audio.md)
- [audio/config/ambience](02-config/01-ambience.md)
