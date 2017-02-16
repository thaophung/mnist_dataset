import os
import struct
import numpy as np
import scipy.misc
from PIL import Image
"""
Loosely inspired by http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py
which is GPL licensed.
"""

def read(dataset = "testing", path = "."):
    """
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
    """

    if dataset is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError, "dataset must be 'testing' or 'training'"

    # Load everything in some numpy arrays
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)

    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(len(lbl), rows, cols)

    get_img = lambda idx: (lbl[idx], img[idx])

    # Create an iterator which returns each image in turn
    for i in xrange(len(lbl)):
        yield get_img(i)

def show(image):
    """
    Render a given numpy.uint8 2D array of pixel data.
    """
    from matplotlib import pyplot
    import matplotlib as mpl
    fig = pyplot.figure()
    ax = fig.add_subplot(1,1,1)
    imgplot = ax.imshow(image, cmap=mpl.cm.Greys)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
    pyplot.show()

images = read()
images = list(images)
#image = images[0]
#print image
#make directory mnist_training_images
#training_folder=('./mnist_training_images')
testing_folder=('./mnist_testing_images')
#os.makedirs(training_folder)
os.makedirs(testing_folder)
#make folders for each label
for i in range (0,10):
    #class_folder = ('./mnist_training_images/' + str(i))
    class_folder=('./mnist_testing_images/' + str(i))
    os.makedirs(class_folder)

#create file train.txt and test.txt
#train_txt = open("train.txt", "w")
test_txt = open("test.txt","w")
for i in range(0,len(images)):
    image = images[i]
    label = image[0]
    image = image[1]
    im = Image.fromarray(image)
    #im.save('./mnist_training_images/'+str(label) +'/'+ str(i)+'.jpeg')  #save images in appropriate folders
    im.save('./mnist_testing_images/'+str(label) +'/'+ str(i)+'.jpeg')  #save images in appropriate folders
    #train_txt.write('mnist_training_images/'+str(label)+'/'+str(i)+'.jpeg' + ' ' + str(label) + '\n')
    test_txt.write('mnist_testing_images/'+str(label)+'/'+str(i)+'.jpeg' + ' ' + str(label) + '\n')
