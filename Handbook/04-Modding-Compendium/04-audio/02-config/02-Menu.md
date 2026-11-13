# audio/config/Menu.txt

`Menu.txt` sets the sound of the main menu: its music, the crackle of its torches, the music under the opening logo, and the sounds of its buttons.

## At a glance

| | |
|---|---|
| **Location** | `assets/audio/config/Menu.txt` |
| **Adding new files** | No. Only this file is read. |
| **Companion files** | The recordings in [audio/music](../04-music.md) and [audio/mono](../03-mono.md) |

## Tags

Each tag takes a [sound path](../00-audio.md#sound-paths). A list is accepted, but only the first file it names is used, so there's no random choice here. A missing tag gives silence.

### CLICK

The default sound when a button in the main menu is clicked. The path is relative to `assets/audio/mono`, so the file must meet the rules for [sound effects](../03-mono.md#the-files).

Once a game has loaded, the game's own buttons use [`UI_CLICK`](03-mono.md#tags) from config/mono instead.

| | |
|---|---|
| **Type** | Sound path, in `assets/audio/mono` |
| **Required** | No |

```text
CLICK: gui->Click,
```

### HOVER

The default sound when the mouse moves onto a button in the main menu. The path is relative to `assets/audio/mono`.

Once a game has loaded, the game's own buttons use [`UI_HOVER`](03-mono.md#tags) from config/mono instead.

| | |
|---|---|
| **Type** | Sound path, in `assets/audio/mono` |
| **Required** | No |

```text
HOVER: gui->Hover,
```

### LOGO

The music for the GAMATRON logo that opens the game. It plays at half volume, and stops when the main menu's music starts. The logo is shown once each time the game is launched. The path is relative to `assets/audio/music`.

| | |
|---|---|
| **Type** | Sound path, in `assets/audio/music` |
| **Required** | No |

```text
LOGO: misc->_Logo,
```

### MENU

The main menu's music. The path is relative to `assets/audio/music`.

Unverified: the code doesn't set this track to repeat, so it may play only once.

| | |
|---|---|
| **Type** | Sound path, in `assets/audio/music` |
| **Required** | No |

```text
MENU: misc->_Menu_New,
```

### TORCH

The crackle of the torches that light the main menu. It starts with the menu music and repeats. The path is relative to `assets/audio/music`, so it's controlled by the Music volume slider.

| | |
|---|---|
| **Type** | Sound path, in `assets/audio/music` |
| **Required** | No |

```text
TORCH: misc->_Torch,
```

## Related

- [audio/config](00-config.md)
- [audio/music](../04-music.md)
- [sprite/menu](../../03-sprite/06-menu/00-menu.md), the main menu's images
