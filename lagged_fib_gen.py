from random import randint
from math import pow
from scipy.stats import chi2_contingency, chisquare
import numpy as np


def lagfibG(n, lag1=55, lag2=24, modulus=1, firstterms=None, acc=[]):
    lagmax = max(lag1, lag2)
    if firstterms is None:
        firstterms = [randint(0, int(pow(2, modulus - 1)))
                      for x in range(lagmax)]
        # print(firstterms)
    if n <= lagmax:
        return firstterms[n]
    else:
        return (lagfibG(n-lag1, firstterms=firstterms) + lagfibG(n-lag2, firstterms=firstterms)) % int(pow(2, modulus))


def T(r=24, s=55, l=52):
    return (2 ** max(r, s) - 1) * 2 ** l


def launch(seq_length, fib_num, r, s):
    selection = [lagfibG(fib_num, r, s) for x in range(seq_length)]

    selection_file = open("selection.txt", "w")

    for el in selection:
        selection_file.write(str(el))

    selection_file.close()

    analytics = open("analytics.txt", "w")

    top = f"{'Distance':^12} {'pvalue':^12} {'Uniform?':^8}" + "\n"

    dist, pvalue = chisquare(selection)
    uni = 'YES' if pvalue > 0.05 else 'NO'

    result = f"{dist:12.3f} {pvalue:12.8f} {uni:^8}"

    analytics.writelines([top, result])
    analytics.close()

    period = open("period.txt", "w")
    period.write(str(T(r, s)))
    period.close()
