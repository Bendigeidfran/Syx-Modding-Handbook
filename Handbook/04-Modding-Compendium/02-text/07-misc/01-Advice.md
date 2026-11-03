# text/misc/Advice.txt

This file holds the advisor's messages, which point new players to a part of the interface when something first goes wrong. Each one is sent at most once per game, and highlights a button when it appears.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/misc/Advice.txt` |
| **Adding new messages** | No. The game asks for these four by name. |

## Tags

### WORKFORCE, SICKNESS, CRIME and LOYALTY

One block for each message, all required. The game adds `Advisor: ` to the start of the title.

| Block | When it's sent |
|---|---|
| `WORKFORCE` | Your rooms need more than 5 workers above your workforce. |
| `SICKNESS` | A subject is sick. |
| `CRIME` | A crime has been recorded. |
| `LOYALTY` | Citizens' loyalty falls below 0.85, once you have more than 15 subjects. |

| Tag | Meaning | Type and range | Required |
|---|---|---|---|
| `NAME` | The message's title. | Text | Yes |
| `NAMES` | The game reads this, but nothing here uses it. Vanilla doesn't use it. | Text | No |
| `DESC` | The message's text. | Text | Yes |
| `WIKI` | Adds an article to the in-game wiki, as described under [`WIKI` on the init/animal page](../../01-init/01-animal.md#wiki). Vanilla doesn't use it here. | Block | No |

The example leaves out the `DESC`.

```text
CRIME: {
	NAME: "Crime",
},
```

## Related

- [text/misc](00-misc.md)
