# This statement is used for importing a csv module that is used for
# parsing tabular like data structure such as data in excel format,
# and these files are saved in .csv extension; this csv modules provide
# various classes for reading and writing data to CSV files.
import csv

import matplotlib.pyplot as plt
import numpy as np


def plot_data(csv_file_path):
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            results.append(row)

        # results = np.stack(results)

        # We need to convert the data we read from the file into a float data type
        results = np.stack(results).astype(np.float32)

    # plt.plot(results[:, 1], results[:, 0])

    # The Precision column is displayed on the x-axis and the Recall column is displayed on the y-axis.
    # That's why we have to change the order.
    plt.plot(results[:, 0], results[:, 1])

    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])

    # plt.xlabel('Recall')
    plt.xlabel('Precision')

    # plt.ylabel('Precision')
    plt.ylabel('Recall')

    plt.show()


f = open("data_file.csv", "w", newline='')
w = csv.writer(f)
_ = w.writerow(["precision", "recall"])
w.writerows([[0.013, 0.951],
             [0.376, 0.851],
             [0.441, 0.839],
             [0.570, 0.758],
             [0.635, 0.674],
             [0.721, 0.604],
             [0.837, 0.531],
             [0.860, 0.453],
             [0.962, 0.348],
             [0.982, 0.273],
             [1.0, 0.0]])
f.close()
plot_data('data_file.csv')
