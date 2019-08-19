# Changelog

## x.x.x

### New

-   Added [.editorconfig](https://editorconfig.org/) file.
-   Added development requirements file.

### Change

-   Markdown: removed useless encoding hints.

### Fix

-   Sorted imports with `isort`.

## 0.2.2: PEP8 and other minor changes (25 May 2018)

### Fix

-   Applied PEP8 with `yapf`.

## 0.2.1: Gui fixed (17 February 2018)

### Fix

-   Bug in the Gui introduced by the random password's length.

## 0.2.0: With random length (17 February 2018)

### New

-   Added random password's length.

### Change

-   Moved argument parsing to a command-line interface function.
-   Added a variable for the number of candidates and reduced the number of
    candidates so the length is more random after the candidate selection.

### Fix

-   Applied PEP8.

## 0.1.0: First useful version (3 January 2018)

### New

-   Multi-platform.
-   Entropy source: the one of the system only.
-   Option to avoid homoglyph characters (`dclI1B8O0S5Z2rnm`).
-   Option to use only characters common to QWERTY and AZERTY layouts
    (`bcdefghijklnoprstuvxy`).

