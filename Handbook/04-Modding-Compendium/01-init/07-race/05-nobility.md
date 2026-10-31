# init/race/nobility

The vanilla game includes an `init/race/nobility` folder, with files such as `FARM.txt` and `MINES.txt`, and matching text files in `text/race/nobility`. **Version 0.71.44 doesn't read either folder.** Changing these files, or adding new ones, has no effect on the game.

The files look like definitions of noble offices: each has a colour, a bonus, and a name such as "Master of Farms". The game builds its noble offices in its own code instead, as described below.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/race/nobility/` |
| **Files** | 17 in vanilla, e.g. `FARM.txt`, `INDUSTRY.txt`, `MINES.txt` |
| **Read by the game** | No |
| **Text files** | `assets/text/race/nobility/`, also not read |

## What the files contain

For reference, each vanilla file has a colour and a bonus block. From `FARM.txt`:

```text
COLOR: 80_60_5,
BOOST: {
	ROOM_FARM*>ADD: 0.1,
},
```

Each matching text file has a name and description. From `text/race/nobility/FARM.txt`:

```text
INFO: {
	NAME: "Master of Farms",
	DESC: "The Master of farms handles our farms and boosts their yield.",
},
```

## Where noble offices come from

The game creates one office, "Master of …", for each kind of production room. These are mines, the wood cutter, farms, orchards, pastures, fisheries, refiners and workshops, plus the embassy, libraries, laboratories and admin rooms. An office is named after its room, such as "Master of Farms", and boosts the work of that room's workers. There's also a Governing office.

Because offices come from rooms, a mod that adds a new room of one of these kinds gets a matching office automatically. Neither the offices nor their bonuses can be changed through data files.

The names of noble ranks are the one part of nobility that does come from a file: `RANKS` in `assets/text/player/noble/_RANKS.txt`.

## Related

- [init/race](00-race.md)
