# init/room: military rooms

These rooms train and supply your soldiers, and defend your walls: archery ranges, barracks, artillery and the supply depot. Besides the tags on this page, they use the [common tags](01-common.md), and those with workers use [employment](02-employment.md).

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | `ARCHERY_*.txt`, `BARRACKS_*.txt`, `ARTILLERY_*.txt` and `_MILITARY_SUPPLY.txt` |
| **Adding new rooms** | Yes for archery ranges, barracks and artillery. `_MILITARY_SUPPLY` is a single room. |
| **Text file** | `assets/text/room/<KEY>.txt` |

## ARCHERY

An archery range trains soldiers. It uses an `EMPLOYMENT` block rather than `WORK`. It has exactly one `ITEMS` block, the training targets (at least one per room), and one statistic.

The examples come from the vanilla `ARCHERY_VANILLA.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: ARCHERY,
```

### DIV_SPRITE

How a division in this training is marked in the interface.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
DIV_SPRITE: {
	ICON: 16->Misc->5,
	COLOR: [
		175_112_66,
		200_200_200,
		255_190_0,
	],
},
```

#### ICON

The icon, as an icon path.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path |
| **Required** | No. Without it, the game uses a standard icon. |

```text
ICON: 16->Misc->5,
```

#### COLOR

The colours, as a list of `RED_GREEN_BLUE` values.

| | |
|---|---|
| **Type** | List of colours |
| **Required** | Yes |

```text
175_112_66,
```

### TRAINING

What the training does.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
TRAINING: {
	FULL_TRAINING_IN_DAYS: 100,
	BOOST: {
		BATTLE_RANGED_BOW>ADD: 1,
		BATTLE_MORALE>MUL: 1.0,
	},
},
```

#### FULL_TRAINING_IN_DAYS

How many days of training give a soldier full training, before bonuses. Soldiers first complete a basic training of 10 days.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked. It shouldn't be 0, because the game divides by it. |
| **Required** | Yes |

```text
FULL_TRAINING_IN_DAYS: 100,
```

#### BOOST

What the training gives, in the same form as a race's [`BOOST`](../07-race/01-race-file.md#boost) block.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BATTLE_RANGED_BOW>ADD: 1,
```

#### BONUS

Multiplies the speed of training by climate, in the same form as a room's [`BONUS`](02-employment.md#bonus). Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `TARGET_1X1` | The targets. | `1x1` |
| `LANE_1X1` | The lanes. | `1x1` |
| `PLATFORM_1X1` | The platform archers stand on. | `1x1` |
| `TABLE_1X1` | The table. | `1x1` |
| `FENCE_COMBO` | The fence. | `combo` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## BARRACKS

Barracks train soldiers in the same way as an archery range. They use an `EMPLOYMENT` block rather than `WORK`. They have exactly one `ITEMS` block, the training dummies (at least one per room), and one statistic.

The examples come from the vanilla `BARRACKS_VANILLA.txt`.

### TYPE

The game never reads this tag here.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
TYPE: BARRACKS,
```

### FULL_TRAINING_IN_DAYS

The game never reads this tag at the top level of the file. It reads the one inside `TRAINING`.

| | |
|---|---|
| **Type** | Integer |
| **Required** | No |
| **Effect** | Unread |

```text
FULL_TRAINING_IN_DAYS: 100,
```

### RACE_PREFERENCE

The game never reads this tag.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | No |
| **Effect** | Unread |

```text
RACE_PREFERENCE: 0.7,
```

### SERVICE

The game never reads this block for barracks.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |
| **Effect** | Unread |

### DIV_SPRITE

How a division in this training is marked in the interface.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
DIV_SPRITE: {
	ICON: 16->Misc->4,
	COLOR: [
		175_112_66,
		200_200_200,
		255_190_0,
	],
},
```

#### ICON

The icon, as an icon path.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path |
| **Required** | No. Without it, the game uses a standard icon. |

```text
ICON: 16->Misc->4,
```

#### COLOR

The colours, as a list of `RED_GREEN_BLUE` values.

| | |
|---|---|
| **Type** | List of colours |
| **Required** | Yes |

```text
175_112_66,
```

### TRAINING

What the training does.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

```text
TRAINING: {
	FULL_TRAINING_IN_DAYS: 100,
	BOOST: {
		BATTLE_OFFENCE_SKILL>MUL: 2.0,
		BATTLE_DEFENCE_SKILL>MUL: 2.0,
		BATTLE_FORMATION_SKILL>ADD: 1,
		BATTLE_BLUNT_ATTACK>MUL: 1.25,
		PHYSICS_STAMINA>MUL: 1.5,
		BATTLE_MORALE>ADD: 4.0,
	},
},
```

#### FULL_TRAINING_IN_DAYS

How many days of training give a soldier full training, before bonuses. Soldiers first complete a basic training of 10 days.

| | |
|---|---|
| **Type** | Integer |
| **Range** | Not checked. It shouldn't be 0, because the game divides by it. |
| **Required** | Yes |

```text
FULL_TRAINING_IN_DAYS: 100,
```

#### BOOST

What the training gives, in the same form as a race's [`BOOST`](../07-race/01-race-file.md#boost) block.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BATTLE_MORALE>ADD: 4.0,
```

#### BONUS

Multiplies the speed of training by climate, in the same form as a room's [`BONUS`](02-employment.md#bonus). Vanilla doesn't use this tag.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `MANAKIN_A_1X1` | The training dummies. | `1x1` |
| `MANAKIN_B_1X1` | The training dummies, drawn over the first. | `1x1` |
| `PODEUM_BOX` | The podium. Note the game's spelling. | `box` |
| `TABLE_1X1` | The table. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## ARTILLERY

An artillery piece fires at enemies. It has no workers of its own. It has exactly one `ITEMS` block (at least one per room) and no statistics.

The examples come from the vanilla `ARTILLERY_CATAPULT.txt`.

### PROJECTILE_RESOURCE

The resource it fires, by its key.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
PROJECTILE_RESOURCE: STONE,
```

### SOUND_WORK

The game never reads this tag.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
SOUND_WORK: CATAPULT_WORK,
```

### PROJECTILE

What it fires. The format is the same as [DefaultProjectile.txt](../03-config/04-DefaultProjectile.md), which has fuller descriptions. `FROM` and `TO` are both required and hold the same tags. The sounds come from the audio entries `PROJECTILE_RELEASE_ROOM_<KEY>` and `PROJECTILE_HIT_ROOM_<KEY>`.

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `SPRITE_FILE` | The projectile's image, in `assets/sprite/settlement/projectile/`. | Key | No |
| `COLOR` | A colour applied to the projectile. | Colour | Yes |
| `TILE_SPEED` | How fast it flies, in `FROM` and `TO`. | Decimal, 0.5 to 250 | Yes |
| `MASS` | How heavy it is, in `FROM` and `TO`. | Decimal, 0.01 to 100000 | Yes |
| `DAMAGE` | Damage by type, in `FROM` and `TO`. | Block of decimals, each value 0 to 100000 | No |
| `TILE_RADIUS_DAMAGE` | The radius of its damage, in `FROM` and `TO`. | Decimal, 0 to 10000 | No. Default `0`. |
| `MAX_ARCH_ANGLE_DEGREES` | The highest angle it can be fired at, in `FROM` and `TO`. | Decimal, 0 to 75 | Yes |
| `ACCURACY` | How accurate it is, in `FROM` and `TO`. | Decimal, 0.01 to 1 | Yes |
| `RELOAD_SECONDS` | The time between shots, in `FROM` and `TO`. | Decimal, 0.01 to 10000 | Yes |

| Tag | Meaning | Effect |
|---|---|---|
| `DEXTERITY` | Read, but nothing uses it. In `FROM` and `TO`, where it must be 0 to 10000000. | None |

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `BASE_2X2` | The base. | `2x2` |
| `BASE_ROT_2X2` | The rotating part of the base. | `2x2` |
| `ARM_2X2` | The arm. | `2x2` |
| `ARM_ROT_2X2` | The rotating part of the arm. | `2x2` |
| `TORCH_1X1` | The torches. | `1x1` |
| `STORAGE_1X1` | The storage. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## _MILITARY_SUPPLY

The supply depot, which sends [supplies](../09-resource/06-supply.md) to your armies. It has exactly one `ITEMS` block, the crates, and two statistics.

The examples come from the vanilla `_MILITARY_SUPPLY.txt`.

### FLOOR2

A second floor, by its key.

| | |
|---|---|
| **Type** | Key (a floor) |
| **Required** | Yes |

```text
FLOOR2: DIRT,
```

### LIVESTOCK

The resource the depot uses up when delivering supplies, by its key: one for every 10th trip.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
LIVESTOCK: LIVESTOCK,
```

### FENCE

The game never reads this tag. The depot's fence is drawn by its `SPRITES`.

| | |
|---|---|
| **Type** | Key |
| **Required** | No |
| **Effect** | Unread |

```text
FENCE: BARRICADE,
```

### SPRITES

The images the room is drawn with. Each name is a required [sprite entry](../../03-sprite/03-game.md#sprite-entries) of the kind its name ends with.

| Tag | What it draws | Kind of sheet |
|---|---|---|
| `FENCE_COMBO` | The fence. | `combo` |
| `TORCH_1X1` | The torches. | `1x1` |
| `OVERLAY_1X1` | A marker over the crates. | `1x1` |

| | |
|---|---|
| **Type** | Block of sprite entries |
| **Required** | Yes |

## The text file

Archery ranges and barracks also need a `TRAINING` block in their text file. These examples come from the vanilla `BARRACKS_VANILLA.txt`.

### TRAINING

The name and description of the training.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes, for archery ranges and barracks |

#### NAME

The training's name.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

```text
NAME: "Melee Training",
```

#### DESC

The training's description.

| | |
|---|---|
| **Type** | Text |
| **Required** | Yes |

## Related

- [init/room](00-room.md)
- [Common tags](01-common.md)
- [Employment](02-employment.md)
- [init/config/DefaultProjectile.txt](../03-config/04-DefaultProjectile.md)
- [init/resource/supply](../09-resource/06-supply.md)
