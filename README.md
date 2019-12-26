# MichelAI

MichelAI, music video generator based on [BigGAN](https://github.com/ajbrock/BigGAN-PyTorch), created for Bend the Future first album and inspired by the works of [Mario Klingemann](http://quasimondo.com/) and [Mike Tyka](http://www.miketyka.com/).

### An example with our first single
[![](http://img.youtube.com/vi/IYK83KiojzA/0.jpg)](http://www.youtube.com/watch?v=IYK83KiojzA "Reaching For - Bend the Future")

# How it works

MichelAI comes in two ways :

 - [Windows exe](https://1drv.ms/u/s!AjwQADba1lMhyxw3wobgg5XetgSj?e=3Vyr0t)
 - Python program
 
 If you want to make the program run faster you might want to use the python code to run it on your GPU.
 
 In both cases to make it work, you have to insert a WAV file and an MP3 file of the same music in the input folder, and then start the program, you can then fiddle with the settings and start the generation, results will appear in the output folder.
 
 The first run might take longer since the program downloads the cache files of the BigGAN model. Once this step is done, the subsequent runs should work normally.

## Parameters

|                |Function                         
|----------------|-------------------------------|
|Music file name            |Both MP3 and WAV must have the same name   
|Width|Width at which the video will be resized, this doesn't affect quality
|Height|Height at which the video will be resized, this doesn't affect quality
|Use custom theme|Custom themes are textfiles using which you can include your selected images in the setup according to your preference, more info below
|LD/MD/HD|Define the resolution of the output image (128x128,256x256,512x512)
|Number of vids|When generating videos with a random theme, you might want to create more that one video and keep only the best one
|Sensibility|The reactivity control parameter of the images to the changing sounds
|Real frames|Number of frames/sec that are calculated directly by the sound, while the other frames are calculated by interpolation
|Randomize theme|Will flip randomly certain parts of the theme, you can set the number of flipped themes in Randomized themes
|Img buffer|Number of images stored in RAM before they get written on disk
|Frequency group|Makes a sum of a group of frequencies instead of using all of them
|Floor freq array|Starting point for the array of frequencies
|Z max|Set the maximum number for the Zvector
|FFT Decrease|Regulate how much the maxFFT will go down between frames


## Themes

Since MichelAI is using the BigGAN model that's already trained on imagenet, it binds categories of this dataset to some sound frequencies, which means you can choose what image will correspond to which frequency.

You can find the list of categories in the PDF linked with it, to created a custom theme you have to make a textfile with the 1000 categories in the order of your choice, put it in the input folder, and name it the same as you named the music files.

Each time a music clip is generated, the theme file used is also saved with the video meaning that you can reload the same theme for future projects.
