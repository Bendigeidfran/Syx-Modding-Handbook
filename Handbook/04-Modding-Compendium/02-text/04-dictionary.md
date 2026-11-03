# text/dictionary

This file holds most of the wording built into the game's interface: button labels, tooltips, messages and more. If some text in the game doesn't come from another file, it's probably here, and this is the file to edit to change it.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/dictionary/Dic.txt` |
| **Files** | This one file |
| **Adding new files** | No. Only this file is read. |
| **Adding new entries** | No. An entry only does something if the game's code asks for it. |

## File format

The file holds one block for each part of the game's code, named after the code's class. Each block holds entries, and each entry is a name and its text. The file is long, but that's the whole format.

This is the whole of the first block in the vanilla file:

```text
cutscene.CutScene: {
	desc: "Hold left mouse button to skip.",
	loading: "Loading...",
},
```

To change some wording, search `Dic.txt` for the words you want to change, then change the text. Leave the names as they are, because they're what the code looks for.

### Placeholders

Text with `{0}`, `{1}` and so on has values put in by the game, so keep them. This example comes from the block `game.events.slave.EventUprising`:

```text
amount: "{0} slaves have joined the uprising.",
```

## Notes

### Changing it from a mod

Your file is [layered over vanilla's](../../02-Getting-Started.md#changing-a-vanilla-file), so it only needs the blocks you change. Each block is replaced whole, though. Put `_JSON_ADD` in your file so that it only needs the entries you change, or else copy every entry in the block.

### Missing entries

A missing entry doesn't stop the game. The text usually shows the entry's name instead, which looks like `exhMess`. If the class's whole block is missing, some text keeps the wording built into the code, while the rest shows the entry's name. The game only reports these with Debug or Developer mode on.

## Related

- [text](00-text.md)
- [Changing a vanilla file](../../02-Getting-Started.md#changing-a-vanilla-file)
