# init/config/DefaultProjectile.txt

`DefaultProjectile.txt` defines the projectile that invading armies fire at your settlement. When an invasion lays siege, the attackers bombard your defences, and every shot uses the projectile described here.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/DefaultProjectile.txt` |
| **Adding new files** | No. Only this file is read. |
| **Sprite** | An image in `assets/sprite/settlement/projectile/`, named by `SPRITE_FILE`. Vanilla uses `_CATAPULT.png`. |
| **Sound** | The entries `PROJECTILE_RELEASE__DefaultProjectile` and `PROJECTILE_HIT__DefaultProjectile` (note the double underscore) in a file in `assets/audio/config/mono/`. Vanilla keeps them in `AA_PROJECTILE.txt`. |

## File structure

The file contains a single `PROJECTILE` block. Inside it are the projectile's appearance and two blocks of statistics, `FROM` and `TO`:

```text
PROJECTILE: {
	SPRITE_FILE: _CATAPULT,
	COLOR: 255_255_255,

	FROM: {
		TILE_SPEED: 50,
		MASS: 20,
		DEXTERITY: 0,
		DAMAGE: {
			
		},
		ACCURACY: 0.95,
		TILE_RADIUS_DAMAGE: 2,
		RELOAD_SECONDS: 60,
		MAX_ARCH_ANGLE_DEGREES: 50,
	},
	TO: {
		...the same tags...
	},
},
```

The same projectile format is used elsewhere in the game, for artillery and ranged weapons. There, `FROM` holds the projectile's statistics at the lowest skill level and `TO` at the highest, and the game blends between them according to the skill of whoever is firing.

Invaders always fire at the highest level, so **only the `TO` values affect invasions**. `FROM` must still be present and valid.

## Tags

### SPRITE_FILE

The image the projectile is drawn with: the name of a file in `assets/sprite/settlement/projectile/`, without `.png`.

| | |
|---|---|
| **Type** | Key (an image in `assets/sprite/settlement/projectile/`) |
| **Required** | No. Without it, the projectile is drawn as a simple coloured streak. |

```text
SPRITE_FILE: _CATAPULT,
```

### COLOR

A colour applied to the projectile, written as `RED_GREEN_BLUE`. Vanilla uses white, `255_255_255`.

| | |
|---|---|
| **Type** | Colour (`RED_GREEN_BLUE`) |
| **Required** | Yes |

```text
COLOR: 255_255_255,
```

### FROM and TO

The projectile's statistics, as described above. Both blocks are required, and both use the tags below.

#### TILE_SPEED

How fast the projectile flies. As the name suggests, the value is measured in tiles.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0.5 to 250 |
| **Required** | Yes |

#### MASS

How heavy the projectile is. Mass decides how much force it hits with.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0.01 to 100000 |
| **Required** | Yes |

#### DAMAGE

Damage by type, keyed by the damage types in [`assets/init/stats/damage/`](../13-stats/02-damage.md) (vanilla has `PIERCE` and `SLASH`). Vanilla's default projectile leaves this empty, so it does force damage only.

| | |
|---|---|
| **Type** | Block of decimals, keyed by damage type |
| **Range** | Each value 0 to 100000 |
| **Required** | No |

#### TILE_RADIUS_DAMAGE

The radius, in tiles, of the area damaged around the point of impact.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000 |
| **Required** | No. Default `0`, meaning only the point of impact is hit. |

#### MAX_ARCH_ANGLE_DEGREES

The steepest angle, in degrees, the projectile can be fired at. Together with `TILE_SPEED`, this decides how far it can reach.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 75 |
| **Required** | Yes |

#### ACCURACY

How accurate the shot is, where `1` is perfectly accurate.

Invaders always fire with perfect aim, so this has no effect on invasions.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0.01 to 1 |
| **Required** | Yes |

#### RELOAD_SECONDS

How long it takes to reload between shots.

Invasions fire on their own schedule, so this has no effect on invasions.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0.01 to 10000 |
| **Required** | Yes |

#### DEXTERITY

The game reads this value, but in v0.71.44 nothing uses it, for this or any other projectile: changing it has no effect.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10000000 |
| **Required** | Yes. The tag must be present even though it has no effect. |

## Related

- [init/config](00-config.md)
- [sprite/settlement/projectile](../../03-sprite/10-settlement/04-projectile.md)
