# init/battle/divType

Files in `init/battle/divType` define the **division types** the game uses when it builds divisions on its own. A division type is a combination of training and equipment, such as "plate armour, short sword and shield, trained in the barracks", together with how often it should be chosen.

Division types are used whenever the game generates a division rather than the player recruiting one:

- armies raised by AI factions on the world map
- mercenaries
- raiders
- invasions of your settlement

If you add new training or equipment to the game, this is where you make AI-built armies use it. The vanilla file says as much in its opening comment.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/battle/divType/` |
| **Files** | Any number of `.txt` files. Vanilla has one, `Vanilla.txt`. |
| **Key** | None. Nothing refers to these files by name; the game loads every file in the folder and combines the types from all of them. |
| **Adding new files** | Yes. Every file in the folder is loaded, so a new file adds its types to the pool. |
| **Companion files** | None |

## File structure

Each file contains a single `TYPES` list. Each entry in the list is a block describing one or more division types:

```text
TYPES: [
	{
		OCCURENCE: 0.15,
		TRAININGS: [
			ARCHERY_VANILLA,
		],
		EQUIPMENT: {
			0: [
				BATTLE_ARMOUR_PLATE,
				RANGED_BOW,
			],
			1: [
				BATTLE_ARMOUR_LEATHER,
				RANGED_BOW,	
			],
		},
	},
],
```

This example, taken from `Vanilla.txt`, defines two division types: archers in plate armour and archers in leather armour, both trained at the archery range.

## Tags

### TYPES

The list of type blocks. Every block in the list is read using the tags below.

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | Yes |

### OCCURENCE

How often the types in this block are chosen, relative to the others. Note the game's spelling, with a single R.

The value is shared equally between the equipment sets in the block's `EQUIPMENT`. A block with `OCCURENCE: 0.5` and ten equipment sets makes ten division types, each with a weight of 0.05.

These weights aren't used exactly as written. For each race, the game multiplies each type's weight by how strong a division of that type would be, so stronger types are chosen more often than their `OCCURENCE` alone suggests.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | Not checked. Use 0 or more. |
| **Required** | Yes |

```text
OCCURENCE: 0.5,
```

### TRAININGS

The kinds of training divisions of this type have, as a list of training keys. A training key is the key of a training room in `assets/init/room/`; vanilla has `BARRACKS_VANILLA` (melee training) and `ARCHERY_VANILLA` (ranged training). A block can list both.

A key that doesn't match a training room causes a loading error.

| | |
|---|---|
| **Type** | List of keys (training rooms) |
| **Required** | No. If it's missing, the division has no training. |

```text
TRAININGS: [
	ARCHERY_VANILLA,
	BARRACKS_VANILLA,
],
```

### EQUIPMENT

The equipment sets for this block. Each entry inside the block is one equipment set and becomes a separate division type, sharing the block's `TRAININGS` and an equal share of its `OCCURENCE`.

The names of the entries don't matter. Vanilla numbers them `0`, `1`, `2` and so on, but they only need to be different from each other.

Each entry is a list of military equipment keys. These are formed from the equipment files in `assets/init/stats/equip/`:

- a file in `battle/` gives the key `BATTLE_` followed by the file name, such as `BATTLE_ARMOUR_PLATE` or `BATTLE_MOUNT`;
- a file in `ranged/` gives the key `RANGED_` followed by the file name, such as `RANGED_BOW`.

A key that doesn't match any military equipment causes a loading error.

| | |
|---|---|
| **Type** | Block of lists of keys (military equipment) |
| **Required** | Yes |

```text
EQUIPMENT: {
	0: [
		BATTLE_ARMOUR_PLATE,
		BATTLE_WEAPON_SHORT,	
		BATTLE_WEAPON_SHIELD,
		BATTLE_MOUNT,
	],
},
```

## Notes

### Which and how much

A division type only decides *which* training and equipment a division has. It doesn't decide how well trained or how well equipped the division is. Those levels are set separately by whatever is creating the division, usually with an element of chance. Mercenaries, for example, are given random levels, while raiders' levels depend on the quality of the raiding party.

### Races and equipment

Some equipment isn't available to every race. When choosing a type for a division of a particular race, the game skips any type that includes equipment that race can't use.

If no type is allowed for a race at all, the game picks a type at random and simply leaves out the equipment the race can't use.

### Keep at least one type

The game must always have at least one division type to choose from. If you use `_IgnoreVanilla.txt` to remove the vanilla file, make sure your own files define at least one type, or the game will fail when it tries to generate a division.

## Related

- [init/battle](00-battle.md)
- [init/battle/formation](02-formation.md)
