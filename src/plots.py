from hamiltonian import *
from teleportation import *
from concurrence import *
import multiprocessing
from functools import partial
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ['Times New Roman'],
})
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.tick_params(axis='both', which='major', labelsize=20)

b=[]
if __name__ == '__main__':
    pool = multiprocessing.Pool(20)
    J=1.0
    u=np.linspace(0,20,50)
    for x in [4,6]:
        func = partial(teleportation,x,J,0.0,0.0)
        b=pool.map(func,u)
        plt.plot(u,b,label=r'$L=%s$'%x)
    plt.ylabel(r'$\mathcal{F}(1,L)$',fontsize=20)
    plt.xlabel(r'$U$',fontsize=20)
    plt.legend(fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.tight_layout()
    plt.show()
