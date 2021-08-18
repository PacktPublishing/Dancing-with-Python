numbers = [4, 46, 40, 15, 50, 34, 32, 20, 24, 30, 22, 49, 36, 16, 5, 2]
numbers

def find_number(n, list_of_numbers):
    for j in range(len(list_of_numbers)):
        if n == list_of_numbers[j]:
            return (j, j + 1)
    return (None, len(list_of_numbers))

find_number(4, numbers)

find_number(2, numbers)

find_number(17, numbers)

numbers.sort()
numbers

def find_number(n, list_of_numbers):
    # list_of_numbers must be sorted in ascending order
    for j in range(len(list_of_numbers)):
        if n == list_of_numbers[j]:
            return (j, j + 1)
        if n < list_of_numbers[j]:
            break
    return (None, len(list_of_numbers))

for n in [2, 17, 30, 50]:
    print(f"n = {n:2}: {find_number(n, numbers)}")

def find_number(n, list_of_numbers):
    """Returns index of found number via binary search or None

    Parameters
    ----------
    n : `int` or `float` or `Fraction`
        The number we seek.
    list_of_numbers: `list`
        Sorted list of numbers.

    Returns
    -------
    `int` or None
        The index of n in list_of_numbers if found,
        None otherwise.
    """

    def print_num(j):
        # Utility function to display search progress
        if j is not None:
            print(f"-> {list_of_numbers[j]}", end=' ')
        else:
            print("-> None", end=' ')

    def binary_find(start, end, count):
        # Recursive binary search
        # start and end are list indices, count is the
        # number of times this function is called.

        count += 1

        # Handle the case when the list has one item.
        if start + 1 == end:
            if n == list_of_numbers[start]:
                print_num(start)
                return (start, count)

            print_num(None)
            return (None, count)

        # Find the index of the item in the middle of the list.
        mid_point = (start + end) // 2

        # Have we succeeded?
        if n == list_of_numbers[mid_point]:
            print_num(mid_point)
            return (mid_point, count)

        print_num(mid_point)

        # Should we check the second half of the list?
        if n > list_of_numbers[mid_point]:
            return binary_find(mid_point + 1, end, count)

        # Check the first half of the list.
        return binary_find(start, mid_point, count)

    # Begin the search on the entire list.
    return binary_find(0, len(list_of_numbers), 0)

numbers

for n in [2, 4, 17, 30, 34, 50]:
    print(f"n = {n:>2}:", end=' ')
    result = find_number(n, numbers)
    print('\n', 9*' ', result)

from qiskit import QuantumCircuit
import math
import matplotlib

# Set up the options to draw the circuit
draw_kwargs = {
    "output": "mpl",         # use matplotlib
    "idle_wires": False,     # don't show unused wires

    "style": {
        "name": "bw",        # black-and-white for book
        "subfontsize": 9,    # font size of subscripts
        "dpi": 600           # image resolution
    }
}

circuit = QuantumCircuit(1)
circuit.z(0)

savefig_dpi = 600
histogram_color = "#82caaf"
file_name = "work/images-to-trim/w-22-iqx-oracle-01.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(1)
circuit.x(0)
circuit.z(0)
circuit.x(0)

file_name = "work/images-to-trim/w-22-iqx-oracle-02.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(2)
circuit.cz(0, 1)

file_name = "work/images-to-trim/w-22-iqx-oracle-06A.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(2)
circuit.h(1)
circuit.cx(0, 1)
circuit.h(1)
file_name = "work/images-to-trim/w-22-iqx-oracle-06B-gray.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi, facecolor="#efeeed")

circuit = QuantumCircuit(2)
circuit.cx(0, 1)
circuit.cz(0, 1)
circuit.cx(0, 1)

file_name = "work/images-to-trim/w-22-iqx-oracle-04A.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(2)
circuit.x(1)
circuit.cz(0, 1)
circuit.x(1)
file_name = "work/images-to-trim/w-22-iqx-oracle-04B-gray.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi, facecolor="#efeeed")

circuit = QuantumCircuit(2)
circuit.x(0)
circuit.cz(0, 1)
circuit.x(0)

file_name = "work/images-to-trim/w-22-iqx-oracle-05-gray.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi, facecolor="#efeeed")

circuit = QuantumCircuit(2)
circuit.x(0)
circuit.x(1)
circuit.cz(0, 1)
circuit.x(0)
circuit.x(1)

file_name = "work/images-to-trim/w-22-iqx-oracle-03.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(3)
circuit.h(2)
circuit.ccx(0, 1, 2)
circuit.h(2)

file_name = "work/images-to-trim/w-22-iqx-oracle-10.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit = QuantumCircuit(3)
for q in range(3): circuit.x(q)
circuit.h(2)
circuit.ccx(0, 1, 2)
circuit.h(2)
for q in range(3): circuit.x(q)

file_name = "work/images-to-trim/w-22-iqx-oracle-11.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

data = [3, 1, 2, 5]
mean = float(sum(data)) / len(data)
mean

def invert_about_the_mean(data):
    assert data
    mean = sum(data) / float(len(data))
    return [2.0 * mean - x for x in data]

invert_about_the_mean(data)

data = [0.5, -0.5, 0.5, 0.5]
invert_about_the_mean(data)

import math

amplitudes = [1.0/math.sqrt(8) for _ in range(8)]
amplitudes[0] = -amplitudes[0]

# Amplitude for |000>
amplitudes[0]

abs(amplitudes[0])**2

# Amplitude for |001>
amplitudes[1]

abs(amplitudes[1])**2

inverted_amplitudes = invert_about_the_mean(amplitudes)
inverted_amplitudes[0]

abs(inverted_amplitudes[0])**2

inverted_amplitudes[1]

abs(inverted_amplitudes[1])**2

amplitudes = inverted_amplitudes
amplitudes[0] = -amplitudes[0]
inverted_amplitudes = invert_about_the_mean(amplitudes)
inverted_amplitudes[0]

abs(inverted_amplitudes[0])**2

inverted_amplitudes[1]

abs(inverted_amplitudes[1])**2

# Set the drawing options
draw_kwargs = {
  "output": "mpl",         # use matplotlib
  "initial_state": True,   # show |0> and 0
  "idle_wires": False,     # don't show unused wires

  "style": {
      "name": "bw",        # black-and-white for book
      "subfontsize": 9,    # font size of subscripts
      "dpi": 600           # image resolution
  }
}

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.h(1)
circuit.barrier()

file_name = "work/images-to-trim/w-24-iqx-oracle-15A.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit.cz(0, 1)
circuit.barrier()

file_name = "work/images-to-trim/w-24-iqx-oracle-15B.jpg"
circuit.draw(**draw_kwargs).savefig(file_name, dpi=savefig_dpi)

circuit.h(0)
circuit.h(1)
circuit.x(0)
circuit.x(1)
circuit.id(0)
circuit.h(1)
circuit.cx(0, 1)
circuit.id(0)
circuit.h(1)
circuit.x(0)
circuit.x(1)
circuit.h(0)
circuit.h(1)

circuit.measure_all()

file_name = "work/images-to-trim/w-24-iqx-oracle-15C.jpg"
figure = circuit.draw(**draw_kwargs)
figure.text(0.342, 0.9, "oracle", fontsize=16,
            horizontalalignment='center',
            verticalalignment='center')
figure.text(0.58, 0.9, "inversion about the mean", fontsize=16,
            horizontalalignment='center',
            verticalalignment='center')
figure.text(0.84, 0.9, "measurement", fontsize=16,
            horizontalalignment='center',
            verticalalignment='center')
figure.savefig(file_name, dpi=savefig_dpi)

from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

simulator = Aer.get_backend("aer_simulator")

result = execute(circuit, simulator, shots=1000).result()
counts = result.get_counts(circuit)
counts

histogram_color = "#82caaf"

histogram = plot_histogram(counts, color=histogram_color,
                           title="Searching for |11>")

histogram.savefig("work/images-to-trim/w-24-iqx-oracle-15-histogram.jpg", dpi=savefig_dpi, bbox_inches="tight", pad_inches=0.1)

