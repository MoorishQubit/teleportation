from quspin.operators import hamiltonian # Hamiltonians and operators
from quspin.basis import spinful_fermion_basis_1d
import numpy as np # generic math functions
from qutip import *
from scipy import linalg as la
from scipy import integrate as integrate
from scipy.linalg import toeplitz, det

#here we construct the Fermi-Hubbard hamiltonian via the library QuSpin.
def fermi_hubbard(L:int, J:float, U:float, mu:float, w:float):
    N_up = L//2 +L%2 # number of fermions with spin up
    N_down = L//2 # number of fermions with spin down
    basis = spinful_fermion_basis_1d(L,Nf=(N_up,N_down))

    hop_right=[[J*(1+w*(-1)**(i+1)),i,(i+1)] for i in range(L-1)]
    hop_left= [[-(J*(1+w*(-1)**(i+1))),i,(i+1)] for i in range(L-1)] 
    pot=[[-mu,i] for i in range(L-1)] 
    interact=[[U,i,i] for i in range(L)] 
    static=[
            ['+-|',hop_left],  # up hops left
            ['-+|',hop_right], # up hops right
            ['|+-',hop_left],  # down hops left
            ['|-+',hop_right], # down hops right
            ['n|',pot],        # up on-site potention
            ['|n',pot],        # down on-site potention
            ['n|n',interact]   # up-down interaction
                                    ]
    dynamic=[]
    
    no_checks = dict(check_pcon=False,check_symm=False,check_herm=False)
    H=hamiltonian(static,dynamic,basis=basis,**no_checks)
    return H

#the following function construct the reduced density matrix of two sites (0,L-1)
def two_site_density_matrix(L:int, J:float, U:float, mu:float, w:float):
    E,V=fermi_hubbard(L,J,U,mu,w).eigsh(k=1,which='SA',maxiter=1E10)
    basis=fermi_hubbard(L,J,U,mu,w).basis
    rdm1=Qobj(np.abs(basis.partial_trace(V,sub_sys_A=([0,L-1],[0,L-1]),return_rdm="A",enforce_pure=False,sparse=False,subsys_ordering=True)))
    rdm2= rdm1[[15,13,7,5,14,12,6,4,11,9,3,1,10,8,2,0]]
    rdm3= Qobj(rdm2[:,[15,13,7,5,14,12,6,4,11,9,3,1,10,8,2,0]])    
    rdm3.dims=[[4,4],[4,4]]
    return rdm3