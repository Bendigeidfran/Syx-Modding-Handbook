# text/event

These files hold the words events show the player: titles, messages and the labels on choices. Events are defined in [`init/event`](../01-init/05-event/00-event.md), and [Event text](../01-init/05-event/04-text.md) explains this format and its placeholders.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/event/` |
| **Files** | One `.txt` file per event file, named after it in `assets/init/event/` |
| **Required** | No. An event without text has no name or message. |
| **Tags** | Described on the [Event text](../01-init/05-event/04-text.md) page |

This is how a block starts in the vanilla `ARTI.txt`:

```text
VOLCANO: {
	NAME: "Promising artifact",
	DESC: "A decision awaits.",
```

## Notes

### A vanilla file the game doesn't read

`TEST2.txt` has no matching file in `assets/init/event/`, so the game doesn't read it.

## Related

- [text](00-text.md)
- [Event text](../01-init/05-event/04-text.md)
- [init/event](../01-init/05-event/00-event.md)
