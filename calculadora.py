from calendar import c
from math import sqrt
from pickletools import string1
from tracemalloc import stop
from turtle import back
import colorama
from colorama import Back, Fore



print( '             Calculadora Phyton')
print('Instruções')
print('soma = +')
print('subtração = -')
print('divisão = /')
print('multiplicação = *')

while True:
 a=int(input('Digite um valor:'))
 b=int(input('Digite o outro valor:'))
 c=(input('Operação:'))

 if c == "+":
  soma = a+b
  print('o valor da soma: {}'.format(soma))

 elif c == "-":
  sub = a-b
  print('o valor da subtração: {}'.format(sub))
  
 elif c == "/":
  div = a/b
  print('o valor da divisão: {}'.format(div))
 
 elif c == "*":
  mult = a*b
  print('o valor da multiplicação: {}'.format(mult))
  input()

 else:
  print('erro: operação invalida')

 out=input("Aperte enter se quiser continuar, se quiser sair digite sair: ")
 if out == "sair":
  break