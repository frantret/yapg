# yapg: yet another password generator

yapg is a simple password generator.

## Dependencies

It is implemented in Python. Its only dependency is a basic Python
installation. More specifically: Python 3.4 or above, and Python-TK for
the graphical interface.

## Features

-   multi-platform
-   entropy source: the one of the system only
-   password's length is random
-   option to avoid homoglyph characters (`dclI1B8O0S5Z2rnm`)
-   option to use only characters common to QWERTY and AZERTY layouts (`bcdefghijklnoprstuvxy`)

## Use

-   for a command line interface (with no options, it yields a password
    with default options):

    ```bash
    ./yapg.py [options]
    # description of the options:
    ./yapg.py -h
    ```

-   for a graphical interface:

    ```bash
    ./gyapg.pyw
    ```

## License

[3-clause BSD-type](LICENSE.md).
