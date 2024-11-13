import quantumsim as sim

# Unit tests for testing the Toffoli gate in upwards position:
#   X   Target qubit
#   o   Control qubit A
#   o   Control qubit B

def test_toffoli_upwards_000():
    circuit = sim.Circuit(3)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|000>" 

def test_toffoli_upwards_001():
    circuit = sim.Circuit(3)
    circuit.pauli_x(2)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|001>" 

def test_toffoli_upwards_010():
    circuit = sim.Circuit(3)
    circuit.pauli_x(1)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|010>" 

def test_toffoli_upwards_100():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|100>" 

def test_toffoli_upwards_011():
    circuit = sim.Circuit(3)
    circuit.pauli_x(1)
    circuit.pauli_x(2)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|111>" 

def test_toffoli_upwards_101():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(2)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|101>"

def test_toffoli_upwards_110():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(1)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|110>"

def test_toffoli_upwards_111():
    circuit = sim.Circuit(3)
    circuit.pauli_x(0)
    circuit.pauli_x(1)
    circuit.pauli_x(2)
    circuit.toffoli(2, 1, 0)
    circuit.execute()
    measurement = circuit.measure()
    assert measurement == "|011>"