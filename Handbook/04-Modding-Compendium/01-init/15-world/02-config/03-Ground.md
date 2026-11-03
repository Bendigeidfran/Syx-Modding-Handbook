# init/world/config/Ground.txt

`Ground.txt` sets the colours of the ground on the world map.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/world/config/Ground.txt` |
| **Adding new files** | No. Only this file is read. |

## Tags

### COLOR

The colours of the ground, from the wettest land to the driest. The game blends the list into nine shades, so it can have any number of colours.

| | |
|---|---|
| **Type** | List of colours |
| **Required** | Yes |

```text
COLOR: [

	132_128_80,
	174_154_122,
	174_154_122,
	218_190_170,
],
```

### COLOR_DEVASTATED_DRY

The colour of devastated ground at its driest. The game blends it with `COLOR_DEVASTATED_WET` for the shades in between.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR_DEVASTATED_DRY: 150_140_135,
```

### COLOR_DEVASTATED_WET

The colour of devastated ground at its wettest.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR_DEVASTATED_WET: 120_115_110,
```

## Related

- [init/world/config](00-config.md)
