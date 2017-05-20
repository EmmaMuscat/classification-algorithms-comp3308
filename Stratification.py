import sys
import numpy
from lib.Instance import Instance


def parse_input_file(filename):
    yes_instances = []
    no_instances = []
    with open(filename, "r") as infile:
        for line in infile:
            attributes = line.split(',')
            instance = Instance(attributes[0],
                                attributes[1],
                                attributes[2],
                                attributes[3],
                                attributes[4],
                                attributes[5],
                                attributes[6],
                                attributes[7],
                                class_variable=attributes[8].replace('\n', ''))
            if instance.class_variable == 'yes':
                yes_instances.append(instance)
            else:
                no_instances.append(instance)
    return yes_instances, no_instances


def write_output_file(yes_instances, no_instances):
    folds = dict()
    for i in range(10):
        folds[i] = []
    i = 0
    while len(yes_instances) > 0:
        folds[i % 10].append(yes_instances.pop())
        i += 1
    while len(no_instances) > 0:
        folds[i % 10].append(no_instances.pop())
        i += 1
    with open('pima-folds.csv', 'w') as outfile:
        count = 0
        for fold in folds:
            count += 1
            outfile.write('fold{}\n'.format(count))
            for instance in folds[fold]:
                outfile.write(convert_instance_to_string(instance))
            if count < 10:
                outfile.write('\n')


def convert_instance_to_string(instance):
    string = ",".join(instance.attributes)
    string = '{0},{1}\n'.format(string, instance.class_variable)
    return string


if __name__ in '__main__':
    input_file = sys.argv[1]
    yes, no = parse_input_file(input_file)

    write_output_file(yes, no)
