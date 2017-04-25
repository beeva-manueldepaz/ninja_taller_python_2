#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mypy
from typing import List

# def suma(a, b) -> válido pero confuso

def suma(a: int, b:int) -> int:
    return a + b

# Ver fira code -> para que ponga flechitas :)

def my_two_function(l: List[str]) -> Dict[str, int]:
    d = {}
    for i, x in enumerate(l):
        d[str(i)] = x

    return d


r = my_two_function(1)
