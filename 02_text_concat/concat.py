#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

result = []
for x in range(random.randint(50,2000)):
    t = random.choice("asdfasd")
    result.append(t)

# Todo es un objeto
text = "".join(result)

print(result)
