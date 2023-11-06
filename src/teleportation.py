from hamiltonian import *

def u(n,m):
    d=4
    op=sum(np.exp(2*np.pi*1j*k*n/d)*(fock(d,k)*fock(d,(k+m)%d).dag()) for k in range(d))
    return op

def teleportation(L,J,mu,w,U):
    d=4
    psi=sum(tensor(fock(d,r),fock(d,r)) for r in range(0,d))/np.sqrt(d) # maximaly entangled state \psi^+
    r_in=ket2dm(sum(fock(d,r) for r in range(d)).unit()) # the state to teleporte (density matrix of 1 ququart)
    state=sum(sum(((tensor(u(n,m),identity(d))*psi*psi.dag()*tensor(u(n,m),identity(d)).dag()*fermi_hubbard(L,J,U,mu,w)).tr())*u(n,-m)*r_in*u(n,-m).dag()
                  for n in range(d)) for m in range(d))
    return fidelity(r_in,state)**2