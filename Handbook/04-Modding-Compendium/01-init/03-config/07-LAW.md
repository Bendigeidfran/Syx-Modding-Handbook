# init/config/LAW.txt

`LAW.txt` sets the default behaviour of your settlement's justice system: how your subjects feel about each crime being punished, and how severe each punishment is.

Crimes are committed by your subjects and dealt with in your settlement's law system, where you choose a punishment for each crime. Choosing a punishment is a trade-off. Harsh punishments strengthen the law, which makes subjects more loyal, but they also come across as tyranny, which makes subjects unhappy. This file sets how strong those two effects are.

The values here are **defaults**. Each race can override them for itself in the `CRIME` and `PUNISHMENT` blocks of its `PREFERRED` section.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/LAW.txt` |
| **Adding new files** | No. Only this file is read. |
| **Adding new crimes or punishments** | No. Both lists are built into the game. You can change their settings but not add, remove or rename them. |
| **Companion files** | `assets/text/config/LAW.txt`, which holds the names and descriptions of the crimes and punishments |

## File structure

The file has two blocks, `CRIMES` and `PUNISHMENTS`. Both are required, as is every crime and punishment listed below.

```text
CRIMES: {
	MURDER: {
		FREEDOM: 0.025,
		LAW: 0.25,
	},
	...
},

PUNISHMENTS: {
	PRISON: {
		ICON: 24->law->1,
		VALUE: 0.5,
	},
	...
},
```

## Crimes

The `CRIMES` block contains one entry for each crime. The crimes are:

| Key | Committed by | Name in game |
|---|---|---|
| `MURDER` | Citizens | Murder |
| `THEFT` | Citizens | Theft |
| `VANDALISM` | Citizens | Vandalism |
| `FLASHING` | Citizens | Flashing |
| `DISRESPECT` | Citizens | Disrespect |
| `SPEECH` | Citizens | Criticism |
| `PLEASURE` | Citizens | Persecution |
| `S_MURDER` | Slaves | Murder |
| `S_THEFT` | Slaves | Theft |
| `S_DISRESPECT` | Slaves | Disrespect |
| `S_PLEASURE` | Slaves | Persecution |
| `WAR` | Captives | Captive |

Note that the "Persecution" crimes (`PLEASURE` and `S_PLEASURE`) are arrests made on your own orders, and `WAR` covers captives taken in war or bought as slaves. The names in game come from the companion text file.

Each crime entry has two tags.

### FREEDOM

How much your subjects resent this crime being punished. When the crime is punished, the tyranny your subjects feel is this value multiplied by the severity of the punishment (its `VALUE`). Tyranny lowers happiness.

A crime with a high `FREEDOM` value is one your subjects feel should be left alone.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

### LAW

How much punishing this crime strengthens the law. When the crime is punished, the law gained is this value multiplied by the square root of the punishment's severity. Law raises loyalty.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

From the vanilla file:

```text
MURDER: {
	FREEDOM: 0.025,
	LAW: 0.25,
},
PLEASURE: {
	FREEDOM: 1.0,
	LAW: 0.0,
},
```

Punishing murder causes very little resentment and does a good deal for the law. Persecuting subjects on your own orders causes the most resentment possible and does nothing for the law.

## Punishments

The `PUNISHMENTS` block contains one entry for each punishment. The punishments are `PARDON`, `NONE`, `BANISH`, `PRISON`, `EXECUTE`, `HARVEST` and `ENSLAVE`.

`NONE` is the punishment of leaving an offender in the stocks until you decide what to do with them.

Each punishment entry can have four tags.

### ICON

The punishment's icon in the law interface, written as an icon path.

An icon path is `SIZE->FOLDERS->IMAGE->NUMBER`, relative to `assets/sprite/icon/`: the size folder (`16`, `24` or `32`), any sub-folders, the image name without `.png`, then the icon's number within that image. Numbers count from `0`, left to right and then top to bottom.

| | |
|---|---|
| **Type** | Icon path |
| **Required** | Yes |

### VALUE

How severe the punishment is. Severity is used in both effects described under Crimes: tyranny rises in line with it, and law with its square root.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | Yes |

### MERCY

How merciful the punishment is seen to be when used on captives (the `WAR` crime). Each time it's used on a captive, your faction's reputation for mercy rises. The amount is this value scaled by the size of your population, so it matters less in a large settlement.

Your mercy reputation affects how other factions see you.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `0`. |

### CRUELTY

The opposite of `MERCY`: each time the punishment is used on a captive, your reputation for mercy falls by this value, again scaled by population.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 1 |
| **Required** | No. Default `0`. |

From the vanilla file:

```text
PARDON: {
	ICON: 24->law->0,
	VALUE: 0,
	MERCY: 1,
},
EXECUTE: {
	ICON: 24->law->3,
	VALUE: 1.0,
	CRUELTY: 1,
},
```

Mercy and cruelty aren't applied for `NONE`.

## The text file

`assets/text/config/LAW.txt` holds the in-game wording, in the same two blocks:

- each crime has `NAME`, `NAMES`, `TITLE` (what an offender is called) and `TITLES`, and `DESC`;
- each punishment has `NAME`, `NAMES`, `ACTION`, `VERB` and `DESC`.

## Related

- [init/config](00-config.md)
