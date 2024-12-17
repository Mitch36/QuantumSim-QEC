from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
 
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram

import random as rnd

class Q():
    @staticmethod
    def D1() -> int:
        return 0
    @staticmethod
    def D2() -> int:
        return 1
    @staticmethod
    def D3() -> int:
        return 2
    @staticmethod
    def D4() -> int:
        return 3
    @staticmethod
    def D5() -> int:
        return 4
    @staticmethod
    def D6() -> int:
        return 5
    @staticmethod
    def D7() -> int:
        return 6
    @staticmethod
    def D8() -> int:
        return 7
    @staticmethod
    def D9() -> int:
        return 8
    @staticmethod
    def A1() -> int:
        return 9
    @staticmethod
    def A2() -> int:
        return 9
    @staticmethod
    def A3() -> int:
        return 9
    @staticmethod
    def A4() -> int:
        return 9
    @staticmethod
    def A5() -> int:
        return 9
    @staticmethod
    def A6() -> int:
        return 9
    @staticmethod
    def A7() -> int:
        return 9
    @staticmethod
    def A8() -> int:
        return 9

class C():
    @staticmethod
    def A1() -> int:
        return 0
    @staticmethod
    def A2() -> int:
        return 1
    @staticmethod
    def A3() -> int:
        return 2
    @staticmethod
    def A4() -> int:
        return 3
    @staticmethod
    def A5() -> int:
        return 4
    @staticmethod
    def A6() -> int:
        return 5
    @staticmethod
    def A7() -> int:
        return 6
    @staticmethod
    def A8() -> int:
        return 7

class SurfaceCode:
    def __init__(self, qubits: int=10, bits: int=8):
        self.qubits = qubits
        self.bits = bits

        self.qc = QuantumCircuit(self.qubits, self.bits)

    def __add_encoder_circuit__(self):
        # self.qc.h(Q.D1())
        # self.qc.cx(Q.D1(), Q.D2())
        # self.qc.cx(Q.D2(), Q.D3())
        # self.qc.cx(Q.D3(), Q.D4())
        # self.qc.cx(Q.D4(), Q.D5())
        # self.qc.cx(Q.D5(), Q.D6())
        # self.qc.cx(Q.D6(), Q.D7())
        # self.qc.cx(Q.D7(), Q.D8())
        # self.qc.cx(Q.D8(), Q.D9())

        self.qc.h(Q.D2())
        self.qc.h(Q.D4())
        self.qc.h(Q.D6())
        self.qc.h(Q.D8())

        self.qc.cx(Q.D4(), Q.D3())
        self.qc.cx(Q.D6(), Q.D5())
        self.qc.cx(Q.D8(), Q.D9())

        self.qc.cx(Q.D2(), Q.D1())
        self.qc.cx(Q.D4(), Q.D5())
        self.qc.cx(Q.D6(), Q.D7())
        
        self.qc.cx(Q.D3(), Q.D2())
        self.qc.cx(Q.D7(), Q.D8())

        self.qc.barrier()

    def __add_upper_left_stabilizers__(self):
        self.qc.h(Q.A1())
        self.qc.cx(Q.A1(), Q.D4())
        self.qc.cx(Q.A1(), Q.D1())
        self.qc.cx(Q.A1(), Q.D5())
        self.qc.cx(Q.A1(), Q.D2())
        self.qc.h(Q.A1())

        self.qc.measure(Q.A1(), C.A1())
        self.qc.reset(Q.A1())

        # self.qc.cx(Q.D2(), Q.A1())
        # self.qc.cx(Q.D5(), Q.A1())        

        # self.qc.measure(Q.A1(), C.A2())
        # self.qc.reset(Q.A1())

    def __add_upper_right_stabilizers__(self):
        self.qc.h(Q.A1())
        self.qc.cx(Q.A1(), Q.D2())
        self.qc.cx(Q.A1(), Q.D3())
        self.qc.h(Q.A1())

        self.qc.measure(Q.A1(), C.A3())
        self.qc.reset(Q.A1())

        self.qc.cx(Q.D2(), Q.A1())
        self.qc.cx(Q.D3(), Q.A1())
        self.qc.cx(Q.D5(), Q.A1())        
        self.qc.cx(Q.D6(), Q.A1())        

        self.qc.measure(Q.A1(), C.A4())
        self.qc.reset(Q.A1())


        



    




    
