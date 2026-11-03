# text/misc/Quotes.txt

This file holds the quotes the game picks from at random for its loading screen.

## At a glance

| | |
|---|---|
| **Location** | `assets/text/misc/Quotes.txt` |
| **Adding new files** | No. Only this file is read. |

## Tags

### QUOTES

The quotes, as a list of text. Each entry is the quote, then `:::`, then who said it, and `::` works too. An entry the game can't split into those two parts appears blank and gets a line in its log. An empty list stops the game with an error.

| | |
|---|---|
| **Type** | List of text |
| **Range** | 1 or more |
| **Required** | Yes |

```text
QUOTES: [

""To be rich is to be content with what one has.":::-The Burned Preacher",
],
```

## Related

- [text/misc](00-misc.md)
