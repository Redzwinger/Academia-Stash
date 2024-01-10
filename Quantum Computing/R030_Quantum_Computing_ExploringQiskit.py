'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Quantum Computing
Date: 14/10/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Quantum Computing \n Date: 14/10/2023")

print("\n ############# ################ ####################\n")

# Importing Stuff
from qiskit import *
import matplotlib.pyplot as plt

# Creating a Quantum Register with 2 qubits.
quantum_register = QuantumRegister(2)

# Creating a Classical Register with 2 qubits.
classy_register = ClassicalRegister(2)

quantum_circuit = QuantumCircuit(quantum_register, classy_register)

plt.style.use('seaborn-darkgrid')

# Initialisation
quantum_circuit.draw()

# Hadamard Gate
quantum_circuit.h(quantum_register[0])
#quantum_circuit.draw(output='mpl')

# NOT Gate
quantum_circuit.cx(quantum_register[0],quantum_register[1])

# Introducing Measure
quantum_circuit.measure(quantum_register,classy_register)
quantum_circuit.draw(output='mpl')
plt.show()