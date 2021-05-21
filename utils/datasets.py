from scipy.io import loadmat
from random import shuffle

def get_labels(dataset_name):
    if dataset_name == 'fer2013':
        return {0:'angry',1:'disgust',2:'fear',3:'happy',
                4:'sad',5:'surprise',6:'neutral'}

    else:
        raise Exception('Invalid dataset name')







