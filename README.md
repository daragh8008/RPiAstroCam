# RPiAstroCam
A simple Camera App for cmdline astrophotography


I hope you find this script useful. Please bear in mind that this was written because I could not find a suitable tool to use the raspiberry pi hi-quality camera on a ssh connection for astrophotography. Maybe there is a better tool around now? 

Nice feature is that you only need to input numbers to set the various parameters of the camera. You can save a particular method to use again and again. Also you can set up a sequence of shots so you can stack and process later. Also very nice is that you can view single shot images using feh over a terminal, so no need to run a full x- enviornment. I run it all through a terminal.

See https://feh.finalrewind.org/ for details on feh and how cool it is. You will need to install feh on your pi. 'sudo apt-get install feh' should do the trick. When using Feh do not use 'sudo' to launch this script Just cd to the diretory where it is saved and type in: python3 astropicam.py


The script is designed to be used over a wifi connection to help set up the the pi HQ cam mounted on a telescope.But hey who am I to dictate. Use it for whatever the hell you want. Also you can set up a wifi hotspot on the pi and login directly from your computer. I used the excellent tutorial available at

https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/157-raspberry-pi-auto-wifi-hotspot-switch-internet

Super handy and well worth checking out.

This script bascially composes a command for the raspistill program by setting a whole bunch of variables and holding them until ready to take a photo Each variable is set by entering the desired number and hitting enter. After that, follow the options. Couple of things though, not all setting are compatible. Ie, you wouldn't use the autowhitebalance inconjunction with autowhitebalance gain or ISO or exposuremode with Analogue and digital gains together. Where it was clear in the raspistill
docs, I tried to implement lockouts. Ie turning one on, turns the other off.
    
Note to use all the functions you need to have installed a couple of things
            Raspistill - comes as standard")
            Feh - doesn't come as standard sudo apt-get install feh  <- I think
            PyDNG - available from https://github.com/schoolpost/PyDNG
python modules used:
                     time
                     glob
                     os
and of course python3 and a HQ cam (enabled in raspiconfig)

Loading images using FEH and the HQ camera takes a few moments...not too long but give it a chance and they should load if an image is open, you have to hit q and enter to close and continue.
    
00 is probably the most useful command as it will bring up the list of commands. But you have to be finished inputting your variables first
    
Processing Raws - what is it!
The high quality camera outputs the raw file appended to a jpeg. Thus to make it useable it must first be stripped away and made into its own file
This is what the pydng library is used for. This takes a few seconds if enabled. The intershot delay doesn't start counting untill all other processes are finished so you don't have to worry about it. But just bear in mind that it will increase the lenght of time taken to run though a sequence.
    
Saving and loading camera configurations
DON'T ENTER FILE PATHS OR EXTENSIONS
Just enter a name such as goodcamconfig. A folder called cameraconfigs if not in existance will be created in the same folder as the script and your setting will be saved there. Same holds true for laoding settings. The script will print a list of camconfig files just type in the one you want (no extension) ie goodcamconfig 
and then you should get confirmation that the load was sucessfull.

Note that the print current configuration will return what is actually being sentto raspistill. In particular note that the units are not the same as the interface. For example the shutter time will be in microseconds, and the timeout time mill be in milliseconds etc.

I haven't tested every aspect yet beyond, it seems to do what I want.. If strange things happen let me know and I'll take a looksee and see whats up. All testing was done on a pi zero w with HQ cam (raspbian 10 stretch). No reason to believe that it wouldn't work with other flavors. There are some raspistill functions I haven't used because I haven't had time, and they don't really interest me that much. Some others are there but it wasn't clear if they were for raspivid or raspistill. For example the antiflicker options. How would that work on a camera taking a still? Anyway play with them and report
back if you figure it out.

      **************   WARNING   **************      
I have absolutely no software trainning or idea how to program correctly

 You use this script  at your own risk.

But really if you are a software engineer and looking through this code in horror.
Remember you were a learner once too!

Happy snapping and if you get some good shots of anything I would love to see on twitter

Peace out
Twitter: @Daragh__Byrne
