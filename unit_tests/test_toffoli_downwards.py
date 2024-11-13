import quantumsim as sim

# Unit tests for testing the Toffoli gate in downwards position:
#   o   Control qubit A
#   o   Control qubit B
#   X   Target qubit

def test_toffoli_downwards_000():
    circuit = sim.Circuit(3)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|000>" 

def test_toffoli_downwards_001():
    circuit = sim.Circuit(3)
    circuit.pauli_x(2)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|001>" 

def test_toffoli_downwards_010():
    circuit = sim.Circuit(3)
    circuit.pauli_x(1)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|010>" 

def test_toffoli_downwards_100():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|100>" 

def test_toffoli_downwards_011():
    circuit = sim.Circuit(3)
    circuit.pauli_x(1)
    circuit.pauli_x(2)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|011>" 

def test_toffoli_downwards_101():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(2)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|101>" 

def test_toffoli_downwards_110():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(1)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|111>" 

def test_toffoli_downwards_111():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(1)
    circuit.pauli_x(2)
    circuit.toffoli(0, 1, 2)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|110>" 