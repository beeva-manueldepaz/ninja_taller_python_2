#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        self.a = "hola"


def hola():
    return "sobrecargado"

aa = A()
aa.b = hola() # Me lo acabo de inventar :)

print(aa.a)
print(aa.b)
