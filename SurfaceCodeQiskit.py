from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

class Q(): # Quantum register naming aliases 
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
    def X1() -> int:
        return 9
    @staticmethod
    def X2() -> int:
        return 10
    @staticmethod
    def X3() -> int:
        return 11
    @staticmethod
    def X4() -> int:
        return 12
    @staticmethod
    def Z1() -> int:
        return 13
    @staticmethod
    def Z2() -> int:
        return 14
    @staticmethod
    def Z3() -> int:
        return 15
    @staticmethod
    def Z4() -> int:
        return 16

class C(): # Classical register naming aliases 
    @staticmethod
    def X1() -> int:
        return 0
    @staticmethod
    def X2() -> int:
        return 1
    @staticmethod
    def X3() -> int:
        return 2
    @staticmethod
    def X4() -> int:
        return 3
    @staticmethod
    def Z1() -> int:
        return 4
    @staticmethod
    def Z2() -> int:
        return 5
    @staticmethod
    def Z3() -> int:
        return 6
    @staticmethod
    def Z4() -> int:
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

"""
This class offers functions for simulating the rotated surface 17 code implementation using Qiskit
"""
class SurfaceCode:
    # Sources used for creating this class:
    # https://errorcorrectionzoo.org/c/surface-17#citation-3
    # https://arxiv.org/pdf/2303.17211
    # http://arxiv.org/pdf/1612.08208

    def __init__(self):
        q_D = QuantumRegister(9, name="Q_D")
        q_X = QuantumRegister(4, name="Q_AncX")
        q_Z = QuantumRegister(4, name="Q_AncZ")
        c_X = ClassicalRegister(4, name="C_AncX")
        c_Z = ClassicalRegister(4, name="C_AncZ")
        c_D = ClassicalRegister(9, name="C_Data")

        self.qc = QuantumCircuit(q_D, q_X, q_Z, c_X, c_Z, c_D)

    def add_encoder_circuit(self):
        # Step 1. initialize D2, D4, D6, D8 in Hadamard basis.
        self.qc.h(Q.D2())
        self.qc.h(Q.D4())
        self.qc.h(Q.D6())
        self.qc.h(Q.D8())
        self.qc.barrier()

        # Step 2. Make four different Bell and Greenberger-Horne-Zeilinger states.
        self.qc.cx(Q.D2(), Q.D1())
        self.qc.cx(Q.D6(), Q.D3())
        self.qc.cx(Q.D6(), Q.D5())
        self.qc.cx(Q.D4(), Q.D5())
        self.qc.cx(Q.D4(), Q.D7())
        self.qc.cx(Q.D8(), Q.D9())
        self.qc.barrier()

        # Step 3. Entangle all Bell and Greenberger-Horne-Zeilinger states.
        self.qc.cx(Q.D3(), Q.D2())
        self.qc.cx(Q.D7(), Q.D8())
        self.qc.barrier()

    def add_stabilizer_x_syndrome_extraction(self): # Marked BLUE lines

        # Step 1. Prepare ancillary stabilizer X qubits, put in Hadamard basis
        self.qc.h(Q.X1())
        self.qc.h(Q.X2())
        self.qc.h(Q.X3())
        self.qc.h(Q.X4())
        self.qc.barrier()

        # Step 2. Peform CNOT's, ancillary qubits as control and data qubit as target 
        # Step 2.1. First cycle
        self.qc.cx(Q.X1(), Q.D1())
        self.qc.cx(Q.X2(), Q.D7())
        self.qc.cx(Q.X3(), Q.D5())
        self.qc.barrier()

        # Step 2.2. Second cycle
        self.qc.cx(Q.X2(), Q.D4())
        self.qc.cx(Q.X3(), Q.D2())
        self.qc.cx(Q.X4(), Q.D8())
        self.qc.barrier()

        # Step 2.3. Third cycle
        self.qc.cx(Q.X1(), Q.D2())
        self.qc.cx(Q.X2(), Q.D8())
        self.qc.cx(Q.X3(), Q.D6())
        self.qc.barrier()

        # Step 2.4. Fourth cycle
        self.qc.cx(Q.X2(), Q.D5())
        self.qc.cx(Q.X3(), Q.D3())
        self.qc.cx(Q.X4(), Q.D9())
        self.qc.barrier()

        # Step 3. Prepare ancillary qubits for measurement, put in computational basis
        self.qc.h(Q.X1())
        self.qc.h(Q.X2())
        self.qc.h(Q.X3())
        self.qc.h(Q.X4())
        self.qc.barrier()

        # Step 4. Syndrome measurement
        self.qc.measure(Q.X1(), C.X1())
        self.qc.measure(Q.X2(), C.X2())
        self.qc.measure(Q.X3(), C.X3())
        self.qc.measure(Q.X4(), C.X4())

    def add_stabilizer_z_syndrome_extraction(self): # Marked RED lines

        # Step 1. Peform CNOT's, ancillary qubits as target and data qubit as control 
        # Step 1.1. First cycle
        self.qc.cx(Q.D4(), Q.Z2())
        self.qc.cx(Q.D8(), Q.Z3())
        self.qc.cx(Q.D6(), Q.Z4())
        self.qc.barrier()

        # Step 1.2. Second cycle
        self.qc.cx(Q.D7(), Q.Z1())
        self.qc.cx(Q.D5(), Q.Z2())
        self.qc.cx(Q.D9(), Q.Z3())
        self.qc.barrier()

        # Step 1.3. Third cycle
        self.qc.cx(Q.D1(), Q.Z2())
        self.qc.cx(Q.D5(), Q.Z3())
        self.qc.cx(Q.D3(), Q.Z4())
        self.qc.barrier()

        # Step 1.4. Fourth cycle
        self.qc.cx(Q.D4(), Q.Z1())
        self.qc.cx(Q.D2(), Q.Z2())
        self.qc.cx(Q.D6(), Q.Z3())
        self.qc.barrier()

        # Step 2. Syndrome measurement
        self.qc.measure(Q.Z1(), C.Z1())
        self.qc.measure(Q.Z2(), C.Z2())
        self.qc.measure(Q.Z3(), C.Z3())
        self.qc.measure(Q.Z4(), C.Z4())

    def measure_all_data_qubits(self):
        self.qc.measure(Q.D1(), C.D1())
        self.qc.measure(Q.D2(), C.D2())
        self.qc.measure(Q.D3(), C.D3())
        self.qc.measure(Q.D4(), C.D4())
        self.qc.measure(Q.D5(), C.D5())
        self.qc.measure(Q.D6(), C.D6())
        self.qc.measure(Q.D7(), C.D7())
        self.qc.measure(Q.D8(), C.D8())
        self.qc.measure(Q.D9(), C.D9())

    def add_decoder_circuit(self):
        # Decoding is the opposite of encoding, reverting the encoding steps results in the initiliazed state
        # Step 1. Dentangle all Bell and Greenberger-Horne-Zeilinger states.
        self.qc.cx(Q.D3(), Q.D2())
        self.qc.cx(Q.D7(), Q.D8())
        self.qc.barrier()

        # Step 2. Dentagle different Bell and Greenberger-Horne-Zeilinger states.
        self.qc.cx(Q.D2(), Q.D1())
        self.qc.cx(Q.D6(), Q.D3())
        self.qc.cx(Q.D6(), Q.D5())
        self.qc.cx(Q.D4(), Q.D5())
        self.qc.cx(Q.D4(), Q.D7())
        self.qc.cx(Q.D8(), Q.D9())
        self.qc.barrier()

        # Step 3. Put D2, D4, D6, D8 out of the Hadamard basis.
        self.qc.h(Q.D2())
        self.qc.h(Q.D4())
        self.qc.h(Q.D6())
        self.qc.h(Q.D8())
        self.qc.barrier()

    def create_bit_flip(self, q: int):
        self.qc.x(q)

    def create_phase_flip(self, q: int):
        self.qc.z(q)










        



        



    




    
