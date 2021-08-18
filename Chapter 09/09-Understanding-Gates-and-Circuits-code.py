savefig_dpi = 600

not 0

not 1

def bit_not(bit):
    return 0 if bit else 1

bit_not(0)

bit_not(1)

~0

~1

[~5, ~2, ~1, ~0, ~1, ~2, ~5]

def print_truth_table(op, name):
    print(f"{name:4} | 0    1")
    print("-----+-------")
    for bit in (0, 1):
        print(f"{bit}    | {op(bit, 0)}    {op(bit, 1)}")

print_truth_table(lambda x,y: x and y, "and")

print_truth_table(lambda x,y: x or y, "or")

print_truth_table(lambda x,y: x ^ y, "xor")

print_truth_table(lambda x,y: bit_not(x and y), "nand")

def bit_nand(bit_0, bit_1):
    return bit_not(bit_0 and bit_1)

print_truth_table(lambda x,y: bit_not(x or y), "nor")

print_truth_table(lambda x,y: bit_not(x ^ y), "xnor")

def mystery_gate(bit_0, bit_1):
    x = bit_nand(bit_0, bit_1)
    y = bit_nand(bit_0, x)
    z = bit_nand(bit_1, x)
    return bit_nand(y, z)

def another_mystery_gate(bit_0, bit_1):
    return abs(bit_0 - bit_1)

def bit_cnot(bit_0, bit_1):
    return (bit_0, bit_not(bit_1) if bit_0 else bit_1)

def bit_add(bit_0, bit_1):
    return (bit_0 and bit_1, bit_0 ^ bit_1)

for bit_0 in (0, 1):
    for bit_1 in (0, 1):
        sum_ = bit_add(bit_0, bit_1)
        print(f"{bit_0} + {bit_1} = {sum_[0]}{sum_[1]}")

import math

a = math.sqrt(3)/2
b = 1/2
(a, b)

abs(a)**2 + abs(b)**2

for x in (1, -1, 1j, -1j):
    print(x * math.sqrt(2)/2)

def qubit_id(a, b): return (a, b)

def qubit_X(a, b): return (b, a)

def qubit_Z(a, b): return (a, -b)

ket_0 = (1, 0)
qubit_X(*ket_0)

qubit_Z(*qubit_X(*ket_0))

import random

random.seed(23)

def fake_measure(a, b):
    a_abs_squared = abs(a)**2

    # handle the endpoints
    if a_abs_squared == 0:
        return 1
    if a_abs_squared == 1:
        return 0

    # get a random number in a uniform distribution
    # that includes 0 and 1
    u = random.uniform(0.0, 1.0)

    return 0 if u <= a_abs_squared else 1

a = complex(0, math.sqrt(3)/2)
a

b = -0.5

counts = [0, 0]

for _ in range(10000):
    counts[fake_measure(a, b)] += 1

for bit in (0, 1):
    print(f"Number of times we saw {bit}: {counts[bit]}")

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import execute, transpile, Aer, IBMQ
from qiskit.visualization import plot_histogram
import math
import matplotlib

draw_kwargs = {
    "output": "mpl",         # use matplotlib
    "cregbundle": False,     # separate classical register wires
    "initial_state": True,   # show |0> and 0
    "idle_wires": False,     # don't show unused wires

    "style": {
        "name": "bw",        # black-and-white for book
        "subfontsize": 9,    # font size of subscripts
        "dpi": 600           # image resolution
    }
}

histogram_color = "#82caaf"

qreg_q = QuantumRegister(1, "q")
creg_c = ClassicalRegister(1, "meas")

circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])

file_name = "work/images-to-trim/w-22-iqx-example-00B.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit.measure(qreg_q[0], creg_c[0])

file_name = "work/images-to-trim/w-22-iqx-example-00C.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(1)
circuit.x(0)
circuit.measure_all()

file_name = "work/images-to-trim/t-iqx-example-01.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)
file_name = "work/images-to-trim/w-22-iqx-example-01.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

simulator = Aer.get_backend("aer_simulator")

result = execute(circuit, simulator, shots=1000).result()
counts = result.get_counts(circuit)
counts

histogram = plot_histogram(counts, color=histogram_color,
                           title="IBM Quantum Simulator")

histogram.savefig("work/images-to-trim/w-24-iqx-example-01A-histogram.jpg", dpi=savefig_dpi, bbox_inches="tight", pad_inches=0.1)

IBMQ.load_account()

IBMQ.providers()
provider = IBMQ.get_provider("ibm-q")

print("System Name            Number of Qubits")
print("---------------------------------------")
for backend in sorted(provider.backends(), key=lambda x: x.name()):
    config = backend.configuration()
    print(f"{config.backend_name:22}      {config.n_qubits:>3}")

from qiskit.providers.ibmq import least_busy

device = least_busy(provider.backends(
    filters=lambda x: x.configuration().n_qubits >= 3 and
                      not x.configuration().simulator and
                      x.status().operational==True))

device

quantum_hw = provider.get_backend("ibmq_belem")

# this is from an actual run on ibmq_belem
counts = {'0': 34, '1': 966}

counts

histogram = plot_histogram(counts, color=histogram_color,
                           title="ibmq_belem Hardware")

histogram.savefig("work/images-to-trim/w-24-iqx-example-01B-histogram.jpg", dpi=savefig_dpi, bbox_inches="tight", pad_inches=0.1)

circuit = QuantumCircuit(2)

circuit.cx(0, 1)
circuit.h(0)
circuit.h(1)

file_name = "work/images-to-trim/w-22-iqx-example-02A.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit.cx(0, 1)
circuit.h(0)
circuit.h(1)

file_name = "work/images-to-trim/w-22-iqx-example-02B.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit.cx(0, 1)

file_name = "work/images-to-trim/w-22-iqx-example-02C.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

initialization_circuit = QuantumCircuit(2)
initialization_circuit.id(0)
initialization_circuit.x(1)
initialization_circuit.barrier()

file_name = "work/images-to-trim/w-22-iqx-example-03.jpg"
initialization_circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

new_circuit = initialization_circuit.compose(circuit)
new_circuit.measure_all()

file_name = "work/images-to-trim/w-22-iqx-example-04.jpg"
new_circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

result = execute(new_circuit, simulator, shots=1000).result()

counts = result.get_counts(new_circuit)
counts

histogram = plot_histogram(counts, color=histogram_color,
                           title="IBM Quantum Simulator")

histogram.savefig("work/images-to-trim/w-24-iqx-example-05A-histogram.jpg", dpi=savefig_dpi, bbox_inches="tight", pad_inches=0.1)

# this is from an actual run on ibmq_belem
counts = {'00': 49, '01': 923, '10': 12, '11': 16}

counts

histogram = plot_histogram(counts, color=histogram_color,
                           title="ibmq_belem Hardware")

histogram.savefig("work/images-to-trim/w-24-iqx-example-05B-histogram.jpg", dpi=savefig_dpi, bbox_inches="tight", pad_inches=0.1)

new_circuit_hw = transpile(new_circuit, quantum_hw, optimization_level=1)

file_name = "work/images-to-trim/w-22-iqx-example-05C-trans-hw.jpg"
new_circuit_hw.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

a, b = quantum_state = (-math.sqrt(3)/2, complex(0, 1/2))
abs(a)**2 + abs(b)**2

circuit = QuantumCircuit(1)
circuit.initialize(quantum_state, 0)
circuit.measure_all()

file_name = "work/images-to-trim/w-22-iqx-example-06.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

result = execute(circuit, simulator, shots=5000).result()

counts = result.get_counts(circuit)
counts

histogram = plot_histogram(counts, color=histogram_color,
                           title="IBM Quantum Simulator")

histogram.savefig("work/images-to-trim/w-24-iqx-example-06A-histogram.jpg", dpi=savefig_dpi, bbox_inches="tight", pad_inches=0.1)

# this is from an actual run on ibmq_belem
counts = {'0': 3950, '1': 1050}

counts

histogram = plot_histogram(counts, color=histogram_color,
                          title="ibmq_belem Hardware")

histogram.savefig("work/images-to-trim/w-24-iqx-example-06B-histogram.jpg", dpi=savefig_dpi, bbox_inches="tight", pad_inches=0.1)

circuit_hw = transpile(circuit, quantum_hw, optimization_level=1)

file_name = "work/images-to-trim/w-22-iqx-example-06C-trans-hw.jpg"
circuit_hw.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cnot(0, 1)

file_name = "work/images-to-trim/w-22-iqx-example-07.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

