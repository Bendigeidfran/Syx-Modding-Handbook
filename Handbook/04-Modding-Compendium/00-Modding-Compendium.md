# Modding Compendium

The rest of this handbook is a reference. Where Getting Started and Your First Mod lead you down a set path, the compendium is for looking things up: it documents the game's moddable files and the tags inside them, one area at a time.

You don't need to read it in order. Find the area you're working on, read its page, and follow the links to related pages as you need them.

## How it's organised

The compendium follows the layout of the game's own data. Every moddable file lives somewhere under `data/assets` inside `base/data.zip`, and the compendium's chapters mirror those folders exactly:

- **init** holds the data files that define how things behave: races, rooms, resources, animals, technologies, events and more. Most modding happens here.
- **text** holds the names, descriptions and other text shown to the player.
- **sprite** holds the images: character sprite sheets, icons, map graphics and so on.
- **audio** holds sound effects, music and the files that configure them.

Each folder has a chapter page introducing it. Below that, the structure depends on the folder:

- When every file in a folder follows the same format (for example, every file in `init/animal` describes one animal, using the same tags), the folder gets **a single page** documenting that format.
- When each file in a folder has its own format (for example, `init/config`, where every file configures something different), the folder gets a chapter page and **one page per file**.

So if you know where a file sits in the game's data, you know where to find it here.

## How to read a page

Every page follows the same layout:

1. **An overview** of what the files control and where you'll see their effects in game.
2. **At a glance**: where the files live, what they're called, how other files refer to them, whether you can add new ones, and which other files go with them.
3. **Tags**: every tag the game reads from the file, one section each. Closely related tags, such as those inside a block, may share a table instead. A name such as `WIKI.TEXT` means the `TEXT` tag inside the `WIKI` block.
4. **Notes**: anything that doesn't fit under a single tag, such as rules that span several files or tags that appear in vanilla files but have no effect.
5. **Related pages**.

### Tag entries

Each tag entry describes what the tag does, followed by a short table:

| Field | Meaning |
|---|---|
| **Type** | What kind of value the tag takes. See the list below. |
| **Range** | The values the game accepts. A value outside this range causes a loading error, with one exception: for integers, the game only checks the minimum. Where the game's code also names a maximum for an integer, the entry mentions it; staying within it is the safe choice, even though exceeding it won't cause an error. |
| **Required** | Whether the tag must be present. If it's optional, the entry gives the default the game uses when it's missing. |
| **Effect** | Shown on some tags that do nothing. `None` means the game reads the tag but nothing uses it. `Unread` means the game doesn't read it at all. |

The types you'll see are:

- **Integer**: a whole number, such as `4`.
- **Decimal**: a number that may have a fractional part, such as `0.5`.
- **True/false**: either `true` or `false`, in lower case.
- **Text**: words in double quotes, such as `"Auroch"`. Mostly found in `text` files.
- **Key**: the name of something defined elsewhere, written without quotes, such as `MEAT` or `AUROCH`. The entry says what kind of thing the key must refer to.
- **List**: several values in square brackets, each followed by a comma, such as `[MEAT, LEATHER,]`.
- **Block**: a group of tags in curly brackets, such as `CLIMATE: { COLD: 0.8, },`. The entry lists which tags the block can contain.

Each entry ends with an example taken from a vanilla file, so you can see the tag as the game itself uses it.

A sentence starting with **Unverified:** hasn't been confirmed in the game's code, so treat it as a best understanding, and test it in game if you depend on it.

### Spelling

Tag names, keys and file names are reproduced exactly as the game spells them, including any unusual spelling. The game reads them literally, so a "corrected" spelling won't work.

## Chapters

Chapters are added as they're written. Those not yet available are listed without a link.

- [init](01-init/00-init.md)
- text (not yet written)
- sprite (not yet written)
- audio (not yet written)
