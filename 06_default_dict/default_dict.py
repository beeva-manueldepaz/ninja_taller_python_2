#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = ["hola", "mundo"]

results = {}
for i,x in enumerate(range(1000)):
    k = a[0] if i%2 == 0 else a[1]

    if k not in results.keys():
        results[k] = []