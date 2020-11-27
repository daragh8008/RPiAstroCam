#!/usr/bin/python
#################################################################
### Author: Daragh Byrne                                      ###
### Version 1.0		                                          ###
### Title: Ascafclap                                          ###
###  A simple Camera App for cmdline astrophotography	      ###
#################################################################


##### Import library components ######
from time import sleep
import glob
import os
from pydng.core import RPICAM2DNG

######################################


class cameraproperties:
    Quit = True
    viewlastimage = True
    lastimage = str("")
#Raspberry pi camera command line settings

#--preview turns on priewiew command -p
# wont' be using preview

#--fullscreen turns on full screen mode -f
# Won't be using full screen

#--nopreview do not display a preview -n
    preview = False
    previewcmd = str("-n ")

#--opacity sets opacity of preview window range 0-255 command -op
# Won't be using opacity

#--sharpness range -100 to 100 command -sh default 0
    sharpness = 0
    sharpnessmax = 100
    sharpnessmin = -100
    sharpnessunit = str("na")
    sharpnesscmd = str("-sh 0 ")

#--contrast  range -100 to 100 command -co default 0
    contrast = 0
    contrastmax = 100
    contrastmin = -100
    contrastunit = str("na")
    contrastcmd = str("-co 0 ")

#--brightness  range 0 to 100 command -br default 50
    brightness = 50
    brightnessmax = 100
    brightnessmin = 0
    brightnessunit = str("na")
    brightnesscmd = str("-br 50 ")

#--saturation  range -100 to 100 command -sa default 0
    saturation = 0
    saturationmax = 100
    saturationmin = -100
    saturationunit = ("na")
    saturationcmd = str("-sa 0 ")

#--ISO range range 100 to 800 command -ISO
    iso = 100
    isomax = 800
    isomin = 100
    isounit = str("na")
    isocmd = str("-ISO 100 ")

#--vstab turns on video stabilisation command -vs (video mode)
# won't be using vstab

#--ev sets ev compensation range -10 to 10 command -ev (video mode)
# won't be using ev

#--exposure sets exposure mode command -ex
# exposure modes available :

    exposuremode = ("")
    exposuremodeunit = str("na")
    exposuremodecmd = str("")

#--flicker anti flicker mode command -fli

    antiflicker = str("off")
    antiflickerunit =str("na")
    antiflickercmd = str("-fli off ")

#--awb sets auto white balance command -awb

    autowhitebalance = ("auto")
    autowhitebalanceunit = ("na")
    autowhitebalancecmd = str("-awb auto ")
    autowhitebalancestatus = True

#--awbg autowhitebalance gain when awb is off range 0-8 command awbg 1,2

    awbg = ("1.1,1.2")
    awbgmax = 8
    awbgmin = 0
    awbgunit = str("na")
    awbgstatus = False
    awbgcmd = str("-awbg 1.1,1.2 ")

#--imxfx sets image effects command -ifx
# image effects options are
#Set an effect to be applied to the image:

#     none: no effect (default)
#     negative: invert the image colours
#     solarise: solarise the image
#     posterise: posterise the image
#     whiteboard: whiteboard effect
#     blackboard: blackboard effect
#     sketch: sketch effect
#     denoise: denoise the image
#     emboss: emboss the image
#     oilpaint: oil paint effect
#     hatch: hatch sketch effect
#     gpen: graphite sketch effect
#     pastel: pastel effect
#     watercolour: watercolour effect
#     film: film grain effect
#     blur: blur the image
#     saturation: colour saturate the image

    imageeffect = ("none")
    imageeffectunit = str("na")
    imageeffectcmd = str("-ifx none ")

#--colfx sets color effects command -cfx <U:V>

#--metering, sets metering mode command -mm

    meteringmode = ("average")
    meteringmodeunit = ("na")
    meteringmodecmd = str("-mm average ")


#--rotation sets rotation (only supports 90 incriments but will take any value) command -rot
    rotation = 0
    rotationunit = str("degrees")
    rotationcmd = str("-rot 0 ")


#--hflip horizontal flip command -hf
# do this in port processing

#--vflip verticle flip command -vf
#do this in post processing

#--roi region of interest command -roi
# Allows the specification of the area of the sensor to be used as the source for the preview
#and capture. This is defined as x,y for the top-left corner, and a width and height, with all
#values in normalised coordinates (0.0 - 1.0). So, to set a ROI at halfway across and down the
#sensor, and a width and height of a quarter of the sensor, use:
#-roi 0.5,0.5,0.25,0.25
#Might do this

#--shutter sets shutter speed/time range for HQ cam 200000000 (microseconds ie 200s) command -ss
    shutterspeed = 100000
    shutterspeedmax = 200000000
    shutterspeedmin = 50
    shutterspeedunit = str("microseconds")
    shutterspeedcmd = str("-ss 100000 ")

#--drc dynamic range compression command -drc

    dynamicrange = ("off")
    dynamicrangeunit = str("na")
    dynamicrangecmd = str("-drc off ")

#raspistill specific commands
#--width set an image width range 4056 command -w
    imgwidth = 4056
    imgwidthmin = 200
    imgwidthmax = 4056
    imgdimensionunit = str("pixels")
    imgwidthcmd = str("-w 4056 ")

#--height set image height range 3040 command -h
    imgheight = 3040
    imgheightmin = 200
    imgheightmax = 3040
    imgheightunit = str("pixels")
    imgheightcmd = str("-h 3040 ")

#--quality set jpeg image compression range 0-100 command -q
#--raw adds raw bayer data to jpeg data command -raw
    quality = 80
    qualitymin = 0
    qualitymax = 100
    qualityunit = ("%")
    qualitycmd = str("-q 80 ")
    qualitystatus = True
    rawstatus = False
    processraws = False
    rawcmd = str("-r ")


    
#--output sets output to file name command -o
#--timeout time before camera takes picture and shuts down command -t
# with out specification this is 5 seconds (-t 5000)
    timeout = 5000
    timeoutmin = 500
    timeoutmax = 10000000
    timeoutunit = str("milliseconds")
    timeoutcmd = str("-t 5000 ")

#--timelapse time lapse command -tl
# used in conjunction with time out to set duration see raspistill docs for details
# not sure I'll use this may just cycle the capture command for set number of loops
# some thought required!

#--burst prevents camera returning tto preview mode between captures command -bm
    burstmode = False
    burstmodecmd = str("")

#digital and analogue gains command -ag and -dg
    Again = float(1)
    Dgain = float(1)
    AandDgains = False
    AandDgainscmd = str("")

#set camera mode command -md Options 1-4
    cameramode = 3
    cameramodecmd = str("-md 3 ")

#sequence settings
    sequencenumber = 10
    sequencenumbermin = 1
    sequencenumbermax = 1000
    sequencenumberunits = str("shots")
    sequencestartdelay = int(0)
    sequenceshotdelay = int(0)

    filename = "test"
    filetype = ".jpg"

def Quitnow():
    cameraproperties.Quit = False

def Quitnowpowerdown():
    cameraproperties.Quit = False
    os.system("sudo shutdown now")
    
def printoptions():
    print(" Select which parameter or action you wish to take")
    print("00)   View this list again")
    print(" 1)   Set Exposure time                   2)    Set timeout ")
    print(" 3)   Set image rotation                  4)    Meteringmode     ")
    print(" 5)   Autowhitebalance                    6)    Autowhitebalance gain ")
    print(" 7)   ISO                                 8)    Exposure mode ")
    print(" 9)   Brightness                         10)    Contrast ")
    print("11)   Sharpness                          12)    Antiflicker ")
    print("13)   Burstmode                          14)    Prieview on/off (HDMI output)")
    print("15)   Set Image dimensions               16)    Turn dynamic range compression on/off")
    print("17)   Set Analoge and digital gains      18)    Set Camera mode ")
    print("19)   Setup capture sequence             20)    Set Region of interest TODO")
    print("21)   File type                          22)    Camera setting summary ")
    print("23)   Save current settings              24)    Capture test Image")    
    print("25)   Process Raws during run            26)    Capture sequence ")
    print("27)   Load camera setting from file      28)    Disable View image after shot ")
    print("29)   Load last capture                  30)    Help")
    print("99)   QUIT without powerdown             91)    QUIT with powderdown ")
    print("101)  Readme or not your call")


def checkinputisnumber(a):
    num = a
    try:
        val = int(num)
        return True
    except ValueError:
        try:
            float(num)

            return True
        except ValueError:
            print("This is not a number. Next time try using a realy number")
            return False
    
def checknumber(a,b,c,d):
    if type(a) == int:
        anum = int(a)
        astr = anum
        astr = str(astr)
        
        bnum = int(b)
        bstr = bnum
        bstr = str(bstr)
        
        cnum=int(c)
        cstr = cnum
        cstr = str(cstr)
        
        if anum>bnum or anum<cnum:
            print("value is out of range")
            print("the range for this variable is min " + cstr + " " + "max " + bstr + " Units: " + d)
            return False
        else:
            print("parameter is in range")
            return True
    else:
        print("we were really looking for a number here")
        return False


def setexposure():
    shutterspeed1 = cameraproperties.shutterspeed/1000000
    print("current shutter speed = " + str(shutterspeed1) + " seconds")
    print("enter new shutter speed in seconds ")
    shutterspeedvar = input()
    if checkinputisnumber(shutterspeedvar):
        shutterspeedvar = float(shutterspeedvar)
        shutterspeedvar = shutterspeedvar*1000000
        shutterspeedvar = int(shutterspeedvar)
    else:
        print("Not a vaild option and my coffee is going cold")

    if checknumber(shutterspeedvar,cameraproperties.shutterspeedmax,cameraproperties.shutterspeedmin,cameraproperties.shutterspeedunit):
        cameraproperties.shutterspeed = shutterspeedvar
        shutterspeed1 = cameraproperties.shutterspeed
        cameraproperties.shutterspeedcmd = str("-ss " + str(shutterspeed1) + " ")
        shutterspeed1 = shutterspeedvar/1000000
        print("new shutter speed set to = " + str(shutterspeed1) + " seconds") 
    else:
        pass
        
        
def settimeout():
    print(type(cameraproperties.timeout))
    timeout1 = cameraproperties.timeout/1000
    print("current timeout = " + str(timeout1) + " seconds")
    print("enter new shutter speed in seconds ")
    timeoutvar = input()
    if checkinputisnumber(timeoutvar):
        timeoutvar = int(timeoutvar)
        timeoutvar = timeoutvar*1000
    else:
        print("I really hate to say it but ya know...not a vaild option")

    if checknumber(timeoutvar,cameraproperties.timeoutmax,cameraproperties.timeoutmin,cameraproperties.timeoutunit):
        cameraproperties.timeout = timeoutvar
        timeout1 = timeoutvar
        cameraproperties.timeoutcmd = str("-t " + str(timeout1) + " ")
        timeout1 = timeoutvar/1000
        print("new timeout set to = " + str(timeout1) + " seconds") 
    else:
        pass

def setrotation():
    rotation1 = cameraproperties.rotation
    rotation1 = str(rotation1)
    
    print("Current image rotation = " + rotation1)
    print("Select new rotation:")
    print("                     1 = 0 degrees ")
    print("                     2 = 90 degrees")
    print("                     3 = 180 degrees")
    print("                     4 = 270 degrees")
    print("Enter value:")
    userinput = input()
    if checkinputisnumber(userinput):
        userinput = int(userinput)    
        if userinput == int(1):
            cameraproperties.rotation = 0
        if userinput == int(2):
            cameraproperties.rotation = 90
        if userinput == int(3):
            cameraproperties.rotation = 180
        if userinput == int(4):
            cameraproperties.rotation = 270 
    else:
        print("not a valid option")
    rotation1 = cameraproperties.rotation
    rotation1 = str(rotation1)
    cameraproperties.rotationcmd = str("-ro " + rotation1 + " ")  
    print("Image rotation set to = " + rotation1)

def setmeteringmode():
    meteringmod1 = ("average")
    meteringmod2 = ("spot")
    meteringmod3 = ("backlit")
    meteringmod4 = ("matrix")

    meteringmode1 = cameraproperties.meteringmode
    meteringmode1 = str(meteringmode1)
    
    print("Current metering mode = " + meteringmode1)
    print("Select new metering mode:")
    print("                     1 = " + meteringmod1)
    print("                     2 = " + meteringmod2)
    print("                     3 = " + meteringmod3)
    print("                     4 = " + meteringmod4)
    print("Enter value:")
    meteringmodevar = input()
    if checkinputisnumber(meteringmodevar):
        meteringmodevar = int(meteringmodevar)
        if meteringmodevar == int(1):
            cameraproperties.meteringmode = meteringmod1
        if meteringmodevar == int(2):
            cameraproperties.meteringmode = meteringmod2
        if meteringmodevar == int(3):
            cameraproperties.meteringmode = meteringmod3
        if meteringmodevar == int(4):
            cameraproperties.meteringmode = meteringmod4
    else:
        print("not a valid option Who me?")
        print("There is no one else here!")
    meteringmode1 = cameraproperties.meteringmode
    meteringmode1 = str(meteringmode1)
    cameraproperties.meteringmodecmd = str("-mm " + meteringmode1 + " ")
    print("Metering mode set to = " + meteringmode1)

def setautowhitebalance():
    autowb1 = str("auto")
    autowb2 = str("sun")
    autowb3 = str("cloud")
    autowb4 = str("shade")
    autowb5 = str("tungsten")
    autowb6 = str("fluorescent")
    autowb7 = str("incandescent")
    autowb8 = str("flash")
    autowb9 = str("horizon")
    autowb10 = str("greyworld")
    autowb11 = str("off")
    
    if cameraproperties.awbgstatus==True:
        print("The manual auto white balance gains are currently active")
        print(" Do you want to turn these off: Y/N")
        awbgstatuschangerequest = input()
        awbgstatuschangerequest = str(awbgstatuschangerequest)
        awbgresponsevar1 = str("y")
        awbgresponsevar2 = str("Y")
        if awbgstatuschangerequest==awbgresponsevar1 or awbgstatuschangerequest==awbgresponsevar2:
            cameraproperties.awbgstatus = False
        else:
            print("The manual gains are still active")
            print("changing the auto white balance here won't have any effect")
    

    autowhitebalance1 = cameraproperties.autowhitebalance
    autowhitebalance1 = str(autowhitebalance1)
    
    print("Current Autowhitebalance mode = " + autowhitebalance1)
    print("Select new Autowhitebalance mode:")
    print("                     1 = " + autowb1)
    print("                     2 = " + autowb2)
    print("                     3 = " + autowb3)
    print("                     4 = " + autowb4)
    print("                     5 = " + autowb5)
    print("                     6 = " + autowb6)
    print("                     7 = " + autowb7)
    print("                     8 = " + autowb8)
    print("                     9 = " + autowb9)
    print("                     10 = " + autowb10)
    print("                     11 = " + autowb11)
    print("Enter value:")
    autowhitebalancevar = input()
    if checkinputisnumber(autowhitebalancevar):
        autowhitebalancevar = int(autowhitebalancevar)
        if autowhitebalancevar == int(1):
            cameraproperties.autowhitebalance = autowb1
        if autowhitebalancevar == int(2):
            cameraproperties.autowhitebalance = autowb2
        if autowhitebalancevar == int(3):
            cameraproperties.autowhitebalance = autowb3
        if autowhitebalancevar == int(4):
            cameraproperties.autowhitebalance = autowb4
        if autowhitebalancevar == int(5):
            cameraproperties.autowhitebalance = autowb5
        if autowhitebalancevar == int(6):
            cameraproperties.autowhitebalance = autowb6
        if autowhitebalancevar == int(7):
            cameraproperties.autowhitebalance = autowb7
        if autowhitebalancevar == int(8):
            cameraproperties.autowhitebalance = autowb8
        if autowhitebalancevar == int(9):
            cameraproperties.autowhitebalance = autowb9
        if autowhitebalancevar == int(10):
            cameraproperties.autowhitebalance = autowb10
        if autowhitebalancevar == int(11):
            cameraproperties.autowhitebalance = autowb11    
    else:
        print("not a valid option")
    autowhitebalance1 = cameraproperties.autowhitebalance
    autowhitebalance1 = str(autowhitebalance1)
    cameraproperties.autowhitebalancecmd = str("-awb " + autowhitebalance1 + " ")
    print("Autowhite balance mode set to = " + autowhitebalance1)
    
def setautowhitebalancegain():

    print("This requires the auto white balance to be turned off")
    print(" Turn it off? Y/N")
    turnoffawb = input()
    turnoffawb = str(turnoffawb)
    responsevar1 =str("y")
    responsevar2 =str("Y")
    
    if turnoffawb==responsevar1 or turnoffawb==responsevar2:
        cameraproperties.autowhitebalancecmd = str("-awb off")
        cameraproperties.autowhitebalance = str("off")
        print("Auto white balnce turned off")
        print("Manualy enter Red and Blue gains between value between 0 and 12")
#Future work pipe current values from raspistill and print here
        print("Please enter Red gain:")
    
        Rgainvar = input()
#        Rgainvar = float(Rgainvar)
        if checkinputisnumber(Rgainvar):
            Rgainvar = float(Rgainvar)
            if Rgainvar>float(12):
                Rgainvar = 1
            if Rgainvar<float(0):
                Rgainvar = 1
        
        else:
            print("Not in range Red gain will be set to one")
        print("Please enter Blue gain:")
    
        Bgainvar = input()
#        Bgainvar = float(Bgainvar)
        if checkinputisnumber(Bgainvar):
            Bgainvar = float(Bgainvar)
            if Bgainvar>float(12):
                Bgainvar = 1
            if Bgainvar<float(0):
                Bgainvar = 1
        else:
            print("Not in range Blue gain will be set to one")
        cameraproperties.awbg =str(str(Rgainvar) + "," +str(Bgainvar))
        cameraproperties.awbgcmd = str("-awbg " + cameraproperties.awbg + " ")
        cameraproperties.awbgstatus = True
        print("Gains set to (R,B): " + cameraproperties.awbg)
    else:
        print("Auto white balance gain remains on")
        
#def setisoasnumber():
    
#    iso1 = cameraproperties.iso
#    print("current iso setting = " + str(iso1) )
#    print("enter new iso value in range 100 to 800")
#    isovar = input()
#    if checkinputisnumber(isovar):
#        isovar = int(isovar)
#    else:
#        print("Computer says nooooo... not a vaild option")

#    if checknumber(isovar,cameraproperties.isomax,cameraproperties.isomin,cameraproperties.isounit):
#        cameraproperties.iso = isovar
#        iso1 = cameraproperties.iso
#        cameraproperties.isocmd = ("-ISO " + str(iso1) + " ")
#        print("new ISO set to = " + iso1) 
#    else:
#        pass

def setisoselection():
    if cameraproperties.AandDgains:
        print("Manual analogue and digital gains are active")
        print("Exposure mode not useable")
        print(" Turn of manual gain in option 17 to use ISO and exposure mode")
    else:
        iso1 = cameraproperties.iso
        iso1 = str(iso1)
    
        print("Current ISO setting = " + iso1)
        print("Select new ISO value:")
        print("                     1 = 100 ")
        print("                     2 = 200 ")
        print("                     3 = 300 ")
        print("                     4 = 400 ")
        print("                     5 = 500 ")
        print("                     6 = 600 ")
        print("                     7 = 700 ")
        print("                     8 = 800 ")
    
        print("Enter value:")
        isoselectionvar = input()
        if checkinputisnumber(isoselectionvar):
            isoselectionvar = int(isoselectionvar)
            if isoselectionvar == int(1):
                cameraproperties.iso = 100
            if isoselectionvar == int(2):
                cameraproperties.iso = 200
            if isoselectionvar == int(3):
                cameraproperties.iso = 300
            if isoselectionvar == int(4):
                cameraproperties.iso = 400
            if isoselectionvar == int(5):
                cameraproperties.iso = 500
            if isoselectionvar == int(6):
                cameraproperties.iso = 600
            if isoselectionvar == int(7):
                cameraproperties.iso = 700
            if isoselectionvar == int(8):
                cameraproperties.iso = 800
        else:
            print("not a valid option")
        iso1 = cameraproperties.iso
        iso1 = str(iso1)
        cameraproperties.isocmd = ("-ISO " + iso1 + " ")
        print("Camera ISO set to = " + iso1)

def setexposuremode():
    if cameraproperties.AandDgains:
        print("Manual analogue and digital gains are active")
        print("Exposure mode not useable")
        print(" Turn of manual gain in option 17 to use ISO and exposure mode")
    else:
        exposuremode1 = cameraproperties.exposuremode
        exposuremode1 = str(exposuremode1)
    
    
        print("Current Exposure mode setting = " + exposuremode1)
        print("Select new Exposure mode value:")
        print("                     1 = auto ")
        print("                     2 = night ")
        print("                     3 = backlight ")
        print("                     4 = spotlight ")
        print("                     5 = sports ")
        print("                     6 = snow ")
        print("                     7 = beach ")
        print("                     8 = very long exposure ")
        print("                     9 = fixed frames per second ")
        print("                     10 = antishake ")
        print("                     11 = fireworks ")
        print("                     12 = off ")
        print("                     13 = blank ")
    
        print("Enter value:")
        exposuremodevar = input()
        if checkinputisnumber(exposuremodevar):
            exposuremodevar = int(exposuremodevar)
            if exposuremodevar == int(1):
                cameraproperties.exposuremode = str("auto")
            if exposuremodevar == int(2):
                cameraproperties.exposuremode = str("night")
            if exposuremodevar == int(3):
                cameraproperties.exposuremode = str("backlight")
            if exposuremodevar == int(4):
                cameraproperties.exposuremode = str("spotlight")
            if exposuremodevar == int(5):
                cameraproperties.exposuremode = str("sports")
            if exposuremodevar == int(6):
                cameraproperties.exposuremode = str("snow")
            if exposuremodevar == int(7):
                cameraproperties.exposuremode = str("beach")
            if exposuremodevar == int(8):
                cameraproperties.exposuremode = str("verylong")
            if exposuremodevar == int(9):
                cameraproperties.exposuremode = str("fixedfps")
            if exposuremodevar == int(10):
                cameraproperties.exposuremode = str("antishake")
            if exposuremodevar == int(11):
                cameraproperties.exposuremode = str("fireworks")
            if exposuremodevar == int(12):
                cameraproperties.exposuremode = str("off")
            if exposuremodevar == int(13):
                cameraproperties.exposuremode == str("blank")
        else:
            print("Does not compute... not a valid option")
        exposuremode1 = cameraproperties.exposuremode
        exposuremode1 = str(exposuremode1)
        cameraproperties.exposuremodecmd = ("-ex " + exposuremode1 + " ")
        print("Camera exposure mode set to = " + exposuremode1)
            
    
def setbrightness():

    brightness1 = cameraproperties.brightness
    print("current brightness = " + str(brightness1) )
    print("enter new brightness value between 0 and 100 ")
    brightnessvar = input()
    if checkinputisnumber(brightnessvar):
        brightnessvar = int(brightnessvar)
    else:
        print("This is not quite right... not a vaild option")

    if checknumber(brightnessvar,cameraproperties.brightnessmax,cameraproperties.brightnessmin,cameraproperties.brightnessunit):
        cameraproperties.brightness = brightnessvar
        brightness1 = cameraproperties.brightness
        cameraproperties.brightnesscmd = str("-br " + str(brightness1) + " ")
        print("new brightness set to = " + str(brightness1)) 
    else:
        pass

def setcontrast():

    contrast1 = cameraproperties.contrast
    print("current contrast = " + str(contrast1) )
    print("enter new contrast value between -100 and 100 ")
    contrastvar = input()
    if checkinputisnumber(contrastvar):
        contrastvar = int(contrastvar)
    else:
        print("Oh come on... not a vaild option")

    if checknumber(contrastvar,cameraproperties.contrastmax,cameraproperties.contrastmin,cameraproperties.contrastunit):
        cameraproperties.contrast = contrastvar
        contrast1 = cameraproperties.contrast
        cameraproperties.contrastcmd = str("-co " + str(contrast1) + " ")
        print("new contrast set to = " + str(contrast1)) 
    else:
        pass

def setsharpness():

    sharpness1 = cameraproperties.sharpness
    print("current shaprness = " + str(sharpness1) )
    print("enter new sharpness value between -100 and 100 ")
    sharpnessvar = input()
    if checkinputisnumber(sharpnessvar):
        sharpnessvar = int(sharpnessvar)
    else:
        print("Really!! Not a vaild option")

    if checknumber(sharpnessvar,cameraproperties.sharpnessmax,cameraproperties.sharpnessmin,cameraproperties.sharpnessunit):
        cameraproperties.sharpness = sharpnessvar
        sharpness1 = cameraproperties.sharpness
        cameraproperties.sharpnesscmd = str("-co " + str(sharpness1) + " ")
        print("new contrast set to = " + str(sharpness1)) 
    else:
        pass
def setantiflicker():

    antiflicker1 = cameraproperties.antiflicker
    antiflicker1 = str(antiflicker1)
    
    print("Current Antiflicker mode setting = " + antiflicker1)
    print("Select new antiflicker mode value:")
    print("                     1 = off ")
    print("                     2 = auto ")
    print("                     3 = 50 Hz ")
    print("                     4 = 60 Hz ")
    print("Enter value:")

    antiflickervar = input()
    if checkinputisnumber(antiflickervar):
        antiflickervar = int(antiflickervar)
        if antiflickervar == int(1):
            cameraproperties.antiflicker = str("off")
        elif antiflickervar == int(2):
            cameraproperties.antiflicker = str("auto")
        elif antiflickervar == int(3):
            cameraproperties.antiflicker = str("50hz")
        elif antiflickervar == int(4):
            cameraproperties.antiflicker = str("60hz")
        else:
            print("are these my feet... invalid option")
            
        antiflicker1 = cameraproperties.antiflicker
        antiflicker1 = str(antiflicker1)
        cameraproperties.antiflickercmd = ("-fli " + antiflicker1 + " ")
        print("Camera antiflicker mode set to = " + antiflicker1)
    else:
        print("FFS! not a valid option")
    
def setburstmode():
     
    if cameraproperties.burstmode:
        print("burst mode is active: Enter 1 to keep active or enter 0 to turn off")
    else:
        print("burst mode is inactive: Enter 1 to Turn on or enter 0 to keep inactive")
    burstmodevar = input()
    
    if checkinputisnumber(burstmodevar):
        burstmode1 = burstmodevar
        burstmode1 = int(burstmode1)
        if burstmode1==int(0):
            cameraproperties.burstmode = False
            cameraproperties.burstmodecmd = str(" ")
            print("Burstmode inactive")
        elif burstmode1==int(1):
            cameraproperties.burstmode = True
            cameraproperties.burstmodecmd = str("-bm ")
            print("Burstmode active")
        else:
            print("Invalid option ..how did you even get here ")
    else:
        print(" so here we are again... Invaild option")
            
def setpreview():
    
    print("The preview image is dumped on the HDMI output of the pi.")
    print("Unless hooked up to a screen I'd leave it off")
    print("Since this a cmdline program to use on a ssh")
    print("If you are using a screen, why not use the way better PiCameraApp")
    print("And help them impliment the timelapse feature")
    print("               Just sayin' like")
    print("         It would be real cool if you did")
     
    if cameraproperties.preview:
        print("preview mode is active: Enter 1 to keep active or enter 0 to turn off")
    else:
        print("preview mode is inactive: Enter 1 to Turn on or enter 0 to keep inactive")
    previewvar = input()
    
    if checkinputisnumber(previewvar):
        preview1 = previewvar
        preview1 = int(preview1)
        if preview1==int(0):
            cameraproperties.preview = False
            cameraproperties.previewcmd = str("-n ")
            print("preview inactive")
        elif preview1==int(1):
            cameraproperties.preview = True
            cameraproperties.previewcmd = str("")
            print("preview active")
        else:
            print("Invalid option ")
    else:
        print(" Jeeze Louise... Invaild option")          
        
def setdimensions():

    
    imgwidth1 = cameraproperties.imgwidth
    imgheight1 = cameraproperties.imgheight
    imgwidth1 = str(imgwidth1)
    imgheight1 = str(imgwidth1)
    
    print("Current image dimensions are set as: " + "W " + imgwidth1 + " H " + imgheight1)
    print("Set new dimensions:"               )
    print("                   1: H 4056 x W 3040")
    print("                   2: H 2028 x W 1520")
    print("                   3: H 1014 x W 760")
    print("                   4: H 507 x 380")
    print("                   5: Custom")

    print("")
    print("Select Image dimensions")
    dimensionsvar = input ()
    if checkinputisnumber(dimensionsvar):
        dimensionsvar = int(dimensionsvar)
        if dimensionsvar>int(5):
            print("not a vaild option")
        elif dimensionsvar<int(1):
            print("not a vaild option")
        elif dimensionsvar == int(1):
            cameraproperties.imgwidth = int(4056)
            cameraproperties.imgheight = int(3040)
            cameraproperties.imgwidthcmd = str("-w 4056 ")
            cameraproperties.imgheightcmd = str("-h 3040 ")
        elif dimensionsvar == int(2):
            cameraproperties.imgwidth = int(2028)
            cameraproperties.imgheight = int(1520)
            cameraproperties.imgwidthcmd = str("-w 2028 ")
            cameraproperties.imgheightcmd = str("-h 1520 ")
        elif dimensionsvar == int(3):
            cameraproperties.imgwidth = int(1014)
            cameraproperties.imgheight = int(760)
            cameraproperties.imgwidthcmd = str("-w 1014 ")
            cameraproperties.imgheightcmd = str("-h 760 ")
        elif dimensionsvar == int(4):
            cameraproperties.imgwidth = int(507)
            cameraproperties.imgheight = int(380)
            cameraproperties.imgwidthcmd = str("-w 507 ")
            cameraproperties.imgheightcmd = str("-h 380 ")
        elif dimensionsvar == int(5):
            print("Please enter new value for width (max value 4056): ")
            customwidthvar = input()
            if checkinputisnumber(customwidthvar):
                customwidthvar = int(customwidthvar)
                if customwidthvar>cameraproperties.imgwidthmax:
                    customwidthvar = cameraproperties.imgwidthmax
                else:
                    pass
                if customwidthvar<cameraproperties.imgwidthmin:
                    customwidthvar = cameraproperties.imgwidthmin
                else:
                    pass
                cameraproperties.imgwidth = customwidthvar
                cameraproperties.imgwidthcmd = ("-w " + str(customwidthvar) + " ")

            print("Please enter new value for height (max value 3020): ")
            customheightvar = input()
            if checkinputisnumber(customheightvar):
                customheightvar = int(customheightvar)
                if customheightvar>cameraproperties.imgheightmax:
                    customheightvar = cameraproperties.imgheightmax
                else:
                    pass
                if customheightvar<cameraproperties.imgheightmin:
                    customheightvar = cameraproperties.imgheightmin
                else:
                    pass
                cameraproperties.imgheight = customheightvar
                cameraproperties.imgheightcmd = ("-h " + str(customheightvar) + " ")
            else:
                print("how did you get this error.. Good god man!")
    imgwidth1 = cameraproperties.imgwidth
    imgheight1 = cameraproperties.imgheight
    imgwidth1 = str(imgwidth1)
    imgheight1 = str(imgheight1)
    
    print("Your dimensions are set to: " + "W " + imgwidth1 + " H " + imgheight1)


def setdynamicrange():

    dynamicrange1 = cameraproperties.dynamicrange
    dynamicrange1 = str(dynamicrange1)
    
    print("Current dynamic range mode setting = " + dynamicrange1)
    print("Select new dynamic range mode value:")
    print("                     1 = off ")
    print("                     2 = low ")
    print("                     3 = medium ")
    print("                     4 = heigh ")
    print("Enter value:")

    dynamicrangevar = input()
    if checkinputisnumber(dynamicrangevar):
        dynamicrangevar = int(dynamicrangevar)
        if dynamicrangevar == int(1):
            cameraproperties.dynamicrange = str("off")
        elif dynamicrangevar == int(2):
            cameraproperties.dynamicrange = str("low")
        elif dynamicrangevar == int(3):
            cameraproperties.dynamicrange = str("med")
        elif dynamicrangevar == int(4):
            cameraproperties.dynamicrange = str("heigh")
        else:
            print("So this is kinda strange but... invalid option")
            
        dynamicrange1 = cameraproperties.dynamicrange
        dynamicrange1 = str(dynamicrange1)
        cameraproperties.dynamicrangecmd = ("-drc " + dynamicrange1 + " ")
        print("Camera dynamic range mode set to = " + dynamicrange1)
    else:
        print("not a valid option")
        print(" Quick primer: Try using the number keys")

def setAandDgains():

    Again1 = cameraproperties.Again
    Again1 = str(Again1)
    Dgain1 = cameraproperties.Dgain
    Dgain1 = str(Dgain1)
    
    if cameraproperties.AandDgains:
        print("Manual gains are currently: On")
    else:
        print("Manual gains are currently: off")
        
    print("Change manual gain status Y/N")
    turngain = input()
    inputresponse1 = str("Y")
    inputresponse2 = str("y")
    if turngain==inputresponse1 or turngain==inputresponse2:
        if cameraproperties.AandDgains:
            cameraproperties.AandDgains = False
            cameraproperties.iso = str("100")
            cameraproperties.isocmd = str("-ISO 100 ")
            print("manual gain settings are turned off")
            print("Camera Exposure mode set to Auto")
            print("Camera ISO set to 100")
        else:
            cameraproperties.AandDgains = True
            cameraproperties.exposuremode = str("")
            cameraproperties.exposuremodecmd = str("")
            cameraproperties.iso = str("")
            cameraproperties.isocmd = str("")
            print("manual gain settings are turned on")
    
    if cameraproperties.AandDgains:
        print("manual gain setting set to apply")
        print("current gains are: Analogue " + Again1 + " Digital " + Dgain1)
        print("Enter new values: y/n")
        gainsconfirm = input()
        if gainsconfirm==inputresponse1 or gainsconfirm==inputresponse2 :
            print("enter analogue gain:  (float value between 1 and 12)")
            newAgain = input()
            if checkinputisnumber(newAgain):
                newAgain = float(newAgain)
                if newAgain>float(12):
                    print("analogue gain greater than range and will set to max 12")
                    newAgain = 12
                    cameraproperties.Again = newAgain
                elif newAgain<float(1):
                    print("analogue gain less than range and will set to min 1")
                    newAgain = float(1)
                    cameraproperties.Again = newAgain
                else:
                    cameraproperties.Again = newAgain
            
            print("enter Digital gain:  (float value between 1 and 64)")
            newDgain = input()
            if checkinputisnumber(newDgain):
                newDgain = float(newDgain)
                if newDgain>float(64):
                    print("Digital gain greater than range and will set to max 64")
                    newDgain = 64
                    cameraproperties.Dgain = newDgain
                elif newDgain<float(1):
                    print("analogue gain less than range and will set to min 1")
                    newDgain = float(1)
                    cameraproperties.Dgain = newDgain
                else:
                    cameraproperties.Dgain = newDgain
    else:
        pass
    if cameraproperties.AandDgains:
        
        cameraproperties.AandDgainscmd = str("-ag " + str(cameraproperties.Again) + " " + "-dg " + str(cameraproperties.Dgain) + " ")
        print("Current gain settings are: Analogue = " + str(cameraproperties.Again) + (" Digital = ") + str(cameraproperties.Dgain))
    else:
        cameraproperties.AandDgaincmd = str("")
        print("Manual gain settings are off")
    
    
                
def setcameramode():
    
    cameramode1 = cameraproperties.cameramode
    cameramode1 = str(cameramode1)
    
    print("Current camera mode setting = " + cameramode1)
    print("Select new camera mode value:")
    print("                     0 = auto ")
    print("                     1 = 2028 x 1080 2x2 Binning ")
    print("                     2 = 2028 x 1520 2x2 Binning ")
    print("                     3 = Full FOV no Binning ")
    print("                     4 = 1012 x 760 4x4 Scaled ")
    print("Enter value:")

    cameramodevar = input()
    if checkinputisnumber(cameramodevar):
        cameramodevar = int(cameramodevar)
        print(str(cameramodevar))
        if cameramodevar == int(0):
            cameraproperties.cameramode = str("0")
        elif cameramodevar == int(1):
            cameraproperties.cameramode = str("1")
        elif cameramodevar == int(2):
            cameraproperties.cameramode = str("2")
        elif cameramodevar == int(3):
            cameraproperties.cameramode = str("3")
        elif cameramodevar == int(4):
            cameraproperties.cameramode = str("4")
        else:
            print("Its late and I'm tired... invalid option")
            
        cameramode1 = cameraproperties.cameramode
        cameramode1 = str(cameramode1)
        cameraproperties.cameramodecmd = ("-md " + cameramode1 + " ")
        print("Camera mode set to = " + cameramode1)
    else:
        print("not a valid option")

def setfiletype():

    filetype1 = cameraproperties.filetype
    filetype1 = str(filetype1)
    
    print("Current file type setting = " + filetype1)
    print("Select new camera mode value:")
    print("                     1 = .jpg ")
    print("                     2 = .jpg + raw ")
    print("                     3 = .png ")
    print("                     4 = .bmp ")
    print("                     5 = .gif ")
    print("Enter value:")

    filetypevar = input()
    if checkinputisnumber(filetypevar):
        filetypevar = int(filetypevar)
        print(str(filetypevar))
        
        if filetypevar == int(1):
            cameraproperties.filetype = str(".jpg")
            cameraproperties.qualitystatus = True
            setjpgquality()
            cameraproperties.rawstatus = False
        elif filetypevar == int(2):
            cameraproperties.filetype = str(".jpg")
            cameraproperties.qualitystatus = True
            setjpgquality()
            cameraproperties.rawstatus = True
        elif filetypevar == int(3):
            cameraproperties.filetype = str(".png")
            cameraproperties.qualitystatus = False
            cameraproperties.rawstatus = False
        elif filetypevar == int(4):
            cameraproperties.filetype = str(".bmp")
            cameraproperties.qualitystatus = False
            cameraproperties.rawstatus = False
        elif filetypevar == int(5):
            cameraproperties.filetype = str(".gif")
            cameraproperties.qualitystatus = False
            cameraproperties.rawstatus = False
        else:
            print("Its late and I'm tired... invalid option")
            
        print("Capture filetype set to = " + cameraproperties.filetype)
    else:
        print("not a valid option")

def setjpgquality():
    jpgquality1 = cameraproperties.quality
    print("current quality = " + str(jpgquality1) + " %")
    print("enter new quality value Range 0 - 100 ")
    jpgqualityvar = input()
    if checkinputisnumber(jpgqualityvar):
        jpgqualityvar = int(jpgqualityvar)
        
    else:
        print("I really hate to say it but ya know...not a vaild option")

    if checknumber(jpgqualityvar,cameraproperties.qualitymax,cameraproperties.qualitymin,cameraproperties.qualityunit):
        cameraproperties.quality = jpgqualityvar
        jpgquality = jpgqualityvar
        cameraproperties.qualitycmd = str("-q " + str(jpgquality) + " ")
        print("new file quality set to = " + str(jpgquality) + " %") 
    else:
        pass
    
def setprocessraws():
     
    if cameraproperties.processraws:
        print("Processing raw images is active: Enter 1 to keep active or enter 0 to turn off")
    else:
        print("Process raw mode is inactive: Enter 1 to Turn on or enter 0 to keep inactive")
    processrawsvar = input()
    
    if checkinputisnumber(processrawsvar):
        processraws1 = processrawsvar
        processraws1 = int(processraws1)
        if processraws1==int(0):
            cameraproperties.processraws = False
            print("Process raws is inactive")
        elif processraws1==int(1):
            cameraproperties.processraws = True
            print("Process raws is now active")
            print("make sure you set the file type to jpeg+raws in option 21")
        else:
            print("Invalid option ..how did you even get here ")
    else:
        print(" so here we are again... Invaild option")

def processrawsfunction(jpegtoprocess):
    filetoprocess = jpegtoprocess
    filetoprocess = str(filetoprocess)
    d = RPICAM2DNG()
    d.convert(filetoprocess)


def capturetestimage():
    print("please enter filename:")
    filenameinput = input()
    filenameinput = str(filenameinput)
    
    var1 = cameraproperties.previewcmd
    var2 = cameraproperties.sharpnesscmd
    var3 = cameraproperties.contrastcmd
    var4 = cameraproperties.brightnesscmd
    var5 = cameraproperties.saturationcmd
    var6 = cameraproperties.isocmd
    var7 = cameraproperties.exposuremodecmd
    var8 = cameraproperties.antiflickercmd
    if cameraproperties.awbgstatus:
        var9 = cameraproperties.awbgcmd
    else:
        var9 = cameraproperties.autowhitebalancecmd
    
    var10 = cameraproperties.imageeffectcmd
    var11 = cameraproperties.meteringmodecmd
    var12 = cameraproperties.rotationcmd
    var13 = cameraproperties.shutterspeedcmd
    var14 = cameraproperties.dynamicrangecmd
    var15 = cameraproperties.imgwidthcmd
    var16 = cameraproperties.imgheightcmd
    if cameraproperties.qualitystatus:
        var17 = cameraproperties.qualitycmd
    else:
        var17 = str("")
    var18 = cameraproperties.timeoutcmd
    var19 = cameraproperties.burstmodecmd
    var20 = cameraproperties.AandDgainscmd
    var21 = cameraproperties.cameramodecmd
    if cameraproperties.rawstatus:
        var22 = cameraproperties.rawcmd
    else:
        var22 = str("")
    var23 = " -o "
    var24 = filenameinput
    var25 = 0
    var26 = cameraproperties.filetype
    loopno = 0    
    
    capture = True
    responseval1 = str("Y")
    responseval2 = str("y")
    while capture:
        var25m = var25+loopno
        imageindex = str(var25m)
        print("capture a test image: Y/N")
        captureresponse = input()
        if captureresponse==responseval1 or captureresponse==responseval2:
            print("capturing image test1")
            capturecommand =str("raspistill "+var1+var2+var3+var4+var5+var6+var7+var8+var9+var10
                  +var11+var12+var13+var14+var15+var16+var17+var18+var19+var20+var21+var22
                  +var23+var24+imageindex+var26)
#            print(capturecommand)
            os.system(capturecommand)
            cameraproperties.lastimage = str(var24+imageindex+var26)
            print(cameraproperties.lastimage)
            if cameraproperties.processraws:
                print("processing raws")
                try:
                    processrawsfunction(cameraproperties.lastimage)
                except Exception as er:
                    print("couldn't process the raw...Did you set the file type right..option 21") 
                    print(er)
            else:
                print("process raws false")
                pass
            if cameraproperties.viewlastimage:
                try:
                    print("Loading... please wait.... press q on image to close image")
                    displaylastimage()
                except Exception as e:
                    print(e)
                    pass
            else:
                pass
            print("recapture image: Y/N")
            captureresponse = input()
            captureresponse = str(captureresponse)
            try:                             
                if captureresponse==responseval1 or captureresponse==responseval2:
                    capture = True
                    loopno = loopno + 1
                else:
                    capture = False
                    loopno = 0
                    break
            except Exception as e:
                print(e)        
        else:           
            captureresponse = False
            break
        
#def setroi
        

def setcapturesequence():
    print("Current settings:")
    print("Number of shots: " + str(cameraproperties.sequencenumber) )
    print("Start delay: " +str(cameraproperties.sequencestartdelay))
    print("Sequence shot delay: " +str(cameraproperties.sequenceshotdelay))
    print("")
    print("Change setting: Y/N")
    
    capturesequenceresponse = input()
    captresponseval1 = str("Y")
    captresponseval2 = str("y")
    if capturesequenceresponse==captresponseval1 or capturesequenceresponse==captresponseval2:
        print("Enter number of shots: ")
        shotsnumberval = input()
        if checkinputisnumber(shotsnumberval):
            shotsnumberval = int(shotsnumberval)
            if shotsnumberval>cameraproperties.sequencenumbermax:
                shotsnumberval = 1000
            elif shotsnumberval<cameraproperties.sequencenumbermin:
                shotsnumberval = 1
            else:
                pass
            cameraproperties.sequencenumber = shotsnumberval
                
        else:
            pass
        print("Enter start delay: ")
        shotsstartdelayval = input()
        if checkinputisnumber(shotsstartdelayval):
            shotsstartdelayval = int(shotsstartdelayval)
            cameraproperties.sequencestartdelay = shotsstartdelayval
        else:
            print("Not a number")
            pass
        print("Enter inter-shot delay: ")
        intershotdelayval = input()
        if checkinputisnumber(intershotdelayval):
            intershotdelayval = int(intershotdelayval)
            cameraproperties.sequenceshotdelay = intershotdelayval
        else:
            print("Not a number")
            pass
    else:
        pass

def capturesequence():
    print("please enter filename:")
    filenameinput = input()
    filenameinput = str(filenameinput)
    
    var1 = cameraproperties.previewcmd
    var2 = cameraproperties.sharpnesscmd
    var3 = cameraproperties.contrastcmd
    var4 = cameraproperties.brightnesscmd
    var5 = cameraproperties.saturationcmd
    var6 = cameraproperties.isocmd
    var7 = cameraproperties.exposuremodecmd
    var8 = cameraproperties.antiflickercmd
    if cameraproperties.awbgstatus:
        var9 = cameraproperties.awbgcmd
    else:
        var9 = cameraproperties.autowhitebalancecmd
    
    var10 = cameraproperties.imageeffectcmd
    var11 = cameraproperties.meteringmodecmd
    var12 = cameraproperties.rotationcmd
    var13 = cameraproperties.shutterspeedcmd
    var14 = cameraproperties.dynamicrangecmd
    var15 = cameraproperties.imgwidthcmd
    var16 = cameraproperties.imgheightcmd
    if cameraproperties.qualitystatus:
        var17 = cameraproperties.qualitycmd
    else:
        var17 = str("")
    var18 = cameraproperties.timeoutcmd
    var19 = cameraproperties.burstmodecmd
    var20 = cameraproperties.AandDgainscmd
    var21 = cameraproperties.cameramodecmd
    if cameraproperties.rawstatus:
        var22 = cameraproperties.rawcmd
    else:
        var22 = str("")
    var23 = " -o "
    var24 = filenameinput
    var25 = cameraproperties.filetype
        
    responseval1 = str("Y")
    responseval2 = str("y")
    print("capture the sequence: Y/N")
    captureresponse = input()
    if captureresponse==responseval1 or captureresponse==responseval2:
        time.sleep(cameraproperties.sequencestartdelay)
        loopnumber = 0
        while cameraproperties.sequencenumber>loopnumber:
            var24 = str(str(filenameinput)+str(loopnumber))
            print("capturing image " + str(loopnumber) + " of " + str(cameraproperties.sequencenumber))
            capturecommand =str("raspistill "+var1+var2+var3+var4+var5+var6+var7+var8+var9+var10
                  +var11+var12+var13+var14+var15+var16+var17+var18+var19+var20+var21+var22
                  +var23+var24+var25)
#            print(capturecommand)
            os.system(capturecommand)
            cameraproperties.lastimage = str(var24+var25)
            if cameraproperties.processraws:
                try:
                    processrawsfunction(cameraproperties.lastimage)
                    print(str(cameraproperties.lastimage)+" captured and processed")
                except Exception as er:
                    print("couldn't process raws... did you set the file type right ... option 21")
            else:
                print("Image captured")
                pass
            
            time.sleep(cameraproperties.sequenceshotdelay)
            loopnumber = loopnumber + 1
            
        
    
#def printcamerasettings():
    #todo
def savecurrentsettings():
    if not os.path.exists('cameraconfigs'):
        os.makedirs('cameraconfigs')
    print("please enter filename")
    filetoname = input()
    filetoname = str("cameraconfigs/" +filetoname + ".camfigs")
    stufftosave=createvariablelist()
    filetoname = str(filetoname)
    with open(filetoname, 'w') as f:
        for item in stufftosave:
            f.write('%s\n' % item)
            f.close
    

def createvariablelist():
    var1 = cameraproperties.viewlastimage
    var2 = cameraproperties.preview
    var3 = cameraproperties.previewcmd
    var4 = cameraproperties.sharpness
    var5 = cameraproperties.sharpnesscmd
    var6 = cameraproperties.contrast
    var7 = cameraproperties.contrastcmd
    var8 = cameraproperties.brightness
    var9 = cameraproperties.brightnesscmd
    var10 = cameraproperties.saturation
    var11= cameraproperties.saturationcmd 
    var12 = cameraproperties.iso 
    var13 = cameraproperties.isocmd 
    var14 = cameraproperties.exposuremode 
    var15 = cameraproperties.exposuremodecmd
    var16 = cameraproperties.antiflicker
    var17= cameraproperties.antiflickercmd
    var18 = cameraproperties.autowhitebalance
    var19 = cameraproperties.autowhitebalancecmd
    var20 = cameraproperties.autowhitebalancestatus
    var21 = cameraproperties.awbg
    var22 = cameraproperties.awbgstatus
    var23 = cameraproperties.awbgcmd
    var24 = cameraproperties.imageeffect
    var25 = cameraproperties.imageeffectcmd
    var26 = cameraproperties.meteringmode
    var27 = cameraproperties.meteringmodecmd
    var28 = cameraproperties.rotation
    var29 = cameraproperties.rotationcmd
    var30 = cameraproperties.shutterspeed
    var31 = cameraproperties.shutterspeedcmd
    var32 = cameraproperties.dynamicrange
    var33 = cameraproperties.dynamicrangecmd
    var34 = cameraproperties.imgwidth
    var35 = cameraproperties.imgwidthcmd
    var36 = cameraproperties.imgheight
    var37 = cameraproperties.imgheightcmd
    var38 = cameraproperties.quality
    var39 = cameraproperties.qualitycmd
    var40 = cameraproperties.qualitystatus
    var41 = cameraproperties.rawstatus
    var42 = cameraproperties.processraws
    var43 = cameraproperties.rawcmd
    var44 = cameraproperties.timeout
    var45 = cameraproperties.timeoutcmd
    var46 = cameraproperties.burstmode
    var47 = cameraproperties.burstmodecmd
    var48 = cameraproperties.Again
    var49 = cameraproperties.Dgain
    var50 = cameraproperties.AandDgains
    var51 = cameraproperties.AandDgainscmd
    var52 = cameraproperties.cameramode
    var53 = cameraproperties.cameramodecmd
    var54 = cameraproperties.sequencenumber
    var55 = cameraproperties.sequencestartdelay
    var56 = cameraproperties.sequenceshotdelay
    var57 = cameraproperties.filename
    var58 = cameraproperties.filetype
    
    varlist =[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,
                 var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,
                 var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,
                 var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,
                 var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,
                 var57,var58]
    
    return varlist



def converttruefalse(valuetf):
    
    checkastr = valuetf[0]
    avalt = str("T")
    avalf = str("F")
    print(checkastr)
    if checkastr == avalt:
        return True
    elif checkastr == avalf:
        return False
    else:
        return False
    
def printcamerasettings():
    print(str(cameraproperties.viewlastimage)+str(" viewlastimage"))
    print(str(cameraproperties.preview)+str(" camera preview"))
    print(str(cameraproperties.sharpness)+str(" sharpness"))
    print(str(cameraproperties.contrast) + str(" contrast"))
    print(str(cameraproperties.brightness) + str(" Brightness"))
    print(str(cameraproperties.saturation) + str(" Saturation"))
    print(str(cameraproperties.iso)+ str(" ISO"))
    print(str(cameraproperties.exposuremode) + str(" Exposuremode"))
    print(str(cameraproperties.antiflicker) + str(" Antiflickerr"))
    print(str(cameraproperties.autowhitebalancestatus)+str("autowhitebalance status"))
    print(str(cameraproperties.autowhitebalance)+ str(" Autowhitebalance"))
    print(str(cameraproperties.awbgstatus)+ str("awbg status"))
    print(str(cameraproperties.awbg) + str(" awbg"))
    print(str(cameraproperties.imageeffect) + str(" Image effects"))
    print(str(cameraproperties.meteringmode) + str(" Metering mode"))
    print(str(cameraproperties.rotation) + str(" Rotation"))
    print(str(cameraproperties.shutterspeed) + str(" Shutterspeed"))
    print(str(cameraproperties.dynamicrange) + str(" Dynamic range compression"))
    print(str(cameraproperties.imgwidth) + str(" Image width"))
    print(str(cameraproperties.imgheight) + str(" Image height"))
    print(str(cameraproperties.qualitystatus)+ str(" Quality Status"))
    print(str(cameraproperties.quality) + str(" Quality"))
    print(str(cameraproperties.rawstatus) + str(" Record Raws"))
    print(str(cameraproperties.processraws) + str(" Process Raws"))
    print(str(cameraproperties.timeout) + str(" time out"))
    print(str(cameraproperties.burstmode) + str(" Burst mode"))
    print(str(cameraproperties.AandDgains)+str(" a and d gains status"))
    print(str(cameraproperties.Again) + str(" Analogue Gain"))
    print(str(cameraproperties.Dgain) + str(" Digital gain"))
    print(str(cameraproperties.cameramode)+ str(" Camera mode"))
    print(str(cameraproperties.sequencenumber) + str(" Number of shots in sequence"))
    print(str(cameraproperties.sequencestartdelay) + str(" Sequence start delay"))
    print(str(cameraproperties.sequenceshotdelay) + str(" Intershot delay"))
    print(str(cameraproperties.filename) + str(" File name"))
    print(str(cameraproperties.filetype) + str(" File type"))

        
    
def loadcamerasettings():
    if not os.path.exists('cameraconfigs'):
        print("no camera configuration file detected")
    else:
        
        print("PLEASE ENTER FILENAME WITHOUT EXTENSION or enter c to cancel")
        print("")
        print("for example for: 'cameraconfigs\\mysupercamerasetting.camfigs'")
        print("")
        print("just type 'mysupercamerasetting' and hit enter")
        time.sleep(5)
        print("Here are your pre-saved configuration files")
        print(glob.glob("cameraconfigs/*.camfigs"))
        userselectfile = input()
        userselectfile = str(userselectfile)
        if userselectfile==str("c"):
            pass
        else:
            userselectfile = str(userselectfile+".camfigs")
            filetoopen = str("cameraconfigs/" + userselectfile)
            try:
                with open(filetoopen) as filepath:
                    camerastatelist = filepath.readlines()
                    print("we arre here")
                    
                    cameraproperties.viewlastimage = converttruefalse(camerastatelist[0])
                    cameraproperties.preview = converttruefalse(camerastatelist[1])
                    cameraproperties.previewcmd = camerastatelist[2]
                    cameraproperties.sharpness = camerastatelist[3]
                    cameraproperties.sharpnesscmd = camerastatelist[4]
                    cameraproperties.contrast = camerastatelist[5]            
                    cameraproperties.contrastcmd = camerastatelist[6]
                    cameraproperties.brightness = camerastatelist[7]
                    cameraproperties.brightnesscmd = camerastatelist[8]
                    cameraproperties.saturation = camerastatelist[9]
                    cameraproperties.saturationcmd = camerastatelist[10]
                    cameraproperties.iso  = camerastatelist[11]
                    cameraproperties.isocmd = camerastatelist[12]
                    cameraproperties.exposuremode = camerastatelist[13]
                    cameraproperties.exposuremodecmd = camerastatelist[14]
                    cameraproperties.antiflicker = camerastatelist[15]
                    cameraproperties.antiflickercmd = camerastatelist[16]
                    cameraproperties.autowhitebalance = camerastatelist[17]
                    cameraproperties.autowhitebalancecmd = camerastatelist[18]
                    cameraproperties.autowhitebalancestatus = converttruefalse(camerastatelist[19])
                    cameraproperties.awbg = camerastatelist[20]
                    cameraproperties.awbgstatus = converttruefalse(camerastatelist[21])
                    cameraproperties.awbgcmd = camerastatelist[22]
                    cameraproperties.imageeffect = camerastatelist[23]
                    cameraproperties.imageeffectcmd = camerastatelist[24]
                    cameraproperties.meteringmode = camerastatelist[25]
                    cameraproperties.meteringmodecmd = camerastatelist[26]
                    cameraproperties.rotation = camerastatelist[27]
                    cameraproperties.rotationcmd = camerastatelist[28]
                    cameraproperties.shutterspeed = float(camerastatelist[29])
                    cameraproperties.shutterspeedcmd = camerastatelist[30]
                    cameraproperties.dynamicrange = camerastatelist[31]
                    cameraproperties.dynamicrangecmd = camerastatelist[32]
                    cameraproperties.imgwidth = camerastatelist[33]
                    cameraproperties.imgwidthcmd = camerastatelist[34]
                    cameraproperties.imgheight = camerastatelist[35]
                    cameraproperties.imgheightcmd = camerastatelist[36]
                    cameraproperties.quality = camerastatelist[37]
                    cameraproperties.qualitycmd = camerastatelist[38]
                    cameraproperties.qualitystatus = converttruefalse(camerastatelist[39])
                    cameraproperties.rawstatus = converttruefalse(camerastatelist[40])
                    cameraproperties.processraws = converttruefalse(camerastatelist[41])
                    cameraproperties.rawcmd = camerastatelist[42]
                    cameraproperties.timeout = float(camerastatelist[43])
                    cameraproperties.timeoutcmd = camerastatelist[44]
                    cameraproperties.burstmode = converttruefalse(camerastatelist[45])
                    cameraproperties.burstmodecmd = camerastatelist[46]
                    cameraproperties.Again = camerastatelist[47]
                    cameraproperties.Dgain = camerastatelist[48]
                    cameraproperties.AandDgains = converttruefalse(camerastatelist[49])
                    cameraproperties.AandDgainscmd = camerastatelist[50]
                    cameraproperties.cameramode = camerastatelist[51]
                    cameraproperties.cameramodecmd = camerastatelist[52]
                    cameraproperties.sequencenumber = camerastatelist[53]
                    cameraproperties.sequencestartdelay = camerastatelist[54]
                    cameraproperties.sequenceshotdelay = camerastatelist[55]
                    cameraproperties.filename = camerastatelist[56]       
                    cameraproperties.filetype = camerastatelist[57]
                    
                    print("settings loaded")
            except:
                pass
    
def displaylastimage():
    
    if not os.path.exists(cameraproperties.lastimage):
        print("file not found")
    else:
        lastimagefilecmd = str("feh "+ cameraproperties.lastimage)
        try:
            
            os.system(lastimagefilecmd)  #Try no1       
            
        except Exception as Er:
            print(Er)
            print("something went wrong")
            pass

def setviewlastimage():
     
    if cameraproperties.viewlastimage==True:
        print("View last image is active: Enter 1 to keep active or enter 0 to turn off")
    else:
        print("View last image is inactive: Enter 1 to Turn on or enter 0 to keep inactive")
    viewlastimagevar = input()
    
    if checkinputisnumber(viewlastimagevar):
        viewlastimagevar1 = viewlastimagevar
        viewlastimagevar1 = int(viewlastimagevar1)
        if viewlastimagevar1==int(0):
            cameraproperties.viewlastimage = False
            print("View last image inactive")
        elif viewlastimagevar1==int(1):
            cameraproperties.viewlastimage = True
            
            print("View last image is active")
        else:
            print("Invalid option ..how did you even get here ")
    else:
        print(" so here we are again... Invaild option")
    
def readme():
    print("      **************   WARNING   **************      ")
    print(" I have absolutely no software trainning or idea how to program correctly")
    print("")
    print("")
    print(" You use this script  at your own risk.")
    print("")
    print("")
    time.sleep(3)
    print("I hope you find this script useful. Please bear in mind that this was written")
    print("because I could not find a suitable tool to use the raspiberry pi hi-quality")
    print("camera on a ssh connection for astrophotography. Maybe there is a better tool")
    print("around now? Nice feature is that you only need to input numbers to set the various")
    print("parameters of the camera. You can save a particular method to use again and again")
    print("Also very nice is that you can view the images using feh over a terminal, so no need")
    print("to run a full x- enviornment. See https://feh.finalrewind.org/ for details on feh and")
    print("how cool it is. You will need to install feh on your pi. 'sudo apt-get install feh'")
    print("should do the trick. When using Feh do not use 'sudo' to launch this script" )
    print("Just cd to the diretory where it is saved and type in:> python3 astropicamera.py" )
    print("")
    print("")
    time.sleep(10)
    print("Copyright <2020> <Daragh Byrne>")
    print("Permission is hereby granted, free of charge, to any person obtaining a copy")
    print("of this software and associated documentation files (the 'Software'), to deal ")
    print("in the Software without restriction, including without limitation the rights to use,")
    print("copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the ")
    print("Software, and to permit persons to whom the Software is furnished to do so, subject ")
    print("to the following conditions:")
    print("The above copyright notice and this permission notice shall be included in all ")
    print("copies or substantial portions of the Software.")
    print("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, ")
    print("INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR ")
    print("PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE ")
    print("LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, ")
    print("TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE ")
    print("OR OTHER DEALINGS IN THE SOFTWARE.")
    print("")
    print("PS... let me know how you get on! Twitter: @Daragh__Byrne")
    print("PPS... My wife helped me write this and now she thinks I'll do the dishes")
    print("find out more? Enter Y/N")
    moreinfo = input()
    if moreinfo ==str("y") or moreinfo ==str("Y"):
        print(" I was giving out about not being able to load all the setting parameters")
        print(" from a saved settings file. In particular the boolean values")
        print(" she rightly suggested I look for blank spaces before or after the string in")
        print(" the file. So BIG thank you to her. BUT she thinks that this is an excuse for")
        print(" not doing the dishes. In particular the ones SHE left in the sink")
        print("                ... since SUNDAY")
        print(" For reference today is Thursday.")
        print("Am I being unreasonable: Y/N")
        pollquestionval1 = str(y)
        pollquestionval2 = str(Y)
        pollquestion = input()
        pollquestion = str(pollquestion)
        if pollquestion==pollquestionval1 or pollquestion==pollquestionval2:
            print("I think you need a reboot")
#            os.system("sudo shutdown now")
            pass
        else:
            print("thank you for the support")
            pass
        
    else:
        pass
def helpme():
    print("The script is designed to be used over a wifi connection to help set up the")
    print("the pi HQ cam mounted on a telescope. But hey who am I to dictate. Use it for")
    print("whatever the hell you want. It bascially composes a command for the raspistill")
    print("program")
    print("by setting a whole bunch of variables and holding them until ready to take a")
    print("photo Each variable is set by entering the desired number and hitting")
    print("enter. After that, follow the options. Couple of things though, not all")
    print("setting are compatible. Ie, you wouldn't use the autowhitebalance")
    print("inconjunction with autowhitebalance gain or ISO or exposuremode with Analogue ")
    print("and digital gains together. Where it was clear in the raspistill")
    print("docs, I tried to implement lockouts. Ie turning one on, turns the other off")
    print("")
    print("Note to use all the functions you need to have installed a couple of things")
    print("Raspistill - comes as standard")
    print("Feh - doesn't come as standard sudo apt-get install feh  <- I think")
    print("PyDNG - available from https://github.com/schoolpost/PyDNG")
    print(" python modules used:")
    print("                     time")
    print("                     glob")
    print("                     os")
    print(" and of course python3 and a HQ cam (enabled in raspiconfig)")
    print("Loading images using FEH and the HQ camera takes a few moments...not too long")
    print("but give it a chance and they should load")
    print("if an image is open, you have to hit q and enter to close and continue")
    print("00 is probably the most useful command as it will bring up the list of")
    print("But you have to be finished inputting your variables first")
    print("")
    print("processing raws - what is it!")
    print("The high quality camera outputs the raw file appended to a jpeg")
    print("thus to make it useable it must first be stripped away and made into its own file")
    print("This takes a few seconds if enabled")
    print("The intershot delay doesn't start counting untill all other processes are finished")
    print("so you don't have to worry about it. But just bear in mind that it will increase")
    print(" the lenght of time taken to run a sequence")
    print("")
    print("Saving and loading camera configurations")
    print("DON'T ENTER FILE PATHS OR EXTENSIONS")
    print("just enter a name such as goodcamconfig")
    print("A folder called cameraconfigs if not in existance will be created in ")
    print("the same folder as the script and your setting will be saved there")
    print("Same holds true for laoding settings. The script will print a list ")
    print("of camfig files just type in the one you want (no extension) ie goodcamfig ")
    print("and then you should get confirmation that the load was sucessfull")
    print("")
    print("")
    print("Note that the print current configuration will return what is actually being sent")
    print("to raspistill. In particular note that the units are not the same as the ")
    print("interface. For example the shutter time will be in microseconds, and the ")
    print("timeout time mill be in milliseconds etc.")
    print("")
    print("I haven't tested every aspect yet beyond, it seems to do what I want..")
    print("If strange things happen let me know and I'll take a looksee and see whats up")
    print("All testing was done on a pi zero w with HQ cam (raspbian 10 stretch)")
    print(" no reason to believe that it wouldn't work with other flavors")
    print("There are some raspistill functions I haven't used because I haven't had time,")
    print("and they don't really interest me that much. Some others are there but it wasn't")
    print("clear if they were for raspivid or raspistill. For example the antiflicker options")
    print("How would that work on a camera taking a still? Anyway play with them and report")
    print("back if you figure it out")
    print("")
    print("      **************   WARNING   **************      ")
    print(" I have absolutely no software trainning or idea how to program correctly")
    print("")
    print("")
    print(" You use this script  at your own risk.")
    print("")
    print("But really if you are a software engineer and looking through this code in horror")
    print("Remember you were a learner once too!")
    print("Happy snapping and if you get some good shots of anything I would love to see")
    print("Peace out")
    print("Twitter: @Daragh__Byrne")
    
    
##############################################
printoptions()
try:
    while cameraproperties.Quit:
        print ("Select Option")
        modeselect=input()
        if checkinputisnumber(modeselect):
            modeselect=int(modeselect)
            if modeselect==int(1):
                setexposure()
            if modeselect==int(2):
                settimeout()
            if modeselect==int(3):
                setrotation()
            if modeselect==int(4):
                setmeteringmode()
            if modeselect==int(5):
                setautowhitebalance()
            if modeselect==int(6):
                setautowhitebalancegain()
#            if modeselect==int(7):
#                setisoasnumber()
            if modeselect==int(7):
                setisoselection()
            if modeselect==int(8):
                setexposuremode()
            if modeselect==int(9):
                setbrightness()
            if modeselect==int(10):
                setcontrast()
            if modeselect==int(11):
                setsharpness()
            if modeselect==int(12):
                setantiflicker()
            if modeselect==int(13):
                setburstmode()
            if modeselect==int(14):
                setpreview()
            if modeselect==int(15):
                setdimensions()
            if modeselect==int(16):
                setdynamicrange()
            if modeselect==int(17):
                setAandDgains()
            if modeselect==int(18):
                setcameramode()
            if modeselect==int(19):
                setcapturesequence()
            if modeselect==int(20):
                print("I'm not 100% sure I am going to set this up")
                #setroi()
            if modeselect==int(21):
                setfiletype()
            if modeselect==int(22):
                printcamerasettings()
            if modeselect==int(23):
                savecurrentsettings()
            if modeselect==int(24):
                capturetestimage()
            if modeselect==int(25):
                setprocessraws()
            if modeselect==int(26):
                capturesequence()
            if modeselect==int(27):
                loadcamerasettings()
            if modeselect==int(28):
                setviewlastimage()
            if modeselect==int(29):
                displaylastimage()
            if modeselect==int(30):
                helpme()
            if modeselect==int(101):
                readme()
            if modeselect==int(99):
                Quitnow()
            if modeselect==int(91):
                Quitnowpowerdown()
            if modeselect==int(00):
                printoptions()
        else:
            print("To see options again Enter 00")
except:
    print("So here we are again")
    print("We have reached an impass. I think its time to part ways")
    pass

