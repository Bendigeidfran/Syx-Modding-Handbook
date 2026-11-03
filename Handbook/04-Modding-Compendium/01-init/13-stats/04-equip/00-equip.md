# init/stats/equip

These files define the equipment subjects and soldiers use. Each file turns a [resource](../../09-resource/01-resource-file.md) into something that can be worn or carried, with its own bonuses, and takes its name, description and icon from that resource, so equipment has no text file of its own.

Which sub-folder a file goes in decides who uses it:

| Sub-folder | Who uses it | Key |
|---|---|---|
| [`battle/`](01-battle.md) | Soldiers. Armour, melee weapons, shields and mounts. | `BATTLE_<FILE>`, e.g. `BATTLE_MOUNT` |
| [`civic/`](02-civic.md) | Your subjects in everyday life. Clothes and jewellery. | `CIVIC_<FILE>`, e.g. `CIVIC_JEWELRY` |
| [`ranged/`](03-ranged.md) | Soldiers. Ranged weapons, which also fire a projectile. | `RANGED_<FILE>`, e.g. `RANGED_BOW` |

Vanilla also has an empty `mount/` folder, which the game doesn't read. Mounts are ordinary files in `battle/`, as `MOUNT.txt` shows.

As in most folders, a file whose name starts with `_` isn't picked up automatically. The one exception here is `_CLOTHES.txt` in `civic/`, which the game loads by name. So vanilla's `civic/_EXAMPLE.txt`, a commented sample file, isn't loaded.

## Equipment is also a stat

Each piece of equipment creates a stat named `EQUIP_` followed by its key, such as `EQUIP_CIVIC_JEWELRY`, which [`loyalty`](../05-loyalty.md) and race [`STATS`](../../07-race/03-stats.md) blocks can name.

## How strong bonuses are

A `BOOST` block on equipment follows the same rule as [`bonus`](../01-bonus.md#how-strong-a-bonus-is), where the stat's value is the amount carried divided by `MAX_AMOUNT`. A soldier carrying 3 of a possible 5 gets 60% of the way to the value in the file.

## Sections

- [Battle equipment](01-battle.md)
- [Civic equipment](02-civic.md)
- [Ranged equipment](03-ranged.md)

## Related

- [init/stats](../00-stats.md)
- [EQUIPMENT in init/battle/divType](../../02-battle/01-divType.md#equipment)
- [EQUIPMENT_NOT_ENABLED and EQUIPMENT_ENABLED in the race file](../../07-race/01-race-file.md#equipment_not_enabled-and-equipment_enabled)
