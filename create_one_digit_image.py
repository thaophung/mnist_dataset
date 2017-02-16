from PIL import Image
from PIL import ImageDraw
import os

#path = './mnist_training_images/'
path = './mnist_testing_images/'
#new_path = './84x28_training_images'
new_path = './84x28_testing_images'

os.makedirs(new_path)

#new_train_txt = open("new_train.txt","w")
new_test_txt = open("new_test.txt","w")
def create_image(image):
    size = (84, 28)
    canvas = Image.new("RGB", size, (0,0,0))
    #draw_canvas = ImageDraw.Draw(canvas)
    #canvas.save('image1.jpeg')

    #Add imagei
    #original_image = Image.open('image1.jpeg')
    image_added = Image.open(image)
    #canvas = canvas.crop((0,0,28,28))
    canvas.paste(image_added, (0,0))
    canvas.save(image)

for i in range(0,10):
    #path = './mnist_training_images/'+str(i)+'/'
    path = './mnist_testing_images/' + str(i)+'/'
    label = str(i)
    label_folder = new_path+'/'+str(i)
    os.makedirs(label_folder)
    #print i
    for fn in os.listdir(path):
        #print fn
        size = (84, 28)
        canvas = Image.new("RGB", size, (0,0,0))
        image_name = fn
        #print fn
        image_added = Image.open(path+'/'+fn)
        canvas.paste(image_added, (0,0))
        canvas.save(label_folder + '/' + image_name)
        #new_train_txt.write('84x28_training_images/'+label+'/'+image_name+' '+label+'\n')
        new_test_txt.write('84x28_testing_images/'+label+'/'+image_name+' '+ label + '\n')


