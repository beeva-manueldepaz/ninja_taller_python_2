#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from functools import partial

def my_fun(data, status):
    print(data)

def main(data:str, callback:Callable):
    d = data + "----> añadido"
    callback(d)

# Sólo un parámetro
# main("Hola mundo", my_fun)

# main con varios parámetros
main("Hola mundo", my_fun)

f = partial(my_fun, "status")
f2 = partial(my_fun, "status", "otroo", "mass") # debe ser el último

main("Hola mundo", f)