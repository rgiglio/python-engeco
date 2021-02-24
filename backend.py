import pandas as pd
import numpy as np


def de_vp_para_vf(vp, n, i):
    return vp * (1 + i) ** n


def de_vp_para_su(vp, n, i):
    return vp * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
