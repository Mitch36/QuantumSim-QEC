from quantumsim import Circuit

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
        return 9
    @staticmethod
    def X3() -> int:
        return 9
    @staticmethod
    def X4() -> int:
        return 9
    @staticmethod
    def Z1() -> int:
        return 9
    @staticmethod
    def Z2() -> int:
        return 9
    @staticmethod
    def Z3() -> int:
        return 9
    @staticmethod
    def Z4() -> int:
        return 9

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
This class offers functions for simulating the rotated surface 17 code implementation using QuantumSim
"""
class SurfaceCode:
    # Sources used for creating this class:
    # https://errorcorrectionzoo.org/c/surface-17#citation-3
    # https://arxiv.org/pdf/2303.17211
    # http://arxiv.org/pdf/1612.08208
    
    def __init__(self):

        # Simulating many qubits is expensive resource wise, the rotated surface 17 code is simulated using only 10 qubits using QuantumSim.
        self.qubits = int(10)
        # All 17 simulated qubits are eventually measured, therefore 17 classical bits are required.
        self.bits = int(17)
        # Memory optimization flag, when simulating many qubits (10 or more) this flag should always be set to TRUE
        self.save_instructions_flag = True

        self.circuit = Circuit(self.qubits, self.bits, self.save_instructions_flag)





    
