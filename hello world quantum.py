# Quantum Helloworld
from qiskit import *
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
# circuit = QuantumCircuit(2, 2)
# circuit.gate_name(target_index)
circuit.x(0)
circuit.h(0)
circuit.y(1)
circuit.z(1)
# After all gates are applied, measure the circuit
circuit.measure([0,1], [0,1])
# circuit.measure(range(2), range(2))
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator, shots=100).result()
print(circuit)
# circuit.draw()
print("Measurement is:", result.get_counts(circuit))

