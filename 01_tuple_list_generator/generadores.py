#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def my_generador():
    yield 1
    print("no. 1")
    yield 10
    print("no. 10")
    yield "a"
    print("letra a")
    yield "h"
    print("letra h")
    yield "random"
    print("texto random")

    #for x in range(200):
        #yield x

# Opc 1 a traves de un for
for x in my_generador():
    print(x)
    time.sleep(2)

# Convertimos a una lista
print(list(my_generador()))

# Tuplas: Estructuras iterables diseñadas para recorrer pero no para operar
# -> diseñada para el rendimiento y ahorro de memoria
# p.e. settings en los framework de web

tupla = (1, "a", "b")


# > set(['a', 'c', 'b'])

# Ojo con las transformaciones -> no conservan los órdenes
# Los elementos de un set deben ser diferentes, los repetidos se eliminan
# Los set ofrecen operaciones matemáticas

l2 = ["a", "b", "c", "a", "a"]
print(set(l2))
l3 = ["h", "j", "k"]

s1 = set(l2)
s2 = set(l3)

i = s1.intersection(s2)
print (i)

if 1:
    print("x")

if "a":
    print("a")

# Ojo con esto, la condicion seria falsa, cuidado con el length = 0
if []:
    print("a")

if not []:
    print("lista") # imprime esto

if i:
    print("no son diferentes")


# Nota:

#range -> en memoria
# xrange -> utiliza generadores por debajo
