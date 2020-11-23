# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:25:39 2020

@author: Mr. Toc
"""

import math

"""---Variables---"""
# Basic Wind Velocity [m/s]
Vb = 25

# Terrain Category
# 0 (Sea or coastal area exposed to the open sea)
# 1 (Lakes or flat and horizontal area with negligible vegetation and without obstacles)
# 2 (Area with low vegetation such as grass and isolated obstacles (trees, buildings) with separations of at least 20 obstacle heights)
# 3 (Area with regular cover of vegetation or buildings or with isolated obstacles with separations of maximum 20 obstacle heights (such as villages, suburban terrain, permanent forest))
# 4 (Area in which at least 15 % of the surface is covered with buildings and their average height exceeds 15 m)
terrain_category = 1

# Density of air [kg/m3]
air_density = 1.25

# Maximum height of structure [m]
z = 7.3

"""---Variables---"""

"""---Eurocode---"""

# Basic velocity pressure
qb = 0.5 * air_density * (Vb)**2
print('Basic velocity pressure:', round(qb/1000, 2), 'kPa')

# Terrain Roughness Coefficients 1
if terrain_category==0:
    z0 = 0.003
    zmin = 1
elif terrain_category==1:
    z0 = 0.01
    zmin = 1
elif terrain_category==2:
    z0 = 0.05
    zmin = 2
elif terrain_category==3:
    z0 = 0.3
    zmin = 5
elif terrain_category==4:
    z0 = 1
    zmin = 10
else:
    print('Terrain Roughness cannot be calculated!')
print('z0 and zmax are', z0, 'm', 'and', zmin, 'm', 'respectively.')

# Terrain Roughness Coefficient 2
kr = 0.19*(z0/0.05)**0.07
print('kr is equal to', round(kr,2))
if z >= zmin:
    Crz = kr*math.log(z/z0)
else:
    Crz = kr*math.log(zmin/z0)
print('Crz is equal to', round(Crz,2))

# Orography Factor
C0z = 1.0
print('Orography factor is taken as 1.0')

# Mean Wind Velocity
Vm = Crz*C0z*Vb
print('Mean wind velocity is equal to', round(Vm,0), 'm/s')

# Turbulance Factor
kl = 1.0
print('Turbulance factor is taken as 1.0')

# Turbulance Intensity
if z >= zmin:
    Ivz = kl/(C0z*math.log(z/z0))
else:
    Ivz = kl/(C0z*math.log(zmin/z0))
print('Turbulence Intensity:', round(Ivz,2))

# Peak Velocity Pressure
qp = 0.5*(1+7*Ivz)*air_density*(Vm)**2
print('Peak Velocity Pressure:', round(qp/1000, 2), 'kPa')

# Exposure Factor
Cez = qp/qb
print('Exposure Factor:', round(Cez,2))


"""---Eurocode---"""









