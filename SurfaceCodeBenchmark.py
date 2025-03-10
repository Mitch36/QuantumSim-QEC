from SurfaceCodeNoisyQuantumSim import NoisySurfaceCode

class NoisySurfaceCodeBenchmark:
    def __init__(self, stabilizer_rounds_interval: int, noise_factor: float = 1):
        self.stabilizer_rounds_interval = stabilizer_rounds_interval

        self.noise_factor = noise_factor
        self.quantumStateLog = []
        self.sf = NoisySurfaceCode(noise_factor)
        self.sf.circuit.classicalBitRegister.partitions.clear()

        self.p = self.sf.circuit.parameters["p"][0]
        self.T1 = self.sf.circuit.parameters["T1"][0]
        self.T2 = self.sf.circuit.parameters["T2"][0]

    def __save_state__(self, id: int, stateString: str):

        if(stateString[0] == '|'):
            stateString = stateString.replace("|", "")
        if(stateString[-1] == '>'):
            stateString = stateString.replace(">", "") 

        # ancillary_x_syndrome = str(stateString[0]) + str(stateString[1]) + str(stateString[2]) + str(stateString[3])
        # ancillary_z_syndrome = str(stateString[4]) + str(stateString[5]) + str(stateString[6]) + str(stateString[7]) 
        dataString = str(stateString[8]) + str(stateString[9]) + str(stateString[9]) + str(stateString[10]) + str(stateString[11]) + str(stateString[12]) + str(stateString[13]) + str(stateString[14]) + str(stateString[15])

        amountOfZeros = 0
        amountOfOnes = 0
        for char in dataString:
            if char == '1':
                amountOfOnes = amountOfOnes + 1
            elif char == '0':
                amountOfZeros = amountOfZeros + 1
            else:
                raise Exception(f"Forbidden character in stateString: {dataString}")
            
        logString = str(id) + ";[" + dataString + "];" + str(amountOfZeros) + ";" + str(amountOfOnes) + ";" + str(self.sf.circuit.logical_error_count) + ";" + str(self.p) + ";" + str(self.T1) + ";" + str(self.T2) + "\n"
        self.sf.circuit.logical_error_count = 0
        # print(logString)
        self.quantumStateLog.append(logString)

    def __build_nine_qubit_pauli_x_benchmark_circuit__(self, pauli_X_Gates: int):

        self.sf.add_encoder_circuit()    

        for x in range(int(pauli_X_Gates / self.stabilizer_rounds_interval)):
            for y in range(int(self.stabilizer_rounds_interval)):
                self.sf.add_noisy_pauli_x_on_all_data_qubits()
            
            self.sf.add_x_stabilizer_syndrome_extraction()
            self.sf.add_z_stabilizer_syndrome_extraction()
            self.sf.add_recovery_from_syndrome_x_stabilizer()
            self.sf.add_recovery_from_syndrome_z_stabilizer()

        self.sf.add_decoder_circuit()    
        self.sf.add_measure_all_data_qubits()


    def __build_nine_qubit_pauli_z_benchmark_circuit__(self, pauli_Z_Gates: int):
        
        self.sf.add_encoder_circuit()    
        
        for x in range(int(pauli_Z_Gates / self.stabilizer_rounds_interval)):
            for y in range(int(self.stabilizer_rounds_interval)):
                self.sf.add_noisy_pauli_z_on_all_data_qubits()
                
            self.sf.add_x_stabilizer_syndrome_extraction()
            self.sf.add_z_stabilizer_syndrome_extraction()
            self.sf.add_recovery_from_syndrome_x_stabilizer()
            self.sf.add_recovery_from_syndrome_z_stabilizer()
            
        self.sf.add_decoder_circuit()    

        self.sf.add_measure_all_data_qubits()
        
    def export_to_file(self, fileName: str):
        with open(f"output/{fileName}.csv", "w") as file:
            file.write("Index;State;Amount_of_zeros;Amount_of_ones;Logical_error_count;p;T1;T2\n")
            for dataLog in self.quantumStateLog:
                file.write(dataLog)
        file.close()
        
    def build_and_run_nine_qubit_pauli_x_benchmark(self, pauli_gates: int, iterations: int = 100):
        self.__build_nine_qubit_pauli_x_benchmark_circuit__(pauli_gates)
        for i in range(iterations):
            self.sf.circuit.execute()
            stateString = self.sf.circuit.classicalBitRegister.toString()
            self.__save_state__(i, stateString)
        data = "SurfaceCode_Pauli_X_Benchmark_Pauli_Gates" + str(pauli_gates) + "Recovery_interval" + str(self.stabilizer_rounds_interval) + "Factor" + str(self.noise_factor)
        print(data)
        self.export_to_file(data)

    def build_and_run_nine_qubit_pauli_z_benchmark(self, pauli_gates: int, iterations: int = 100):
        self.__build_nine_qubit_pauli_z_benchmark_circuit__(pauli_gates)
        for i in range(iterations):
            self.sf.circuit.execute()
            stateString = self.sf.circuit.classicalBitRegister.toString()
            self.__save_state__(i, stateString)
        data = "SurfaceCode_Pauli_Z_Benchmark_Pauli_Gates" + str(pauli_gates) + "Recovery_interval" + str(self.stabilizer_rounds_interval) + "Factor" + str(self.noise_factor)
        print(data)
        self.export_to_file(data)
                