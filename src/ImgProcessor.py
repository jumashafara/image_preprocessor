import numpy as np
import cv2
import pathlib


class ImgProcessor:
    """
    This simple class will help you convert your images folder into a numpy array.
    Sub-folders in the images directory will form the categories from which the target variable y.

    Paramters:
        images_dir: This is the string path to the directory that contains the subfolders with the images.
        classes: This is a list of names that will form the categories, these should preferably be identical to the sub-folder names.
        images_size = size of the images
        normalize: A boolean whether to normalize the values to lie between 0 and 1.

    Methods:
        images_object: This creates and returns two objects, the 'images_object' which contains each created class(category) with a list of images belonging to the class(category).
                       The categories(classes) are created from the sub-folders.
        get_Xy: This method returns two numpy arrays X(images array), and y(target). 
                These arrays are created from the images_object.
    """

    def __init__(self, images_dir=None, classes=[], image_size=(256, 256), normalize=False):
        self.images_dir = images_dir
        self.image_size = image_size
        self.classes = classes
        self.normalize = normalize

    def images_object(self):
        images_list = list(pathlib.Path(self.images_dir).glob("*"))

        images_object, class_labels = {}, {}

        print("Classifying and labelling classes...")

        for count, list_item in enumerate(images_list):
            images_object[f"{self.classes[count]}"] = list(list_item.glob("*"))
            class_labels[f"{self.classes[count]}"] = count

        print("Finished classifying and labeling classes")

        return images_object, class_labels

    def get_Xy(self):
        X, y = [], []

        images_object, class_labels = self.images_object()

        print("Creating numpy arrays from the images, this may take a while...")

        for image_name, images in images_object.items():
            for image in images:
                img = cv2.imread(str(image))
                resized_img = cv2.resize(img, self.image_size)
                X.append(resized_img)
                y.append(class_labels[image_name])

        print("Done creating numpy arrays from the images ")

        if self.normalize:

            print("Normalizing values to lie between 0 and 1 included..")
            X, y = np.array(X)/255, np.array(y)/255

            print("Finished normalizing.")

        else:
            X, y = np.array(X), np.array(y)

        print("Completed creating image datset ????")

        return X, y
