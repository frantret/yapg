#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""yapg: yet another password generator"""

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
    "length":
    f"number of {HELP_CHARS}",
    "digits":
    "allow digits",
    "lowercase":
    "allow lowercase letters",
    "uppercase":
    "allow uppercase letters",
    "punctuation":
    "allow punctuation",
    "homoglyphs":
    "allow characters potentially confused ({})".format(HOMOGLYPHS),
    "compatible":
    "only allow characters common between QWERTY and AZERTY layouts ({})"
    .format(ERTYCOM),
}


def build_list(**kwargs):
    """Builds the list of allowed characters."""
    Set = set()
    if kwargs.get("digits"):
        Set.update(string.digits)
    if kwargs.get("lowercase"):
        Set.update(string.ascii_lowercase)
    if kwargs.get("uppercase"):
        Set.update(string.ascii_uppercase)
    if kwargs.get("punctuation"):
        Set.update(string.punctuation)
    if not kwargs.get("homoglyphs"):
        for m in HOMOGLYPHS:
            Set.discard(m)
    if kwargs.get("compatible"):
        Set = Set.intersection(ERTYCOMMON)
    return "".join(Set)


def gen_pwd_cand(List, LenMin, LenMax):
    """Generates one password candidate."""
    return "".join(
        SYSRAND.choice(List)
        for _ in range(SYSRAND.choice(range(LenMin, LenMax + 1))))


def entropy(String):
    """Calculates the Shannon entropy of a string."""
    Prob = (float(String.count(c)) / len(String) for c in set(String))
    return -sum(p * math.log(p) / math.log(2.0) for p in Prob)


def gen_pwd(List, LenMin, LenMax):
    """Selects one password for its relative higher entropy, amongst a
    set of password candidates.
    """
    Candidates = (gen_pwd_cand(List, LenMin, LenMax) for _ in range(NB_CAND))
    Entropies = {c: entropy(c) for c in Candidates}
    MaxEnt = max(Entropies.values())
    Strongest = tuple(c for c in Entropies if Entropies[c] == MaxEnt)
    return SYSRAND.choice(Strongest)


def build_pwd(List, **kwargs):
    """Builds a password."""
    Length = kwargs.get("length", DEFAULT["length"]).strip().strip(" -")
    try:
        Len1, Len2 = Length.split("-")
    except ValueError:
        Len1 = Len2 = Length
    try:
        Len1 = int(Len1)
        Len2 = int(Len2)
    except ValueError:
        return "Error: the length(s) must be one or two integer(s)."
    LenMin = min(Len1, Len2)
    LenMax = max(Len1, Len2)
    try:
        assert 0 < LenMin <= LenMax
    except AssertionError:
        return "Error: the length(s) must be strictly positive."
    try:
        assert List
    except AssertionError:
        return "Error: the set of allowed characters is empty."
    return gen_pwd(List, LenMin, LenMax)


def main(**kwargs):
    """Main function."""
    # The following condition is for the command line interface to
    # generate a password even if no arguments for allowing characters
    # are given.
    if not (kwargs.get("digits") or kwargs.get("lowercase")
            or kwargs.get("uppercase") or kwargs.get("punctuation")):
        kwargs["digits"] = DEFAULT["digits"]
        kwargs["lowercase"] = DEFAULT["lowercase"]
        kwargs["uppercase"] = DEFAULT["uppercase"]
        kwargs["punctuation"] = DEFAULT["punctuation"]
    List = build_list(**kwargs)
    return build_pwd(List, **kwargs)


def cli():
    """Command-line interface function."""
    Parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    Parser.add_argument(
        "-l",
        "--length",
        type=str,
        default=DEFAULT["length"],
        help=HELP["length"])
    Parser.add_argument(
        "-d", "--digits", action="store_true", help=HELP["digits"])
    Parser.add_argument(
        "-w", "--lowercase", action="store_true", help=HELP["lowercase"])
    Parser.add_argument(
        "-u", "--uppercase", action="store_true", help=HELP["uppercase"])
    Parser.add_argument(
        "-p", "--punctuation", action="store_true", help=HELP["punctuation"])
    Parser.add_argument(
        "-m", "--homoglyphs", action="store_true", help=HELP["homoglyphs"])
    Parser.add_argument(
        "-c", "--compatible", action="store_true", help=HELP["compatible"])
    return vars(Parser.parse_args())


if __name__ == "__main__":
    kwargs = cli()
    print(main(**kwargs))
