# -*- coding: utf-8 -*-
"""Practica2_Biseccion.ipynb

# Método de la búsqueda incremental

import numpy as np
from sympy.abc import x, y
from sympy import *
import time
import math
import matplotlib.pyplot as plt


class NumericalMethods:
    
    def bisectionMethod(self, a, b, tol, maxIter, func):
      #Mult +*+ -*- -> no hay cambio de signo...resultado positivo
        if func.subs(x,a) * func.subs(x,b) < 0: #Evaluación de la función en límite inferior * evaluación límite superior
            print("Existe un cambio de signo")
        else: 
            print("No existen raices reales en el intervalo")
            return np.inf 
        error = np.inf #Garantía de entrar a la función aunque el error sea gigante
				# TODO: Completar el método de la bisección
        i = 0 #Se inicia contador
        while( error > tol and i <= maxIter):
            c = (a + b) /2
            error = (b - a) / 2
            #if f(c) = 0 or (b – a)/2 < TOL then
            if func.subs(x, c) == 0 or error < tol: #Ya tienes la solución
              	return c
            i += 1 #Contador aumenta en 1
            # if sign(f(c)) = sign(f(a)) then a ← c else b ← c // new interval
            if func.subs(x,c) <0 and func.subs(x,a) <0 or  func.subs(x,c) >0 and func.subs(x,a) >0:
              	a=c
            else: #No olvides ":"
            		b=c
            
class NaiveMethods:

    def incrementalSearch(self, a, b, func):
        X = np.linspace(a, b, 10000) #(10000 iteraciones desde a hasta b)
        for i in range(len(X)):
            if func.subs(x, X[i]) == 0: #Subs. sustituye el primer parámetro por el segundo
                print("La Raíz real: ", X[i])
            
def main():

    x0 = 0
    maxIter = 10000
    Error = 0.0001
    func = 3*x - 45

    # Crear objetos para el método ingenuo
    objN = NaiveMethods()
    # Instanciar el método de la búsqueda exahustiva
    start = time.time()
    objN.incrementalSearch(-100, 100, func)
    end = time.time()
    elapsedNaive = end-start
    print("The total elapsed time of incremental search was: ", (end-start), "secs")

    # Objeto para métodos numéticos
    objNM = NumericalMethods()
    # Instanciar el método de la bisección
    start = time.time()
    #Parámetros se igualan por posiciones PE: (a=-100, b=100, tol=error, maxIter, func)
    root = objNM.bisectionMethod(-100, 100, Error, maxIter, func) 
    end = time.time()
    elapsedBisection = end-start
    print("Elapsed time Bisection Method: ", end - start)

    print("Naive/Bisection = ", elapsedNaive/elapsedBisection)

    if (root != np.inf): # Interpreta igual un número complejo que infinito
        print("La raíz real es: ", float(root))
    else:
        print("No se encontró la raíz")


if __name__ == "__main__":
    main()
