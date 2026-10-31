# Your First Mod

In this section you'll build a complete, working mod: a new playable race. It's the most common thing new modders want to make, and it touches several parts of the modding system at once, which makes it a good first project.

The race is based on the vanilla Dondorians, with a few changes:

- Their favourite food is fruit.
- They prefer plain stone buildings, rather than mountain halls and grand architecture.
- They move faster than normal.
- When butchered in the Cannibal room, they yield metal.

Follow the steps in order and your mod will match the one described here exactly. If you've read [Getting Started](02-Getting-Started.md), the setup steps will be familiar.

## Step 1: Set up the mod

In your `mods` folder (see [Finding the mods folder](02-Getting-Started.md#finding-the-mods-folder)), create a folder called `MyFirstMod`.

Inside it, create `_Info.txt` with the following contents:

```text
NAME: "My First Mod",
DESC: "Adds the Pomaris, a fruit-loving offshoot of the Dondorians.",
AUTHOR: "Your name",
VERSION: "1.0",
INFO: "",
GAME_VERSION_MAJOR: 71,
GAME_VERSION_MINOR: 44,
```

Then, next to `_Info.txt`, create the version folder `V71`, and inside that, a folder called `assets`. Your mod now looks like this:

```text
MyFirstMod/
├── _Info.txt
└── V71/
    └── assets/
```

## Step 2: Copy the vanilla files

A race is made of several files that work together. Rather than write them from scratch, you'll copy the Dondorian versions and change them.

If you haven't already, copy `base/data.zip` from the game's installation folder and unzip the copy somewhere convenient. All the vanilla paths below are inside its `data/assets` folder.

Copy each vanilla file into your mod's `V71/assets` folder at the path shown, creating folders as needed, and rename it as shown:

| Vanilla file (in `data/assets`) | Copy to (in `V71/assets`) | What it does |
|---|---|---|
| `init/race/DONDORIAN.txt` | `init/race/MYRACE.txt` | How the race behaves: preferences, population, bonuses and so on. |
| `text/race/DONDORIAN.txt` | `text/race/MYRACE.txt` | The race's name, descriptions and dialogue. |
| `init/race/sprite/DONDORIAN.txt` | `init/race/sprite/MYRACE.txt` | How the race looks: which sprite sheet to use, colours, faces and so on. |
| `sprite/race/Dondorian.png` | `sprite/race/MyRace.png` | The sprite sheet: the image the race's characters are drawn from. |

Note the capitalisation: the three `.txt` files are `MYRACE`, while the image is `MyRace.png`. This matches how the vanilla files are named.

### How these files connect

It helps to know how the game finds these files, because the same patterns appear throughout the modding system:

- The game finds every race by scanning `init/race`. Each file there is one race, and the file name (without `.txt`) is the race's **key**, which other files use to refer to it. Our race's key is `MYRACE`.
- For each race, the game loads the file with the **same name** from `text/race`. That's why the text file must be called `MYRACE.txt` too.
- The race file names its appearance file with a `SPRITE_FILE` entry, which points to a file in `init/race/sprite`.
- The appearance file in turn names the sprite sheet with its own `SPRITE_FILE` entries, which point to an image in `sprite/race`.

Steps 3 to 5 make those connections point at your new files instead of the Dondorian ones.

## Step 3: Edit the text file

Open `text/race/MYRACE.txt`. This file holds everything the player reads about the race.

### Names

The first four lines set what the race is called:

```text
NAME: "Dondorian",
NAMES: "Dondorians",
POSSESSIVE: "Dondorian",
POSSESSIVES: "Dondorian",
```

For the Dondorians, three of these happen to be the same word, which hides what each one is for. Our race will be called the Pomari, a name chosen because its singular, plural and adjective forms are all different:

```text
NAME: "Pomari",
NAMES: "Pomaris",
POSSESSIVE: "Pomarian",
POSSESSIVES: "Pomarian",
```

Change the four lines to match. Here's what each one does:

| Field | Form | Example |
|---|---|---|
| `NAME` | Singular: one member of the race | "a **Pomari**" |
| `NAMES` | Plural: more than one | "two **Pomaris**" |
| `POSSESSIVE` | Adjective: describing something that belongs to, or comes from, the race | "a **Pomarian** home" |
| `POSSESSIVES` | The same adjective, used in a few places where the game refers to the race as a group | "**Pomarian** Raiders" |

Every vanilla race uses the same word for `POSSESSIVE` and `POSSESSIVES`, as we do here. The vanilla Cantors follow the same pattern as the Pomari: Cantor, Cantors, Cantorian.

### Short description

Find the `DESC` entry. In the vanilla file it spans two lines:

```text
DESC: 
"Dondorians are sturdy and stubborn. Don't care much for farming, but excel at mining, enjoy refinement, and are sturdy in battle."
",
```

Replace all three of those lines with this single line:

```text
DESC: "The Pomaris are a fruit-loving offshoot of the Dondorians. Quick on their feet, fond of plain stone buildings, and, when butchered, a surprising source of metal.",
```

### Long description

Find the last line of the `DESC_LONG` entry:

```text
Their favourite foods are Meat, Fish, and Mushrooms.
```

Change it to:

```text
Their favourite food is Fruit.
```

Leave the closing `",` on the line below it as it is.

The rest of this file (greetings, insults, army names and so on) can stay as it is. The `PROS` and `CONS` lists at the bottom still describe the Dondorians, so you may want to update them to match your changes, but the mod works without doing so.

Save the file.

## Step 4: Edit the race file

Open `init/race/MYRACE.txt`. This is the largest of the files, and it controls how the race behaves. You'll make five changes.

### Favourite food

Near the top, inside the `PREFERRED` block, find:

```text
	FOOD: [
		MEAT,
		FISH,
		MUSHROOM,
	],
```

`FOOD` is a list of the race's favourite foods. Each entry must be the key of an edible resource, and the list must contain at least one. Change it to:

```text
	FOOD: [
		FRUIT,
	],
```

### Building preferences

Just below, find the `STRUCTURE` block:

```text
	STRUCTURE: {
		MOUNTAIN: 1.0,
		STONE: 0.3,
		GRAND: 0.6,
		OUTDOORS: 0.2,
		WOOD: 0.1,
	},
```

Each value, from `0` to `1`, sets how much the race likes living in that type of building. Higher values mean a stronger preference. Change the first three values:

```text
	STRUCTURE: {
		MOUNTAIN: 0.1,
		STONE: 1.0,
		GRAND: 0.4,
		OUTDOORS: 0.2,
		WOOD: 0.1,
	},
```

The Pomaris now strongly prefer stone buildings, are lukewarm about grand ones, and have little interest in mountain halls.

### Butchering resources

Further down, find the `RESOURCE` block:

```text
RESOURCE: {
	MEAT: 25,
	LEATHER: 5,
	COTTON: 10,
},
```

These are the resources produced when a member of the race is butchered in the Cannibal room. Replace `MEAT` with `METAL`:

```text
RESOURCE: {
	METAL: 25,
	LEATHER: 5,
	COTTON: 10,
},
```

### Appearance file

Find this line:

```text
SPRITE_FILE: DONDORIAN,
```

This names the appearance file in `init/race/sprite`. Point it at your copy:

```text
SPRITE_FILE: MYRACE,
```

Leave the `ICON_SMALL` and `ICON_BIG` lines below it unchanged; your race will use the Dondorian icons.

### Speed

Near the end of the file is the `BOOST` block. Boosts adjust the race's abilities. Each line names something to change, how to change it (`>MUL` multiplies, `>ADD` adds), and by how much. For example, the existing line `PHYSICS_MASS>MUL: 1.1,` makes Dondorians 10% heavier than the base value.

Find this line in the block:

```text
	PHYSICS_MASS>MUL: 1.1,
```

and add a new line directly beneath it:

```text
	PHYSICS_SPEED>MUL: 1.5,
```

This multiplies the Pomaris' speed by 1.5, making them half again as fast as they would otherwise be.

Save the file.

### A note on the `TRAITS` block

While you're in this file, you may see a `TRAITS` block listing `FIGHTER`, `GLUTTON` and `SPRINTER`. You might expect to change these to make the race faster, as the previous edition of this handbook did. In v0.71.44 the game doesn't read this block at all, and those traits no longer exist. Traits are now defined in [`init/race/trait`](04-Modding-Compendium/01-init/07-race/07-trait.md), and each trait file sets how common it is for each race. Changing the `TRAITS` block has no effect, which is why this guide uses a speed boost instead.

## Step 5: Edit the appearance file

Open `init/race/sprite/MYRACE.txt`. This file controls the race's appearance. It names the sprite sheet twice: once for children (in the `CHILD` block) and once for adults (in the `TYPES` block). Both lines look like this:

```text
		SPRITE_FILE: Dondorian,
```

Change **both** of them to:

```text
		SPRITE_FILE: MyRace,
```

The value is the name of the image in `sprite/race`, without `.png`. Leave the other entries in these blocks unchanged.

Save the file.

Your race now uses its own sprite sheet, `MyRace.png`. At the moment it's an exact copy of the Dondorian sheet, so the Pomaris look like Dondorians. You can open it in an image editor and change it however you like, but that's optional, and the mod works either way.

## Step 6: Check your files

Your finished mod should look like this:

```text
MyFirstMod/
├── _Info.txt
└── V71/
    └── assets/
        ├── init/
        │   └── race/
        │       ├── MYRACE.txt
        │       └── sprite/
        │           └── MYRACE.txt
        ├── sprite/
        │   └── race/
        │       └── MyRace.png
        └── text/
            └── race/
                └── MYRACE.txt
```

## Step 7: Test it

Open the launcher, select **My First Mod** in the mod list, and start the game. While you're testing, it's worth turning on **Debug** in the launcher's Settings so that any problems are reported in detail.

Start a new game. The Pomaris should be available as a playable race, with the name and description you gave them. Once you're playing as them, you can check each change:

- **Food:** they want fruit.
- **Housing:** they prefer stone buildings.
- **Speed:** they move noticeably faster than Dondorians.
- **Butchering:** a Pomari butchered in the Cannibal room yields metal.

If the launcher shows your mod with an error, or the game reports a problem while loading, the message will usually name the file and line at fault. The most common causes are a missing comma, a file in the wrong folder, or a name that doesn't match exactly, including capitalisation.

## What's next

You've made a new race by copying vanilla files and changing them. This is how most modding in Songs of Syx works. Everything else in the race files (population, work preferences, bonuses, colours, faces) can be changed the same way, and the [Modding Compendium](04-Modding-Compendium/00-Modding-Compendium.md) explains what each part does.
