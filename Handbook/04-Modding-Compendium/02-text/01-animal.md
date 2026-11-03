# text/animal

These files hold the name and description of each animal species. The species itself is defined by the file of the same name in [`init/animal`](../01-init/01-animal.md), and that's the page that explains the format.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/animal/` |
| **Files** | One `.txt` file per species, named after its file in `assets/init/animal/`, e.g. `AUROCH.txt` |
| **Required** | Yes, for every species |
| **Tags** | `NAME`, `NAMES`, `DESC` and `WIKI`, described under [The text file on the init/animal page](../01-init/01-animal.md#the-text-file) |

This is the whole of the vanilla `MOUNT.txt`:

```text
INFO: {
	NAME: "War-Beast",
	NAMES: "War-Beast",
	DESC: "The war beast. Can be tamed enough to ride upon and give our troops much leverage in battle.",
},
```

## Related

- [text](00-text.md)
- [init/animal](../01-init/01-animal.md)
