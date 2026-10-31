# init/config

The `init/config` folder holds the game's one-off settings: values that apply to the whole game rather than to one race, room or resource. They cover things like the size of armies, the three climates, the calendar, the laws of your settlement and how new settlement maps are generated.

Unlike most `init` folders, each file here has its own format, so each has its own page.

## How these files work

The game loads each of these files by its exact name. That has two consequences:

- **You can change them, but not add to them.** To change a setting, put a file of the same name at `V71/assets/init/config/` in your mod. A new file with a different name will simply be ignored.
- **Your file only needs the tags you change.** It's laid over the vanilla file tag by tag, so any tag you leave out keeps its vanilla value. To change only the size of a division, for example, your `Battle.txt` can contain just `MEN_PER_DIVISION: 200,` with your own number. Blocks are replaced whole unless you use `_JSON_ADD`; see [Changing a vanilla file](../../../02-Getting-Started.md#changing-a-vanilla-file).

Several files here contain comments that state ranges, such as `** 1-255`. These don't always match what the game actually accepts. The pages below give the ranges from the game's code.

## Files

- [Battle.txt](01-Battle.md)
- [CLIMATE.txt](02-CLIMATE.md)
- [Charset.txt](03-Charset.md)
- [DefaultProjectile.txt](04-DefaultProjectile.md)
- [GameSprites.txt](05-GameSprites.md)
- [GenerationSettlement.txt](06-GenerationSettlement.md)
- [LAW.txt](07-LAW.md)
- [LEAVE_CAUSE.txt](08-LEAVE_CAUSE.md)
- [LandingParty.txt](09-LandingParty.md)
- [SETT_MAP_DECORATION.txt](10-SETT_MAP_DECORATION.md)
- [Sett.txt](11-Sett.md)
- [SettColors.txt](12-SettColors.md)
- [TERRAIN.txt](13-TERRAIN.md)
- [Time.txt](14-Time.md)

## Related

- [init](../00-init.md)
