from hamiltonian import *
from teleportation import *
from concurrence import *
from multiprocessing import Pool
pool = Pool(processes = 20)
from functools import partial
import matplotlib.pyplot as plt
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ['Times New Roman'],
})
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.tick_params(axis='both', which='major', labelsize=20)

u=np.linspace(0.0,20,50)
L=6
params_list = [(L,1.0,0.0,0.0,y) for y in u]
with Pool(processes=20) as pool:
    b=pool.map(teleportation,params_list)
    np.savez("/home/zakaria/QT_Fermi-Hubbard/data/fig1b_L=%s"%L,b)
plt.plot(u,b,label=r'$L=%s$'%L)
plt.ylabel(r'$\mathcal{F}(1,L)$',fontsize=20)
plt.xlabel(r'$U$',fontsize=20)
plt.legend(fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.tight_layout()
plt.savefig('/home/zakaria/QT_Fermi-Hubbard/figures/fig1b.pdf') 