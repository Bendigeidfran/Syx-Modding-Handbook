# text/tech

These files hold the name of each technology tree, and the name and description of its technologies. The tree itself is defined by the file of the same name in [`init/tech`](../01-init/14-tech.md), and that's the page that explains the format.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/tech/` |
| **Files** | One `.txt` file per tree, named after its file in `assets/init/tech/` |
| **Required** | Yes, for every tree |
| **Tags** | Described under [The text file on the init/tech page](../01-init/14-tech.md#the-text-file) |

This is the start of the vanilla `SCIENCE.txt`:

```text
NAME: "Science",
TECHS: {
	EMBA0: {
		NAME: "Embassy",
		DESC: "Unlocks a place that lets us improve relations with other factions and manipulate their courts.",
	},
```

## Related

- [text](00-text.md)
- [init/tech](../01-init/14-tech.md)
