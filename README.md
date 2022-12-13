# ImgProcessor

This simple class will help you convert your images folder into a numpy array.Sub-folders in the images directory will form the categories from which the target variable y.
    
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

## How to use
1. Initialize your image processor object as below

```
img_proc = ImgProcessor(images_dir = "path/to/image/directory", class= ["list", "of", "class", "names"], image_size = (256, 256), normalize= True)
```
2. Get your images numpy arrays by calling the get_Xy method on your processor object
```
X, y = img_proc.get_Xy()
```
3. You can obtain the numeric values corresponding to your class labels by calling the images_object method on your processor object
```
img_obj = img_proc.images_object()
```
