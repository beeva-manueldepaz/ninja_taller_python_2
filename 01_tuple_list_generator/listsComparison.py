#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# tupla = (1,2,3)
# lista = [1,2,3]

# 3G de memoria -> acceso aleatorio
c = (x for x in range(1000000000))

time.sleep(400)

# 5.8 megas de memoria -> consumo secuencia cuando no leemos
c = [x for x in range(1000000000)]

