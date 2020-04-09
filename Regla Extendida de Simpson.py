"""
Métodos Numéricos

Regla 1/3 Extendida de Simpson

@author: José Manuel Ruvalcaba Rascón
"""
import sympy as sy  #Definir funciones de forma simbólica.
from sympy import exp,sin
from sympy.interactive import printing
printing.init_printing(use_latex=True)  #Imprimir como LaTeX.

x=sy.Symbol("x") #Símbolo para definir la función.
func=exp(x)*sin(x**2) #Función a integrar.

def f(y): #Para evaluar la función en algún punto y.
    return func.subs(x,y)

def CuartaDerivada(x): #Cuarta derivada de la función en algún punto x.
    h=1*10**(-4)  
    return (f(x+2*h)+f(x-2*h)-4*f(x+h)-4*f(x-h)+6*f(x))/(h**4)

def ReglaSimpson(a,b):
    N=int(((b-a)/0.01+1)*2) #Número de subintervalos par.
    h,c=(b-a)/N, (b+a)/2 #Definimos h y x media (c).
    Int=h/3*(f(a)+f(b))-(b-a)*(h**4)/180*CuartaDerivada(c)
    for i in range(1,N):
        if i%2==0:   Int+=(2/3)*h*f(a+i*h) #Para i par.
        elif i%2!=0: Int+=(4/3)*h*f(a+i*h) #Para i impar.
    return Int

a=float(input("Ingrese el límite inferior: ")) #Para el ejemplo es -1.
b=float(input("Ingrese el límite superior: ")) #Para el ejemplo es 1.
Integral=ReglaSimpson(a,b)

print("La integral de la función ")
display(func) #Función print utilizando sympy
print(f"en el intervalo [{a},{b}] es:")
print(sy.N(Integral))

