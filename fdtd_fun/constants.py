from enum import Enum

from numpy import pi

stability = 0.99
c = 299792458.0
mu_0 = 4 * pi * 10 ** -7
eps_0 = c ** -2 / mu_0


class Field(Enum):
    E = 1
    H = 2
    J = 3
    rho = 4
