# init/resource

The `init/resource` folder defines the goods of the game: everything your subjects can gather, make, store, trade and use. Each file directly in the folder is one resource, giving its icon, its images and how fast it spoils.

Six sub-folders then give some of those resources a further role. A resource becomes a drink, a food, a crop or a mineral because a file in the matching sub-folder says so:

| Sub-folder | What a file there does |
|---|---|
| [`drinkable/`](02-drinkable.md) | Makes a resource a drink, served in taverns. |
| [`edible/`](03-edible.md) | Makes a resource a food, served in eateries and canteens. |
| [`growable/`](04-growable.md) | Defines a crop: how it looks, when it's harvested, and how much of it grows wild. |
| [`minable/`](05-minable.md) | Defines a mineral deposit on the map. |
| [`supply/`](06-supply.md) | Defines a supply that armies consume. |
| [`work/`](07-work.md) | Defines equipment that workers use to boost a room's output. |

So a new resource starts with a file in `init/resource`, then gets a file in each sub-folder that applies. Rooms in `assets/init/room/` are what actually produce resources, and [every resource must have a room that can produce it](01-resource-file.md#every-resource-needs-a-producer), or the game crashes.

## Sections

- [The resource file](01-resource-file.md)
- [init/resource/drinkable](02-drinkable.md)
- [init/resource/edible](03-edible.md)
- [init/resource/growable](04-growable.md)
- [init/resource/minable](05-minable.md)
- [init/resource/supply](06-supply.md)
- [init/resource/work](07-work.md)

## Related

- [init](../00-init.md)
