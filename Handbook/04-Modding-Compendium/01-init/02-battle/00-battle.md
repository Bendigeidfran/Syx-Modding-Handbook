# init/battle

The `init/battle` folder controls two things about armies that the game builds or arranges for you, rather than ones you design yourself:

- **What computer-generated divisions are made of.** When the game creates a division for an AI faction's army, raiders, invaders or mercenaries, it picks a division type from `init/battle/divType`, which says what training and equipment the division has.
- **How armies line up at the start of a battle.** When a battle begins, the game places every division automatically, using a formation from `init/battle/formation` to decide which divisions go in the centre, on the flanks, at the front and at the back.

The folder contains no files of its own, only these two sub-folders. Neither has companion files in `text`, `sprite` or `audio`.

## Sections

- [init/battle/divType](01-divType.md)
- [init/battle/formation](02-formation.md)

## Related

- [init](../00-init.md)
