# MichelAI

MichelAI, music video generator based on [BigGAN](https://github.com/ajbrock/BigGAN-PyTorch), created for Bend the Future first album and inspired by Mario Klingemann and Mike Tyka works on art using AI

An example with our first single
[![](http://img.youtube.com/vi/IYK83KiojzA/0.jpg)](http://www.youtube.com/watch?v=IYK83KiojzA "Reaching For - Bend the Future")

# How it works

MichelAI comes in two ways

 - [Windows exe](https://1drv.ms/u/s!AjwQADba1lMhyxw3wobgg5XetgSj?e=3Vyr0t)
 - Python program
 
 If you want to make the program run faster you might want to use the python code to run it on your GPU
 
 In both cases to make it work, you have to insert a WAV file and an MP3 file of the same music in the input folder, and then start the program, you can then fiddle with the settings and start the generation, results will appear in the output folder

## Parameters

|                |Function                         
|----------------|-------------------------------|
|Music file name            |Both MP3 and WAV must be named the same   
|Width|Width at which the video will be resize, this doesn't affect quality 
|Height|Height at which the video will be resize, this doesn't affect quality 
|Use custom theme|Custom themes are textfiles that you can include to setup which image you want to appear, more info below
|LD/MD/HD|Define the resolution of the output image (128x128,256x256,512x512)
|Number of vids|When generating videos with a random theme, you might want to create more that one video and keep only the best one
|Sensibility|Manage the reactivity of the image to changing sounds
|Real frames|Number of frames/sec that a calculated directly by the sound, others frames will be calcultated by interpolation
|Randomize theme|Will flip randomly certain parts of the theme, you can set the number of flipped themes in Randomized themes
|Img buffer|Number of images stored in RAM before they get written on disk
|Frequency group|Makes a sum of a group of frequencies instead of using all of them
|Floor freq array|Starting point for the array of frequencies
|Z max|Set the maximum number for the Zvector
|Y max|Set the maximum number for the Yvector
|FFT Decrease|Regulate how much the maxFFT will go down between frames


## Themes

Since MichelAI is using the BigGAN model that's already trained on imagenet, it binds categories of this dataset to some sound frequencies, which means you can choose what image will correspond to which frequency

You can find the list of categories in the PDF linked with it, to created a custom theme you have to make a textfile with the 1000 categories in the order of your choice, put it in the input folder, and name it the same you named the music files

Each time a music clip is generated, the theme file used is also saved with the video, which mean you can reload the same theme for future projects
