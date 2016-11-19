<!-- -*- coding: utf-8 -*- -->

*(French version below.)*

yapg: yet another password generator
====================================

yapg is a simple password generator.

Dependencies
------------

It is implemented in Python. Its only dependency is a basic Python
installation. More specifically: Python 3.4 or above, and Python-TK for
the graphical interface.

Features
--------

-   multi-platform
-   entropy source: the one of the system only
-   option to avoid homoglyph characters (``dclI1B8O0S5Z2rnm``)

Use
---

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

License
-------

3-clause BSD-type license---see [LICENSE.md][1].

------------------------------------------------------------------------

yapg : encore un générateur de mots de passe
============================================

yapg est un générateur de mots de passe simple.

Dépendances
-----------

Il est mis en œuvre en Python. Sa seule dépendance est une installation
basique de Python. Plus spécifiquement : Python 3.4 ou supérieur, et
Python-TK pour l'interface graphique.

Caractéristiques
----------------

-   multi-plateforme
-   source d'entropie : uniquement celle du système
-   option pour éviter les caractères homoglyphes (``dclI1B8O0S5Z2rnm``)

Utilisation
-----------

-   pour une interface en ligne de commande (sans option, elle génère un
    mot de passe avec des options par défaut) :

    ```bash
    ./yapg.py [options]
    # description des options :
    ./yapg.py -h
    ```

-   pour une interface graphique :

    ```bash
    ./gyapg.pyw
    ```

Licence
-------

Licence de type BSD avec 3 clauses -- voir [LICENSE.md][1].

[1]: LICENSE.md
