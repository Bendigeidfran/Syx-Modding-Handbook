# Getting Started

This section covers everything you need before you start changing the game: how mods work, where they live, and how to set one up so the game recognises it. By the end you'll have an empty mod that shows up in the launcher, ready for content.

## How mods work

All of the game's vanilla data (the files that define races, rooms, resources, sprites, text and so on) is packed into a single archive in the game's installation folder:

```text
<install folder>/base/data.zip
```

Inside that archive is a folder called `data`, and inside that, a folder called `assets`. Everything you'll mod initially, lives under `assets`.

A mod is a folder that mirrors the layout of that `data` folder. When the game needs a file, it looks in your enabled mods as well as in the vanilla data. This gives you two basic ways to change the game:

- **Change a vanilla file.** Put a file with the same name in the same place in your mod. Your file's tags take the place of the vanilla ones, as described in [Changing a vanilla file](#changing-a-vanilla-file) below.
- **Add a new file.** Many folders are read as lists: the game loads every file it finds there. Put a new file in one of these folders and it's loaded alongside the vanilla ones. This is how mods add new races, rooms, resources and so on.

### Changing a vanilla file

When your mod has a `.txt` file with the same name and place as a vanilla one, the game doesn't simply swap the vanilla file for yours. It reads the vanilla file first, then lays your file over it, **tag by tag**:

- a tag in your file replaces the vanilla tag of the same name;
- a tag in your file that vanilla doesn't have is added;
- a vanilla tag that your file doesn't mention keeps its vanilla value.

This means your file only needs the tags you want to change. For example, this file in your mod at `V71/assets/init/animal/AUROCH.txt` makes aurochs faster and leaves everything else about them as it is in vanilla:

```text
SPEED: 8,
```

It also means you **can't remove a tag** by leaving it out of your copy. Vanilla's value is still there underneath. To change it, include the tag with the value you want.

#### Blocks and lists

Layering normally works on the tags at the top of the file. A block (`{ }`) or list (`[ ]`) in your file replaces the vanilla one as a whole. With this in your mod's `AUROCH.txt`:

```text
CLIMATE: {
	HOT: 1,
},
```

the auroch's `CLIMATE` block contains only `HOT`. Vanilla's `COLD` and `TEMPERATE` values are gone, so aurochs would no longer spawn in cold or temperate climates.

Two optional tags at the top of your file change this:

| Tag | Effect |
|---|---|
| `_JSON_ADD: true,` | Blocks are layered too, tag by tag, at every depth. With it, the `CLIMATE` example above changes `HOT` and keeps vanilla's `COLD` and `TEMPERATE`. |
| `_ARRAY_ADD: true,` | Lists in your file are added to the end of the vanilla lists instead of replacing them. This only works together with `_JSON_ADD`. |

Each applies only to the file it's in. The game only checks whether the tag is present, so `_JSON_ADD: false,` has the same effect as `true`. To turn it off, leave the tag out.

**Don't use these tags in files where every top-level block is its own entry**, such as event files. The game would read `_JSON_ADD` as an entry like any other, and stop with an error.

#### What isn't layered

Layering only applies to `.txt` files. For other files, such as images, the game uses the first copy it finds, looking in your mods before vanilla.

A few `.txt` files are also read this way, without layering, so your copy is used whole. The compendium notes these where they occur; the race biography files in `text/race/bio/` are one example.

### Files that start with an underscore

Files and folders whose names begin with `_` are treated differently. The game doesn't pick them up when it scans a folder for content; it only loads them when it asks for that exact name. For example, `init/room/_CANNIBAL.txt` defines one specific room the game always expects to exist.

You can change an underscore file by placing your own file at the same path, but adding a new underscore file won't create a new entry. If you copy one and rename it, the game won't notice it.

### Hiding vanilla files

Sometimes you want to replace a whole list rather than add to it. For example, you might want your mod's races to be the *only* races. To do this, put an empty file named `_IgnoreVanilla.txt` in the folder. The game will then ignore the vanilla files in that folder and load only the files supplied by mods.

The Steam Workshop mod *Songs of Nirn (TES)* by maxmydoc is a good example. Its `init/race` folder contains `_IgnoreVanilla.txt`, followed by its own race files, including copies of the vanilla races it wants to keep.

`_IgnoreVanilla.txt` only hides vanilla files that your mod doesn't also supply. If your mod has a file with the same name as a vanilla one, that file is still laid over the vanilla version, as described above.

## Finding the mods folder

Mods are kept in a `mods` folder inside the game's user data folder, not in the installation folder. The simplest way to find it is through the launcher: open **Info** from the main launcher screen. It lists the game's local folders, including **Mods**.

By default, the folder is here:

| System | Mods folder |
|---|---|
| Windows | `%AppData%\songsofsyx\mods` (usually `C:\Users\<you>\AppData\Roaming\songsofsyx\mods`) |
| macOS | `~/Library/Application Support/songsofsyx/mods` |
| Linux | `~/.local/share/songsofsyx/mods` |

If you play through Steam, the game also loads mods you've subscribed to on the Steam Workshop from Steam's own workshop folder. You don't need to do anything with that folder; mods you make yourself go in the `mods` folder above.

## Creating your mod folder

Inside the `mods` folder, create a new folder for your mod. The folder name isn't shown to players, so choose something unique that won't clash with other mods. Don't start the name with `_`, because the launcher skips folders whose names begin with an underscore.

This handbook calls this folder your mod's **root folder**.

## The `_Info.txt` file

Every mod needs a file called `_Info.txt` in its root folder. The capital `I` matters, so spell it exactly as shown. This file tells the launcher what to display for your mod.

Create the file and paste in the following:

```text
NAME: "My Mod",
DESC: "A short description of what my mod does.",
AUTHOR: "Your name",
VERSION: "1.0",
INFO: "",
GAME_VERSION_MAJOR: 71,
GAME_VERSION_MINOR: 44,
```

### What each field does

| Field | Purpose |
|---|---|
| `NAME` | The name shown in the launcher's mod list. It doesn't need to match the folder name. |
| `DESC` | A description shown when a player hovers over your mod. |
| `AUTHOR` | Your name, or whatever you'd like to be credited as. |
| `VERSION` | Your mod's own version number. Use any scheme you like, as long as you're consistent. |
| `INFO` | Any extra information, such as a link to your mod's page. Can be left empty. |
| `GAME_VERSION_MAJOR`, `GAME_VERSION_MINOR` | The game version the mod was made for. See the note below. |

If a field is missing, the launcher shows `???` in its place.

**A note on the game version fields:** many mods include `GAME_VERSION_MAJOR` and `GAME_VERSION_MINOR`. They're a useful record of which version you built against, but the game itself doesn't read them. The version the game actually checks comes from your mod's version folder, covered in the next section.

There is also one optional, more technical field, `TEXTURE_CACHE_SIZE`, which accepts `4096`, `8192` or `16384` and defaults to `4096`. Most mods don't need it. Any other value stops the mod from loading.

### Formatting rules

The game's data files, including `_Info.txt`, all follow the same basic format. The same rules apply throughout the rest of the handbook:

- Each entry is a name, a colon, then a value: `NAME: "My Mod",`
- **Every value must be followed by a comma**, including the last one in the file. A missing comma usually causes a loading error, or makes the game read the value wrongly.
- Text values go inside double quotes. The game treats a double quote as the end of the text only when it's followed directly by a comma, so a `"` followed by a comma inside your text will cut it short. It's safest to avoid double quotes inside text altogether.
- Numbers don't need quotes.
- `**` starts a comment: the game ignores everything from there to the end of the line. Put comments on their own line or after an entry's comma, not in the middle of a value.

## The version folder

Next to `_Info.txt`, create a folder named `V` followed by the game's major version number. For v0.71.44, the major version is `71`, so the folder is:

```text
V71
```

All of your mod's content goes inside this folder. A mod without a version folder fails to load.

The version folder is how the game decides whether a mod is up to date. If your mod has no folder matching the major version you're running, the launcher shows it in orange and marks it as outdated. You can still enable an outdated mod, but files and tags change between major versions, so it may fail to load or cause errors.

A mod can contain more than one version folder (for example, `V70` and `V71`) so that it can support several game versions at once. If there's no exact match, the game falls back to another version folder, but you shouldn't rely on which one it picks. Always include a folder for the version you're targeting.

## Inside the version folder

Your version folder mirrors the `data` folder inside `data.zip`. In practice, that means an `assets` folder, with some or all of these inside it:

| Folder | Contains |
|---|---|
| `init` | Data files that define how things behave: races, rooms, resources, animals, technologies, events and more. |
| `text` | Names, descriptions and other text shown to the player. |
| `sprite` | `.png` images: character sprites, icons, map graphics and so on. |
| `audio` | Sound effects and music. |

You only need the folders you're actually using. Here is a cut-down example of a mod that changes races and resources:

```text
mods/
└── MyMod/                       ← the mod's root folder
    ├── _Info.txt
    └── V71/
        └── assets/
            ├── init/
            │   ├── race/
            │   ├── resource/
            │   └── ...
            ├── sprite/
            │   ├── icon/
            │   ├── race/
            │   └── ...
            └── text/
                ├── race/
                ├── names/
                └── ...
```

### Getting copies of the vanilla files

To see how vanilla files are laid out, or to use them as a starting point, copy `base/data.zip` out of the installation folder and unzip it somewhere convenient. Work from that copy. Don't modify `data.zip` itself; your changes belong in your mod.

When you copy a vanilla file into your mod, recreate its full folder path inside your version folder. For example, the vanilla file

```text
data/assets/init/race/DONDORIAN.txt
```

belongs in your mod at

```text
V71/assets/init/race/DONDORIAN.txt
```

### Capitalisation

Treat every file and folder name as case sensitive, and match the capitalisation of the vanilla files exactly. On a case-sensitive file system, which is the norm on Linux, the game won't find a file whose capitalisation is different. On any system, differently capitalised names can be treated as separate files, so a mod's `Dondorian.txt` might sit alongside the vanilla `DONDORIAN.txt` rather than replacing it.

## Load order

You can enable several mods at once. In the launcher's mod list, mods are enabled in the order you click them, and each one shows a number for its place in the load order, starting from `0`.

When more than one mod supplies the same `.txt` file, the game lays them over vanilla one after another, ending with the mod with the **lowest** number. Where two mods set the same tag, the lowest-numbered mod's value wins. For other files, such as images, the lowest-numbered mod's copy is used. Files that mods add, rather than files that share a vanilla name, are combined from every enabled mod.

## Testing your mod

Once your mod folder contains `_Info.txt` and a version folder, it should appear in the launcher's mod list. Select it, then start the game.

Two options in the launcher's **Settings** are worth turning on while you're modding:

- **Debug** starts the game in debug mode, which prints extra information and diagnostics. It's slower, but helpful for tracking down problems.
- **Developer** enables in-game tools for testing things quickly.

If the launcher can't read your mod at all (for example, because the version folder is missing or `_Info.txt` has a formatting error), the mod still appears in the list, along with an error message describing the problem.

## Coming from the old handbook

If you used the v0.57 edition of this handbook, these are the main changes to setup:

- Vanilla files are no longer in a `res/data/assets` folder. They're packed in `base/data.zip`.
- Mod content now goes inside a version folder (`V71`), not directly in the mod's root folder.
- The info file is `_Info.txt`, with a capital `I`.
- `GAME_VERSION_MAJOR` and `GAME_VERSION_MINOR` no longer decide which version a mod is for; the version folder does.
- A mod's copy of a vanilla `.txt` file no longer replaces the whole file. It's laid over the vanilla file tag by tag, so it only needs the tags you change (see [Changing a vanilla file](#changing-a-vanilla-file)).

## What's next

You now have an empty mod that the game recognises. Next, [Your First Mod](03-Your-First-Mod.md) walks you through filling it with content: a new playable race.
