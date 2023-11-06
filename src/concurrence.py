from hamiltonian import *

def LBC(L:int, J:float, mu:float, U:float, w:float):
    basis=fermi_hubbard(L,J,U,mu,w).basis
    E_GS,V_GS=fermi_hubbard(L,J,U,mu,w).eigsh(k=1,which='SA',maxiter=1E10)
    subsyst2 = basis.partial_trace(V_GS,sub_sys_A=([0,L-1],[0,L-1]),return_rdm="A",enforce_pure=False,sparse=False,subsys_ordering=True)
    summ=0
    L1 = np.array([[0, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0],[0, 0, 0, 0]])
    L2 = np.array([[0, 0, 1, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0]])
    L3 = np.array([[0, -1, 0, 0],[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    L4 = np.array([[0, 0, 0, -1],[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
    L5 = np.array([[0, 0, 0, 0],[0, 0, 0, -1], [0, 0, 0, 0], [0, 1, 0, 0]])
    L6 = np.array([[0, 0, 0, 0],[0, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
    l = [L1, L2, L3, L4, L5, L6]   
    subsyst22= subsyst2[[15,13,7,5,14,12,6,4,11,9,3,1,10,8,2,0]]
    subsystb = subsyst22[:,[15,13,7,5,14,12,6,4,11,9,3,1,10,8,2,0]]
    for i in range (0,6):
        for j in range (0,6):
            ij= np.kron(l[i],l[j])
            cnj=subsystb.conjugate()
            matg = np.linalg.multi_dot([subsystb,ij, cnj , ij ]) 
            eng= la.eigvals(matg)
            diagn=[eng[k] for k in range (0,16)]
            diagn.sort(reverse=True)
            somm=sum([np.sqrt(max(0,diagn[h])) for h in range(0,16)])
            concurr= max(0,2*np.sqrt(diagn[0]) - somm)
            summ = summ + pow(concurr,2) 
    lowerrb=np.sqrt((2/3)*summ) 
    return lowerrb