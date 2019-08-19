#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""yapg: yet another password generator"""
__app__ = "yapg"
__version__ = "0.2.3-dev"

import argparse
import math
import random
import string

HOMOGLYPHS = "dclI1B8O0S5Z2rnm"
ERTYCOM = "bcdefghijklnoprstuvxy"
ERTYCOMMON = set(ERTYCOM)
ERTYCOMMON.update(ERTYCOM.upper())
NB_CAND = 10
SYSRAND = random.SystemRandom()
DEFAULT = {
    "length": "30-40",
    "digits": True,
    "lowercase": True,
    "uppercase": True,
    "punctuation": False,
    "homoglyphs": True,
    "compatible": False,
}
HELP_CHARS = "characters (can be random: min-max)"
HELP = {
    "length": f"number of {HELP_CHARS}",
    "digits": "allow digits",
    "lowercase": "allow lowercase letters",
    "uppercase": "allow uppercase letters",
    "punctuation": "allow punctuation",
    "homoglyphs": f"allow characters potentially confused ({HOMOGLYPHS})",
    "compatible": f"only allow characters common between QWERTY and AZERTY layouts ({ERTYCOM})",
}


def build_list(**kwargs):
    """Builds the list of allowed characters."""
    chars = set()
    if kwargs.get("digits"):
        chars.update(string.digits)
    if kwargs.get("lowercase"):
        chars.update(string.ascii_lowercase)
    if kwargs.get("uppercase"):
        chars.update(string.ascii_uppercase)
    if kwargs.get("punctuation"):
        chars.update(string.punctuation)
    if not kwargs.get("homoglyphs"):
        for homoglyph in HOMOGLYPHS:
            chars.discard(homoglyph)
    if kwargs.get("compatible"):
        chars = chars.intersection(ERTYCOMMON)
    return "".join(chars)


def gen_pwd_cand(chars, len_min, len_max):
    """Generates one password candidate."""
    return "".join(
        SYSRAND.choice(chars)
        for _ in range(SYSRAND.choice(range(len_min, len_max + 1)))
    )


def entropy(string_):
    """Calculates the Shannon entropy of a string."""
    probs = (float(string_.count(c)) / len(string_) for c in set(string_))
    return -sum(p * math.log(p) / math.log(2.0) for p in probs)


def gen_pwd(chars, len_min, len_max):
    """Selects one password for its relative higher entropy, amongst a
    set of password candidates.
    """
    candidates = (gen_pwd_cand(chars, len_min, len_max) for _ in range(NB_CAND))
    entropies = {c: entropy(c) for c in candidates}
    max_ent = max(entropies.values())
    strongest = tuple(c for c in entropies if entropies[c] == max_ent)
    return SYSRAND.choice(strongest)


def build_pwd(chars, **kwargs):
    """Builds a password."""
    length = kwargs.get("length", DEFAULT["length"]).strip().strip(" -")
    try:
        len_1, len_2 = length.split("-")
    except ValueError:
        len_1 = len_2 = length
    try:
        len_1 = int(len_1)
        len_2 = int(len_2)
    except ValueError:
        return "Error: the length(s) must be one or two integer(s)."
    len_min = min(len_1, len_2)
    len_max = max(len_1, len_2)
    try:
        assert 0 < len_min <= len_max
    except AssertionError:
        return "Error: the length(s) must be strictly positive."
    try:
        assert chars
    except AssertionError:
        return "Error: the set of allowed characters is empty."
    return gen_pwd(chars, len_min, len_max)


def main(**kwargs):
    """Main function."""
    # The following condition is for the command line interface to
    # generate a password even if no arguments for allowing characters
    # are given.
    if not (
        kwargs.get("digits")
        or kwargs.get("lowercase")
        or kwargs.get("uppercase")
        or kwargs.get("punctuation")
    ):
        kwargs["digits"] = DEFAULT["digits"]
        kwargs["lowercase"] = DEFAULT["lowercase"]
        kwargs["uppercase"] = DEFAULT["uppercase"]
        kwargs["punctuation"] = DEFAULT["punctuation"]
    chars = build_list(**kwargs)
    return build_pwd(chars, **kwargs)


def cli():
    """Command-line interface function."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-V", "--version", action="version", version=f"{__app__} {__version__}"
    )
    parser.add_argument(
        "-l", "--length", type=str, default=DEFAULT["length"], help=HELP["length"]
    )
    parser.add_argument("-d", "--digits", action="store_true", help=HELP["digits"])
    parser.add_argument(
        "-w", "--lowercase", action="store_true", help=HELP["lowercase"]
    )
    parser.add_argument(
        "-u", "--uppercase", action="store_true", help=HELP["uppercase"]
    )
    parser.add_argument(
        "-p", "--punctuation", action="store_true", help=HELP["punctuation"]
    )
    parser.add_argument(
        "-m", "--homoglyphs", action="store_true", help=HELP["homoglyphs"]
    )
    parser.add_argument(
        "-c", "--compatible", action="store_true", help=HELP["compatible"]
    )
    return parser


if __name__ == "__main__":
    PARSER = cli()
    print(main(**vars(PARSER.parse_args())))
