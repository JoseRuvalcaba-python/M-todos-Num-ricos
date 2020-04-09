# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:53:11 2020

@author: Usuario
"""
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from sympy import log,exp,tan,cos,sin,ln
x=sy.Symbol("x")
def CuartaDerivada(f,x,c):
    h=1*10**(-4)  #Tener cuidado
    return (f.subs(x,c+2*h)+f.subs(x,c-2*h)-4*f.subs(x,c+h)-4*f.subs(x,c-h)+6*f.subs(x,c))/(h**4)
def PrimeraDerivada(f,x,c):
    h=1*10**(-6) #tener cuidado
    return (f.subs(x,c+h)-f.subs(x,c-h))/(2*h)
def SegundaDerivada(f,x,c):
    h=1*10**(-4)  #Tener cuidado
    return (f.subs(x,c+h)+f.subs(x,c-h)-2*f.subs(x,c))/(h**2)
def TerceraDerivada(f,x,c):
    h=1*10**(-4)  #Tener cuidado
    return (f.subs(x,c+2*h)-f.subs(x,c-2*h)-2*(f.subs(x,c+h)-f.subs(x,c-h)))/(2*h**3)

##Regla de  1/3 de Simpson Extendida
##func=exp(x)*sin(x**2)
#o=1
#m=0
#func=1/(o*(2*np.pi)**(1/2))*exp((-(x-m)**2)/(2*o**2))  #Distribución Normal
#a=float(input("Ingrese el límite inferior: "))
#b=float(input("Ingrese el límite superior: "))
#N=int(input("Ingrese el número de subintervalos: "))
#h,c=(b-a)/N, (b+a)/2
#Int=h/3*(func.subs(x,a)+func.subs(x,b))-((b-a)*(h**4)/180)*CuartaDerivada(func,x,c)
#for i in range(1,N):
#    if i%2==0:
#        Int=Int+(2/3)*h*func.subs(x,a+i*h)
#    elif i%2!=0:
#        Int=Int+(4/3)*h*(func.subs(x,a+i*h))
##print(sy.N(CuartaDerivada(func,x,c)))
#print(sy.N(Int))

# #Relga de Trapecio
# x=sy.Symbol("x")
# a=float(input("Ingrese el límite inferior: "))
# b=float(input("Ingrese el límite superior: "))
# N=int(input("Ingrese el número de subintervalos: "))
# N=100
# o=1
# m=0
# func=1/(o*(2*np.pi)**(1/2))*exp((-(x-m)**2)/(2*o**2))  #Distribución Normal
# h=(b-a)/N
# b=a+h
# c=(a+b)/2
# I=h/2*(func.subs(x,a)+func.subs(x,b))-1/12*(h**3)*SegundaDerivada(func,x,c)
# for i in range(1,N-1):
#     a=b
#     b=a+h
#     c=(a+b)/2
#     I=I+h/2*(func.subs(x,a)+func.subs(x,b))-1/12*(h**3)*SegundaDerivada(func,x,c)
# print(f"La integral es {I}")
    
# #Método de Euler. Péndulo Simple
# g,l,t0,v0,theta0=[9.81,1,0,0,np.pi/4]
# y0=l*(1-abs(np.cos(theta0)))
# x0=l*np.sin(theta0)
# h=0.001
# c=3
# a0=-g/l*np.sin(theta0)-c*v0
# listax,listat,listay,listav0,listatheta0,listaa0=[[],[],[],[],[],[]]
# s=10000
# for i in range(1,s):
#     listat.append(i*h)
#     listax.append(x0)
#     listay.append(y0)
#     listatheta0.append(theta0)
#     listav0.append(v0)
#     listaa0.append(a0)
#     t0=h*i
#     theta0=theta0+h*v0
#     v0=v0+h*a0
#     a0=-g/l*np.sin(theta0)-c*v0
#     y0=l*(1-abs(np.cos(theta0)))
#     x0=l*np.sin(theta0)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(listat,listatheta0,color="green",linewidth=2)
# plt.show()
# listaabs=[]
# for i in listay:
#     listaabs.append(abs(i))
# indicemin=listaabs.index(min(listaabs))
# indicemax=listaabs.index(max(listaabs))
# xmax=listax[indicemax]
# vmin=listav0[indicemin]
# print(f"La distancia máxima en x es {abs(xmax)}")
# print(f"La velocidad máxima es {max(listav0)}")

##Método de Biyección
#a=float(input("Ingrese su estimación en a: "))
#b=float(input("Ingrese su estimación en b: "))
#c=(a+b)/2
#x=sy.Symbol("x")
#func=cos(exp(1/log(x,10)))
#fa=func.subs(x,a)
#fb=func.subs(x,b)
#fc=func.subs(x,c)
#epsilon=1/10**(6)
#while True:
#    c=(a+b)/2
#    fa=func.subs(x,a)
#    fb=func.subs(x,b)
#    fc=func.subs(x,c)
#    if abs(fa)>abs(fb):
#        a=c
#    elif abs(fa)<abs(fb):
#        b=c
#    if abs(b-a)<epsilon:
#        break
#print(f"La raíz es {c}")        

##Método de Newton para Raíces
#epsilon=1/10**(6)
#def eval(x0):
#    Derivada=PrimeraDerivada(func,x,x0)
#    xi=x-func/Derivada
#x=sy.Symbol("x")
#func=cos(exp(1/log(x,10)))
#x0=float(input("Ingrese su estimación: "))
#Derivada=PrimeraDerivada(func,x,x0)
#xi=x-func/Derivada
#while abs(func.subs(x,x0)/Derivada)>=epsilon:
#    x0=sy.N(xi.subs(x,x0))
#    eval(x0)
#print(f"La raíz es {x0}")