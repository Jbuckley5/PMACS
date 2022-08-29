# PMACS

## Description

Post Machine Algorithm Collaboration Software is an image manipulation software geared towards artists using machine learning algorithms to produce collaborative works with artificial intelligence. As an artist interested in using machine learning models to expand my creative endeavors, I've found that that some functions found in the OpenCV, NumPy, and MatPlotLib libraries can be used to quickly manipulate images in ways that are tailored towards outputs of AI collaborations. The lack of definition that results from style transfer in particular could prompt a desire to outline shapes in the composition, which can be accomplished using OpenCV's threshold segmentation and NumPy's array masking to isolate the in between pixels to be bolded. Color control can be difficult with theses models as well. MatPlotLib's colormaps give the user a dropdown menu with several options for the colorscheme of the image, as well as a second colormap for the outline that was added. Data visualization libraries are fantastic for the organization and display of data. This project demonstrates the effectiveness of using them to manipulate the representative array of an image, thus, manipulating the image.

## Access

This software can be accessed via http://PMACS.herokuapp.com 

## Usage

The first step of using PMACS is uploading an image to manipulate.  <img width="164" alt="image" src="https://user-images.githubusercontent.com/89647114/187094984-2650c02b-629d-4c6d-903b-06481adb0b33.png">


First click "Choose File". Select a file from the explorer, then click "Open". Click the submit button to confirm the choice. 

Making a selection on the "Outline Thickness" slider or either colormap dropdown menu will automatically display a new image that applies the changes that the user has made, allowing for comparison on the same screen as well as real time edits.

<p align="center">
  <img width="885" align="center" alt="image" src="https://user-images.githubusercontent.com/89647114/187095176-14e8379f-ff7f-4d05-b1d5-a4bbb7d2878d.png">
</p>


## Credits

Morgan Benton https://github.com/morphatic advised and collaborated on this project

Roy Tutorials https://roytuts.com/upload-and-display-image-using-python-flask/ 

Yağmur Çiğdem Aktaş https://yagmurcigdemaktas.medium.com/
https://towardsdatascience.com/image-segmentation-with-classical-computer-vision-based-approaches-80c75d6d995f
