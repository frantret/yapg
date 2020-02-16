# Changelog

## 0.2.4-dev: *summary* (unreleased)

-   New
-   Change
    -   Use the `secrets` module.
-   Deprecate
-   Remove
-   Fix
    -   Readme: f-strings were introduced in Python 3.6.
-   Security

## 0.2.3: Apply Black and Pylint (19 August 2019)

-   New
    -   Added [.editorconfig](https://editorconfig.org/) file.
    -   Added development requirements file.
    -   Added the version in the CLI and in the about window of the GUI.
-   Change
    -   GUI: propagated help text for random length.
    -   Replaced `.format()` by f-strings.
    -   Markdown / readme: use ATX-style headers.
    -   GUI: use monospaced font to display the password.
    -   CLI: the `cli()` function returns the parser.
    -   Replaced `assert` statements by `if` conditions.
-   Remove
    -   Markdown: removed useless encoding hints.
    -   CLI: removed useless parser option.
-   Fix
    -   Sorted imports with `isort`.
    -   Applied PEP8 with `black`.
    -   Applied linting with `pylint`.

## 0.2.2: PEP8 and other minor changes (25 May 2018)

-   Fix
    -   Applied PEP8 with `yapf`.

## 0.2.1: Gui fixed (17 February 2018)

-   Fix
    -   Bug in the Gui introduced by the random password's length.

## 0.2.0: With random length (17 February 2018)

-   New
    -   Added random password's length.
-   Change
    -   Moved argument parsing to a command-line interface function.
    -   Added a variable for the number of candidates and reduced the number of
        candidates so the length is more random after the candidate selection.
-   Fix
    -   Applied PEP8.

## 0.1.0: First useful version (3 January 2018)

-   New
    -   Multi-platform.
    -   Entropy source: the one of the system only.
    -   Option to avoid homoglyph characters (`dclI1B8O0S5Z2rnm`).
    -   Option to use only characters common to QWERTY and AZERTY layouts
        (`bcdefghijklnoprstuvxy`).
