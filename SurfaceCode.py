import quantumsim as sim

class Qubit:
    def __init__(self, id, name, type, x, y):
        self.id = id
        self.name = name
        self.type = type # Data OR Ancillary qubit type
        self.x = x
        self.y = y
    
    def toString(self):
        return "id: " + str(self.id) + " Qubit: " + str(self.name) + " type: " + str(self.type) + "\tx: " + str(self.x) + " y: " + str(self.y)

class SurfaceCode:

    def __init__(self, code_distance):
        if(code_distance < 1):
            raise Exception("Code distance must be greater than 0")
        if code_distance % 2 == 0:
            if code_distance != 2:
                raise Exception("Code distance can not be even, exception is 2")

        self.codeDistance = code_distance
        self.lattice = (code_distance * 2) -1
        self.totalQubits = self.lattice ** 2 
        print("Surface code initliazed with lattice: " + str(self.lattice))
        print("Total qubits used for surface: " + str(self.totalQubits))

        self.qubits = []

        previousQubitWasDataQubit = False
        nameCounter = 1

        for i in range(self.totalQubits):
            if previousQubitWasDataQubit:
                self.qubits.append(Qubit(i, "A" + str(nameCounter), "Ancillary", self.__toPosition_X(i), self.__toPosition_Y(i)))
                previousQubitWasDataQubit = False
                nameCounter += 1
            else:
                self.qubits.append(Qubit(i, "D" + str(nameCounter), "Data", self.__toPosition_X(i), self.__toPosition_Y(i)))
                previousQubitWasDataQubit = True

    def __toPosition_X(self, index):
        amount = index // self.lattice
        return index - (self.lattice * amount)
    
    def __toPosition_Y(self, index):
        amount = index // self.lattice
        return amount
    
    def encode(self):
        self.circuit.hadamard(0)
        # for qubit in self.qubits:
        #     if(qubit.type == "Data" and qubit.id  != self.totalQubits - 1):
        #         self.circuit.cnot(qubit.id, qubit.id + 2)
        return
    
    def toStringQubits(self):
        for qubit in self.qubits:
            print(qubit.toString())

    def toStringCircuit(self):
        return self.circuit.toString_gates_and_descriptions()

    def execute(self):
        return
