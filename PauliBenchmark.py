from quantumsim import Circuit

class PauliBenchmark:
    def __init__(self, noise_factor: float = 1):
        self.quantumStateLog = []
        self.noise_factor = noise_factor

        self.cr = Circuit(9, 9, True, noise_factor)
        # A greater p value means more noise
        self.p = self.cr.parameters["p"][0] * self.noise_factor
        # A smaller T1 value means more noise
        self.T1 = self.cr.parameters["T1"][0] / self.noise_factor
        # A smaller T2 value means more noise
        self.T2 = self.cr.parameters["T2"][0] / self.noise_factor

    def __save_state__(self, id: int, stateString: str):

        if(stateString[0] == '|'):
            stateString = stateString.replace("|", "")
        if(stateString[-1] == '>'):
            stateString = stateString.replace(">", "") 

        amountOfZeros = 0
        amountOfOnes = 0
        for char in stateString:
            if char == '1':
                amountOfOnes = amountOfOnes + 1
            elif char == '0':
                amountOfZeros = amountOfZeros + 1
            else:
                raise Exception(f"Forbidden character in stateString: {stateString}")
            
        logString = str(id) + ";[" + stateString + "];" + str(amountOfZeros) + ";" + str(amountOfOnes) + ";" + str(self.p) + ";" + str(self.T1) + ";" + str(self.T2) + "\n"
        self.quantumStateLog.append(logString)

    def __add_measure_all_data_qubits__(self):
        self.cr.measurement(0, 0)
        self.cr.measurement(1, 1)
        self.cr.measurement(2, 2)
        self.cr.measurement(3, 3)
        self.cr.measurement(4, 4)
        self.cr.measurement(5, 5)
        self.cr.measurement(6, 6)
        self.cr.measurement(7, 7)
        self.cr.measurement(8, 8)

    def __add_hadamard_all_data_qubits__(self):
        self.cr.hadamard(0)
        self.cr.hadamard(1)
        self.cr.hadamard(2)
        self.cr.hadamard(3)
        self.cr.hadamard(4)
        self.cr.hadamard(5)
        self.cr.hadamard(6)
        self.cr.hadamard(7)
        self.cr.hadamard(8)

    def __build_nine_qubit_pauli_x_benchmark_circuit__(self, pauli_X_Gates: int):
        for i in range(pauli_X_Gates):
            self.cr.noisy_pauli_x(0)
            self.cr.noisy_pauli_x(1)
            self.cr.noisy_pauli_x(2)
            self.cr.noisy_pauli_x(3)
            self.cr.noisy_pauli_x(4)
            self.cr.noisy_pauli_x(5)
            self.cr.noisy_pauli_x(6)
            self.cr.noisy_pauli_x(7)
            self.cr.noisy_pauli_x(8)

        self.__add_measure_all_data_qubits__()

    def __build_nine_qubit_pauli_z_benchmark_circuit__(self, pauli_Z_Gates: int):
        self.__add_hadamard_all_data_qubits__()
        for i in range(pauli_Z_Gates):
            self.cr.noisy_pauli_z(0)
            self.cr.noisy_pauli_z(1)
            self.cr.noisy_pauli_z(2)
            self.cr.noisy_pauli_z(3)
            self.cr.noisy_pauli_z(4)
            self.cr.noisy_pauli_z(5)
            self.cr.noisy_pauli_z(6)
            self.cr.noisy_pauli_z(7)
            self.cr.noisy_pauli_z(8)

        self.__add_hadamard_all_data_qubits__()
        self.__add_measure_all_data_qubits__()
        
    def export_to_file(self, fileName: str):
        with open(f"output/{fileName}.csv", "w") as file:
            file.write("index;state;amountOfZeros;amountOfOnes;p;T1;T2\n")
            for dataLog in self.quantumStateLog:
                file.write(dataLog)
        file.close()
        
    def build_and_run_nine_qubit_pauli_x_benchmark(self, pauli_gates: int, iterations: int = 100):
        self.__build_nine_qubit_pauli_x_benchmark_circuit__(pauli_gates)
        for i in range(iterations):
            self.cr.execute()
            stateString = self.cr.classicalBitRegister.toString()
            self.__save_state__(i, stateString)
        p = "Nine_Qubit_Pauli_X_Benchmark_Pauli_Gates" + str(pauli_gates) + "Factor" + str(self.noise_factor)
        print(p)
        self.export_to_file(p)

    def build_and_run_nine_qubit_pauli_z_benchmark(self, pauli_gates: int, iterations: int = 100):
        self.__build_nine_qubit_pauli_z_benchmark_circuit__(pauli_gates)
        for i in range(iterations):
            self.cr.execute()
            stateString = self.cr.classicalBitRegister.toString()
            self.__save_state__(i, stateString)
        p = "Nine_Qubit_Pauli_Z_Benchmark_Pauli_Gates" + str(pauli_gates) + "Factor" + str(self.noise_factor)
        print(p)
        self.export_to_file(p)
                