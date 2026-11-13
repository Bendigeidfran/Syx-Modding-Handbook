# audio/config/ambience

The files in this folder name the ambient sounds of your settlement: the sound of plants, water, wind, rain, thunder and caves, and an optional sound for each type of room. Each entry points to recordings in [audio/ambience](../01-ambience.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/audio/config/ambience/` |
| **Files** | Any number of `.txt` files. Vanilla has `Ambiance.txt` and `Room.txt`. |
| **Adding new files** | Yes. Every `.txt` file in the folder is read, except those whose names start with `_`. |
| **Companion files** | The recordings in [audio/ambience](../01-ambience.md) |

## How the files work

The game reads every file in the folder and pools their entries, so which file an entry is in doesn't matter. Each entry's name is what the game asks for, and its value is a [sound path](../00-audio.md#sound-paths), or a list of them, relative to `assets/audio/ambience`.

Each name may appear in only one file. If two files have the same name, the game stops with an error when it loads. To change a vanilla entry, put a file with the same name as the vanilla file that holds it (`Ambiance.txt` or `Room.txt`) in your mod, with just that entry: it's laid over the vanilla file, as described in [Changing a vanilla file](../../../02-Getting-Started.md#changing-a-vanilla-file). To add room sounds for a new room, a new file of your own works.

## Tags

The first eight names are built into the game, and vanilla sets them all in `Ambiance.txt`. The game only turns them up while it's drawing your settlement.

### NATURE

Plays during the day while plants are on screen, unless it's raining. It's quieter the further you zoom out.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes. See [Missing names](#missing-names). |

```text
NATURE: [
	nature->Nature,
],
```

### WIND

Wind heard from high up. It's silent when you're fully zoomed in, and grows louder the further you zoom out and the stronger the wind blows.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes |

```text
WIND: [
	nature->Wind,
],
```

### NIGHT

Takes the place of `NATURE` at night: it plays while plants are on screen, unless it's raining, and it's quieter the further you zoom out.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes |

```text
NIGHT: [
	nature->Night,
],
```

### WATER

Plays while water is on screen. The more of the screen is water, the louder it is, and it's quieter the further you zoom out.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes |

```text
WATER: [
	nature->Water,
],
```

### RAIN

Plays while it's raining, but not while it snows or while the game is paused. The harder the rain, the louder it is.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes |

```text
RAIN: [
	nature->Rain,
],
```

### WIND_TREES

Wind in the plants. It plays while plants are on screen, unless it's raining, and the stronger the wind, the louder it is.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes |

```text
WIND_TREES: [
	nature->WindTrees,
],
```

### CAVE

Plays while cave floor is on screen. The more of the screen it covers, the louder it is, and it's quieter the further you zoom out.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes |

```text
CAVE: [
	nature->Cave1,
	nature->Cave2,
],
```

### THUNDER

Thunder claps during a thunderstorm. Unlike the others, a thunder clap isn't a continuous sound: every second or two, scaled by how much thunder there is, the game plays one file from the list once. A `*` path to a folder of separate claps, as vanilla uses, gives variety.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | Yes |

```text
THUNDER: [
	nature->thunder->*,
],
```

### ROOM_&lt;KEY&gt;

A sound for one type of room, named `ROOM_` followed by the room's key, such as `ROOM_FARM_GRAIN`. For rooms whose key starts with `_`, the name has two underscores: `ROOM__STOCKPILE`. It plays while rooms of that type are on screen, louder the more of the screen they cover.

Every room asks for its entry. Vanilla lists every vanilla room in `Room.txt`, all set to `DUMMY`, so no room has an ambient sound. Unverified: because vanilla never uses it, how a room sound behaves in the game hasn't been tested.

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/ambience` |
| **Required** | No. A missing entry gives silence, but is reported as described in [Missing names](#missing-names). |

```text
ROOM__STOCKPILE: DUMMY,
```

## Notes

### How many play at once

At most five ambient sounds play at once, not counting thunder. When more are wanted, the game picks the five that matter most, which mostly means those covering the most of the screen. Rain counts as covering the whole screen. Each sound fades in and out by up to a second when it starts or stops.

### When sounds stop

The tags above describe when the game turns each sound up. Each time the settlement is drawn, the game turns every ambient sound down by an amount that depends on how far you're zoomed out, and then turns up the ones that apply. Unverified: when you're fully zoomed in, that amount is zero, so a sound that the game has stopped turning up isn't lowered. `WATER`, `CAVE` and `WIND` are set afresh every time and aren't affected. From the code, `NATURE` may go on playing at night alongside `NIGHT`, `RAIN` after the rain stops, and a room sound may keep growing, until you zoom out. This hasn't been tested in the game.

### Missing names

If the game asks for a name that no file defines, the first missing name is reported only when Debug is on; each one after that is recorded as an error, and the game lists them in an error box when it closes. A missing room sound is simply silent. Unverified: if one of the first eight names is missing, the code looks like it would stop the game with an error as soon as the settlement is shown. Vanilla's entries can't be removed by layering, so this only matters if a mod hides vanilla's `Ambiance.txt` with `_IgnoreVanilla.txt`.

### Other users

The [`SOUND_AMBIENT`](../../01-init/05-event/03-actions.md#sound_ambient) event action plays recordings from `audio/ambience` by sound path. It doesn't use the names on this page.

## Related

- [audio/config](00-config.md)
- [audio/ambience](../01-ambience.md)
- [Sound in init/room](../../01-init/10-room/01-common.md#sound)
