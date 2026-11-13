# Accessibility statement

The Songs of Syx Modding Handbook should be usable by everyone who wants to learn to mod the game, including people who use a screen reader, a keyboard instead of a mouse, zoom or high-contrast settings.

## Standard

The website, https://bendigeidfran.github.io/Syx-Modding-Handbook/, **conforms to the [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) at level AA**.

The PDF has the same content as the website. It isn't claimed to conform to a standard: the website is its accessible version (see [The PDF](#the-pdf)).

## What this means on the site

- All text meets the WCAG contrast ratios in both the light and the dark theme. Links in the text are underlined.
- Every page can be used with a keyboard alone, and pages reflow to a 320-pixel-wide screen without scrolling sideways.
- The tables that list a tag's facts mark each label as a row header, so screen readers read each value with its label.
- **Interactive sprite sheets:** each section of a sheet is a button with a name and a description, and its tooltip can be opened with the keyboard, stays open while the pointer is on it and closes with Escape. Some sprites are smaller than the 24-pixel touch target WCAG asks for, so every sheet is followed by a list of all its sections with the same information.

## How it was tested

Last tested on 13 November 2026, against Songs of Syx Modding Handbook for v0.71.44.

- Every page was checked automatically with [axe-core](https://github.com/dequelabs/axe-core) 4.10 against all WCAG 2.2 A and AA rules, in the light and the dark theme.
- Every page was checked for sideways scrolling at 320 pixels wide.
- The colour contrast of text that axe couldn't measure automatically was measured separately in both themes.
- The sprite sheet controls were tested with the mouse and the keyboard in Microsoft Edge.
- Pages were used with the keyboard alone and zoomed to 200% by hand.
- The site hasn't yet been tested with a screen reader. Labels, headings and table headers were checked in the page code instead. If you use a screen reader and something doesn't work, please report it (see below).

## Known limitations

These don't affect conformance, but you may notice them:

- The site uses the Material for MkDocs theme. Its sidebar sub-menus aren't given distinct names, so a screen reader may announce several navigation areas with the same name. On the audio chapter page, one sub-menu refers to a label the theme doesn't output.
- The image of each sprite sheet has a short text description naming the file. The details of the sheet are in its list of sections, not in the image's description.

## The PDF

The PDF is printed from the same pages as the website. It is tagged, has its language set, has a bookmark for every page and carries each image's text description. It hasn't been checked against the PDF/UA standard, and it doesn't include the sprite sheets' tooltips or section lists. If the PDF doesn't work for you, please use the website.

## Reporting a problem

If something on the site is hard or impossible to use, please [report an accessibility problem](https://github.com/Bendigeidfran/Syx-Modding-Handbook/issues/new?template=accessibility.yml). Say which page, what you were trying to do, and what you use to browse (for example a screen reader, zoom, or keyboard only), if you're happy to share it.
