# init/stats

The `init/stats` folder holds several systems that revolve around your subjects: what each stat is worth, the damage types used in battle, the equipment subjects carry and the needs that send them looking for services.

A **stat** is one thing the game tracks about a subject or a group of subjects, such as how well furnished their home is, or how many handouts they've received. Most stats are built into the game's code, so these files can tune them but can't add new ones. Equipment is the exception, because each equipment file creates a stat of its own.

The folder holds only sub-folders. Each one has its own format:

| Sub-folder | What it does |
|---|---|
| [`bonus/`](01-bonus.md) | Gives a stat bonuses and penalties, such as handouts raising loyalty. |
| [`damage/`](02-damage.md) | Defines the damage types used in battle. |
| [`dynamicBoost/`](03-dynamicBoost.md) | Adds new boostable values, such as administration. |
| [`equip/`](04-equip/00-equip.md) | Defines the equipment subjects and soldiers can use. |
| [`loyalty/`](05-loyalty.md) | Sets how much each stat matters to a subject's happiness. |
| [`need/`](06-need.md) | Defines the needs that services satisfy. |

The names and descriptions of most stats are in one shared file, [`text/stats/NAMES.txt`](07-NAMES.md).

## Stat names

`bonus` and `loyalty` both name stats by their key, such as `HOME_FURNITURE`. To find a key, use the method described under [Stat names on the race stats page](../07-race/03-stats.md#stat-names): the first time a file uses a name that doesn't exist, the game shows a warning that lists every name available.

## Sections

- [init/stats/bonus](01-bonus.md)
- [init/stats/damage](02-damage.md)
- [init/stats/dynamicBoost](03-dynamicBoost.md)
- [init/stats/equip](04-equip/00-equip.md)
- [init/stats/loyalty](05-loyalty.md)
- [init/stats/need](06-need.md)
- [text/stats/NAMES.txt](07-NAMES.md)

## Related

- [init](../00-init.md)
- [Race stats](../07-race/03-stats.md)
