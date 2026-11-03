# init/stats/damage

These files define the damage types used in battle. Vanilla has two, pierce and slash. Force, the game's third kind of damage, is built into the code and has no file.

Each file creates three values that other files can boost: an attack, a defence and a block.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/damage/` |
| **Files** | One `.txt` file per damage type, e.g. `PIERCE.txt` |
| **Key** | The file name, e.g. `PIERCE` |
| **Adding new damage types** | Yes |
| **Text file** | `assets/text/stats/damage/<KEY>.txt`, required |

## Tags

The examples come from the vanilla `PIERCE.txt`.

### ATTACK, DEFENCE and DEFENCE_DIR

The three values the damage type creates, each in a block of its own. All three blocks are required, and they use the same tags. Each one becomes a boost named after the file: `PIERCE` creates `BATTLE_PIERCE_ATTACK`, `BATTLE_PIERCE_DEFENCE` and `BATTLE_PIERCE_DEFENCE_DIR`.

`ATTACK` is the damage dealt. `DEFENCE` reduces incoming damage of this type, and `DEFENCE_DIR` reduces it on a successful block.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `ICON` | The value's icon, as described under [`ICON` on the init/animal page](../01-animal.md#icon). | Icon path, or a block | Yes |
| `DEFAULT_VALUE` | The value everyone starts with, before any boosts. | Decimal, 0 to 100000 | Yes |

```text
ATTACK: {
	ICON: 16->Misc->1,
	DEFAULT_VALUE: 0,
},
```

## The text file

Each damage type needs a file of the same name in `assets/text/stats/damage/`. These examples come from the vanilla `PIERCE.txt`.

### NAME

The damage type's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Pierce",
```

### ATTACK, DEFENCE and DEFENCE_DIR

The name and description of each value, in blocks matching those in the data file. All three blocks are required.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `NAME` | The value's name. | Text | Yes |
| `NAMES` | The plural of the value's name. Vanilla doesn't use it here. If it's missing, `NAME` is used. | Text | No |
| `DESC` | The value's description. | Text | Yes |
| `WIKI` | Adds an article to the in-game wiki, as described under [`WIKI` on the init/animal page](../01-animal.md#wiki). Vanilla doesn't use it here. | Block | No |

```text
ATTACK: {
	NAME: "Pierce Damage",
	DESC: "Pierce armor defends against this.",
},
```

## Notes

### Where damage types are used

Boost blocks use the three boosts above, as vanilla's armour does:

```text
BATTLE_PIERCE_DEFENCE>ADD: 1.25,
```

Projectiles name damage types by key in their [`DAMAGE`](04-equip/03-ranged.md#from-and-to) block. A race, room or other file can also boost these values like any other.

## Related

- [init/stats](00-stats.md)
- [init/stats/equip](04-equip/00-equip.md)
- [Ranged equipment](04-equip/03-ranged.md)
