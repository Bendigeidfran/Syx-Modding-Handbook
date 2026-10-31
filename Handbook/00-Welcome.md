# Welcome to the Songs of Syx Modding Handbook

*Written for Songs of Syx v0.71.44*

## About the author

I'm Bendigeidfran. I modded Songs of Syx for several years, and I wrote the earlier version of this handbook back in v0.57. This edition is a ground-up revision of that work.

**A note on AI use:** This handbook was written with the help of a large language model (LLM). I have a day job, and a project of this size wouldn't be practical otherwise; the LLM helped speed up the writing, and the content was checked against the game's own files. This is a living document. If you spot an error or something that's unclear, please ping me (**Bendigeidfran**) on the Songs of Syx Discord (I'm a moderator so my name will be in yellow at the top), so it can be corrected in a future version. You may also comment on the guide wherever you found it, Steam, mod.io, etc - but I can't guarantee a swift response in that case. I do hope people understand my use of an LLM in this case, I wrote the prior versions by hand and it was a labour of many, many hours and was outmoded within a few months - hopefully that shows that I'm not just trying to make slop here, I just don't have that kind of time any more.

## Why this handbook exists

Songs of Syx is unusually open to modding. Races, buildings, resources, animals, climates, events, sprites and text are nearly all defined in plain files you can read and change. You don't need to know how to program to make substantial changes to the game.

That openness comes with a cost. The modding system is large, its files depend on one another in ways that aren't always obvious, and most of it has no official documentation. New modders often learn by copying existing files and changing values until something works. That approach can get you started, but it leaves gaps: when something breaks, or when you want to do something no example covers, you have little to go on.

The game has also changed a great deal since the last edition of this handbook. Files have moved, tags have been added and removed, and the way mods are packaged is different. Much of the old handbook no longer matches the game.

This edition explains *how* the modding system works, as well as *what* each file contains. The aim is for you to understand why a file is laid out the way it is, how it connects to the rest of the game, and what to look at when something goes wrong. Once you have that, the rest of the system becomes much easier to explore on your own.

## Who it's for

This handbook is written for people who are new to modding Songs of Syx. It assumes you have played the game and are comfortable finding and editing files on your computer. It doesn't assume any programming knowledge.

To follow along you'll need:

- A copy of Songs of Syx.
- A plain text editor. Anything that saves plain `.txt` files will do; editors with syntax highlighting and search across files, such as Notepad++ or VS Code, make the work easier.
- An image editor that can handle `.png` files, if you plan to work with sprites.

## Acknowledgements

This handbook builds on the earlier edition, which was a community effort. My thanks to **Jake**, the developer of Songs of Syx, and to **Superwutz** for their contributions to that version. Much of what's here started with their work.

Thanks also to Jake for building a game that invites this kind of tinkering.
