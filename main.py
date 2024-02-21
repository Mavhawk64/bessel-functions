import numpy as np
import scipy as sp
from scipy.special import *

euler_mascheroni = 0.57721566490153286060651209008240243104215933593992


def BesselJ(m, x):
    return jv(m, x)


def BesselY(m, x):
    return yv(m, x)


def BesselI(m, x):
    return iv(m, x)


def BesselK(m, x):
    return kv(m, x)
