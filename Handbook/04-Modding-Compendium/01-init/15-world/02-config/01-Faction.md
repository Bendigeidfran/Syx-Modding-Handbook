# init/world/config/Faction.txt

`Faction.txt` lists the colours used for faction banners on the world map.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/world/config/Faction.txt` |
| **Adding new files** | No. Only this file is read. |

## Tags

### COLORS

The colours banners are drawn from. The game shuffles the list, then gives each faction one colour for its background and another from further along the list for its foreground. If there are more factions than colours, it blends colours to make more.

| | |
|---|---|
| **Type** | List of colours |
| **Required** | Yes |

```text
COLORS: [
	220_220_220,
	47_79_79,
	85_107_47,
],
```

## Related

- [init/world/config](00-config.md)
