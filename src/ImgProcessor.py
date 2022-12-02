import numpy as np
import cv2
import pathlib


class ImgProcessor:
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

            print("Completed creating image datset 🎉")

        else:
            X, y = np.array(X), np.array(y)

        return X, y
