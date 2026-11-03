# text/room

These files hold the wording of each room: its name and description, and text for its services, work and upgrades. The room itself is defined by the file of the same name in [`init/room`](../01-init/10-room/00-room.md), and that's the chapter that explains the format.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/room/` |
| **Files** | One `.txt` file per room, named after its file in `assets/init/room/` |
| **Required** | Yes, for every room |
| **Tags** | Described under [The text file on the common tags page](../01-init/10-room/01-common.md#the-text-file). Some room types add their own tags, which the page for each group of rooms covers. |

This is the start of the vanilla `WELL_NORMAL.txt`:

```text
INFO: {
	NAME: "Well",
	NAMES: "Wells",
	DESC: "Can be used to endure hot weather or get clean.",
```

## Related

- [text](00-text.md)
- [init/room](../01-init/10-room/00-room.md)
- [init/room: common tags](../01-init/10-room/01-common.md)
