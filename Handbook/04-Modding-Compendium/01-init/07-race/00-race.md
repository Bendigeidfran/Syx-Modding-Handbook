# init/race

The `init/race` folder defines the game's species: the Humans, Garthimi, Dondorians and the rest. A race decides how its members look, what they eat and drink, where they like to live and work, how happy or loyal different conditions make them, how they fight, and how they spread across the world map.

A race is spread over several files. At its centre is the **race file** in `init/race` itself, which refers by name to the race's other files:

| File | What it holds | Named by |
|---|---|---|
| `init/race/<KEY>.txt` | The race file: properties, preferences, needs, boosts and more. | |
| [`init/race/sprite/`](06-sprite/00-sprite.md) | The race's appearance: colours, body sprites, faces, world-map art. | `SPRITE_FILE` |
| `init/race/home/` | The furniture and floors of the race's homes. | `HOME` |
| `text/race/<KEY>.txt` | The race's name, description and other wording. | Same name as the race file |
| Further text files in `text/race/` and `text/names/` | Biographies, AI kings' speech, raider messages, tourist reviews and world-map names. | `BIO_FILE`, `KING_FILE` and others |

Three more sub-folders hold things that aren't tied to one race:

- `init/race/nobility/` defines the offices nobles can hold, such as Master of Farms, each with its own bonus;
- `init/race/trait/` defines personality traits, such as Cruel or Lazy, that individual subjects can have;
- `init/race/worldcamp/` defines camps of a race that can appear on the world map.

Several files can share a sub-file. All vanilla races use the same `KING_FILE`, for example, while each has its own sprite file.

[Your First Mod](../../../03-Your-First-Mod.md) walks through making a new race step by step. These pages are the full reference.

## Sections

The race file is large, so it's described over three pages.

- [The race file](01-race-file.md)
- [Race preferences](02-preferences.md)
- [Race stats](03-stats.md)
- init/race/home (not yet written)
- init/race/nobility (not yet written)
- [init/race/sprite](06-sprite/00-sprite.md)
- init/race/trait (not yet written)
- init/race/worldcamp (not yet written)

## Related

- [init](../00-init.md)
