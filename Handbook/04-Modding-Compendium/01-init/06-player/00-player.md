# init/player

The `init/player` folder holds things that belong to you as a player rather than to the world: the ranks your ruler rises through, the play modes you can choose when starting a game, and the titles you earn across all your games.

The folder contains no files of its own, only three sub-folders:

- **Levels** (`init/player/level`) are the ranks your ruler is promoted through as the settlement grows, from Mir upwards. Each can bring bonuses and unlock buildings.
- **Modes** (`init/player/mode`) are the play modes offered when you start a new game. Each applies a set of bonuses and penalties for the whole game.
- **Titles** (`init/player/titles`) are earned by achievements and recorded in your player profile, so they carry over from game to game. When you start a new game, you choose up to five unlocked titles to boost your realm.

Modes and titles are connected. Choosing a mode creates a value that title requirements can check, and vanilla uses this to give each mode a title that can only be earned while playing it.

Each sub-folder has a matching text folder in `assets/text/player/`, with one text file per data file.

## Sections

- [init/player/level](01-level.md)
- [init/player/mode](02-mode.md)
- [init/player/titles](03-titles.md)

## Related

- [init](../00-init.md)
