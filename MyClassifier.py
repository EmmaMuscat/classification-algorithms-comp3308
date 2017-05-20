import sys
import numpy
from lib.Instance import Instance
from lib.KNearestNeighbour import k_nearest_neighbour


def parse_input_file(filename):
    """
    parses input file and returns array of instances.
    :param filename: name of file to be parsed
    :return: array of instances
    """
    instances = []
    with open(filename, "r") as infile:
        for line in infile:
            attributes = line.split(',')
            # convert from str to float
            for i in range(8):
                attributes[i] = numpy.float(attributes[i])
            # If this is a testing set
            if len(attributes) == 8:
                instances.append(Instance(attributes[0],
                                          attributes[1],
                                          attributes[2],
                                          attributes[3],
                                          attributes[4],
                                          attributes[5],
                                          attributes[6],
                                          attributes[7]))
            # Otherwise it is a training set
            elif len(attributes) == 9:
                instances.append(Instance(attributes[0],
                                          attributes[1],
                                          attributes[2],
                                          attributes[3],
                                          attributes[4],
                                          attributes[5],
                                          attributes[6],
                                          attributes[7],
                                          class_variable=attributes[8].replace('\n', '')))
    return instances


if __name__ in '__main__':
    training_data = sys.argv[1]
    testing_data = sys.argv[2]
    algorithm = sys.argv[3]

    training_instances = parse_input_file(training_data)
    testing_instances = parse_input_file(testing_data)

    if algorithm == 'NB':
        # Do Naive Bayesian classification
        results = []
        pass
    else:
        k = int(algorithm.replace('NN', ''))
        # Do k-nearest neighbour classification
        results = k_nearest_neighbour(training_instances, testing_instances, k)
    for result in results:
        print(result)