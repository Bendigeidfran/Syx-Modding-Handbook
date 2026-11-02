# init/room

The `init/room` folder defines the rooms the player can build: farms, workshops, temples, homes, barracks and so on. Each file is one room, giving its icon, its building costs, its furniture and how it looks.

Rooms come in many types, and the game knows each type from the start of the file's name. `FARM_GRAIN.txt` and `FARM_COTTON.txt` are both farms, while `TEMPLE_AMINION.txt` is a temple. Each type reads some tags that are shared with other rooms, plus some of its own.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/room/` |
| **Files** | One `.txt` file per room, e.g. `FARM_GRAIN.txt` |
| **Key** | The file name without `.txt`, e.g. `FARM_GRAIN`. Other files use this key to refer to the room. |
| **Text file** | `assets/text/room/<KEY>.txt`, which must exist and have the same name |

## Adding new rooms

Most types can have more than one room. A file named `<TYPE>_<NAME>.txt` adds a room of that type: `FARM_TEA.txt`, for example, would add a new kind of farm. The new file has to provide everything that type reads, so the safest way to make one is to copy a vanilla room of the same type and change it.

These are the types that can be added to in this way:

`ADMIN`, `ARCHERY`, `ARENAG`, `ARTILLERY`, `BARBER`, `BARRACKS`, `BATH`, `BREEDER`, `CANTEEN`, `EATERY`, `FARM`, `FIGHTPIT`, `FISHERY`, `GATEHOUSE`, `GRAVEYARD`, `HUNTER`, `LABORATORY`, `LAVATORY`, `LIBRARY`, `MARKET`, `MINE`, `MONUMENT`, `NURSERY`, `ORCHARD`, `PASTURE`, `PHYSICIAN`, `PLEASURE`, `POOL`, `REFINER`, `RESTHOME`, `SCHOOL`, `SHRINE`, `SPEAKER`, `STAGE`, `TAVERN`, `TEMPLE`, `TOMB`, `UNIVERSITY`, `WELL` and `WORKSHOP`.

Files starting with `_`, such as `_STOCKPILE.txt`, are single rooms that the game loads by name. You can change them, but you can't add more of them.

## Sections

The first four pages cover the tags many rooms share. The rest cover each group of room types, using the game's own groups.

- [Common tags](01-common.md)
- [Employment](02-employment.md)
- [Production](03-production.md)
- [Services](04-services.md)
- [Food rooms](05-food.md)
- [Health rooms](06-health.md)
- [Home rooms](07-home.md)
- [Industry rooms](08-industry.md)
- [Infrastructure rooms](09-infra.md)
- [Knowledge rooms](10-knowledge.md)
- [Law rooms](11-law.md)
- [Military rooms](12-military.md)
- [Service rooms](13-service.md)
- [Spirit rooms](14-spirit.md)
- [Water rooms](15-water.md)

## Related

- [init](../00-init.md)
