import numpy


class Instance(object):
    def __init__(self, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, class_variable=None):
        self.attributes = numpy.array((a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8))
        self.class_variable = class_variable
        self.distance = None

    def set_distance(self, other_instance):
        # Return Euclidean distance between two instances.
        self.distance = numpy.sqrt(numpy.sum((self.attributes-other_instance.attributes)**2))
