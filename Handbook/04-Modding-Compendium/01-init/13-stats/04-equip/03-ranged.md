# init/stats/equip/ranged

These files define the ranged weapons your soldiers can use. A ranged weapon uses every tag of [battle equipment](01-battle.md) and adds its ammunition and the projectile it fires. Vanilla has one, the bow.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/stats/equip/ranged/` |
| **Files** | One `.txt` file per weapon, e.g. `BOW.txt` |
| **Key** | `RANGED_` and the file name, e.g. `RANGED_BOW` |
| **Adding new weapons** | Yes |
| **Text file** | None. The name, description and icon come from the resource. |
| **Sound** | The entries `PROJECTILE_RELEASE_EQUIP_<FILE>` and `PROJECTILE_HIT_EQUIP_<FILE>` in a file in `assets/audio/config/mono/`. Vanilla keeps `BOW`'s in `AA_PROJECTILE.txt`. |

## Tags

The examples come from the vanilla `BOW.txt`.

### Shared tags

These work as they do for [battle equipment](01-battle.md), where each is described in full.

| Tag | Type and range | Required | Effect |
|---|---|---|---|
| `DEFAULT_TARGET` | Integer | Yes | None |
| `EQUIP_GUARDS` | Integer | No | Unread |
| `RACE_ALLOWED` | List | No | Unread |

| Tag | Type and range | Required |
|---|---|---|
| `RESOURCE` | Key (a resource) | Yes |
| `MAX_AMOUNT` | Integer, 1 or more. Stay at or below 15. | Yes |
| `ARRIVAL_AMOUNT` | Integer, 0 or more | Yes |
| `WEAR_RATE` | Decimal, 0 to 100 | Yes |
| `AMOUNT_IN_GARRISON` | Integer, 0 or more | Yes |
| `DIV_SPRITE` | Block | Yes |
| `SLOT_USAGE` | List of exactly 8 decimals | Yes |
| `SPRITE` | Block | No |
| `BOOST` | Block of boosts | No |
| `ADD_TO_FORMATION_SIZE` | Integer, 0 or more | No |
| `STANDING` | Block | No |
| `MOUNTED_ANIMAL` | Key (an animal) | No |

### AMMUNITION_AMOUNT

How many shots each soldier carries. Each shot also tires the soldier, by less per shot when this number is higher.

| | |
|---|---|
| **Type** | Integer |
| **Range** | 1 or more. The game's code names a maximum of 255 but doesn't enforce it. |
| **Required** | Yes |

```text
AMMUNITION_AMOUNT: 40,
```

### AMMUNITION_REPLENISH_TIME_HOURS

How many in-game hours each soldier takes to regain one shot, so a bow's 40 shots at `24` take 960 in-game hours to refill from empty. It only replenishes in the player's divisions, while there's no enemy army in the battle. At `0` or below, ammunition is unlimited.

| | |
|---|---|
| **Type** | Decimal |
| **Required** | Yes |

```text
AMMUNITION_REPLENISH_TIME_HOURS: 24,  
```

## Projectile

The `PROJECTILE` block holds the projectile the weapon fires, in the same format as [`DefaultProjectile.txt`](../../03-config/04-DefaultProjectile.md). The block is required.

### COLOR

A colour applied to the projectile, written as `RED_GREEN_BLUE`.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR: 30_20_8,
```

### SPRITE_FILE

The image the projectile is drawn with: the name of a file in `assets/sprite/settlement/projectile/`, without `.png`. Vanilla's bow doesn't use it.

| | |
|---|---|
| **Type** | Key (an image) |
| **Required** | No. Without it, the projectile is drawn as a simple coloured streak. |

### FROM and TO

The projectile's statistics. `FROM` applies to the weakest shot and `TO` to the best, and the game blends between them. The blend depends on how much of the weapon the soldier carries, and on their skill with it, which is a boost named `BATTLE_RANGED_<FILE>`, such as `BATTLE_RANGED_BOW`, starting at `0.1`. Both blocks are required.

| Tag | Meaning | Type and range | Required | Default |
|---|---|---|---|---|
| `TILE_SPEED` | How fast the projectile flies, in tiles. | Decimal, 0.5 to 250 | Yes | |
| `RELOAD_SECONDS` | How long it takes to reload between shots. | Decimal, 0.01 to 10000 | Yes | |
| `ACCURACY` | How accurate the shot is, where `1` is perfectly accurate. | Decimal, 0.01 to 1 | Yes | |
| `MAX_ARCH_ANGLE_DEGREES` | The steepest angle it can be fired at. With `TILE_SPEED`, this decides its reach. | Decimal, 0 to 75 | Yes | |
| `DAMAGE` | Damage by type, keyed by the [damage types](../02-damage.md). | Block of decimals, each 0 to 100000 | No | `0` for each type |
| `MASS` | How heavy the projectile is, which decides how much force it hits with. | Decimal, 0.01 to 100000 | Yes | |
| `TILE_RADIUS_DAMAGE` | The radius, in tiles, of the area damaged around the point of impact. | Decimal, 0 to 10000 | No | `0` |

```text
TO: {
	TILE_SPEED: 45,
	RELOAD_SECONDS: 3,
	ACCURACY: 0.98,
	MAX_ARCH_ANGLE_DEGREES: 75,
	DEXTERITY: 0,
	DAMAGE: {
		PIERCE: 12,
	},
	MASS: 0.4,
	TILE_RADIUS_DAMAGE: 0,
},
```

#### DEXTERITY

The game reads this value in `FROM` and `TO`, but nothing uses it. The tag must still be present.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000000 |
| **Required** | Yes |
| **Effect** | None |

```text
DEXTERITY: 0,
```

## Notes

### Sound

If a weapon has no matching sound entries, it makes no sound and the game carries on. Missing entries are reported as described under [Sound on the init/animal page](../../01-animal.md#sound).

## Related

- [init/stats/equip](00-equip.md)
- [Battle equipment](01-battle.md)
- [init/config/DefaultProjectile.txt](../../03-config/04-DefaultProjectile.md)
- [init/stats/damage](../02-damage.md)
