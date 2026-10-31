# init/config/TERRAIN.txt

`TERRAIN.txt` contains one empty block for each of the game's five terrain types. In v0.71.44 the blocks must exist, but nothing inside them is read, so there is nothing to configure in this file.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/TERRAIN.txt` |
| **Adding new files** | No. Only this file is read. |
| **Adding new terrains** | No. The five terrain types are built into the game. |
| **Companion files** | None |

## File structure

The vanilla file in full:

```text
OCEAN: {

},
WET: {
	
},
MOUNTAIN: {

},
FOREST: {

},
NONE: {

},
```

All five blocks are required. If one is missing, the file won't load. Anything you put inside them is ignored.

## Notes

### Terrain keys elsewhere

Other files refer to the terrain types by these keys, usually in a block that weights something by terrain. `NONE` means open land. For example, [an animal's TERRAIN block](../01-animal.md#terrain) sets how common it is on each type.

## Related

- [init/config](00-config.md)
- [init/animal](../01-animal.md)
