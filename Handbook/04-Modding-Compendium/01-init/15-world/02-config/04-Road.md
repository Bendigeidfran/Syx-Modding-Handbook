# init/world/config/Road.txt

`Road.txt` sets the colours of roads on the world map.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/world/config/Road.txt` |
| **Adding new files** | No. Only this file is read. |

## Tags

### COLOR_SMALL

One end of the colour range for roads. The game blends between the two colours to make 16 shades.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR_SMALL: 170_140_120,
```

### COLOR_BIG

The other end of the colour range for roads.

| | |
|---|---|
| **Type** | Colour |
| **Required** | Yes |

```text
COLOR_BIG: 80_75_70,
```

## Related

- [init/world/config](00-config.md)
