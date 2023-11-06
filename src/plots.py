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
    mu=0.0
    u=np.linspace(0,20,100)
    for x in [8,10]:
        func = partial(teleportation,x,J,mu,0)
        b=pool.map(func,u)
        np.savez("/home/zakaria/QT_Fermi-Hubbard/data/fig1b_L=%s"%x,b)
        plt.plot(u,b,label=r'$L=%s$'%x)
    plt.ylabel(r'$\mathcal{F}(1,L)$',fontsize=20)
    plt.xlabel(r'$U$',fontsize=20)
    plt.legend(fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.tight_layout()
    plt.savefig('figures/fig1b.pdf')

# data=np.load("/home/zakaria/QT_Fermi-Hubbard/data/fig2c.npz")['arr_0']
# w=np.linspace(0,0.99,50)
# plt.plot(w,data)
# plt.ylabel(r'$P_i$',fontsize=20)
# plt.xlabel(r'$\delta$',fontsize=20)
# plt.tick_params(axis='both', which='major', labelsize=15)
# #plt.legend(fontsize=15)
# plt.tight_layout()
# plt.savefig('figures/fig2c.pdf')
# plt.show()