# audio/config/Music.txt

`Music.txt` lists the music that plays during a game: one list for peaceful times and one for battles in your settlement. The main menu's music is set separately, in [Menu.txt](02-Menu.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/audio/config/Music.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | The tracks in [audio/music](../04-music.md) |

## Tags

### NORMAL

The tracks that play while your settlement is at peace. The value is a [sound path](../00-audio.md#sound-paths), or a list of them, relative to `assets/audio/music`.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/music` |
| **Required** | No. Without it, there's no music outside battle. |

```text
NORMAL: [
	normal->*,
],
```

### BATTLE

The tracks that play while enemy soldiers are in your settlement. The value is a sound path, or a list of them, relative to `assets/audio/music`.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/music` |
| **Required** | No. Without it, battles have no music. |

```text
BATTLE: [
	battle->*,
],
```

## How the music plays

When a game loads, the game shuffles each list into a random order. It then plays the tracks one after another in that order, starting again from the top when it reaches the end.

- **Peace:** the first `NORMAL` track starts as soon as the game loads. A new track only starts during the day. At night, the current track plays to its end, and the music stays silent until morning.
- **Battle:** as soon as enemy soldiers are in your settlement, the current track fades out over a second and the `BATTLE` tracks begin, day or night.
- **After a battle:** once the enemies are gone, during the day, the battle track fades out and the `NORMAL` tracks start again after a pause of 2 to 11 seconds. At night, the battle track stops within a second, without fading, and the music waits for morning.

## Notes

### Empty lists

To have no music in one of the two situations, use `DUMMY` or leave the tag out. Unverified: an empty list, such as `NORMAL: [],`, looks from the code like it would stop the game with an error, when the game loads for `NORMAL` and when a battle starts for `BATTLE`.

## Related

- [audio/config](00-config.md)
- [audio/music](../04-music.md)
