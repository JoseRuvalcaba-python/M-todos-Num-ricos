# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:58:26 2020

@author: Usuario
"""

import vpython as vp 
import numpy as np

MasaSolar = 1.988544e30 
MasaTierra = 5.97219e24 / MasaSolar
MasaSaturno = 5.683e26 / MasaSolar
MasaMercurio = 3.285e23 / MasaSolar
MasaNeptuno = 1.024e26 / MasaSolar
MasaMarte = 6.39e23 / MasaSolar
MasaJupiter = 1898.13e24 / MasaSolar

RadioTierra = 149600e3
RadioSaturno = 1429400e3 / RadioTierra
RadioMercurio = 57910e3 / RadioTierra
RadioNeptuno = 4504300e3 / RadioTierra
RadioMarte = 227940e3 / RadioTierra
RadioJupiter = 778330e3 / RadioTierra

vTierra = 107.244e3
vVenus = 126.108e3 / vTierra
vMercurio = 172.404e3 / vTierra
vMarte = 86.868e3 / vTierra
vJupiter= 47.016e3 / vTierra
vSaturno= 34.705e3 / vTierra
vNeptuno= 19.548e3 / vTierra
 
 
#Condiciones Iniciales del Sol
Sol = vp.sphere(
    pos=vp.vector(0, 0, 0),
    radius=0.3,
    color=vp.color.red,
)
Sol.m = 1
Sol.vel = vp.vector(0, 0, 0)
Sol.force = vp.vector(0, 0, 0)
Sol.name = "Sol"
#Condiciones Iniciales de la Tierra
Tierra = vp.sphere(
    pos=vp.vector(1, 0, 0),
    radius=0.1,
    color=vp.color.blue,
    make_trail=True,
    # retain=100,
)
Tierra.m = MasaTierra
Tierra.vel = vp.vector(0, 1, 0)
Tierra.force = vp.vector(0, 0, 0)
Tierra.name = "Tierra"

#Condiciones Iniciales de Júpiter
jupiter = vp.sphere(
    pos=vp.vector(RadioJupiter, 0, 0),
    radius=0.1,
    color=vp.color.orange,
    make_trail=True,
)
jupiter.m = MasaJupiter
#jupiter.vel = vp.vector(0.036524, -3.6524, 0)
jupiter.vel = vp.vector(0, vJupiter, 0)
jupiter.force = vp.vector(0, 0, 0)
jupiter.name = "Júpiter"


#Condiciones Iniciales de Mercurio
Mercurio = vp.sphere(
    pos=vp.vector(RadioMercurio, 0, 0),
    radius=0.1,
    color=vp.color.red,
    make_trail=True,
    # retain=100,
)
Mercurio.m = MasaMercurio
Mercurio.vel = vp.vector(0, vMercurio, 0)
Mercurio.force = vp.vector(0, 0, 0)
Mercurio.name = "Mercurio"

#Condiciones Iniciales de Saturno
Saturno= vp.sphere(
    pos=vp.vector(RadioSaturno, 0, 0),
    radius=0.1,
    color=vp.color.green,
    make_trail=True,
    # retain=100,
)
Saturno.m = MasaSaturno
Saturno.vel = vp.vector(0, vSaturno, 0)
Saturno.force = vp.vector(0, 0, 0)
Saturno.name = "Saturno"

#Condiciones Iniciales de Neptuno
Neptuno = vp.sphere(
    pos=vp.vector(RadioNeptuno, 0, 0),
    radius=0.1,
    color=vp.color.yellow,
    make_trail=True,
    # retain=100,
)
Neptuno.m = MasaNeptuno
Neptuno.vel = vp.vector(0, vNeptuno, 0)
Neptuno.force = vp.vector(0, 0, 0)
Neptuno.name = "Neptuno"

#Condiciones Iniciales de Marte
Marte = vp.sphere(
    pos=vp.vector(RadioMarte, 0, 0),
    radius=0.1,
    color=vp.color.orange,
    make_trail=True,
    # retain=100,
)
Marte.m = MasaMarte
Marte.vel = vp.vector(0, vMarte, 0)
Marte.force = vp.vector(0, 0, 0)
Marte.name = "Marte"

bodies = [Sol, Tierra]#, jupiter,Neptuno,Mercurio,Marte,Saturno]
N = len(bodies)

dt = 0.005
t = 0
T = 100
G = 4*vp.pi*vp.pi

while t < T:
    vp.rate(50)

    # Reset forces 
    for i in range(0, N):
        bodies[i].force = vp.vector(0, 0, 0)

    # Compute forces
    for i in range(0, N):
        body_i = bodies[i]
        m_i = body_i.m
        r_i = body_i.pos
        
        for j in range(i + 1, N):
            body_j = bodies[j]
            m_j = body_j.m
            r_j = body_j.pos
            
            r = r_i - r_j 

            F = - ((G*m_i*m_j) / (r.mag2 * r.mag)) * r

            body_i.force += F
            body_j.force -= F 

    # Euler-Cromer    
    for i in range(0, N):
        a = bodies[i].force / bodies[i].m
        bodies[i].vel += a * dt
        bodies[i].pos += bodies[i].vel * dt

    t += dt