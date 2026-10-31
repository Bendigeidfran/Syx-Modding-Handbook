# init/config/LEAVE_CAUSE.txt

`LEAVE_CAUSE.txt` sets how much your subjects resent each way of losing a member of the population, whether by death or by leaving. When someone is lost in a way the game counts as wrongful, such as starving, being murdered or freezing to death, their class and race remember it, and this file decides how much each kind of loss counts.

## At a glance

| | |
|---|---|
| **Location** | `assets/init/config/LEAVE_CAUSE.txt` |
| **Adding new files** | No. Only this file is read. |
| **Adding new causes** | No. The list of causes is built into the game. You can change their values but not add, remove or rename them. |
| **Companion files** | None |

## How it works

Every subject who dies or leaves is recorded under a cause. Some causes the game treats as **wrongful**. When a subject is lost to one of these, the cause's value from this file is added to a running tally of wrongful deaths for that subject's class and race.

That tally, relative to the size of the population, is the **wrongful deaths** statistic (`POPULATION_WRONGFUL_DEATHS`). Races that care about it list it in the `STATS` block of their race file, which sets how strongly it affects their happiness; in vanilla, the Argonosh, Cantors, Garthimi and Amevia do. For those races, a high value here makes that kind of loss more damaging.

The other causes are treated as natural. Their values in this file don't add to the tally.

Separately from the tally, any cause with a value above `0` is shown as a cause for anger in the interface: it's marked with an angry icon in the population screens and included in the wrongful-death notification. This happens even for natural causes.

## Tags

The file is a flat list: one tag for each cause, each set to a decimal value.

| | |
|---|---|
| **Type** | Decimal |
| **Range** | 0 to 10 |
| **Required** | Yes, for every cause below |

### Causes that count towards wrongful deaths

| Key | Name in game | Vanilla value |
|---|---|---|
| `STARVED` | Starved | 2 |
| `ANIMAL` | Mauled by a beast | 0.5 |
| `ACCIDENT` | Misadventure | 0.1 |
| `HEAT` | Heat stroke | 0.5 |
| `COLD` | Hypothermia | 0.5 |
| `MURDER` | Murdered | 2 |
| `DISEASE` | Succumbed to Disease | 0 |
| `EXECUTED` | Executed | 0 |
| `BRAWL` | Killed in a Brawl | 0.5 |

### Causes that never count

Values for these causes have no effect on the wrongful deaths statistic, though a value above `0` still marks them as a cause for anger in the interface.

| Key | Name in game | Vanilla value |
|---|---|---|
| `ARMY` | Army Duty | 0 |
| `EMMIGRATED` | Emigrated | 0 |
| `SACRIFICED` | Sacrificed | 0 |
| `SLAYED` | Slain by enemies | 0 |
| `AGE` | Natural Causes | 0 |
| `PUNISHED` | Punished | 0 |
| `DROWNED` | Drowned | 0.1 |
| `DESERTED` | Deserted | 0.1 |
| `EXILED` | Exiled | 0 |
| `OTHER` | Other | 0 |
| `INSANE` | Insane | 0 |
| `SOLD` | Sold | 0 |

Note the game's spellings `EMMIGRATED` and `SLAYED`.

From the vanilla file:

```text
STARVED: 2,
SLAYED: 0,
ANIMAL: 0.5,
```

## Notes

### Vanilla values for drowning and desertion

Vanilla gives `DROWNED` and `DESERTED` a value of `0.1`, but because the game treats both as natural causes, those values only affect the interface, not your subjects' happiness.

## Related

- [init/config](00-config.md)
