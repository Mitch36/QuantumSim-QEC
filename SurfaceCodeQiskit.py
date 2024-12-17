from quantumsim import Circuit
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
    def __init__(self):
        self.qubits = int(10)
        self.bits = int(8)
        self.save_instructions_flag = True

        self.circuit = Circuit(self.qubits, self.bits, self.save_instructions_flag)

    def getLog(self):
        pass

    def syndromeExtraction(self):
        pass

    def add_encoder_circuit(self):
        self.circuit.hadamard(Q.D1())
        self.circuit.cnot(Q.D1(), Q.D2())
        self.circuit.cnot(Q.D2(), Q.D3())
        self.circuit.cnot(Q.D3(), Q.D4())
        self.circuit.cnot(Q.D4(), Q.D5())
        self.circuit.cnot(Q.D5(), Q.D6())
        self.circuit.cnot(Q.D6(), Q.D7())
        self.circuit.cnot(Q.D7(), Q.D8())
        self.circuit.cnot(Q.D8(), Q.D9())
    
        # self.circuit.hadamard(Q.D1())
        # self.circuit.hadamard(Q.D2())
        # self.circuit.hadamard(Q.D3())
        # self.circuit.hadamard(Q.D4())
        # self.circuit.hadamard(Q.D5())
        # self.circuit.hadamard(Q.D6())
        # self.circuit.hadamard(Q.D7())
        # self.circuit.hadamard(Q.D8())
        # self.circuit.hadamard(Q.D9())
        

    def remove_encoder_circuit(self):
        self.circuit.remove_circuit_part(Q.D1(), Q.D9())
        
    def add_bit_flip_circuit(self):
        q = rnd.randint(0, 8)
        self.circuit.bitflip_error(q)
    
    def add_phase_flip_circuit(self):
        q = rnd.randint(0, 8)
        self.circuit.phaseflip_error(q)

    def add_lower_left(self):
        self.circuit.cnot(Q.D4(), Q.A5())

        self.circuit.hadamard(Q.A6())

        self.circuit.hadamard(Q.A6())


        self.circuit.cnot(Q.D4(), Q.A5())
        self.circuit.cnot(Q.D4(), Q.A5())



    def add_circuit_a1(self):
        self.circuit.cnot(Q.D1(), Q.A1())
        self.circuit.cnot(Q.D2(), Q.A1())
        self.circuit.measurement(Q.A1(), C.A1())
        self.circuit.reset(Q.A1(), C.A1())

    def add_circuit_a2(self):
        self.circuit.hadamard(Q.A2())
        self.circuit.cnot(Q.A2(), Q.D1())
        self.circuit.cnot(Q.A2(), Q.D2())
        self.circuit.cnot(Q.A2(), Q.D4())
        self.circuit.cnot(Q.A2(), Q.D5())
        self.circuit.hadamard(Q.A2())
        self.circuit.measurement(Q.A2(), C.A2())
        self.circuit.reset(Q.A2(), C.A2())
        
    def add_circuit_a3(self):
        self.circuit.cnot(Q.D2(), Q.A3())
        self.circuit.cnot(Q.D3(), Q.A3())
        self.circuit.cnot(Q.D5(), Q.A3())
        self.circuit.cnot(Q.D6(), Q.A3())
        self.circuit.measurement(Q.A3(), C.A3())
        self.circuit.reset(Q.A3(), C.A3())

    def add_circuit_a4(self):
        self.circuit.hadamard(Q.A4())
        self.circuit.cnot(Q.A4(), Q.D3())
        self.circuit.cnot(Q.A4(), Q.D6())
        self.circuit.hadamard(Q.A4())
        self.circuit.measurement(Q.A4(), C.A4())
        self.circuit.reset(Q.A4(), C.A4())

    def add_circuit_a5(self):
        self.circuit.hadamard(Q.A5())
        self.circuit.cnot(Q.A5(), Q.D4())
        self.circuit.cnot(Q.A5(), Q.D7())
        self.circuit.hadamard(Q.A5())
        self.circuit.measurement(Q.A5(), C.A5())
        self.circuit.reset(Q.A5(), C.A5())

    def add_circuit_a6(self):
        self.circuit.cnot(Q.D4(), Q.A6())
        self.circuit.cnot(Q.D5(), Q.A6())
        self.circuit.cnot(Q.D7(), Q.A6())
        self.circuit.cnot(Q.D8(), Q.A6())
        self.circuit.measurement(Q.A6(), C.A6())
        self.circuit.reset(Q.A6(), C.A6())

    def add_circuit_a7(self):
        self.circuit.hadamard(Q.A7())
        self.circuit.cnot(Q.A7(), Q.D5())
        self.circuit.cnot(Q.A7(), Q.D6())
        self.circuit.cnot(Q.A7(), Q.D8())
        self.circuit.cnot(Q.A7(), Q.D9())
        self.circuit.hadamard(Q.A7())
        self.circuit.measurement(Q.A7(), C.A7())
        self.circuit.reset(Q.A7(), C.A7())


    def add_circuit_a8(self):
        self.circuit.cnot(Q.D8(), Q.A8())
        self.circuit.cnot(Q.D9(), Q.A8())
        self.circuit.measurement(Q.A8(), C.A8())
        self.circuit.reset(Q.A8(), C.A8())






    
