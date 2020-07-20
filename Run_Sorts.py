# Import random for generating arrays
from random import randint

# Import Sorting Algorithms
import sorting

# Import texttable to create results table
import texttable

# Import matplotlib to create graph of data
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# Take in the lists of sorts, generate an array of length 'size' for each sort then time and record each
def time(size):
    import time
    result = [size]
    unsort = generate_array(size)

    array = unsort[:]
    t0 = time.clock()
    run_sort = sorting.bubble_sort(array)
    t1 = time.clock() - t0
    result.append(round(t1, 6))

    array = unsort[:]
    t0 = time.clock()
    run_sort = sorting.insertion_sort(array)
    t1 = time.clock() - t0
    result.append(round(t1, 6))

    array = unsort[:]
    t0 = time.clock()
    run_sort = sorting.selection_sort(array)
    t1 = time.clock() - t0
    result.append(round(t1, 6))

    array = unsort[:]
    t0 = time.clock()
    run_sort = sorting.merge_sort(array)
    t1 = time.clock() - t0
    result.append(round(t1, 6))

    array = unsort[:]
    t0 = time.clock()
    run_sort = sorting.shell_sort(array)
    t1 = time.clock() - t0
    result.append(round(t1, 6))

    array = unsort[:]
    t0 = time.clock()
    run_sort = sorting.quick_sort(array, 0, len(array))
    t1 = time.clock() - t0
    result.append(round(t1, 6))

    return result


# Generate an a random array of length 'size'
def generate_array(size):
    unsort = []
    while len(unsort) < 10 ** size:
        unsort.append(randint(1, 10 * size))
    return unsort


# Create a table to record times and quantities of each sort
results = []
for i in range(5):
    if 1 < i:
        results.append(time(i))


# Create table, add data and print table
tab = texttable.Texttable()
headings = ["Data Size (10 ** n)", "Bubble", "Insertion", "Selection", "Merge", "Shell", "Quick"]
tab.header(headings)
for result in results:
    tab.add_row(result)
s = tab.draw()
print(s)
print("* all time values have been rounded to 3 decimal places for table presentation\n"
      "* Exact values are shown in the chart")

# Chart Presentation of the Data
for result in results:
    objects = ("Bubble", "Insertion", "Selection", "Merge", "Shell", "Quick")
    y_pos = np.arange(len(objects))
    performance = result[1:]

    plt.bar(y_pos, performance, align='center', alpha=0.2)
    plt.xticks(y_pos, objects)
    plt.ylabel('Time')
    plt.title('Sorting Performance on Data Set 10 ** ' + str(result[0]))
    plt.show()
