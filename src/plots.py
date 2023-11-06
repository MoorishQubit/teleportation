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

# b=[]
# if __name__ == '__main__':
#     pool = multiprocessing.Pool(20)
#     J=1.0
#     w=np.linspace(0,0.99,100)
#     L=10
#     for x in [0,5,10,30]:
#         func = partial(LBC,L,J,0.0,x)
#         b=pool.map(func,w)
#         np.savez("/home/zakaria/QT_Fermi-Hubbard/data/fig2b_U=%s"%x,b)
#         plt.plot(w,b,label=r'$L=%s$'%x)
#     plt.ylabel(r'$\mathcal{C}_{\rho}(1,10)$',fontsize=20)
#     plt.xlabel(r'$\delta$',fontsize=20)
#     plt.legend(fontsize=20)
#     plt.tick_params(axis='both', which='major', labelsize=18)
#     plt.tight_layout()
#     plt.savefig('figures/fig2b.pdf')

data1=np.load("/home/zakaria/QT_Fermi-Hubbard/data/fig1/fig1b_L=4.npz")['arr_0']
data2=np.load("/home/zakaria/QT_Fermi-Hubbard/data/fig1/fig1b_L=6.npz")['arr_0']
data3=np.load("/home/zakaria/QT_Fermi-Hubbard/data/fig1/fig1b_L=8.npz")['arr_0']
data4=np.load("/home/zakaria/QT_Fermi-Hubbard/data/fig1/fig1b_L=10.npz")['arr_0']
u=np.linspace(0,20,100)
plt.plot(u,data1, label=r'$L=4$')
plt.plot(u,data2, label=r'$L=6$')
plt.plot(u,data3, label=r'$L=8$')
u2=np.linspace(0,20,50)
plt.plot(u2,data4, label=r'$L=10$')
plt.ylabel(r'$\mathcal{F}(1,L)$',fontsize=20)
plt.xlabel(r'$U$',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('figures/fig1b.pdf')
plt.show()