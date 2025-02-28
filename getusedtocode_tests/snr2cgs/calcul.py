import numpy as np

units_density=6.807e-23
units_time=31.6e12
units_length=3.086e18
units_mass = units_density*units_length**3
units_pressure = units_mass/(units_time**2*units_length)
print(units_mass)
mp = 1.66e-24
mu = 1
n = 1
rho = n*mu*mp
T = 1e4
Kb = 1.38e-16
rho_code = rho/units_density

Kb_code = Kb/(units_length**2*units_mass/units_time**2)
cgs_pressure = n*Kb*T
pressure_code = cgs_pressure/units_pressure
print(pressure_code, rho_code)