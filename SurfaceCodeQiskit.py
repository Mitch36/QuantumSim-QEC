from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
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
        return 10
    @staticmethod
    def A3() -> int:
        return 11
    @staticmethod
    def A4() -> int:
        return 12
    @staticmethod
    def A5() -> int:
        return 13
    @staticmethod
    def A6() -> int:
        return 14
    @staticmethod
    def A7() -> int:
        return 15
    @staticmethod
    def A8() -> int:
        return 16

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
    @staticmethod
    def D1() -> int:
        return 8
    @staticmethod
    def D2() -> int:
        return 9
    @staticmethod
    def D3() -> int:
        return 10
    @staticmethod
    def D4() -> int:
        return 11
    @staticmethod
    def D5() -> int:
        return 12
    @staticmethod
    def D6() -> int:
        return 13
    @staticmethod
    def D7() -> int:
        return 14
    @staticmethod
    def D8() -> int:
        return 15
    @staticmethod
    def D9() -> int:
        return 16

class SurfaceCode:
    def __init__(self, qubits: int=17, bits: int=8):
        self.qubits = qubits
        self.bits = bits

        q_D = QuantumRegister(9, name="D")
        q_A = QuantumRegister(8, name="A")
        c_A = ClassicalRegister(bits, name="Anc")
        c_D = ClassicalRegister(9, name="Data")

        self.qc = QuantumCircuit(q_D, q_A, c_A, c_D)

    def add_encoder_circuit(self):
        # self.qc.h(Q.D1())
        # self.qc.cx(Q.D1(), Q.D2())
        # self.qc.cx(Q.D2(), Q.D3())
        # self.qc.cx(Q.D3(), Q.D4())
        # self.qc.cx(Q.D4(), Q.D5())
        # self.qc.cx(Q.D5(), Q.D6())
        # self.qc.cx(Q.D6(), Q.D7())
        # self.qc.cx(Q.D7(), Q.D8())
        # self.qc.cx(Q.D8(), Q.D9())

        self.qc.h(Q.D1())
        self.qc.h(Q.D2())
        self.qc.h(Q.D3())
        self.qc.h(Q.D4())
        self.qc.h(Q.D5())
        self.qc.h(Q.D6())
        self.qc.h(Q.D7())
        self.qc.h(Q.D8())
        self.qc.h(Q.D9())

        # self.qc.h(Q.D2())
        # self.qc.h(Q.D4())
        # self.qc.h(Q.D6())
        # self.qc.h(Q.D8())

        # self.qc.cx(Q.D4(), Q.D3())
        # self.qc.cx(Q.D6(), Q.D5())
        # self.qc.cx(Q.D8(), Q.D9())

        # self.qc.cx(Q.D2(), Q.D1())
        # self.qc.cx(Q.D4(), Q.D5())
        # self.qc.cx(Q.D6(), Q.D7())
        
        # self.qc.cx(Q.D3(), Q.D2())
        # self.qc.cx(Q.D7(), Q.D8())

        self.qc.barrier()

    def __add_first_cycle_circuit(self):
        # Prepare phase ancillary qubits
        self.qc.h(Q.A2())
        self.qc.h(Q.A4())
        self.qc.h(Q.A5())
        self.qc.h(Q.A7())
        # A4 is not prepared yet, but will be done later in the circuit to save on qubits

        # Phase-flip measurements
        self.qc.cx(Q.A2(), Q.D2())
        self.qc.cx(Q.A5(), Q.D4())
        self.qc.cx(Q.A7(), Q.D6())

        # Bit-flip measurements
        self.qc.cx(Q.D3(), Q.A3())
        self.qc.cx(Q.D5(), Q.A6())
        self.qc.cx(Q.D9(), Q.A8())

        self.qc.barrier()

    def __add_second_cycle_circuit(self):
        # Phase-flip measurements
        self.qc.cx(Q.A2(), Q.D5())
        self.qc.cx(Q.A5(), Q.D7())
        self.qc.cx(Q.A7(), Q.D9())

        # Bit-flip measurements
        self.qc.cx(Q.D2(), Q.A3())
        self.qc.cx(Q.D4(), Q.A6())
        self.qc.cx(Q.D8(), Q.A8())

        # A5 and A8 are ready for measurement
        # self.qc.h(Q.A5())
        # self.qc.measure(Q.A5(), C.A5())
        # self.qc.measure(Q.A8(), C.A8())

        # self.qc.reset(Q.A5())
        # self.qc.reset(Q.A8())

        # Prepare phase ancillary qubits
        # self.qc.h(Q.A4())

        self.qc.barrier()

    def __add_third_cycle_circuit(self):
        # Phase-flip measurements
        self.qc.cx(Q.A2(), Q.D1())
        self.qc.cx(Q.A4(), Q.D3())
        self.qc.cx(Q.A7(), Q.D5())

        # Bit-flip measurements
        self.qc.cx(Q.D2(), Q.A1())
        self.qc.cx(Q.D6(), Q.A3())
        self.qc.cx(Q.D8(), Q.A6())

        self.qc.barrier()

    def __add_fourth_cycle_circuit(self):
        # Phase-flip measurements
        self.qc.cx(Q.A2(), Q.D4())
        self.qc.cx(Q.A4(), Q.D6())
        self.qc.cx(Q.A7(), Q.D8())

        # Bit-flip measurements
        self.qc.cx(Q.D1(), Q.A1())
        self.qc.cx(Q.D5(), Q.A3())
        self.qc.cx(Q.D7(), Q.A6())

        self.qc.barrier()

        # Prepare phase-flip ancillary qubits for measurement
        self.qc.h(Q.A2())
        self.qc.h(Q.A4())
        self.qc.h(Q.A5())
        self.qc.h(Q.A7())
        
        self.qc.measure(Q.A1(), C.A1())
        self.qc.measure(Q.A2(), C.A2())
        self.qc.measure(Q.A3(), C.A3())
        self.qc.measure(Q.A4(), C.A4())
        self.qc.measure(Q.A5(), C.A5())
        self.qc.measure(Q.A6(), C.A6())
        self.qc.measure(Q.A7(), C.A7())

    def add_first_cycle_circuit(self):
        # Prepare all ancillary qubits
        self.qc.h(Q.A1())
        self.qc.h(Q.A3())
        self.qc.h(Q.A6())
        self.qc.h(Q.A8())

        self.qc.barrier()

        self.qc.cx(Q.D1(), Q.A2())
        self.qc.cx(Q.A3(), Q.D2())
        self.qc.cx(Q.D3(), Q.A4())

        self.qc.cx(Q.A6(), Q.D4())
        self.qc.cx(Q.D5(), Q.A7())
        self.qc.cx(Q.A8(), Q.D8())

        self.qc.barrier()


    def add_second_cycle_circuit(self):
        
        self.qc.cx(Q.A1(), Q.D1())
        self.qc.cx(Q.D2(), Q.A2())
        self.qc.cx(Q.A3(), Q.D5())
        self.qc.cx(Q.D4(), Q.A5())
        self.qc.cx(Q.A6(), Q.D7())
        self.qc.cx(Q.D6(), Q.A7())

        self.qc.barrier()


    def add_third_cycle_circuit(self):
        
        self.qc.cx(Q.D4(), Q.A2())
        self.qc.cx(Q.A3(), Q.D3())
        self.qc.cx(Q.D6(), Q.A4())
        self.qc.cx(Q.A6(), Q.D5())
        self.qc.cx(Q.D8(), Q.A7())
        self.qc.cx(Q.A8(), Q.D9())

        self.qc.barrier()


    def add_measure_all_ancillary(self):
        self.qc.measure(Q.A1(), C.A1())
        self.qc.measure(Q.A2(), C.A2())
        self.qc.measure(Q.A3(), C.A3())
        self.qc.measure(Q.A4(), C.A4())
        self.qc.measure(Q.A5(), C.A5())
        self.qc.measure(Q.A6(), C.A6())
        self.qc.measure(Q.A7(), C.A7())
        self.qc.measure(Q.A8(), C.A8())

    def add_measure_all_data(self):
        self.qc.measure(Q.D1(), C.D1())
        self.qc.measure(Q.D2(), C.D2())
        self.qc.measure(Q.D3(), C.D3())
        self.qc.measure(Q.D4(), C.D4())
        self.qc.measure(Q.D5(), C.D5())
        self.qc.measure(Q.D6(), C.D6())
        self.qc.measure(Q.D7(), C.D7())
        self.qc.measure(Q.D8(), C.D8())
        self.qc.measure(Q.D9(), C.D9())

    def add_fourth_cycle_circuit(self):
        
        self.qc.cx(Q.A1(), Q.D2())
        self.qc.cx(Q.D5(), Q.A2())
        self.qc.cx(Q.A3(), Q.D6())
        self.qc.cx(Q.D7(), Q.A5())
        self.qc.cx(Q.A6(), Q.D8())
        self.qc.cx(Q.D9(), Q.A7())

        self.qc.barrier()

        self.qc.h(Q.A1())
        self.qc.h(Q.A3())
        self.qc.h(Q.A6())
        self.qc.h(Q.A8())

        self.add_measure_all_ancillary()
        # self.add_measure_all_data()

    def add_a1(self):
        self.qc.h(Q.A1())

        self.qc.cx(Q.A1(), Q.D1())
        self.qc.cx(Q.A1(), Q.D2())

        self.qc.h(Q.A1())
        self.qc.measure(Q.A1(), C.A1())






        



        



    




    
