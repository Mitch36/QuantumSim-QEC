from quantumsim import Circuit

class PauliBenchmark:
    def __init__(self, depolarizing_error_probability: float):
        self.dep = depolarizing_error_probability
        self.quantumStateLog = []

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
            
        logString = str(id) + ";" + stateString + ";" + str(amountOfZeros) + ";" + str(amountOfOnes) + "\n"
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
        self.cr = Circuit(9, 9, True)
        for i in range(pauli_X_Gates):
            self.cr.noisy_pauli_x(0, self.dep)
            self.cr.noisy_pauli_x(1, self.dep)
            self.cr.noisy_pauli_x(2, self.dep)
            self.cr.noisy_pauli_x(3, self.dep)
            self.cr.noisy_pauli_x(4, self.dep)
            self.cr.noisy_pauli_x(5, self.dep)
            self.cr.noisy_pauli_x(6, self.dep)
            self.cr.noisy_pauli_x(7, self.dep)
            self.cr.noisy_pauli_x(8, self.dep)

        self.__add_measure_all_data_qubits__()

    def __build_nine_qubit_pauli_z_benchmark_circuit__(self, pauli_Z_Gates: int):
        self.cr = Circuit(9, 9, True)
        self.__add_hadamard_all_data_qubits__()
        for i in range(pauli_Z_Gates):
            self.cr.noisy_pauli_z(0, self.dep)
            self.cr.noisy_pauli_z(1, self.dep)
            self.cr.noisy_pauli_z(2, self.dep)
            self.cr.noisy_pauli_z(3, self.dep)
            self.cr.noisy_pauli_z(4, self.dep)
            self.cr.noisy_pauli_z(5, self.dep)
            self.cr.noisy_pauli_z(6, self.dep)
            self.cr.noisy_pauli_z(7, self.dep)
            self.cr.noisy_pauli_z(8, self.dep)

        self.__add_hadamard_all_data_qubits__()
        self.__add_measure_all_data_qubits__()
        
    def export_to_file(self, fileName: str):
        with open(f"output/{fileName}.csv", "w") as file:
            file.write("index;state;amountOfZeros;amountOfOnes\n")
            for dataLog in self.quantumStateLog:
                file.write(dataLog)
        file.close()
        
    def build_and_run_nine_qubit_pauli_x_benchmark(self, pauli_gates: int, iterations: int = 100):
        self.__build_nine_qubit_pauli_x_benchmark_circuit__(pauli_gates)
        for i in range(iterations):
            self.cr.execute()
            stateString = self.cr.classicalBitRegister.toString()
            self.__save_state__(i, stateString)
        p = str(self.dep)
        p = p.replace(".", "_")
        p = "Nine_Qubit_Pauli_X_Benchmark_p" + p + "Pauli_Gates" + str(pauli_gates) 
        print(p)
        self.export_to_file(p)

    def build_and_run_nine_qubit_pauli_z_benchmark(self, pauli_gates: int, iterations: int = 100):
        self.__build_nine_qubit_pauli_z_benchmark_circuit__(pauli_gates)
        for i in range(iterations):
            self.cr.execute()
            stateString = self.cr.classicalBitRegister.toString()
            self.__save_state__(i, stateString)
        p = str(self.dep)
        p = p.replace(".", "_")
        p = "Nine_Qubit_Pauli_Z_Benchmark_p" + p + "Pauli_Gates" + str(pauli_gates) 
        print(p)
        self.export_to_file(p)
                