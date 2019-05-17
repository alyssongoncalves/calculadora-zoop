#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def calculadora (operando1, operador, operando2):
    if operador == '+' or operador == '-' or operador == '*' or operador == '/' or operador == '**' or operador == 'mod': 
        if operador == '+':
            total = operando1 + operando2
        elif operador == '-':
            total = operando1 - operando2
        elif operador == '*':
            total = operando1 * operando2
        elif operador == '/':
            total = operando1 / operando2
        elif operador == '**':
            total = operando1 ** operando2
        elif operador == 'mod':
            total = operando1 % operando2
        print(total)
    else:
        print ("Operacao Invalida!")

#for param in sys.argv :
#	print (type(param))
operando1 = int(sys.argv [1])
operando2 = int(sys.argv [3])

calculadora (operando1, sys.argv [2], operando2) 
