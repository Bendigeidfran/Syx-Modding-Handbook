# text/wiki

These files hold articles for the in-game wiki that don't belong to any one room or race, such as vanilla's guide. Other articles come from the `WIKI` tag in text files elsewhere, which is described under [`WIKI` on the init/animal page](../01-init/01-animal.md#wiki).

## At a glance

| | |
|---|---|
| **Location** | `assets/text/wiki/` |
| **Files** | Any number of `.txt` files. Vanilla has `GUIDE.txt` and `ROOMS.txt`. |
| **Adding new files** | Yes. The game reads every file in the folder whose name doesn't start with `_`. |

## Tags

The file name doesn't matter, because each article states its own name and category.

### WIKIS

The file's articles, as a list of blocks. Each block has the tags described on the [init/animal page](../01-init/01-animal.md#wiki): [`NAME`](../01-init/01-animal.md#wikiname), [`CATEGORY`](../01-init/01-animal.md#wikicategory), [`TEXT`](../01-init/01-animal.md#wikitext) and [`LINK_KEY`](../01-init/01-animal.md#wikilink_key). This example comes from the vanilla `GUIDE.txt`, and the `TEXT` is left out.

| | |
|---|---|
| **Type** | List of blocks |
| **Required** | No |

```text
WIKIS: [
	{
		CATEGORY: "Guide",
		NAME: "01. Introduction",
		CATEGORIES: [],
		LINK_KEY: INTRODUCTION,
	},
],
```

### WIKI

A single article, as one block with the same tags. Vanilla doesn't use it in this folder.

| | |
|---|---|
| **Type** | Block |
| **Required** | No |

## Related

- [text](00-text.md)
- [WIKI on the init/animal page](../01-init/01-animal.md#wiki)
