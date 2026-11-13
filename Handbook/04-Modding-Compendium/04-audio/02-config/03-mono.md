# audio/config/mono

The files in this folder name the game's sound effects: the sounds of clearing land and building, of work in rooms, of fighting, of people in pain, of animals and of the game's buttons. Each entry points to recordings in [audio/mono](../03-mono.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/audio/config/mono/` |
| **Files** | Any number of `.txt` files. Vanilla has eight, named by topic, such as `AA_ANIMAL.txt`, `AA_BATTLE.txt` and `AA_WORK.txt`. |
| **Adding new files** | Yes. Every `.txt` file in the folder is read, except those whose names start with `_`. |
| **Companion files** | The recordings in [audio/mono](../03-mono.md) |

## How the files work

The game reads every file in the folder and pools their entries, so which file an entry is in doesn't matter. Each entry's name is what the game asks for, and its value is a [sound path](../00-audio.md#sound-paths), or a list of them, relative to `assets/audio/mono`. Each time the sound plays, one recording from the entry is picked at random.

Each name may appear in only one file. If two files have the same name, the game stops with an error when it loads. To change a vanilla entry, put a file with the same name as the vanilla file that holds it in your mod, with just that entry: it's laid over the vanilla file, as described in [Changing a vanilla file](../../../02-Getting-Started.md#changing-a-vanilla-file). For example, this file at `V71/assets/audio/config/mono/AA_Effects.txt` changes only the sound of clearing trees:

```text
CLEAR_TREE: impact->Mine*,
```

For the sounds of a new animal, room or building material, a new file of your own works.

Some entries are named after things defined elsewhere, such as `ANIMAL_CALL_AUROCH` for the animal `AUROCH`. When you add such a thing, add its entry too, or it's silent and the game reports it as [missing](#missing-names).

## Tags

### Built-in names

These names are built into the game. Vanilla sets each of them, in `AA_Effects.txt`, `AA_Race.txt`, `AA_BATTLE.txt` or `AA_UI.txt`.

| Tag | Plays when |
|---|---|
| `CLEAR_BUSH` | A bush, wild crop or mushroom is cleared. |
| `CLEAR_GRASS` | Grass is cleared to build something. |
| `CLEAR` | A flower or a [map decoration](../../01-init/03-config/10-SETT_MAP_DECORATION.md) is cleared. |
| `CLEAR_TREE` | A tree is cut down. |
| `CLEAR_STONE` | A rock is cleared. |
| `CLEAR_STAIRS` | Stairs are removed. |
| `CLEAR_MOUNTAIN` | Mountain is dug out. |
| `CLEAR_WATER` | Water is cleared. |
| `BUILD_ROAD` | A road is built. |
| `BUILD` | A room is built. |
| `SLAUGHTER` | A hunted animal is butchered. |
| `SWORD` | A person strikes in close combat, including gladiators in an arena. |
| `ROTTING_CORPSE` | A corpse is rotting. |
| `IN_PAIN_MOAN` | An injured person moans. |
| `SICK_MOAN` | A sick person moans, including on the way to a hospital. |
| `SLEEP` | A person is asleep. |
| `BODY_EXPLODE` | A person takes heavy damage. The heavier the damage, the likelier it is to play. |
| `BATTLE_CHARGE` | A division charges, yours or the enemy's. A division doesn't sound it again straight away. |
| `UI_CLICK` | A button is clicked, once a game has loaded. |
| `UI_HOVER` | The mouse moves onto a button, once a game has loaded. |
| `UP_PLACE_DIV` | You drag out a position for divisions in the battle view. |

```text
CLEAR_TREE: impact->Axe*,
```

### Names built from keys

These names are made by adding the key of something defined elsewhere to a fixed beginning. For keys that start with `_`, the name has two underscores, as in `ROOM_WORK__STOCKPILE`.

| Tag | Plays when |
|---|---|
| `ANIMAL_CALL_<KEY>` | An [animal](../../01-init/01-animal.md#sound) of that species calls. |
| `BUILD_STRUCTURE_<KEY>` | Something made of that [structure](../../01-init/12-settlement/05-structure.md) is built. |
| `BUILD_FORTIFICATION_<KEY>` | A [fortification](../../01-init/12-settlement/04-fortification.md) of that material is built. |
| `BUILD_FENCE_<KEY>` | A [fence](../../01-init/12-settlement/02-fence.md) of that material is built. |
| `PROJECTILE_RELEASE_<KEY>` | That projectile is shot. |
| `PROJECTILE_HIT_<KEY>` | That projectile lands. |
| `ROOM_WORK_<KEY>` | A worker does that room's work. |
| `ROOM_SERVICE_<KEY>` | A visitor uses that room. Only the barber and the lavatory play this sound. |

```text
ANIMAL_CALL_AUROCH: [
	animal->Bull*,
],
```

```text
ROOM_SERVICE_LAVATORY_NORMAL: human->Fart*,
```

A projectile's key depends on where it's defined: `ROOM_` and the room's key for artillery rooms, `EQUIP_` and the file name for [ranged weapons](../../01-init/13-stats/04-equip/03-ranged.md), and `_DefaultProjectile` for [the default projectile](../../01-init/03-config/04-DefaultProjectile.md). From the vanilla `AA_PROJECTILE.txt`:

```text
PROJECTILE_RELEASE_EQUIP_BOW: swing->Arrow*, 
PROJECTILE_HIT_EQUIP_BOW: impact->Arrow*,
```

### ROOM_CLICK_&lt;KEY&gt;

Every room asks for an entry named `ROOM_CLICK_` followed by its key, but in v0.71.44 the game never plays it. Vanilla sets them all to `DUMMY`. Leaving a new room's entry out only matters because the game reports it as [missing](#missing-names).

| | |
|---|---|
| **Type** | Sound path or list of sound paths, in `assets/audio/mono` |
| **Required** | No |
| **Effect** | None |

```text
ROOM_CLICK__STOCKPILE: DUMMY,
```

## Notes

### Missing names

If the game asks for a name that no file defines, that sound is silent. The first missing name is reported only when Debug is on; each one after that is recorded as an error, and the game lists them in an error box when it closes. To give something no sound without this, add its entry with the value `DUMMY`.

### Empty lists

Vanilla gives several `ROOM_SERVICE_` entries an empty list, `[]`. That's harmless only because those rooms never play their service sound. Unverified: from the code, a sound with an empty list would stop the game with an error if it were ever played. Use `DUMMY` for silence instead.

## Related

- [audio/config](00-config.md)
- [audio/mono](../03-mono.md)
- [Sound in init/room](../../01-init/10-room/01-common.md#sound)
