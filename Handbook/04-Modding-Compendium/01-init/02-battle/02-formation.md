# init/battle/formation

Files in `init/battle/formation` decide how armies are lined up at the start of a battle. Before the fighting begins, the game places every division on the battlefield automatically. A formation file tells it which kinds of division it would prefer in each part of the line: the centre, the flanks, the front and the rear.

Your own army is always placed using `_player.txt`. The enemy army uses one of the other files, chosen at random for each battle.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/battle/formation/` |
| **Files** | `_player.txt`, plus any number of other `.txt` files. Vanilla has `Alphastrike`, `Heavyflank`, `Rush`, `Standard`, `Test` and `Wave`. |
| **Key** | None. Nothing refers to these files by name. |
| **Adding new files** | Yes. Every file other than `_player.txt` is added to the pool the enemy's formation is drawn from. |
| **Companion files** | None |

Because `_player.txt` starts with an underscore, it's loaded only by its exact name and is never part of the enemy's pool. You can replace it, but not add a second player formation.

Note that vanilla's `Test.txt` is an ordinary formation file, so the enemy can be given it like any other.

## How placement works

The game places divisions outward from the middle of the army, working from the front row backwards. Every spot on the field has four position weights depending on where it is: how central it is, how far out on the flank, how far forward and how far back.

Each division gets four scores, one for each part of the line, worked out from the formation's priority tags (below). To fill a spot, the game multiplies each of the division's scores by the matching position weight, adds them up, and places the division with the highest total. That division is then removed from the pool, and the process repeats for the next spot.

So a formation doesn't place specific divisions. It says what kind of division is wanted where, and the game sorts the actual divisions to fit.

## Tags

A formation file contains eight blocks. All eight work the same way: each entry names something about a division and gives it a weight. Positive weights attract divisions with more of that thing towards that part of the line; negative weights push them away.

The four blocks without `_E` score divisions by their **stats**. The four ending in `_E` score them by their **equipment**.

### PRIORITY_CENTRE, PRIORITY_FLANK, PRIORITY_FRONT, PRIORITY_REAR

How strongly each stat draws a division to the centre, the flanks, the front or the rear.

Each entry is a stat key and a weight. For every entry, the division's score for that part of the line goes up by the weight multiplied by the division's value for that stat, divided by one more than the stat's starting value. This dividing step scales down stats that naturally have large values, so their weights don't swamp the others.

Stat keys are the game's boostable stats. Those used in vanilla formations are:

| Key | Stat |
|---|---|
| `PHYSICS_SPEED` | Movement speed |
| `BATTLE_CHARGE` | Charge |
| `BATTLE_OFFENCE_SKILL` | Offence skill |
| `BATTLE_PIERCE_ATTACK`, `BATTLE_SLASH_ATTACK` | Attack with that damage type |
| `BATTLE_PIERCE_DEFENCE` | Defence against that damage type |
| `BATTLE_BLUNT_DEFENCE_DIR` | Force block |
| `BATTLE_RANGED_BOW` | Bow skill |

Any boostable stat can be used. A key that doesn't match one produces a warning, and that entry is ignored.

| | |
|---|---|
| **Type** | Block of decimals, keyed by stat |
| **Range** | Not checked. Negative values are allowed and used in vanilla. |
| **Required** | No. A missing or empty block adds nothing to that part of the line. |

From `Standard.txt`:

```text
PRIORITY_FLANK: {
	PHYSICS_SPEED: 2,
	BATTLE_PIERCE_ATTACK: 1,
	BATTLE_SLASH_ATTACK: 1,
	BATTLE_CHARGE : 5,
	BATTLE_RANGED_BOW: -1,
},
```

This draws fast, hard-hitting divisions that are good at charging out to the flanks, and keeps archers away from them.

### PRIORITY_CENTRE_E, PRIORITY_FLANK_E, PRIORITY_FRONT_E, PRIORITY_REAR_E

The same as the blocks above, but scoring divisions by their equipment instead of their stats. Each entry is a military equipment key and a weight. The division's score goes up by the weight multiplied by how well the division is equipped with that item.

Equipment keys are the same as in division types: `BATTLE_` or `RANGED_` followed by the name of a file in `assets/init/stats/equip/battle/` or `ranged/`, for example `BATTLE_MOUNT` or `RANGED_BOW`. A key that doesn't match produces a warning, and that entry is ignored.

| | |
|---|---|
| **Type** | Block of decimals, keyed by military equipment |
| **Range** | Not checked. Negative values are allowed and used in vanilla. |
| **Required** | No |

From `Standard.txt`:

```text
PRIORITY_REAR_E: {
	BATTLE_MOUNT: -100,
},
```

This strongly keeps mounted divisions out of the rear.

## Notes

### Stats and equipment with similar names

`BATTLE_RANGED_BOW` and `RANGED_BOW` are different things. `BATTLE_RANGED_BOW` is a stat, the division's skill with bows, and belongs in the blocks without `_E`. `RANGED_BOW` is the bow itself, as equipment, and belongs in the `_E` blocks.

### The legend at the top of vanilla files

Most vanilla formation files begin with lines like these:

```text
** ME = Strong melee damage
** AR = Strong health and armour
** SP = fast troops
** RA = ranged troops
** __ = nothing
```

They're comments, so the game ignores them.

### Keep at least one enemy formation

The enemy's formation is chosen from the files other than `_player.txt`, so there must always be at least one. If you use `_IgnoreVanilla.txt` to remove the vanilla formations, make sure you provide at least one of your own, or the game will fail when it sets up a battle.

## Related

- [init/battle](00-battle.md)
- [init/battle/divType](01-divType.md)
