
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this version includes peripherals (eyetracker ans SCR)
#this version rating scale  is present all the time, the cursor/answer marker appears at CS onset and people have 2 SECS to answer. CS is present for 4 secs total
#(using the mouse to answer).Will focus in time bin 4 and 5 the ones closest to Shock onset. Also using gray stim garbors
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.75.01), December 10, 2012, at 15:28
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import pylinkWrapper
from psychopy import visual, core, data, event, logging, gui,sound, misc
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace #asarraypyl
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import math
import peripheralsManagerCompoundSerial #everything to manage labjack
import createMask

class EscapeError(Exception):
    pass

peripheralsmanager = peripheralsManagerCompoundSerial.PeripheralsManager() #creating a PheripheralsManager 

try:
    peripheralsmanager.initialize()
    #peripheralsmanager.blockOff()
    #peripheralsmanager.stimOff()
#    peripheralsmanager.singleCSOff()
#    peripheralsmanager.compoundCSOff()
#    peripheralsmanager.CSPlusOff()
#    peripheralsmanager.CSMinusOff()
#    peripheralsmanager.CondTripletOff()

    
except IOError as myerror:
    print myerror
    print 'Exiting script'
    core.quit()


# Store info about the experiment session
expName = 'CompoundSerial'  # from the Builder filename that created this script
expInfo = {u'session': u'1', u'participant': u'p001', u'rand': u'set1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
if not os.path.isdir('data' + os.path.sep + '%s' %(expInfo['participant'])):
    os.makedirs('data' + os.path.sep + '%s' %(expInfo['participant']))  # if this fails (e.g. permissions) we will get error
if not os.path.isdir('data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + 'eyetracker'):
    os.makedirs('data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + 'eyetracker')  # if this fails (e.g. permissions) we will get error
if not os.path.isdir('data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + 'eyetracker'+ os.path.sep +'%s' %(expInfo['participant'])):
    os.makedirs('data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + 'eyetracker'+ os.path.sep +'%s' %(expInfo['participant']))  # if this fails (e.g. permissions) we will get error

filename = 'data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + '%s_sess%s_%s' %(expInfo['participant'], expInfo['session'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

filename_csv = 'data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + '%s_sess%s_%s' %(expInfo['participant'], expInfo['session'], expInfo['date'])
dataFile = open(filename_csv+'.csv', 'w')#a simple text file with 'comma-separated-values'

#read in the scream volume that you set
filename_volume = 'data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + 'screamLevel'
volumeFile = open(filename_volume+'.csv', 'r')
#set myvolume equal to the predetermined level
myvolume=volumeFile.read()

dataFile.write('Date:, %s\nSubject:, %s\nSession:, %s\nRandomization:, %s\n' %(expInfo['date'], expInfo['participant'], expInfo['session'], expInfo['rand']))

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)

# Setup the Window
#win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
#    monitor='135DMonitor', color=[0,0,0], colorSpace='rgb', units='deg')
#win = visual.Window(size=(1680, 1050), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
#    monitor='Monitor5313', color=[0.3,0.3,0.3], colorSpace='rgb', units='deg')
#    
win = visual.Window(size=(1680, 1050), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='G89', color=[0.3,0.3,0.3], colorSpace='rgb', units='deg')

#inactivating pylinkWrapper for now
#inactivating pylinkWrapper for now
pylinkWrapper = pylinkWrapper.PylinkWrapper() #creating an eyetracker object
##pylinkWrapper = pylinkWrapper.PylinkWrapper_dummy() #creating an eyetracker object

# initializes Eyelink after the psychopy window is created
filename_eyetracker ='ses_%s' %(expInfo['session']) + '.edf'
filename_eyetracker_retrieve = 'data' + os.path.sep + '%s' %(expInfo['participant']) + os.path.sep + 'eyetracker' + os.path.sep + '%s' %(expInfo['participant'])  + os.path.sep+'%s_sess%s_%s' %(expInfo['participant'], expInfo['session'], expInfo['date']) + '.edf'

print(filename_eyetracker)

pylinkWrapper.initialize(win, filename_eyetracker, filename_eyetracker_retrieve)
pylinkWrapper.calibrate(win)

# Initialize components for Routine "theInstructions"
theInstructionsClock = core.Clock()
myInstructions = visual.TextStim(win=win, ori=0, name='myInstructions',
    text='',
    font='Arial',
    pos=[0, 0], height=.82, wrapWidth=28,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
    
myInstructions2 = visual.TextStim(win=win, ori=0, name='myInstructions2',
    text='',
    font='Arial',
    pos=[0, 2], height=.9, wrapWidth=28,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

myInstructionsRating = visual.TextStim(win=win, ori=0, name='myInstructionsRating',
    text='',
    font='Arial',
    pos=[0, -6.3], height=.72, wrapWidth=28,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
    
    
    
if expInfo['session'] == '1':
    myInstructions.setText('Please avoid moving through the whole experiment.\n' 
    + 'This task is split into three main parts.'
    + 'In each part you will see images of different shapes. Please look carefully at them and make sure you are able to recognize them.\n'
    + 'In the FIRST part of the experiment you will simply see the shapes appear in the screen. During this phase, you will NOT receive any electrical or auditory stimulation.\n'
    + 'In the SECOND part of the experiment, you will see the images again, however this time some of the images may be followed by an electric shock and a loud scream.' 
    + 'This SECOND part of the experiment will be divided in 4 BLOCKS of trials. At the end of each block you will get a short break.\n'
    + 'Finally, in the THIRD part of the experiment you will see the images again and you may or may not receive the electric shock and scream.\n\n'
    + 'Throughout the experiment, a rating scale will be up on the screen with each image.When the image appears,your task is to rate how likely is it for the image currently displayed to be followed by the sound and electrical stimulation.\n'
    + 'You will have a limited amount of time to answer, so please be as quick and as accurate as possible. Next you will see an example of the rating scale.')


myInstructionsRating.setText('Use the mouse to hover over the numbers along the 0 - 100 scale.' 
+ 'Remember, 0 = 0% likelihood of the image being followed by stimulation (sound + shock) AND  100 = 100% likelihood of the image being followed by stimulation.\n'
+ 'In the FIRST part of the experiment when stimulation will not occur you may want to select 0 as your answer. However your answer may change for the SECOND and THIRD part of the experiment.\n'
+'Once the marker is positioned in a number you want to select, click on that number to confirm your response.'
+'Please try to answer the rating scale as fast and as acurately as possible.\n\n')

myInstructions2.setText('If you have any questions please ask them now, if not tell the experimenter that you are ready to start.')
    
theBreakClock = core.Clock()
#myBreak = visual.TextStim(win=win, ori=0, name='myBreak',
#    text='Take a short break.\n\n' 
#    + 'Press any key from the keyboard when you are ready to continue.',
#    font='Arial',
#    pos=[0, 0], height=.8, wrapWidth=20,
#    color='black', colorSpace='rgb', opacity=1,
#    depth=0.0)


# Initialize components for Routine "theInstructions2"
theInstructions2Clock = core.Clock()

# Initialize components for Routine "TheFix"
TheFixClock = core.Clock()
Fixation = visual.TextStim(win=win, ori=0, name='Fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=.8, wrapWidth=30,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
Fixation.setAutoLog(False)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
#MyImage1 = visual.ImageStim(win=win, name='MyImage1',
#    image='sin', mask=None,
#    ori=0, pos=[0, 0], size=[2.8,2.8],
#    color=[1,1,1], colorSpace=u'rgb', opacity=1,
#    texRes=128, interpolate=False, depth=0.0)
MyImage2 = visual.ImageStim(win=win, name='MyImage2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[2.8,2.8],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=0.0)
    
#MyImageLeft = visual.ImageStim(win=win, name='MyImageLeft',
#    image='sin', mask=None,
#    ori=0, pos=[-1.7, 0], size=[2.8,2.8],
#    color=[1,1,1], colorSpace=u'rgb', opacity=1,
#    texRes=128, interpolate=False, depth=0.0)

MyImageLeft = 1#visual.Polygon(win, name= "diamond",
#    edges=4, size=[3.6,4.4], fillColor=None, pos=(-1.7,0),  #width/Height , area =  7.92
#    lineColor='black')

MyImageRight = 2 #visual.ImageStim(win=win, name='MyImageRight',
#    image='sin', mask=None,
#    ori=0, pos=[1.7, 0], size=[2.8,2.8],
#    color=[1,1,1], colorSpace=u'rgb', opacity=1,
#    texRes=128, interpolate=False, depth=-1.0)
#MyImageRight= visual.Polygon(win, name= "diamond",
#    edges=4, size=[3.6,4.4], fillColor=None, pos=(1.7,0),  #width/Height , area =  7.92
#    lineColor='black')

#More Stim
MyImage1_grating = visual.GratingStim(win=win, name='MyImage1_grating',
    ori=0, pos=[0, 0], #size=[2.8,2.8],
    #color=[1,1,1], colorSpace=u'rgb', 
    opacity=1, interpolate=False, depth=0.0)



#More Stimuli

#gaborsq = visual.GratingStim(win, tex="sin",texRes=128,
#           size=[2.8], sf=[3,0], ori =0, name='gaborsq', pos=[0,0],interpolate=True)# area = 7.84

sq = visual.Polygon(win,lineWidth=1, name= "square", 
                edges=4, size=[4,4],fillColor=None, ori =45, pos=[0, 0], lineColor=None,interpolate=True)#[0.3,0.3,0.3])  #area 16 -- but same size as above gaborsq ..?
                
#gaborcirc = visual.GratingStim(win, tex="sin",mask="circle",texRes=128,
#           size=[3.2,3.2], sf=[3,0], ori =0, name='gaborcirc', pos=[0,0]) #center right, area =8.04

circ = visual.Polygon(win,lineWidth=1, name= "circle", 
                edges=256, size=[3.2,3.2],fillColor=None, pos=[0, 0], lineColor=None, interpolate=True)#[0.3,0.3,0.3]) #center right, area =8.04

hexagon = visual.Polygon(win,lineWidth=1,name= "hexagon", 
                edges=6, size=[3.2,3.2],fillColor=None, ori=90, pos=[0,0], lineColor=None,interpolate=True)#[0.3,0.3,0.3])  #area = 7.68

triangle= visual.Polygon(win,name= "triangle",lineWidth=1,
                edges=3, fillColor=None, pos=[0,0],size=[4,4],   #area = 8
                ori =0, lineColor=None,interpolate=True)#[0.3,0.3,0.3] )

pentagon= visual.Polygon(win, name= "pentagon",lineWidth=1, 
                edges=5, size=[3.5,3.5], fillColor=None, pos=[0,0],  #area =  7.65
                lineColor=None,interpolate=True)#[0.3,0.3,0.3])

diamond= visual.Polygon(win, name= "diamond",lineWidth=1,
                edges=4, size=[3.6,4.4], fillColor=None, pos=[0,0],  #width/Height , area =  7.92
                lineColor='black')

#gaborcross = visual.GratingStim(win, tex="sin",mask="cross",texRes=128,
#           size=[2.8,2.8], sf=[3,0], contrast= 0.2, ori =0, name='cross', pos=[0,0] ) 
crossVert=[[0.4,0.1],[0.4, -0.1],[0.1, -0.1],[0.1, -0.4],[-0.1, -0.4],[-0.1, -0.1], [-0.4, -0.1],[-0.4,0.1],[-0.1,0.1],[-0.1, 0.4], [0.1,0.4],[0.1, 0.1]]
gaborcross = visual.ShapeStim(win,name="cross", vertices=crossVert, fillColor=None, lineColor=None, lineWidth=1, size=[3.5,3.5],pos=[0,0], interpolate=True, closeShape=False)
#not same area but same width and height as sq

#star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
#star7 = visual.ShapeStim(win, vertices=star7Vert, fillColor=None, lineWidth=1, size=[3.5,3.5],pos=[0,0], name='star',lineColor=[0.3,0.3,0.3])

#draw semicircle
rectVert=[[0, -1.4],[1.4, -1.4],[1.4, 1.4]] #vertices for openbox
theta = np.linspace(90,270, 100)
radius = 1.4 #sensible if using pixels for window
x, y = misc.pol2cart(theta, radius)
xy = np.vstack([x,y]).transpose()# vertices for semicirc

rectSemicircVert= np.concatenate((rectVert, xy))
semicircRec = visual.ShapeStim(win,name="semicircRec", vertices=rectSemicircVert, closeShape=False, fillColor=None,pos=[0, 0], lineWidth=1, ori=90, interpolate=True, lineColor=None,size=1.0)
#same heigh and width as sq

#Set dimensions of screen to convert pixels to degrees
h = 27 # Monitor height in cm
d = 74# Distance between monitor and participant in cm
r = 1050 # Vertical resolution of the monitor

#how many  degrees per pixel?
deg_per_px = math.degrees(math.atan2(.5*h, d)) / (.5*r)
#print '%s degrees correspond to a single pixel' % deg_per_px


#USe these shapes as maskss for a grating
# initialize some values
masksize = 1024
masksizeLeft=1024
masksizeRight=1024

#pos_in_deg = [-1.7, 0]#of myMask (shape) - initialize some values

#convert degrees to pixel
#pos_in_px = pos_in_deg[0] / deg_per_px
#print 'The pos of the stimulus is %s pixels and %s visual degrees' \
#    % (pos_in_px, pos_in_deg)


polyShape = createMask.create_mask_from_vertices(math.ceil(pentagon.size[0]/deg_per_px), pentagon.verticesPix)


polyShapeLeft = createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px), circ.verticesPix)
polyShapeRight = createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px), circ.verticesPix)

#createGrating
myGrating= visual.GratingStim(win, tex='sin', sf=[0.03,0], texRes=256, mask= polyShape, units='pix',contrast= 0.5, #decrease contrast
size=math.ceil(pentagon.size[0]/deg_per_px), pos=np.array(pentagon.pos)/deg_per_px,interpolate=True)#units='pix',

myGratingLeft= visual.GratingStim(win, tex='sin', sf=[0.03,0], texRes=256, mask= polyShapeLeft, units='pix',contrast= 0.5, #decrease contrast
size=math.ceil(circ.size[0]/deg_per_px), pos=np.array(circ.pos)/deg_per_px, interpolate=True) 


myGratingRight= visual.GratingStim(win, tex='sin', sf=[0.03,0], texRes=256, mask= polyShapeRight, units='pix',contrast= 0.5, #decrease contrast
size=math.ceil(circ.size[0]/deg_per_px), pos=np.array(circ.pos)/deg_per_px, interpolate=True)#units='pix',

#circ.pos=[0, 0]
#myGrating.pos= np.array(pentagon.pos)/deg_per_px
#myGratingLeft.pos= np.array(circ.pos)/deg_per_px
#myGratingRight.pos= np.array(circ.pos)/deg_per_px

MySound = sound.Sound(u'stimuli' + os.path.sep + 'skrig_10kHzLP-12dB-mdv.wav')
MySound.setVolume(float(myvolume))
myITI = visual.TextStim(win=win, ori=0, name='myITI',
    text=u'+',
    font=u'Arial',
    pos=[0, 0], height=.8, wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
myITI.setAutoLog(False)

# Initialize components for Routine "theEnd"
theEndClock = core.Clock()
myEnd = visual.TextStim(win=win, ori=0, name='myEnd',
    text='This is the end of the experiment. Thanks!',
    font='Arial',
    pos=[0, 0], height=1, wrapWidth=20,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
    
myBreak = visual.TextStim(win=win, ori=0, name='myBreak',
    text='This block has ended.\n Please take a break.\n ' 
    +'The experiment will start again in 2 minutes',
    font='Arial',
    pos=[0, 0], height=1, wrapWidth=20,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)


##Rating Scales with confirmation box
#myRating_Stim= visual.RatingScale(win=win,choices=['0','10','20','30','40','50','60', '70','80', '90', '100'],acceptPreText='', low=0,high=100, acceptSize=0.5, showAccept=True,
#            acceptKeys=["click", "enter"], #mouseOnly=True,#['3','space', 'up'],leftKeys=['left', '1'],rightKeys=['right','2'],respKeys=['1','2','3'], markerStart=0
#            stretch=1.5,size=1,marker='slider',textColor='black', markerColor='black',  lineColor='Gray', markerExpansion=0,pos=[0, 0.6],minTime=0.05,maxTime=2, disappear=True)#stretch=1.5,size=1.2,
#
#myRating_example= visual.RatingScale(win=win,choices=['0','10','20','30','40','50','60', '70','80', '90', '100'],acceptPreText='', low=0,high=100, acceptSize=0.5, showAccept=True,
#             acceptKeys=["click", "enter"],#mouseOnly=True, #acceptKeys=['3','space', 'up'],#leftKeys=['left', '1'],rightKeys=['right','2'],respKeys=['1','2','3'],markerStart=0,
#            stretch=1.5,size=1,marker='slider', textColor='black', markerColor='black',  lineColor='Gray', markerExpansion=0,pos=[0, 0.6],minTime=0.05,maxTime=0, disappear=True)#stretch=1.5,size=1.2,

##Rating Scales- single click
myRating_Stim= visual.RatingScale(win=win,choices=['0','10','20','30','40','50','60', '70','80', '90', '100'],acceptPreText='', acceptSize=0.5, showAccept=False, #low=0,high=100,
            #acceptKeys=["click", "enter"], #mouseOnly=True,#['3','space', 'up'],leftKeys=['left', '1'],rightKeys=['right','2'],respKeys=['1','2','3'], markerStart=0
            stretch=1.5,size=1,marker='slider',textColor='black', markerColor='black',  lineColor='Gray', markerExpansion=0,pos=[0, 0.6],minTime=0.05,maxTime=0, disappear=False,singleClick=True)#stretch=1.5,size=1.2,

myRating_example= visual.RatingScale(win=win,choices=['0','10','20','30','40','50','60', '70','80', '90', '100'],acceptPreText='',  acceptSize=0.5, showAccept=False,#low=0,high=100,
            #acceptKeys=["click", "enter"],#mouseOnly=True, #acceptKeys=['3','space', 'up'],#leftKeys=['left', '1'],rightKeys=['right','2'],respKeys=['1','2','3'],markerStart=0,
            stretch=1.5,size=1,marker='slider', textColor='black', markerColor='black',  lineColor='Gray', markerExpansion=0,pos=[0, 0.6],minTime=0.05,maxTime=0, disappear=False,singleClick=True)#stretch=1.5,size=1.2,

#Item_Contingency= visual.TextStim(win=win, text="How likely is it for this image to be paired with the scream and shock? ",pos=[0,6],height=0.8,color='black', bold=True, wrapWidth=18)
#ratingValuesText="1: Not at All        ...        3: Moderately        ...        5: Very Much"
#ratingValues=visual.TextStim(self.win,text=self.ratingValuesText,pos=[0, 5.63],height=0.62, color='black', wrapWidth=28)
curKey=[]
curRT=[]
ratingOn=[]

# set up handler to look after randomisation of conditions etc
Loop_Conditions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli' + os.path.sep + '%s' %(expInfo['rand']) + os.path.sep + 'CondOrders_sess_%s.csv' %(expInfo['session'])),
    seed=None, name='Loop_Conditions')
thisExp.addLoop(Loop_Conditions)  # add the loop to the experiment
thisLoop_Condition = Loop_Conditions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLoop_Condition.rgb)
if thisLoop_Condition != None:
    for paramName in thisLoop_Condition.keys():
        exec(paramName + '= thisLoop_Condition.' + paramName)
        
# set up handler to look after randomisation of conditions etc
Loop_Trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli'+ os.path.sep + '%s' %(expInfo['rand']) + os.path.sep + 'TrialOrders_sess_%s.csv' %(expInfo['session'])), #'TrialOrders_sess_%s.csv' %(expInfo['session'])),
    seed=None, name='Loop_Trials')
thisExp.addLoop(Loop_Trials)  # add the loop to the experiment
thisLoop_Trial = Loop_Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLoop_Trial.rgb)
if thisLoop_Trial != None:
    for paramName in thisLoop_Trial.keys():
        exec(paramName + '= thisLoop_Trial.' + paramName)
        
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"theInstructions"-------

# update component parameters for each repeat
EndInstructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
EndInstructions.status = NOT_STARTED
# keep track of which components have finished
theInstructionsComponents = []
theInstructionsComponents.append(myInstructions)
theInstructionsComponents.append(EndInstructions)
for thisComponent in theInstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#timing info
theInstructionsClock.reset()  # clock 
frameN = -1

#-------Start Routine "theInstructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = theInstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *myInstructions* updates
    if t >= 0.0 and myInstructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        myInstructions.tStart = t  # underestimates by a little under one frame
        myInstructions.frameNStart = frameN  # exact frame index
        myInstructions.setAutoDraw(True)
        InstructionsStartTime = globalClock.getTime()
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()

    # *EndInstructions* updates
    if t >= 0.0 and EndInstructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndInstructions.tStart = t  # underestimates by a little under one frame
        EndInstructions.frameNStart = frameN  # exact frame index
        EndInstructions.status = STARTED
        # keyboard checking is just starting
        EndInstructions.clock.reset()  # now t=0
        event.clearEvents()
    if EndInstructions.status == STARTED:  # only update if being drawn
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            EndInstructions.keys = theseKeys[-1]  # just the last key pressed
            EndInstructions.rt = EndInstructions.clock.getTime()
            # abort routine on response
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        break
        
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in theInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "theInstructions"-------
for thisComponent in theInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




##PRACTICE rating scale##
#------Prepare to start Routine"theInstructions2"-------

# update component parameters for each repeat
EndInstructions2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
EndInstructions2.status = NOT_STARTED
# keep track of which components have finished
theInstructions2Components = []
theInstructions2Components.append(myRating_example)
theInstructions2Components.append(myInstructionsRating)
theInstructions2Components.append(myInstructions2)
theInstructions2Components.append(EndInstructions2)

for thisComponent in theInstructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#timing info
theInstructions2Clock.reset()  # clock 
frameN = -1

#-------Start Routine "theInstructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = theInstructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *myInstructions* updates
    if t >= 0.0 and myInstructionsRating.status == NOT_STARTED:
        #polyshape=createMask.create_mask_from_vertices(masksize,pentagon.verticesPix)
        #myGrating.mask= polyshape
        myInstructionsRating.tStart = t  # underestimates by a little under one frame
        myInstructionsRating.frameNStart = frameN  # exact frame index
        myInstructionsRating.setAutoDraw(True)
        pentagon.tStart = t  # underestimates by a little under one frame
        pentagon.frameNStart = frameN  # exact frame index
        #MyImage1.setImage(os.getcwd()+'\stimuli\\1604_1.jpg')
        pentagon.setAutoDraw(True)
        myGrating.setAutoDraw(True)
        while myRating_example.noResponse: #show rating scale for 2 secs
            myRating_example.tStart = t  # underestimates by a little under one frame
            myRating_example.frameNStart = frameN  # exact frame index
            myRating_example.draw()
            win.flip()
        myInstructions2.setAutoDraw(True)
        pentagon.setAutoDraw(False)
        myGrating.setAutoDraw(False)
        myRating_Stim.reset()
        event.Mouse(newPos=[0,7.5])
        event.Mouse(visible=False)
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()

    # *EndInstructions* updates
    if t >= 0.0 and EndInstructions2.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndInstructions2.tStart = t  # underestimates by a little under one frame
        EndInstructions2.frameNStart = frameN  # exact frame index
        EndInstructions2.status = STARTED
        # keyboard checking is just starting
        EndInstructions2.clock.reset()  # now t=0
        event.clearEvents()
    if EndInstructions2.status == STARTED:  # only update if being drawn
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            EndInstructions2.keys = theseKeys[-1]  # just the last key pressed
            EndInstructions2.rt = EndInstructions2.clock.getTime()
            # abort routine on response
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        break
        
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in theInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "theInstructions"-------
for thisComponent in theInstructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


InstructionsEndTime = globalClock.getTime()

dataFile.write('Instructions Start, %f\nInstructions End, %f\nTrial_nb,CondBlock,Triplet, CondTriplet, CS1Left, ExpPhase,CondStim,IsSound,CSPlus, ITI_jitter,TimeStimOn,TimeStimOff,TimeSound,ratingOn, ratingKey, ratingRT, ITIOn, Img1, Img2, BreakOn, BreakOff\n' %(InstructionsStartTime, InstructionsEndTime))


  


#start eyetracker recording
pylinkWrapper.startRecording()

 ##Before routine trial starts "preset" first image shape
if thisLoop_Trial['CondStim'] in (3, 6, 9): #first trial is a compound

            if thisLoop_Trial['CS1Left'] == 1: # this is a column in CondOrders_sessx 1 or 0 .If 1 set CS1 in left; else set CS2 in left
                MyImageLeft=MyStim1
                MyImageRight=MyStim2
                    
            else:
                MyImageLeft=MyStim2
                MyImageRight=MyStim1
            #set stim for compound -Left img
            if MyImageLeft == 1:
                #circ.pos=[-1.7,0]
                MyImageLeft=circ
            elif MyImageLeft == 2:
                #sq.pos=[-1.7,0]
                MyImageLeft=sq
            elif MyImageLeft == 4:
                #triangle.pos=[-1.7,-0.4]
                MyImageLeft=triangle
            elif MyImageLeft == 5:
                #gaborcross.pos=[-1.7,0]
                MyImageLeft=gaborcross
            elif MyImageLeft == 7:
                #hexagon.pos=[-1.7,0]
                MyImageLeft=hexagon
            elif MyImageLeft == 8: 
                #semicircRec.pos=[-1.7,0]
                MyImageLeft=semicircRec
            #*MyImageRight* updates
            if MyImageRight == 1:
                #circ.pos=[1.7,0]
                MyImageRight=circ
            elif MyImageRight == 2:
                #sq.pos=[1.7,0]
                MyImageRight=sq
            elif MyImageRight == 4:
                #triangle.pos=[1.7,-0.4]
                MyImageRight=triangle
            elif MyImageRight == 5:
                #gaborcross.pos=[1.7,0]
                MyImageRight=gaborcross
            elif MyImageRight == 7:
                #hexagon.pos=[1.7,0]
                MyImageRight=hexagon
            elif MyImageRight == 8: 
                #semicircRec.pos=[1.7,0]
                MyImageRight=semicircRec
            polyShapeLeft = createMask.create_mask_from_vertices(math.ceil(MyImageLeft.size[0]/deg_per_px),MyImageLeft.verticesPix)
            polyShapeRight = createMask.create_mask_from_vertices(math.ceil(MyImageRight.size[0]/deg_per_px),MyImageRight.verticesPix)
            myGratingLeft.mask=polyShapeLeft
            myGratingRight.mask=polyShapeRight
            myGratingLeft.size=math.ceil(MyImageLeft.size[0]/deg_per_px)
            myGratingRight.size=math.ceil(MyImageRight.size[0]/deg_per_px)
            if MyImageLeft ==circ:
                circ.pos=[-1.7, 0]
            elif MyImageLeft == sq :
                sq.pos=[-1.7, 0]
            elif MyImageLeft== triangle:
                triangle.pos=[-1.7, -0.4]
            elif MyImageLeft == gaborcross:
                gaborcross.pos=[-1.7, 0]
            elif MyImageLeft == hexagon:
                hexagon.pos=[-1.7, 0]
            elif MyImageLeft == semicircRec:
                polyShapeLeft= createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),MyImageLeft.verticesPix)
                myGratingLeft.mask=polyShapeLeft
                myGratingLeft.size=math.ceil(circ.size[0]/deg_per_px)
                semicircRec.pos=[-1.7, 0]
            if MyImageRight ==circ:
                circ.pos=[1.7, 0]
            elif MyImageRight == sq :
                sq.pos=[1.7, 0]
            elif MyImageRight== triangle:
                triangle.pos=[1.7, -0.4]
            elif MyImageRight == gaborcross:
                gaborcross.pos=[1.7, 0]
            elif MyImageRight== hexagon:
                hexagon.pos=[1.7, 0]
            elif MyImageRight == semicircRec:
                polyShapeRight= createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),MyImageRight.verticesPix)
                myGratingRight.mask=polyShapeRight
                myGratingRight.size=math.ceil(circ.size[0]/deg_per_px)
                semicircRec.pos=[1.7, 0]
#            MyImageRight.pos[0]=1.7
#            MyImageLeft.pos[0]=-1.7
            myGratingLeft.pos= np.array(MyImageLeft.pos)/deg_per_px
            myGratingRight.pos= np.array(MyImageRight.pos)/deg_per_px

else: #not a compound

            stim1=MyStim1
            print "stim 1=  ",  stim1
            stim2=MyStim2
            print "stim 2=  ",  stim2
            if stim1 == 1:
                stim1=circ
            elif stim1 == 2:
                stim1=sq
            elif stim1== 4:
                stim1=triangle
            elif stim1== 5:
                stim1=gaborcross
            elif stim1== 7:
                stim1=hexagon
            elif stim1 == 8:
                stim1=semicircRec
            
            if stim2== 1:
                stim2=circ
            elif stim2== 2:
                stim2=sq
            elif stim2== 4:
                stim2=triangle
            elif stim2== 5:
                stim2=gaborcross
            elif stim2== 7:
                stim2=hexagon
            elif stim2== 8:
                stim2=semicircRec
                
            if thisLoop_Trial['CondStim'] in (1, 4, 7): #CS1
                if stim1==semicircRec:
                    polyShape = createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),stim1.verticesPix)
                else:
                    polyShape = createMask.create_mask_from_vertices(math.ceil(stim1.size[0]/deg_per_px),stim1.verticesPix)
                myGrating.mask=polyShape
                if stim1==semicircRec:
                    myGrating.size=math.ceil(circ.size[0]/deg_per_px)
                else:
                    myGrating.size=math.ceil(stim1.size[0]/deg_per_px)
                if stim1==triangle:
                    triangle.pos=[0, -0.4]
                myGrating.pos=np.array(stim1.pos)/deg_per_px
            elif thisLoop_Trial['CondStim'] in (2, 5, 8): #CS2
                if stim2==semicircRec:
                    polyShape = createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),stim2.verticesPix)#  Un error aqui decia stim1 en vez de stim2
                else:
                    polyShape = createMask.create_mask_from_vertices(math.ceil(stim2.size[0]/deg_per_px),stim2.verticesPix) #
                myGrating.mask=polyShape
                if stim2==semicircRec:
                    myGrating.size=math.ceil(circ.size[0]/deg_per_px)
                else:
                    myGrating.size=math.ceil(stim2.size[0]/deg_per_px)
                if stim2==triangle:
                    triangle.pos=[0, -0.4]
                myGrating.pos=np.array(stim2.pos)/deg_per_px


try:
    for thisLoop_Condition in Loop_Conditions:
        currentLoop = Loop_Conditions
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_Condition.rgb)

    

        if Loop_Conditions.thisIndex >=2:
        #------Prepare to start Routine"theBreak"-------
#
#            # update component parameters for each repeat
            EndBreak = event.BuilderKeyResponse()  # create an object of type KeyResponse
            EndBreak.status = NOT_STARTED
            # keep track of which components have finished
            theBreakComponents = []
            theBreakComponents.append(myBreak)
            theBreakComponents.append(EndBreak)
            for thisComponent in theBreakComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            #timing info
            theBreakClock.reset()  # clock 
            frameN = -1
            routineTimer.reset()
            routineTimer.add(120.000000) 
#            #-------Start Routine "theEnd"-------
#            while routineTimer.getTime() > 0:
#            # get current time
    # update/draw components on
            #-------Start Routine "theBreak"-------
            continueRoutine = True
            while routineTimer.getTime() > 0:
            #while continueRoutine:
                # get current time
                t = theBreakClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *myBreak* updates
                if t >= 0.0 and myBreak.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    myBreak.tStart = t  # underestimates by a little under one frame
                    myBreak.frameNStart = frameN  # exact frame index
                    myBreak.setAutoDraw(True)
                    BreakStartTime = globalClock.getTime()
                    myRating_Stim.draw(False)
                    pylinkWrapper.sendTrialMsg('BREAK_ON')
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
            
                # *EndBreak* updates
                if t >= 0.0 and EndBreak.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    EndBreak.tStart = t  # underestimates by a little under one frame
                    EndBreak.frameNStart = frameN  # exact frame index
                    EndBreak.status = STARTED
                    # keyboard checking is just starting
                    EndBreak.clock.reset()  # now t=0
                    event.clearEvents()
                if EndBreak.status == STARTED:  # only update if being drawn
                    theseKeys = event.getKeys()
                    if len(theseKeys) > 0:  # at least one key was pressed
                        EndBreak.keys = theseKeys[-1]  # just the last key pressed
                        EndBreak.rt = EndBreak.clock.getTime()
                        # abort routine on response
                        continueRoutine = False
                
                # check if all components have finished

                
                if routineTimer.getTime()<=30:
                    myBreak.setText('The Break is ending in 30 secs.\n Please take your position in the chin rest to resume the experiment')
                
                
                if not continueRoutine:  # a component has requested that we end
                    break
                    continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in theBreakComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "theBreak"-------
            for thisComponent in theBreakComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    pylinkWrapper.sendTrialMsg('BREAK_OFF')
            
            BreakEndTime = globalClock.getTime()
            myBreak.setText('This block has ended.\n Please take a break.\nThe experiment will start again in 2 minutes')
            dataFile.write('%f, %f, %s, %f, %f, %f, %f, %f, %f, %f, %f, %f,%f,%f, %s, %f, %f,  %s, %s, %f, %f\n'  
            %(float('NaN'), float('NaN'), 'nan',float('NaN'),float('NaN'), float('NaN'), float('NaN'), float('NaN'), float('NaN'), float('NaN'),
            float('NaN'), float('NaN'),  float('NaN'),float('NaN'),'nan', float('NaN'),float('NaN'),'nan', 'nan', BreakStartTime, BreakEndTime))
            # NaN, 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN','NaN'

    #------Prepare to start Routine"TheFix"-------
    # update component parameters for each repeat
    # keep track of which components have finished
        TheFixComponents = []
        TheFixComponents.append(Fixation)
        for thisComponent in TheFixComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        
        if Loop_Conditions.thisIndex + 1 == 1:
            Fixation.setHeight=.1
            Fixation.setText('Experiment Part 1')
            
            
        #elif Loop_Conditions.thisIndex + 1 == 4:
        #    Fixation.setText('Experiment Part 2, Block 1')

        elif Loop_Conditions.thisIndex + 1 == 2:
            Fixation.setHeight=.1
            Fixation.setText('Experiment Part 2 \n' +
                    'Block ' + str(Loop_Conditions.thisIndex + 1 - 1))
            # Puts a text indicating that new block
        else:
            if Loop_Conditions.thisIndex + 1 <= 5:
                Fixation.setHeight=.1
                Fixation.setText('Block ' + str(Loop_Conditions.thisIndex + 1 - 1))
                #print str(Loop_Conditions.thisIndex)
            else:
                Fixation.setHeight=.1
                Fixation.setText('Experiment Part 3')
        routineTimer.reset()
        routineTimer.add(3.000000)# show "Experiment Part ..." for 1 sec, fixation for 2 sec
            
        #timing info
        TheFixClock.reset()  # clock 
        frameN = -1
        
        
        
        #-------Start Routine "TheFix"-------
        BlockBegin = 0
        ##msg = 'TRIALID 0 %d' %CondBlock
        ##pylinkWrapper.sendTrialMsg(msg)
        while routineTimer.getTime() > 0:
            # get current time
            t = TheFixClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation* updates
            if Fixation.status == NOT_STARTED:
                Fixation.setHeight=.8
                # keep track of start time/frame for later
                Fixation.tStart = t  # underestimates by a little under one frame
                Fixation.frameNStart = frameN  # exact frame index
                Fixation.setAutoDraw(True)
                pylinkWrapper.sendTrialMsg('BLOCK ON')
                
            if routineTimer.getTime()<=2 and BlockBegin == 0: #ha pasado un sec
                Fixation.setText('+')
                #peripheralsmanager.blockOn(CondBlock)
                routineTimer.reset()
                routineTimer.add(2.000000)
                BlockBegin = 1
                pylinkWrapper.sendTrialMsg('BLOCK OFF')
                
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                raise EscapeError()
                
            win.flip()
        
        #-------Ending Routine "TheFix"-------
        for thisComponent in TheFixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
#        #pylinkWrapper.sendTrialMsg('!V TRIAL_VAR CS1ID ' + MyImage1.image)
#        #pylinkWrapper.sendTrialMsg('!V TRIAL_VAR CS2ID ' + MyImage2.image)
#        #pylinkWrapper.sendTrialMsg('!V TRIAL_VAR CSSAFEID ' + MyImage3.image)
        
        #pylinkWrapper.sendTrialMsg('TRIAL_RESULT')
        
       
                

        ##Loop over trials starts
        
        routineTimer.reset()
        for thisLoop_Trial in Loop_Trials:
            print "trial =", thisLoop_Trial #prints: trial = {'ExpPhase': 2, 'MyStim1': u'11276_1.jpg', 'MyStim2': u'11825_1.jpg', 'ITI_jitter': 2.5, 'IsSound': 1, 'CondStim': 6, 'CS1Left': 0, 'Block': 2, 'CondTriplet': 2}
            
            currentLoop = Loop_Trials
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_Trial.rgb)
            if thisLoop_Trial != None:
                #if thisLoop_Trial != 1:
                    for paramName in thisLoop_Trial.keys():
                        exec(paramName + '= thisLoop_Trial.' + paramName)
                
            
            #------Prepare to start Routine"Trial"-------
            #pylinkWrapper.sendTrialMsg('TRIALID %d' %(Loop_Trials.thisIndex+1))
            TrialComponents = []
            
            #if CS1Left[1 :] == 1: # this is a column in CondOrders_sessx 1 or 0 .If 1 set CS1 in left; else set CS2 in left
#                MyImageLeft.setImage('stimuli' + os.path.sep + MyStim1)
#                MyImageRight.setImage('stimuli' + os.path.sep + MyStim2)
#                MyImageLeft=MyStim1
#                MyImageRight=MyStim2

#            else:
#                MyImageLeft.setImage('stimuli' + os.path.sep + MyStim2)
#                MyImageRight.setImage('stimuli' + os.path.sep + MyStim1)
#                MyImageLeft=stim1
#                MyImageRight=MyStim1
            #stim1=MyStim1
            #stim2=MyStim2
            #MyImage1.setImage('stimuli' + os.path.sep + MyStim1)
            #MyImage2.setImage('stimuli' + os.path.sep + MyStim2)
            
            if CondStim in (3, 6,  9): #(or compound) cond Stim 1 = CS1, 2= CS2; 3= Comp; 4 =Safe
                # update component parameters for each repeat for compound presentation
                print "Condstim= ", CondStim 
                TrialComponents.append(MyImageRight)
                TrialComponents.append(MyImageLeft)
#                TrialComponents.append(stim1)
#                TrialComponents.append(stim2)
                TrialComponents.append(myGratingLeft)
                TrialComponents.append(myGratingRight)
            elif CondStim in (1, 4, 7):
                # update component parameters for each repeat for only one stimulus 
                print 'CondStim= ', CondStim
#                polyShape = createMask.create_mask_from_vertices(masksize,stim1.verticesPix)
#                myGrating.mask=polyShape
                TrialComponents.append(MyStim1)
                TrialComponents.append(stim1)
                TrialComponents.append(myGrating)
            elif CondStim in (2, 5, 8):
                print 'CondStim= ', CondStim
#                polyShape = createMask.create_mask_from_vertices(masksize,stim2.verticesPix)
#                myGrating.mask=polyShape
                TrialComponents.append(MyStim2)
                TrialComponents.append(stim2)
                TrialComponents.append(myGrating)
            if IsSound:
                TrialComponents.append(MySound)
            TrialComponents.append(myITI)
            
            # keep track of which components have finished
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #timing info
            TotalTime = 4 + ITI_jitter # trial duration 4 secs + 3.25 ITI
            TrialClock.reset()  # clock 
            routineTimer.reset()
            frameN = -1
            routineTimer.add(TotalTime) #7.25 secs
            

            #-------Start Routine "Trial"-------
            myRating_Stim.reset()
            event.Mouse(newPos=[0,7.5])
            event.Mouse(visible=True)
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TrialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame     
                StimOns = 0
                StimOff = 0
                # *myImage* updates
                myRating_Stim.tStart = t  # underestimates by a little under one frame
                myRating_Stim.frameNStart = frameN  # exact frame index
                myRating_Stim.draw()
                ratingOn=globalClock.getTime()
                #win.flip()
                if CondStim in (3, 6, 9) : #if compound
                    #print " currently presenting Compound" , CondStim
                    if t >= 0.0 and MyImageLeft.status == NOT_STARTED and routineTimer.getTime() > TotalTime - ITI_jitter: #routine timer mayor a 3.25
                        # keep track of start time/frame for later
                        MyImageLeft.tStart = t  # underestimates by a little under one frame
                        MyImageLeft.frameNStart = frameN  # exact frame index
                        MyImageLeft.setAutoDraw(True)
                        myGratingLeft.setAutoDraw(True)
                        MyImageRight.tStart = t  # underestimates by a little under one frame
                        MyImageRight.frameNStart = frameN  # exact frame index
                        MyImageRight.setAutoDraw(True)
                        myGratingRight.setAutoDraw(True)
                        pylinkWrapper.sendTrialMsg('DISPLAY ON')
                        MyStimStart = globalClock.getTime()
                        peripheralsmanager.compoundCSOn()
                        #event.Mouse(visible=True)
                        StimOns = 1
                        if int(CSPlus) ==1: 
                            print " this is a CSPLUS"
                            peripheralsmanager.CSPlusOn()
                            pylinkWrapper.sendTrialMsg('CSPLUS_ON')
                            peripheralsmanager.CondTripletOn(int(CondTriplet))
                        else:
                            print " this is a CSMinus"
                            peripheralsmanager.CSMinusOn()
                            pylinkWrapper.sendTrialMsg('CSMINUS_ON')
                            if int(CondTriplet) != 3:
                                print "current CondTriplet is :", CondTriplet
                                peripheralsmanager.CondTripletOn(int(CondTriplet))
                        #print "My image Right is" , MyImageRight.image,"My image Left is" , MyImageLeft.image
                    #elif MyImageLeft.status == STARTED and routineTimer.getTime() <(ITI_jitter + 2): #timer is less  or equal to 5.25 (han pasado 2 secs)
                    elif  MyImageLeft.status == STARTED and (ITI_jitter +2) > routineTimer.getTime() > ITI_jitter: #5.25 > time <3.25
#                        if myRating_Stim.noResponse==False:
#                            event.Mouse(visible=False)
                        #pylinkWrapper.sendTrialMsg('RATING ON')
                        ratingKey=myRating_Stim.getHistory()[-1][0]
                        ratingRT=myRating_Stim.getRT()
                        curKey.append(ratingKey)
                        curRT.append(ratingRT)
                        event.Mouse(newPos=[5,-7])
                        event.Mouse(visible=False)
                        myRating_Stim.reset()

                    elif MyImageLeft.status == STARTED and routineTimer.getTime() < (ITI_jitter): #timer menor a 3.25 sec
                        MyImageLeft.setAutoDraw(False)
                        MyImageRight.setAutoDraw(False)
                        myGratingLeft.setAutoDraw(False)
                        myGratingRight.setAutoDraw(False)
                        StimOff = 1
                elif CondStim in (1, 4, 7): #CS1 
                    if t >= 0.0 and stim1.status == NOT_STARTED and routineTimer.getTime() > TotalTime - ITI_jitter:
                        stim1.tStart = t  # underestimates by a little under one frame
                            # keep track of start time/frame for later
                        stim1.tStart = t  # underestimates by a little under one frame
                        stim1.frameNStart = frameN  # exact frame index
                        stim1.setAutoDraw(True)
                        myGrating.setAutoDraw(True)
                        pylinkWrapper.sendTrialMsg('DISPLAY ON')
                        MyStimStart = globalClock.getTime()
                        peripheralsmanager.singleCSOn()
                        #event.Mouse(visible=True)
                        StimOns = 1
                        if int(CSPlus)==1: 
                            peripheralsmanager.CSPlusOn()
                            pylinkWrapper.sendTrialMsg('CSPLUS_ON')
                            peripheralsmanager.CondTripletOn(int(CondTriplet))
                        else:
                            peripheralsmanager.CSMinusOn()
                            pylinkWrapper.sendTrialMsg('CSMINUS_ON')
                            if int(CondTriplet) != 3:
                                print "current CondTriple is :", CondTriplet
                                peripheralsmanager.CondTripletOn(int(CondTriplet))
                    elif  stim1.status == STARTED and (ITI_jitter +2) > routineTimer.getTime() > ITI_jitter:#2 secs have pass
#                        if myRating_Stim.noResponse==False:
#                            #event.Mouse(newPos=[0,7.5]
                        #event.Mouse(visible=False)
                        ratingKey=myRating_Stim.getHistory()[-1][0]
                        ratingRT=myRating_Stim.getRT()
                        curKey.append(ratingKey)
                        curRT.append(ratingRT)
                        event.Mouse(newPos=[5,-7])
                        event.Mouse(visible=False)
                        myRating_Stim.reset()
                        #pylinkWrapper.sendTrialMsg('RATING ON')
                    elif stim1.status == STARTED and routineTimer.getTime() < (ITI_jitter):
                        stim1.setAutoDraw(False)
                        myGrating.setAutoDraw(False)
                        #event.Mouse(visible=False)
                        #pylinkWrapper.sendTrialMsg('DISPLAY OFF')
                        #MyStimOff = globalClock.getTime()
                        StimOff = 1
                elif CondStim in (2, 5, 8):
                    #polyShape = createMask.create_mask_from_vertices(masksize,stim2.verticesPix)
                    #myGrating.mask=polyShape
                    if t >= 0.0 and stim2.status == NOT_STARTED and routineTimer.getTime() > TotalTime - ITI_jitter:
                        stim2.tStart = t  
                        stim2.tStart = t  # underestimates by a little under one frame
                        stim2.frameNStart = frameN  # exact frame index
                        stim2.setAutoDraw(True)
                        myGrating.setAutoDraw(True)
                        pylinkWrapper.sendTrialMsg('DISPLAY ON')
                        MyStimStart = globalClock.getTime()
                        peripheralsmanager.singleCSOn()
                        #event.Mouse(visible=True)
                        StimOns = 1
                        if int(CSPlus)==1: 
                            peripheralsmanager.CSPlusOn()
                            pylinkWrapper.sendTrialMsg('CSPLUS_ON')
                            peripheralsmanager.CondTripletOn(int(CondTriplet))
                        else:
                            peripheralsmanager.CSMinusOn()
                            pylinkWrapper.sendTrialMsg('CSMINUS_ON')
                            if int(CondTriplet) != 3:
                                print "current CondTriple is :", CondTriplet
                                peripheralsmanager.CondTripletOn(int(CondTriplet))
                    elif stim2.status == STARTED and (ITI_jitter +2) > routineTimer.getTime() > ITI_jitter:
                        #if myRating_Stim.noResponse==False:
                            #event.Mouse(newPos=[0,7.5])
                        #event.Mouse(visible=False)
                        ratingKey=myRating_Stim.getHistory()[-1][0]
                        ratingRT=myRating_Stim.getRT()
                        curKey.append(ratingKey)
                        curRT.append(ratingRT)
                        event.Mouse(newPos=[5,-7])
                        event.Mouse(visible=False)
                        myRating_Stim.reset()
#                        event.Mouse(visible=True)
#                        ratingOn=globalClock.getTime()
#                        pylinkWrapper.sendTrialMsg('RATING ON')
#                        while routineTimer.getTime() > (ITI_jitter):
#                        #while myRating_Stim.noResponse:
#                                myRating_Stim.tStart = t  # underestimates by a little under one frame
#                                myRating_Stim.frameNStart = frameN  # exact frame index
#                                myRating_Stim.draw()
#                                win.flip()
#                                if myRating_Stim.noResponse==False:
#                                    event.Mouse(visible=False)
#                        #rtKey=globalClock.getTime()
#                        #pylinkWrapper.sendTrialMsg('RATING_Click')
#                        ratingKey=myRating_Stim.getHistory()[-1][0]
#                        ratingRT=myRating_Stim.getRT()
#                        #ratingKey=myRating_Stim.getRating()
#                        myRating_Stim.reset()
#                        event.Mouse(newPos=[0,7.5])
#                        event.Mouse(visible=False)

                    elif stim2.status == STARTED and routineTimer.getTime() < (ITI_jitter):
                        stim2.setAutoDraw(False)
                        myGrating.setAutoDraw(False)
                        #event.Mouse(visible=False)
                        StimOff = 1
                       
                if IsSound: # a shock will be delivered
                    #if routineTimer.getTime() <= (ITI_jitter + MySound.getDuration()) and MySound.status == NOT_STARTED: #whenroutine timer menor a 4secs 
                    if routineTimer.getTime() <= (ITI_jitter) and MySound.status == NOT_STARTED: #whenroutine timer menor a 3.25 (
                        # keep track of start time/frame for later
                        MySound.tStart = t  # underestimates by a little under one frame
                        MySound.frameNStart = frameN  # exact frame index
                        ##peripheralsmanager.shockOn()
                        routineTimer.reset()
                        #routineTimer.add(ITI_jitter + MySound.getDuration())# adding 4 secs to timer
                        routineTimer.add(ITI_jitter)# adding 3.25 secs to timer
                        MySoundStart = globalClock.getTime()
                        peripheralsmanager.shockOn()
                        MySound.play()  # start the sound (it finishes automatically)
                        pylinkWrapper.sendTrialMsg('SOUND_ON')
                        ##peripheralsmanager.CSPlusOn()
                        print "sound duration is :", MySound.getDuration()
                        ##core.wait(MySound.getDuration())
                    elif MySound.status == STARTED and routineTimer.getTime() < (ITI_jitter- MySound.getDuration()) : #if routine gets to less than3.25, reset it and and 3.25
                        peripheralsmanager.shockOff()
                        ##peripheralsmanager.CSPlusOff()
                        #routineTimer.reset()
                        #routineTimer.add(ITI_jitter)
                        MySound.stop()  # stop the sound (if longer than duration)
                        pylinkWrapper.sendTrialMsg('SOUND_OFF')
                else: MySoundStart = 0
                
            ## *myITI* updates + Ratings for sess10, ExpPhase 3
                #if routineTimer.getTime() <= (ITI_jitter) and myITI.status == NOT_STARTED:
                
                continueRoutine = False  # will revert to True if at least one component still running
  
                for thisComponent in TrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    raise EscapeError()
                
                # refresh the screen
                
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen\
                    #event.Mouse(visible=False)
                    if StimOns == 1:
                        print  " the stim is ON"
                        #peripheralsmanager.stimOn(int(CondStim))
                        ##pylinkWrapper.sendTrialMsg('DISPLAY ON')
                        #MyStimStart = globalClock.getTime()
#                        routineTimer.reset()
#                        routineTimer.add(TotalTime) 
                    if StimOff == 1:
                        #event.Mouse(visible=False)
                        pylinkWrapper.sendTrialMsg('DISPLAY OFF')
                        MyStimOff = globalClock.getTime()
                        routineTimer.reset()
                        routineTimer.add(ITI_jitter)
                        ITIOn=globalClock.getTime()
                        pylinkWrapper.sendTrialMsg('ITI ON')
                        print "CS Duration",  (MyStimOff - MyStimStart)
                        ##peripheralsmanager.stimOff()
                        peripheralsmanager.singleCSOff()
                        peripheralsmanager.compoundCSOff()
                        if int(CSPlus)==1: 
                            peripheralsmanager.CSPlusOff()
                        else:
                            peripheralsmanager.CSMinusOff()
                        peripheralsmanager.CondTripletOff(int(CondTriplet))

                        if CondStim in (3, 6, 9): #reset position
                            circ.pos= [0,0]
                            sq.pos=[0,0]
                            gaborcross.pos=[0,0]
                            hexagon.pos=[0,0]
                            semicircRec.pos=[0,0]
                            if thisLoop_Trial['CS1Left'] == 1: # this is a column in CondOrders_sessx 1 or 0 .If 1 set CS1 in left; else set CS2 in left
                                stim1Name=MyImageLeft.name
                                stim2Name=MyImageRight.name
                            else:
                                stim1Name=MyImageRight.name
                                stim2Name=MyImageLeft.name
                        triangle.pos=[0,0]
                        if CondStim in (1,2,4,5,7,8): 
                            stim1Name=stim1.name
                            stim2Name=stim2.name
                        if Loop_Trials.nRemaining > 0:
                            nextTr=Loop_Trials.trialList[Loop_Trials.thisIndex+1]
                            if nextTr['CondStim'] in (3, 6, 9):#a compound is next
                                        if nextTr['CS1Left'] == 1: # this is a column in CondOrders_sessx 1 or 0 .If 1 set CS1 in left; else set CS2 in left
                                            MyImageLeft=nextTr['MyStim1']
                                            MyImageRight=nextTr['MyStim2']
                                
                                        else:
                                            MyImageLeft=nextTr['MyStim2']
                                            MyImageRight=nextTr['MyStim1']
                                        if MyImageLeft == 1:
                                                #circ.pos=[-1.7,0]
                                                MyImageLeft=circ
                                        elif MyImageLeft == 2:
                                                #sq.pos=[-1.7,0]
                                                MyImageLeft=sq
                                        elif MyImageLeft == 4:
                                                #triangle.pos=[-1.7,-0.4]
                                                MyImageLeft=triangle
                                        elif MyImageLeft == 5:
                                                #gaborcross.pos=[-1.7,0]
                                                MyImageLeft=gaborcross
                                        elif MyImageLeft == 7:
                                                #hexagon.pos=[-1.7,0]
                                                MyImageLeft= hexagon
                                        elif MyImageLeft == 8: 
                                                #semicircRec.pos=[-1.7,0]
                                                MyImageLeft=semicircRec
                                            #*MyImageRight* updates
                                        if MyImageRight == 1:
                                                #circ.pos=[1.7,0]
                                                MyImageRight=circ
                                        elif MyImageRight == 2:
                                                #sq.pos=[1.7,0]
                                                MyImageRight=sq
                                        elif MyImageRight == 4:
                                                #triangle.pos=[1.7,-0.4]
                                                MyImageRight=triangle
                                        elif MyImageRight == 5:
                                                #gaborcross.pos=[1.7,0]
                                                MyImageRight=gaborcross
                                        elif MyImageRight == 7:
                                                #hexagon.pos=[1.7,0]
                                                MyImageRight=hexagon
                                        elif MyImageRight == 8: 
                                                #semicircRec.pos=[1.7,0]
                                                MyImageRight=semicircRec
                                        polyShapeLeft = createMask.create_mask_from_vertices(math.ceil(MyImageLeft.size[0]/deg_per_px),MyImageLeft.verticesPix)
                                        polyShapeRight = createMask.create_mask_from_vertices(math.ceil(MyImageRight.size[0]/deg_per_px),MyImageRight.verticesPix)
                                        myGratingLeft.mask=polyShapeLeft
                                        myGratingRight.mask=polyShapeRight
                                        myGratingLeft.size=math.ceil(MyImageLeft.size[0]/deg_per_px)
                                        myGratingRight.size=math.ceil(MyImageRight.size[0]/deg_per_px)
                                        if MyImageLeft ==circ:
                                            circ.pos=[-1.7, 0]
                                        elif MyImageLeft == sq :
                                            sq.pos=[-1.7, 0]
                                        elif MyImageLeft== triangle:
                                            triangle.pos=[-1.7, -0.4]
                                        elif MyImageLeft == gaborcross:
                                            gaborcross.pos=[-1.7, 0]
                                        elif MyImageLeft == hexagon:
                                            hexagon.pos=[-1.7, 0]
                                        elif MyImageLeft == semicircRec:
                                            polyShapeLeft= createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),MyImageLeft.verticesPix)
                                            myGratingLeft.mask=polyShapeLeft
                                            myGratingLeft.size=math.ceil(circ.size[0]/deg_per_px)
                                            semicircRec.pos=[-1.7, 0]
                                        if MyImageRight ==circ:
                                            circ.pos=[1.7, 0]
                                        elif MyImageRight == sq :
                                            sq.pos=[1.7, 0]
                                        elif MyImageRight== triangle:
                                            triangle.pos=[1.7, -0.4]
                                        elif MyImageRight == gaborcross:
                                            gaborcross.pos=[1.7, 0]
                                        elif MyImageRight== hexagon:
                                            hexagon.pos=[1.7, 0]
                                        elif MyImageRight == semicircRec:
                                            polyShapeRight= createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),MyImageRight.verticesPix)
                                            myGratingRight.mask=polyShapeRight
                                            myGratingRight.size=math.ceil(circ.size[0]/deg_per_px)
                                            semicircRec.pos=[1.7, 0]
                                        
#                                        MyImageRight.pos[0]=1.7
#                                        MyImageLeft.pos[0]=-1.7
                                      
#                                        if MyImageLeft== triangle:
#                                            MyImageLeft.pos=[-1.7, -0.4]
#                                        else: 
#                                            MyImageLeft.pos[0]=-1.7
#                                        if MyImageRight== triangle:
#                                            MyImageRight.pos=[1.7, -0.4]
#                                        else: 
#                                            MyImageRight.pos[0]=1.7
                                        myGratingLeft.pos= np.array(MyImageLeft.pos)/deg_per_px
                                        myGratingRight.pos= np.array(MyImageRight.pos)/deg_per_px
                                                                    
                                                    
                            else: #not a compound
                                    if nextTr['MyStim1']==1 :
                                        stim1=circ
                                    elif nextTr['MyStim1']==2:
                                        stim1=sq
                                    elif nextTr['MyStim1']==4:
                                        stim1=triangle
                                    elif nextTr['MyStim1']==5:
                                        stim1=gaborcross
                                    elif  nextTr['MyStim1']==7:
                                        stim1=hexagon
                                    elif nextTr['MyStim1']==8:
                                        stim1=semicircRec
                                    
                                    if nextTr['MyStim2']==1 :
                                        stim2=circ
                                    elif nextTr['MyStim2']==2:
                                        stim2=sq
                                    elif nextTr['MyStim2']==4:
                                        stim2=triangle
                                    elif nextTr['MyStim2']==5:
                                        stim2=gaborcross
                                    elif  nextTr['MyStim2']==7:
                                        stim2=hexagon
                                    elif nextTr['MyStim2']==8:
                                        stim2=semicircRec
                                    if nextTr['CondStim'] in (1, 4, 7):   
                                        if stim1==semicircRec:
                                            polyShape = createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),stim1.verticesPix)
                                            myGrating.size=math.ceil(circ.size[0]/deg_per_px)
                                        else:
                                            polyShape = createMask.create_mask_from_vertices(math.ceil(stim1.size[0]/deg_per_px),stim1.verticesPix)
                                            myGrating.size=math.ceil(stim1.size[0]/deg_per_px)
                                        myGrating.mask=polyShape
                                        if stim1==triangle:
                                            triangle.pos=[0,-0.4]
                                        myGrating.pos=np.array(stim1.pos)/deg_per_px
                                        
                                    elif nextTr['CondStim'] in (2, 5, 8):
                                        if stim2==semicircRec:
                                            polyShape = createMask.create_mask_from_vertices(math.ceil(circ.size[0]/deg_per_px),stim2.verticesPix)
                                            myGrating.size=math.ceil(circ.size[0]/deg_per_px)
                                        else:
                                            polyShape = createMask.create_mask_from_vertices(math.ceil(stim2.size[0]/deg_per_px),stim2.verticesPix)
                                            myGrating.size=math.ceil(stim2.size[0]/deg_per_px)
                                        myGrating.mask=polyShape
                                        if stim2==triangle:
                                            triangle.pos=[0, -0.4]
                                        myGrating.pos=np.array(stim2.pos)/deg_per_px
                                        
                        ITIelapsed = globalClock.getTime()- ITIOn
                        ITIRemaining = ITI_jitter - ITIelapsed
                        routineTimer.reset()
                        routineTimer.add(ITIRemaining)
                        
                        print "how long it took to preset images = ", ITIelapsed
                        print "ITIRemaining", ITIRemaining
#                        while routineTimer.getTime() > (ITIRemaining):
#                            event.Mouse(visible=False)
                        #event.clearEvents()
                        #event.Mouse(visible=False)
                    win.flip()
                

            
            #-------Ending Routine "Trial"-------
          
            dataFile.write('%f, %f, %s, %f, %f, %f, %f, %f, %f, %f, %f, %f,%f,%f, %s, %f,%f, %s, %s\n' 
            %(Loop_Trials.thisIndex+1, Block, Triplet, CondTriplet, CS1Left, ExpPhase, CondStim,
            IsSound, CSPlus, ITI_jitter, MyStimStart, MyStimOff, MySoundStart,ratingOn, curKey[0], curRT[0], ITIOn,
            stim1Name, stim2Name)) 

            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR TRIALID ' + str(Loop_Trials.thisIndex+1))
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR COND %d' %Block)
            ##pylinkWrapper.sendTrialMsg('!V TRIAL_VAR TRIPLET %s' %Triplet)
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR TRIPLET %d' %CondTriplet)
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR CS1LEFT %d' %CS1Left)
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR PHASE %d' %ExpPhase)
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR STIM %d' %CondStim)
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR CSPLUS %d' %CSPlus)
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR SOUND %d' %IsSound)
            ##pylinkWrapper.sendTrialMsg('!V TRIAL_VAR RATINGON %d' %ratingOn)#global clock time
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR RATINGKEY %s' %curKey[0])
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR RATINGRT %f' %curRT[0]) #global time  when 2 secs have passed
            ##pylinkWrapper.sendTrialMsg('!V TRIAL_VAR ITION %d' %ITIOn) #global clock
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR CS1ID ' + stim1Name)
            pylinkWrapper.sendTrialMsg('!V TRIAL_VAR CS2ID ' + stim2Name)

            curKey=[]
            curRT=[]
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #pylinkWrapper.sendTrialMsg('TRIAL_RESULT')
#    #        if Loop_Trials.thisIndex >= 5:
#    #            break
                
            if Loop_Trials.nRemaining > 1:
                if (ExpPhase == 3 and not Loop_Trials.getFutureTrial(1).ExpPhase == 3) or not Block == Loop_Trials.getFutureTrial(1).Block or (ExpPhase == 1 and Loop_Trials.getFutureTrial(1).ExpPhase == 2):
                    break #break exphase ==2  and block is different
            
            
        # completed 1 repeats of 'Loop_Trials'
        #peripheralsmanager.blockOff()
    #    if Loop_Trials.thisIndex >= 5:
    #        break
        thisExp.nextEntry()
        
        
        
    # completed 1 repeats of 'Loop_Conditions' or one block
    for thisComponent in TrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
    
        
    #------Prepare to start Routine"TheFix"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    TheFixComponents = []
    TheFixComponents.append(Fixation)
    
    Fixation.setText('+')
    for thisComponent in TheFixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #timing info
    TheFixClock.reset()  # clock 
    frameN = -1
    routineTimer.reset()
    routineTimer.add(2) #fixation before block starts for 2 sec
    #-------Start Routine "TheFix"-------
    while routineTimer.getTime() > 0:
        # get current time
        t = TheFixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t  # underestimates by a little under one frame
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            raise EscapeError()
        
        win.flip()
    
    #-------Ending Routine "TheFix"-------
    for thisComponent in TheFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

except EscapeError as myerror:
    myEnd.setText('Experimenter terminated the session.')
    myErrorTime = globalClock.getTime()
    dataFile.write('Experimenter terminated the session at time %f' %(myErrorTime))

except Exception as myerror: 
    myEnd.setText('There was an error in the script, please tell the experimenter.')
    myErrorTime = globalClock.getTime()
    print myerror
    dataFile.write(str(myerror) + ' at time %f' %(myErrorTime))


for thisComponent in TrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

#------Prepare to start Routine"theEnd"-------

# update component parameters for each repeat
# keep track of which components have finished
theEndComponents = []
theEndComponents.append(myEnd)
for thisComponent in theEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#timing info
theEndClock.reset()  # clock 
frameN = -1
routineTimer.reset()
routineTimer.add(5.000000)
#-------Start Routine "theEnd"-------
while routineTimer.getTime() > 0:
    # get current time0
    t = theEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *myEnd* updates
    if t >= 0.0 and myEnd.status == NOT_STARTED:
        # keep track of start time/frame for later
        myEnd.tStart = t  # underestimates by a little under one frame
        myEnd.frameNStart = frameN  # exact frame index
        myEnd.setAutoDraw(True)
        myEndStart = globalClock.getTime()
        print "we have reached the end"
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        break
    
    win.flip()


myEndEnd = globalClock.getTime()

#-------Ending Routine "theEnd"-------
for thisComponent in theEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

dataFile.write('End Starts, %f\nEnd Ends, %f\n' %(myEndStart, myEndEnd))


pylinkWrapper.stopRecording()

#closing csv data file
dataFile.close()
pylinkWrapper.close()

# Shutting down:
win.close()
core.quit()
