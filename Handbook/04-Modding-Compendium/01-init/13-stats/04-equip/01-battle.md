# init/stats/equip/battle

These files define the armour, melee weapons, shields and mounts your soldiers can use. Players choose how much of each a division carries, and [division types](../../02-battle/01-divType.md#equipment) name the same equipment.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/equip/battle/` |
| **Files** | One `.txt` file per item, e.g. `ARMOUR_PLATE.txt` |
| **Key** | `BATTLE_` and the file name, e.g. `BATTLE_ARMOUR_PLATE` |
| **Adding new equipment** | Yes |
| **Text file** | None. The name, description and icon come from the resource. |
| **Sprite** | Optional, an image in `assets/sprite/race/battle/`, named by `SPRITE.FILE` |

## Tags

The examples come from the vanilla `MOUNT.txt` unless stated otherwise.

### RESOURCE

The resource this equipment is made from, by its key. A resource that's also an army [supply](../../09-resource/06-supply.md) stops the game with an error.

| | |
|---|---|
| **Type** | Key (a resource) |
| **Required** | Yes |

```text
RESOURCE: WEAPON_MOUNT,
```

### WEAR_RATE

How much of this equipment wears out each year, for each item carried. At `0.1`, a soldier carrying 5 goes through about one every two years.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 100 |
| **Required** | Yes |

```text
WEAR_RATE: 0.1,
```

### MAX_AMOUNT

The most a soldier can carry.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 15 but doesn't enforce it. Stay at or below 15, because the amount is stored in a space that only holds up to 15. |
| **Required** | Yes |

```text
MAX_AMOUNT: 5,
```

### ARRIVAL_AMOUNT

How much of this equipment new immigrants arrive with.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names `MAX_AMOUNT` as the maximum but doesn't enforce it. A higher value is capped at `MAX_AMOUNT` when it's applied. |
| **Required** | Yes |

```text
ARRIVAL_AMOUNT: 0,
```

### DEFAULT_TARGET

The game reads this tag here, but only civic equipment uses it. The tag must still be present.

| | |
|---|---|
| **Type** | Integer |
| **Required** | Yes |
| **Effect** | None |

```text
DEFAULT_TARGET: 0,
```

### ADD_TO_FORMATION_SIZE

Extra room each soldier takes up in formation. If a division carries several items with this tag, the largest value applies.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names a maximum of 100 but doesn't enforce it. |
| **Required** | No. Default `0`. |

```text
ADD_TO_FORMATION_SIZE: 16,
```

### MOUNTED_ANIMAL

The [animal](../../01-animal.md) soldiers ride while carrying this equipment, by its key. An unknown name stops the game with an error.

| | |
|---|---|
| **Type** | Key (an animal) |
| **Required** | No |

```text
MOUNTED_ANIMAL: MOUNT,
```

### DIV_SPRITE

How this equipment is drawn in the picture of a division in the interface.

| | |
|---|---|
| **Type** | Block |
| **Required** | Yes |

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `X`, `Y` | The picture's position. | Integer, -100 or more. The code's maximum of 100 isn't enforced. | No |
| `Z` | The order pictures are drawn in. Higher values are drawn on top. | Integer, -100 or more. The code's maximum of 100 isn't enforced. | No |
| `ICON` | The picture. Without it, the game draws its cancel icon. An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image, counting from `0`, left to right and then top to bottom. A block is described under [`ICON` on the event page](../../05-event/01-structure.md#icon). | Icon path, or a block | No |
| `COLOR` | The colours it's tinted with, as a list. The tint blends along the list as the division carries more. | List of colours | Yes |

```text
DIV_SPRITE: {
	X: 0,
	Y: -11,
	Z: -25,
	ICON: 24->Equipment->8,
	COLOR: [
		175_112_66,
		200_200_200,
		255_190_0,
	],
},
```

### AMOUNT_IN_GARRISON

How much of this equipment soldiers in the garrisons of world regions carry. The game divides it by `MAX_AMOUNT` to work out how well equipped they are.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 0 or more. The game's code names `MAX_AMOUNT` as the maximum but doesn't enforce it. |
| **Required** | Yes |

```text
AMOUNT_IN_GARRISON: 0,
```

### EQUIP_GUARDS

The game never reads this tag.

| | |
|---|---|
| **Type** | Integer |
| **Required** | No |
| **Effect** | Unread |

```text
EQUIP_GUARDS: 0,
```

### SLOT_USAGE

Which equipment can be combined in the division editor. There are eight slots, unnamed, and each item says how much of each slot it fills. The editor won't add an item if that would take any slot above 1.

So in vanilla, armour fills the first slot and doesn't clash with weapons. `WEAPON_SHORT` and `WEAPON_SHIELD` use different slots and can be combined, while `WEAPON_SLASH`, which fills both of those slots, can be combined with neither.

| | |
|---|---|
| **Type** | List of decimals |
| **Range** | Exactly 8 values. Any other length stops the game with an error. |
| **Required** | Yes |

```text
SLOT_USAGE: [
	0, 
	0,
	0,
	1.0,
	0,
	0,
	0,
	0,	
],
```

### RACE_ALLOWED

The game never reads this tag. To choose which races can use equipment, use [`EQUIPMENT_NOT_ENABLED` and `EQUIPMENT_ENABLED`](../../07-race/01-race-file.md#equipment_not_enabled-and-equipment_enabled) in the race file.

| | |
|---|---|
| **Type** | List |
| **Required** | No |
| **Effect** | Unread |

```text
RACE_ALLOWED: [
	*,
],
```

### SPRITE

How this equipment is drawn on the soldier on the battlefield. Without this block, nothing extra is drawn, as with armour. This example comes from the vanilla `WEAPON_HAMMER.txt`.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `FILE` | The name of an image in `assets/sprite/race/battle/`, without `.png`. It must be exactly 132 pixels wide and at least 36 high. Copy a vanilla image for the layout, described in [sprite/race/battle](../../../03-sprite/07-race/02-battle.md). | Text | Yes |
| `OFFSET_X`, `OFFSET_Y` | Where the image is drawn, relative to the soldier. The distance scales with the size of the soldier's race. | Decimal, -100 to 100 | Yes |
| `ANIMATION_DX`, `ANIMATION_DY` | How far the image moves with the soldier's animation. | Decimal, -100 to 100 | Yes |
| `COLOR` | The colours it's tinted with, as a list. The tint blends along the list as the soldier carries more. | List of colours | Yes |

```text
SPRITE: {
	FILE: Hammer,
	OFFSET_X: 0.5,
	OFFSET_Y: 0.45,
	ANIMATION_DX: -0.1,
	ANIMATION_DY: 0.3,
	COLOR: [
		125_87_64,
		74_67_64,
	],
},
```

### BOOST

The bonuses this equipment gives, written in the same way as a race's [`BOOST`](../../07-race/01-race-file.md#boost) block. They grow with the amount carried, as [the equip chapter](00-equip.md#how-strong-bonuses-are) explains.

| | |
|---|---|
| **Type** | Block of boosts |
| **Required** | No |

```text
BOOST: {
	PHYSICS_SPEED>ADD: 2.5,
	PHYSICS_MASS>ADD: 500,
	BATTLE_CHARGE>ADD: 2,
	BATTLE_DEFENCE_SKILL>MUL: 0.5,
	BATTLE_OFFENCE_SKILL>MUL: 1.25,
	BATTLE_FORMATION_SKILL>MUL: 0,
},
```

### STANDING

Unverified: the game's code reads this block here, in the format described under [civic equipment](02-civic.md#standing), but whether it has any effect on battle equipment wasn't confirmed. Vanilla doesn't use it in this folder, and its `_EXAMPLE.txt` comments say it's only for civic equipment.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

## Related

- [init/stats/equip](00-equip.md)
- [Ranged equipment](03-ranged.md)
- [Civic equipment](02-civic.md)
- [init/battle/divType](../../02-battle/01-divType.md)
