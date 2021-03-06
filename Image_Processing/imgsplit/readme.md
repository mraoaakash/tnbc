# Imgsplit
### Introduction
This piece of code serves as a part of the image pipleine used to prepare images for machine learning. The different functions of this script carry out varying image manipulation tasks in order to generate images with sufficient granularity. The use case of this code is specifically catering to the image processing of cancer biopsy images. 

The problem at hand for us was to build a pipeline that randomly selects an image from a repository and randomly samples a defined number of sub-images from it. Here, we have defined our level of granularity at 580\*580px in order to retain sufficient detail in the images. This value will wary depending on the stage of the study at which we are at as well as the type of image being used.

### Packages used
- imagecodecs
- tifffile
- cv2 (openCV)
- re
- os
- random


### Functions
#### imcrop(path,size)
This function takes a path and a size. Upon opening the image at the defined path, it splits the entire image length and breath wise into successive components. The image below illustrates the number of splits:

![imgrop-01](https://user-images.githubusercontent.com/69803820/170626312-e427bdbe-017e-4bd2-8c90-c5a4c318aa2b.png)


#### randcrop(path, filename, size, num)
This function is responsible to pick randomised chunks of a given image. The path of the image is fed in through the function signature and is opened using tifffile's imread function. Using a simple for loop we then cut out randomised size\*size sections of the image. We achieve randomization, or pseudo-randomization by using the randint function in the random package to generate random top-left coordinates for the chosen image. It then writes the generated with a custom name to a selected directory.

![randcrop-01](https://user-images.githubusercontent.com/69803820/170626293-67a985e7-0e25-4b7f-bdee-53e0304e1c38.png)


#### randpath()
This function is designed to chose a random file from given repository. It uses the OS package to access the repository and save the name of a random (pseudo-random) file. It then returns a tuple with a path to this file as well as the file name itself.


#### visit(n)
For the purposes of modularity, this function is designed to call the randpath n times and at each iteration call randcrop on the given filepath.

#### tiffimgs()
For this project, we are dealing with only .tif images. Keeping this in mind, it was necessary for us to be able to find the tif images from our entire directory with images spanning across multiple directories. THis function walks from the root our any given directory and checks if every single file is a .tif and generates a path if-and-only-if the given file is a tif. The path can further be passed on to randcrop(), imgcrop(), or any other function.

#### keyimgs(key)
Our project, at certain instances required the used of specific images, such as those of a slined stained with HnE, Vimentin, etc. This function takes a walk through the entire directory, from the root and checks if every single file is a .tif and contains the key as mentioend by the user. The function generates a path if-and-only-if the given file is a tif and the key is a substring of the filename. The path can further be passed on to randcrop(), imgcrop(), or any other function.

### Workflow
These functions are designed to serve as a part of the image processing pipeline where we first run visit on n images. This will generate approximately n\*500 cropped images. These images will then be fed into our desired model.

![Workflow-01](https://user-images.githubusercontent.com/69803820/170626198-3ffc714e-f5c6-49a7-83f5-af35fac55d2b.png)
