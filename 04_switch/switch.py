#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

def one():
    return "one :)"

def two():
    return "dos :)"

def by_default():
    return "catorce!"

choices = {
    1: one,
    2: two
}

def main(select: str) -> str:
    try:
        f = CHOICES[select]
    except KeyError:
        f = by_default()

    return f

main(2)
main(7)