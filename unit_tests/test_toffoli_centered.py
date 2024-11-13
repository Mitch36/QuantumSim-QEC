import quantumsim as sim

# Unit tests for testing the Toffoli gate in upwards position:
#   o   Control qubit A
#   X   Target qubit
#   o   Control qubit B

def test_toffoli_centered_000():
    circuit = sim.Circuit(3)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|000>" 

def test_toffoli_centered_001():
    circuit = sim.Circuit(3)
    circuit.pauli_x(2)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|001>" 

def test_toffoli_centered_010():
    circuit = sim.Circuit(3)
    circuit.pauli_x(1)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|010>" 

def test_toffoli_centered_100():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|100>" 

def test_toffoli_centered_011():
    circuit = sim.Circuit(3)
    circuit.pauli_x(1)
    circuit.pauli_x(2)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|011>" 

def test_toffoli_centered_101():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(2)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|111>" 

def test_toffoli_centered_110():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(1)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|110>" 

def test_toffoli_centered_111():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(1)
    circuit.pauli_x(2)
    circuit.toffoli(0, 2, 1)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|101>" 