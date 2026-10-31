# init/config/LandingParty.txt

`LandingParty.txt` sets the supplies your settlers bring with them when you found a new settlement. They appear as piles of resources beside your starting camp.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/LandingParty.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | None |

## Tags

### RESOURCES

The starting supplies, as a block of resource keys and amounts. Each entry becomes one pile in the starting camp.

| | |
|---|---|
| **Type** | Block of integers, keyed by resource |
| **Range** | Each amount 1 or more. The game's code names a maximum of 500, but doesn't enforce it. |
| **Required** | Yes |

```text
RESOURCES: {
	STONE: 60,
	WOOD: 100,
	RATION: 40,
	LIVESTOCK: 16,
	FRUIT: 60,
	VEGETABLE: 60,
},
```

A key that doesn't match a resource causes a loading error.

## Notes

### At most ten piles

The starting camp has room for ten piles, so only the **first ten** entries are used. Any further entries are ignored.

### Landing bonuses

Each amount is increased by your landing bonus, which comes from the game's boost system. Without a landing bonus, you get exactly the amounts in this file.

The number of settlers you start with isn't set here; it also comes from the landing bonus.

## Related

- [init/config](00-config.md)
