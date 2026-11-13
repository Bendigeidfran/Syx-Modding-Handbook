# sprite/ui/Colors

`Colors.txt` sets colours used across the interface: the colours of text, of the bars and indicators that show whether something is good or bad, and of the markings drawn on the settlement and world maps.

## At a glance

| | |
|---|---|
| **Location** | `assets/sprite/ui/Colors.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | None |

## Colour format

Each colour is written as `RED_GREEN_BLUE`, with each part a whole number from 0 to 255:

```text
H1: 255_240_190,
```

The game also accepts a block with `R`, `G` and `B` values instead, as in [SettColors.txt](../../01-init/03-config/12-SettColors.md#colour-format).

## Tags

The file has three blocks, `UI`, `TEXT` and `MAP`. All three are required, and so is every colour listed in them: a missing one stops the game with an error.

### UI

Colours for interface elements other than text, such as bars, icons and highlights. The game makes four shades from each of `NORMAL`, `BAD`, `GOOD`, `NEUTRAL`, `GOOD2`, `GREAT` and `SOSO`, for an element that's inactive (55% of the colour's brightness), normal (80%), hovered (the colour as written) and selected (120%).

| Tag | Used for |
|---|---|
| `NORMAL` | The highlight of a text box that's under the mouse or being typed in, and the hovered ends of a gauge you can adjust |
| `BAD` | Bars, icons and indicators for something bad |
| `GOOD` | Bars, icons and indicators for something good |
| `GREAT` | Something better than good, such as the hammer icon in a room's panel |
| `NEUTRAL` | Neutral highlights, such as a hovered statistic |
| `GOOD2` | The good end of the bars in the citizens' panel, which run from `BAD` to this colour |
| `SOSO` | Something middling. Many scales run from `BAD` through `SOSO` to `GOOD`, such as race preferences, diplomacy and the region names on the world map. |
| `BAD_SHIFT` | A warning that flashes, fading from near black to this colour and back once a second, for example in the battle panel and the top panel |
| `GOOD_SHIFT` | The same, for good news |

| Tag | Meaning | Effect |
|---|---|---|
| `GOLD` | A gold colour. The game reads it, but nothing uses it. | None |

| | |
|---|---|
| **Type** | Block of colours |
| **Required** | Yes |

```text
UI: {
	NORMAL: 	30_24_56,
	BAD: 		255_120_120,
	GOOD:		100_255_100,
	GREAT:		0_255_255,
	NEUTRAL:	150_164_126,
	GOOD2: 		0_0_200,
	SOSO: 		225_195_135,
	BAD_SHIFT: 	200_0_0,
	GOOD_SHIFT: 0_200_0,
	GOLD:		188_134_54,
},
```

### TEXT

The colours of text.

| Tag | Used for |
|---|---|
| `IGREAT` | Numbers at the very good end of a scale |
| `IGOOD` | Numbers that are good, such as a positive change |
| `INORMAL` | Numbers that are neither good nor bad |
| `IBAD` | Numbers that are bad, such as a negative change |
| `IWORST` | Numbers at the very bad end of a scale. Numbers in between are blended from these five colours. |
| `H1` | Headings. The ornaments in `Decor.png` are also tinted with it. |
| `H2` | Subheadings |
| `ERROR` | Error messages |
| `WARNING` | Warnings |
| `CLICKABLE` | Text you can click, such as menu entries |
| `HOVERED` | Button labels and some other text under the mouse. See the note below. |
| `SELECTED` | Button labels that are selected |
| `HOVERED_SELECTED` | The second colour of button labels under the mouse. See the note below. |
| `INACTIVE` | Button labels that can't be used |
| `NORMAL` | Ordinary text, when nothing else sets a colour |
| `NORMAL2` | A second colour for ordinary text, used for many short notes in tooltips and for tourists' reviews |

A button label under the mouse doesn't use a single colour: the game fades it back and forth between `HOVERED` and `HOVERED_SELECTED`, taking two seconds for each cycle. It does the same for a button that's both hovered and selected. A selected button that isn't hovered uses `SELECTED` alone. Other text the game marks as hovered takes a blend of the two, as it was at the moment the text was coloured.
| Tag | Meaning | Effect |
|---|---|---|
| `HOVERABLE` | A colour for text that shows more when hovered. The game reads it, but nothing uses it. | None |

| | |
|---|---|
| **Type** | Block of colours |
| **Required** | Yes |

```text
TEXT: {

	IGREAT: 100_255_255,
	IGOOD: 100_200_255,
	INORMAL: 236_255_236,
	IBAD: 255_180_180,
	IWORST: 255_120_110,
	
	HOVERABLE: 230_190_90,
	H1: 255_240_190,
	H2: 255_210_180,
	ERROR: 255_180_180,
	WARNING: 255_255_150,
	
	CLICKABLE: 255_255_255,
	HOVERED: 255_255_130,
	SELECTED: 255_255_130,
	HOVERED_SELECTED: 220_180_90,
	INACTIVE: 96_70_42,
	NORMAL: 236_255_236,
	NORMAL2: 150_255_255,
},
```

### MAP

Colours of the markings drawn on the settlement and world maps. `BAD`, `SOSO`, `OK`, `BETTER` and `BEST` also form a scale from bad to best, used for example when placing rooms and in overlays such as maintenance.

| Tag | Used for |
|---|---|
| `DORMANT` | Jobs that are waiting |
| `BAD` | The bad end of the scale, used by many placement tools and overlays |
| `SOSO` | The middle of the scale |
| `OK` | Jobs that are ready to be worked, and the markings drawn while selecting and placing divisions in battle. Jobs that are blocked use a darker version of it. One of the settlement's overlays marks rooms with a colour that fades back and forth between `OK` and `BETTER`. |
| `BETTER` | Jobs that someone has taken on |
| `BEST` | The best end of the scale. A darker version of it is used too, for example in the maintenance overlay. |
| `OVERLAY_GOOD` | The good end of the settlement's overlays |
| `OVERLAY_BAD` | The bad end of the settlement's overlays |
| `F_PLAYER` | The player's faction, for example on the world minimap and in army lists |
| `F_ALLY` | Factions allied with the player |
| `F_NEAUTRAL` | Factions not at war with the player. The tag is spelled this way in the game. |
| `F_ENEMY` | Factions at war with the player |
| `F_REBEL` | Things that belong to no faction, such as rebels and unowned regions |

| | |
|---|---|
| **Type** | Block of colours |
| **Required** | Yes |

```text
MAP: {
	DORMANT: 160_160_160,
	BAD: 254_20_20,
	SOSO: 254_254_0,
	OK: 0_120_254,
	BETTER: 0_200_254,
	BEST: 20_254_20,
	OVERLAY_GOOD: 100_240_240,
	OVERLAY_BAD: 100_10_10,
	F_PLAYER: 40_254_40,
	F_ALLY: 40_40_254,
	F_NEAUTRAL: 240_240_40,
	F_ENEMY: 254_40_40,
	F_REBEL: 100_100_100,
},
```

## Notes

- A mod's `Colors.txt` is layered over the vanilla file, so a mod only needs the colours it changes, inside their blocks with `_JSON_ADD`. See [Changing a vanilla file](../../../02-Getting-Started.md#changing-a-vanilla-file).
- Some colours of the interface aren't set here: faction banner colours come from [init/world/config/Faction.txt](../../01-init/15-world/02-config/01-Faction.md#colors), and the minimap colours from [init/config/SettColors.txt](../../01-init/03-config/12-SettColors.md).

## Related

- [sprite/ui](00-ui.md)
- [Decor](03-decor.md)
- [init/config/SettColors.txt](../../01-init/03-config/12-SettColors.md)
