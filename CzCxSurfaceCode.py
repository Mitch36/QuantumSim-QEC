from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import random
# Surface code using both CX and CZ gates

class C:
    @staticmethod
    def xa() -> int:
        return 0
    @staticmethod
    def xb() -> int:
        return 1
    @staticmethod
    def xc() -> int:
        return 2
    @staticmethod
    def xd() -> int:
        return 3
    @staticmethod
    def za() -> int:
        return 4
    @staticmethod
    def zb() -> int:
        return 5
    @staticmethod
    def zc() -> int:
        return 6
    @staticmethod
    def zd() -> int:
        return 7
    
class Q:
    @staticmethod
    def xa() -> int:
        return 0
    @staticmethod
    def xb() -> int:
        return 1
    @staticmethod
    def xc() -> int:
        return 2
    @staticmethod
    def xd() -> int:
        return 3
    @staticmethod
    def za() -> int:
        return 4
    @staticmethod
    def zb() -> int:
        return 5
    @staticmethod
    def zc() -> int:
        return 6
    @staticmethod
    def zd() -> int:
        return 7
    
    @staticmethod
    def da() -> int:
        return 8
    @staticmethod
    def db() -> int:
        return 9
    @staticmethod
    def dc() -> int:
        return 10
    @staticmethod
    def dd() -> int:
        return 11
    @staticmethod
    def de() -> int:
        return 12
    @staticmethod
    def df() -> int:
        return 13
    @staticmethod
    def dg() -> int:
        return 14
    @staticmethod
    def dh() -> int:
        return 15
    @staticmethod
    def di() -> int:
        return 16
    

    # X stabilizer uses CNOT (Blue)
    # Z stabilizer uses CZ (Green)

class CzCxSurfaceCode:

    xa, xb, xc, xz = 0, 1, 3, 4

    def __init__(self):
        qrd = QuantumRegister(9, "Data")
        qra = QuantumRegister(8, "Ancillary")
        cr = ClassicalRegister(8,"Syndrome")
        self.qc = QuantumCircuit(qra, qrd, cr)

    def encode(self):
        self.qc.h(Q.da())
        self.qc.cx(Q.da(), Q.db())
        self.qc.cx(Q.db(), Q.dc())
        self.qc.cx(Q.dc(), Q.dd())
        self.qc.cx(Q.dd(), Q.de())
        self.qc.cx(Q.de(), Q.df())
        self.qc.cx(Q.df(), Q.dg())
        self.qc.cx(Q.dg(), Q.dh())
        self.qc.cx(Q.dh(), Q.di())

        self.qc.barrier()

    def hadamard_basis(self):
        self.qc.h(Q.da())
        self.qc.h(Q.db())
        self.qc.h(Q.dc())
        self.qc.h(Q.dd())
        self.qc.h(Q.de())
        self.qc.h(Q.df())
        self.qc.h(Q.dg())
        self.qc.h(Q.dh())
        self.qc.h(Q.di())

    def measure_syndrome(self):
        self.qc.measure(Q.xa(), C.xa())
        self.qc.measure(Q.xb(), C.xb())
        self.qc.measure(Q.xc(), C.xc())
        self.qc.measure(Q.xd(), C.xd())

        self.qc.measure(Q.za(), C.za())
        self.qc.measure(Q.zb(), C.zb())
        self.qc.measure(Q.zc(), C.zc())
        self.qc.measure(Q.zd(), C.zd())

    def generate_phase_flip(self, index=0):
        if(index == 0):   
            qubit = random.randint(Q.da(), Q.di())
            print("Phase flip on qubit: " + str(qubit))
            self.qc.z(qubit)
        elif(index >= Q.da() and index <= Q.di()):
            self.qc.z(index)
        else:
            raise Exception("Index parameter out of bounds")

    def generate_bit_flip(self, index=0):
        if(index == 0):
            qubit = random.randint(Q.da(), Q.di())
            print("Bit flip on qubit: " + str(qubit))
            self.qc.x(str(qubit))
        elif(index >= Q.da() and index <= Q.di()):
            self.qc.x(index)
        else:
            raise Exception("Index parameter out of bounds")

    def apply_h_to_all_ancillary(self):
        # self.qc.h(Q.xa())
        self.qc.h(Q.xb())
        # self.qc.h(Q.xc())
        # self.qc.h(Q.xd())

        # self.qc.h(Q.za())
        # self.qc.h(Q.zb())
        # self.qc.h(Q.zc())
        # self.qc.h(Q.zd())
        self.qc.barrier()


    def first_cycle(self):
        self.qc.cz(Q.za(), Q.da())
        self.qc.cx(Q.xb(), Q.db())

        self.qc.cz(Q.zb(), Q.dc())
        self.qc.cz(Q.zc(), Q.de())

        self.qc.cx(Q.xc(), Q.df())
        self.qc.cx(Q.xd(), Q.dh())
        self.qc.barrier()

    def first_cycle_x(self):
        self.qc.h(Q.db())
        self.qc.h(Q.df())
        self.qc.h(Q.dh())

        self.qc.cz(Q.xb(), Q.db())
        self.qc.cz(Q.xc(), Q.df())
        self.qc.cz(Q.xd(), Q.dh())

        self.qc.h(Q.db())
        self.qc.h(Q.df())
        self.qc.h(Q.dh())
        self.qc.barrier()

    def first_cycle_z(self):
        self.qc.cz(Q.za(), Q.da())
        self.qc.cz(Q.zb(), Q.dc())
        self.qc.cz(Q.zc(), Q.de())
        self.qc.barrier()
    

    def second_cycle(self):
        self.qc.cz(Q.za(), Q.dd())
        self.qc.cx(Q.xb(), Q.da())

        self.qc.cz(Q.zb(), Q.df())
        self.qc.cz(Q.zc(), Q.dh())

        self.qc.cx(Q.xc(), Q.de())
        self.qc.cx(Q.xd(), Q.dg())
        self.qc.barrier()

    def second_cycle_x(self):
        self.qc.h(Q.da())
        self.qc.h(Q.de())
        self.qc.h(Q.dg())

        self.qc.cz(Q.xb(), Q.da())
        self.qc.cz(Q.xc(), Q.de())
        self.qc.cz(Q.xd(), Q.dg())

        self.qc.h(Q.da())
        self.qc.h(Q.de())
        self.qc.h(Q.dg())
        self.qc.barrier()

    def second_cycle_z(self):
        self.qc.cz(Q.za(), Q.dd())
        self.qc.cz(Q.zb(), Q.df())
        self.qc.cz(Q.zc(), Q.dh())
        self.qc.barrier()

    def third_cycle(self):
        self.qc.cx(Q.xa(), Q.dc())
        self.qc.cx(Q.xb(), Q.de())

        self.qc.cz(Q.zb(), Q.db())
        self.qc.cz(Q.zc(), Q.dd())

        self.qc.cx(Q.xc(), Q.di())
        self.qc.cz(Q.zd(), Q.df())
        self.qc.barrier()

    def third_cycle_x(self):
        self.qc.h(Q.dc())
        self.qc.h(Q.de())
        self.qc.h(Q.di())

        self.qc.cz(Q.xa(), Q.dc())
        self.qc.cz(Q.xb(), Q.de())
        self.qc.cz(Q.xc(), Q.di())

        self.qc.h(Q.dc())
        self.qc.h(Q.de())
        self.qc.h(Q.di())
        self.qc.barrier()

    def third_cycle_z(self):
        self.qc.cz(Q.zb(), Q.db())
        self.qc.cz(Q.zc(), Q.dd())
        self.qc.cz(Q.zd(), Q.df())
        self.qc.barrier()


    def fourth_cycle(self):
        self.qc.cx(Q.xa(), Q.db())
        self.qc.cx(Q.xb(), Q.dd())

        self.qc.cz(Q.zb(), Q.de())
        self.qc.cz(Q.zc(), Q.dg())

        self.qc.cx(Q.xc(), Q.dh())
        self.qc.cz(Q.zd(), Q.di())
        self.qc.barrier()

    def fourth_cycle_x(self):
        self.qc.h(Q.db())
        self.qc.h(Q.dd())
        self.qc.h(Q.dh())

        self.qc.cz(Q.xa(), Q.db())
        self.qc.cz(Q.xb(), Q.dd())
        self.qc.cz(Q.xc(), Q.dh())

        self.qc.h(Q.db())
        self.qc.h(Q.dd())
        self.qc.h(Q.dh())
        self.qc.barrier()

    def fourth_cycle_z(self):
        self.qc.cz(Q.zb(), Q.de())
        self.qc.cz(Q.zc(), Q.dg())
        self.qc.cz(Q.zd(), Q.di())
        self.qc.barrier()







