# init

The `init` folder holds the data that defines how the game's content behaves. Each animal, race, room, resource, technology and so on has a file here containing its tags: the values that decide how heavy an animal is, what a race likes to eat, what a building costs and produces, and much more.

Most mods make the bulk of their changes in `init`. A file here usually has companions in the other top-level folders: a file of the same name in `text` for its name and description, and images in `sprite` that it refers to by name.

In the game's data, the folder is at `data/assets/init`. In a mod, it goes in `V71/assets/init`.

## Sections

Sections are added as they're written. Those not yet available are listed without a link.

- [init/animal](01-animal.md)
- [init/battle](02-battle/00-battle.md)
- [init/config](03-config/00-config.md)
- [init/disease](04-disease.md)
- [init/event](05-event/00-event.md)
- [init/player](06-player/00-player.md)
- [init/race](07-race/00-race.md)
- init/religion (not yet written)
- init/resource (not yet written)
- init/room (not yet written)
- init/script (empty in vanilla; not yet written)
- init/settlement (not yet written)
- init/stats (not yet written)
- init/tech (not yet written)
- init/world (not yet written)
