from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
 
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram

# Quantum register alias
class Q:
    @staticmethod
    def Xa() -> int:
        return 0
    @staticmethod
    def Da() -> int:
        return 1
    @staticmethod
    def Db() -> int:
        return 2
    @staticmethod
    def Dc() -> int:
        return 3
    @staticmethod
    def Za() -> int:
        return 4
    @staticmethod
    def Xb() -> int:
        return 5
    @staticmethod
    def Zb() -> int:
        return 6
    @staticmethod
    def Dd() -> int:
        return 7
    @staticmethod
    def De() -> int:
        return 8
    @staticmethod
    def Df() -> int:
        return 9
    @staticmethod
    def Zc() -> int:
        return 10
    @staticmethod
    def Xc() -> int:
        return 11
    @staticmethod
    def Zd() -> int:
        return 12
    def Dg() -> int:
        return 13
    @staticmethod
    def Dh() -> int:
        return 14
    @staticmethod
    def Di() -> int:
        return 15
    @staticmethod
    def Xd() -> int:
        return 16
    

class SurfaceCodeDelft:
    def __init__(self):
        q_D = QuantumRegister(17, name="Q")
        c_A = ClassicalRegister(8, name="CAnc")
        # c_D = ClassicalRegister(9, name="CData")

        self.qc = QuantumCircuit(q_D, c_A)

    def __hadamard_all_data_q(self):
        self.qc.h(Q.Da())
        self.qc.h(Q.Db())
        self.qc.h(Q.Dc())
        self.qc.h(Q.Dd())
        self.qc.h(Q.De())
        self.qc.h(Q.Df())
        self.qc.h(Q.Dg())
        self.qc.h(Q.Dh())
        self.qc.h(Q.Di())

    def reset_all_qubits(self):
        self.qc.reset(Q.Da())
        self.qc.reset(Q.Db())
        self.qc.reset(Q.Dc())
        self.qc.reset(Q.Dd())
        self.qc.reset(Q.De())
        self.qc.reset(Q.Df())
        self.qc.reset(Q.Dg())
        self.qc.reset(Q.Dh())
        self.qc.reset(Q.Di())

        self.qc.reset(Q.Za())
        self.qc.reset(Q.Zb())
        self.qc.reset(Q.Zc())
        self.qc.reset(Q.Zd())

        self.qc.reset(Q.Xa())
        self.qc.reset(Q.Xb())
        self.qc.reset(Q.Xc())
        self.qc.reset(Q.Xd())


    def step0(self):
        self.qc.h(Q.Da())
        self.qc.cx(Q.Da(), Q.Db())
        self.qc.cx(Q.Db(), Q.Dc())
        self.qc.cx(Q.Dc(), Q.Dd())
        self.qc.cx(Q.Dd(), Q.De())
        self.qc.cx(Q.De(), Q.Df())
        self.qc.cx(Q.Df(), Q.Dg())
        self.qc.cx(Q.Dg(), Q.Dh())
        self.qc.cx(Q.Dh(), Q.Di())

        # self.qc.cx(Q.Da(), Q.Db())
        # self.qc.cx(Q.Da(), Q.Dc())
        # self.qc.cx(Q.Da(), Q.Dd())
        # self.qc.cx(Q.Da(), Q.De())
        # self.qc.cx(Q.Da(), Q.Df())
        # self.qc.cx(Q.Da(), Q.Dg())
        # self.qc.cx(Q.Da(), Q.Dh())
        # self.qc.cx(Q.Da(), Q.Di())
        self.qc.barrier()

    def apply_z_to_all_data(self):
        self.qc.z(Q.Da())
        self.qc.z(Q.Db())
        self.qc.z(Q.Dc())
        self.qc.z(Q.Dd())
        self.qc.z(Q.De())
        self.qc.z(Q.Df())
        self.qc.z(Q.Dg())
        self.qc.z(Q.Dh())
        self.qc.z(Q.Di())
        self.qc.barrier()


    def apply_x_to_all_data(self):
        self.qc.x(Q.Da())
        self.qc.x(Q.Db())
        self.qc.x(Q.Dc())
        self.qc.x(Q.Dd())
        self.qc.x(Q.De())
        self.qc.x(Q.Df())
        self.qc.x(Q.Dg())
        self.qc.x(Q.Dh())
        self.qc.x(Q.Di())
        self.qc.barrier()

    def apply_h_to_all_data(self):
        self.qc.h(Q.Da())
        self.qc.h(Q.Db())
        self.qc.h(Q.Dc())
        self.qc.h(Q.Dd())
        self.qc.h(Q.De())
        self.qc.h(Q.Df())
        self.qc.h(Q.Dg())
        self.qc.h(Q.Dh())
        self.qc.h(Q.Di())

    def step1(self):
        self.qc.h(Q.Xa())
        self.qc.h(Q.Db())
        self.qc.h(Q.Za())
        self.qc.h(Q.Xb())
        self.qc.h(Q.Zb())
        self.qc.h(Q.Dd())
        self.qc.h(Q.Df())
        self.qc.h(Q.Zc())
        self.qc.h(Q.Xc())
        self.qc.h(Q.Zd())
        self.qc.h(Q.Dh())
        self.qc.h(Q.Xd())

        self.qc.barrier()

    def step2X(self):
        self.qc.cz(Q.Db(), Q.Xb())
        self.qc.cz(Q.Df(), Q.Xc())
        self.qc.cz(Q.Dh(), Q.Xd())

        # self.qc.cz(Q.Da(), Q.Za())

        # self.qc.cz(Q.Dc(), Q.Zb())
        # self.qc.cz(Q.De(), Q.Zc())

        self.qc.barrier()

    def step2Z(self):
        self.qc.cz(Q.Da(), Q.Za())

        self.qc.cz(Q.Dc(), Q.Zb())
        self.qc.cz(Q.De(), Q.Zc())
        self.qc.barrier()

    def step3(self):
        self.__hadamard_all_data_q()

    def step4X(self):
        self.qc.cz(Q.Da(), Q.Xb())
        self.qc.cz(Q.De(), Q.Xc())
        self.qc.cz(Q.Dg(), Q.Xd())

        # self.qc.cz(Q.Dd(), Q.Za())
        
        # self.qc.cz(Q.Df(), Q.Zb())
        # self.qc.cz(Q.Dh(), Q.Zc())
        self.qc.barrier()

    def step4Z(self):
        self.qc.cz(Q.Dd(), Q.Za())
        
        self.qc.cz(Q.Df(), Q.Zb())
        self.qc.cz(Q.Dh(), Q.Zc())
        self.qc.barrier()


    def step5X(self):
        self.qc.cz(Q.Dc(), Q.Xa())
        self.qc.cz(Q.De(), Q.Xb())
        self.qc.cz(Q.Di(), Q.Xc())

        # self.qc.cz(Q.Db(), Q.Zb())
        # self.qc.cz(Q.Df(), Q.Zd())

        # self.qc.cz(Q.Dd(), Q.Zc())
        self.qc.barrier()

    def step5Z(self):
        self.qc.cz(Q.Db(), Q.Zb())
        self.qc.cz(Q.Df(), Q.Zd())

        self.qc.cz(Q.Dd(), Q.Zc())
        self.qc.barrier()


    def step6(self):
        self.__hadamard_all_data_q()

    def step7X(self):
        self.qc.cz(Q.Db(), Q.Xa())
        self.qc.cz(Q.Dd(), Q.Xb())
        self.qc.cz(Q.Dh(), Q.Xc())

        # self.qc.cz(Q.Di(), Q.Zd())

        # self.qc.cz(Q.De(), Q.Zb())
        # self.qc.cz(Q.Dg(), Q.Zc())
        self.qc.barrier()

    def step7Z(self):
        self.qc.cz(Q.Di(), Q.Zd())

        self.qc.cz(Q.De(), Q.Zb())
        self.qc.cz(Q.Dg(), Q.Zc())
        self.qc.barrier()


    def step8(self):
        self.step1()

    def step9X(self):

        # self.qc.h(Q.Xa())
        # self.qc.h(Q.Xb())
        # self.qc.h(Q.Xc())
        # self.qc.h(Q.Xd())

        self.qc.measure(Q.Xa(), 0)
        self.qc.measure(Q.Xb(), 1)
        self.qc.measure(Q.Xc(), 2)
        self.qc.measure(Q.Xd(), 3)

        self.qc.barrier()


    def step9Z(self):

        # self.qc.h(Q.Za())
        # self.qc.h(Q.Zb())
        # self.qc.h(Q.Zc())
        # self.qc.h(Q.Zd())

        self.qc.measure(Q.Za(), 4)
        self.qc.measure(Q.Zb(), 5)
        self.qc.measure(Q.Zc(), 6)
        self.qc.measure(Q.Zd(), 7)

        self.qc.barrier()

    def reset_all_ancillary(self):
        self.qc.reset(Q.Za())
        self.qc.reset(Q.Zb())
        self.qc.reset(Q.Zc())
        self.qc.reset(Q.Zd())

        self.qc.reset(Q.Xa())
        self.qc.reset(Q.Xb())
        self.qc.reset(Q.Xc())
        self.qc.reset(Q.Xd())




