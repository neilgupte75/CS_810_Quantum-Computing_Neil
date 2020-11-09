# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:53:17 2020

@author: Neil Gupte
"""

from qiskit.aqua.algorithms import Shor
a, N = 2, 3
shor = Shor(N, a)
circuit = shor.construct_circuit()
circuit.draw()

