#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on May 24, 2021, at 16:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'preference_ratings'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mauspad\\Desktop\\new_OEA_stuff\\ratings\\preference_ratings\\preference_ratings.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='AliceBlue', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "internal_state"
internal_stateClock = core.Clock()
IS_slider = visual.Slider(win=win, name='IS_slider',
    size=(1000, 30), pos=(0,0), units=None,
    labels=None, ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
ISlabel1 = visual.TextStim(win=win, name='ISlabel1',
    text='default text',
    font='Arial',
    pos=(-500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISlabel2 = visual.TextStim(win=win, name='ISlabel2',
    text='default text',
    font='Arial',
    pos=(500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
IS_text = visual.TextStim(win=win, name='IS_text',
    text='default text',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=1200, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
IScount = 0
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "wait"
waitClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Wait for instructions',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "tray_2"
tray_2Clock = core.Clock()
tray_display = visual.TextStim(win=win, name='tray_display',
    text='default text',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_ratings = keyboard.Keyboard()
press_enter = visual.TextStim(win=win, name='press_enter',
    text='Press enter to begin',
    font='Arial',
    pos=(0, -100), height=30, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "tastecup"
tastecupClock = core.Clock()
tray_display_2 = visual.TextStim(win=win, name='tray_display_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_ratings_2 = keyboard.Keyboard()
press_enter_2 = visual.TextStim(win=win, name='press_enter_2',
    text='Press enter to rate',
    font='Arial',
    pos=(0, -100), height=30, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
taste_instr = visual.TextStim(win=win, name='taste_instr',
    text='Taste:',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "intense"
intenseClock = core.Clock()
intense_slider = visual.Slider(win=win, name='intense_slider',
    size=(20,800), pos=(500,0), units=None,
    labels=['No sensation','Barely detectable', 'Weak', 'Moderate', 'Strong', 'Very strong', 'Strongest imaginable sensation of any kind'], ticks=[0, 1.4,6,17,35,51,100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
intense_instructions = visual.TextStim(win=win, name='intense_instructions',
    text='How intense is this sample overall?',
    font='Arial',
    pos=(-300,0), height=40, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CupNoLMS = visual.TextStim(win=win, name='CupNoLMS',
    text='default text',
    font='Arial',
    pos=(-300, 100), height=40, wrapWidth=None, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "sweet"
sweetClock = core.Clock()
sweet_slider = visual.Slider(win=win, name='sweet_slider',
    size=(20,800), pos=(500,0), units=None,
    labels=['No sensation','Barely detectable', 'Weak', 'Moderate', 'Strong', 'Very strong', 'Strongest imaginable sensation of any kind'], ticks=[0, 1.4,6,17,35,51,100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
sweet_question = visual.TextStim(win=win, name='sweet_question',
    text='How intense is the sweetness of this sample?',
    font='Arial',
    pos=(-300,0), height=40, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CupNoSweet = visual.TextStim(win=win, name='CupNoSweet',
    text='default text',
    font='Arial',
    pos=(-300, 100), height=40, wrapWidth=None, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "liking"
likingClock = core.Clock()
like_slider = visual.Slider(win=win, name='like_slider',
    size=(20,800), pos=(500,0), units=None,
    labels=['Most disliked sensation imaginable','Dislike extremely','Dislike very much','Dislike moderately','Dislike slightly','Neutral','Like slightly','Like moderately','Like very much','Like extremely','Most liked sensation imaginable'], ticks=[-100, -62.89, -41.58, -17.59, -5.92, 0, 6.25, 17.82, 44.43, 65.72, 100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
like_instructions = visual.TextStim(win=win, name='like_instructions',
    text='How much do you like or dislike this sample?',
    font='Arial',
    pos=(-300, 0), height=40, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CupNoLHS = visual.TextStim(win=win, name='CupNoLHS',
    text='default text',
    font='Arial',
    pos=(-300, 100), height=40, wrapWidth=None, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "VAS"
VASClock = core.Clock()
vas_slider = visual.Slider(win=win, name='vas_slider',
    size=(1000,30), pos=(0,0), units=None,
    labels=None, ticks=(0,1000),
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
vas_question = visual.TextStim(win=win, name='vas_question',
    text='default text',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=1200, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CupNo = visual.TextStim(win=win, name='CupNo',
    text='default text',
    font='Arial',
    pos=(0, 200), height=40, wrapWidth=None, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
vas_label1 = visual.TextStim(win=win, name='vas_label1',
    text='default text',
    font='Arial',
    pos=(-500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
vas_label2 = visual.TextStim(win=win, name='vas_label2',
    text='default text',
    font='Arial',
    pos=(500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
mouse_vas = event.Mouse(win=win)
x, y = [None, None]
mouse_vas.mouseClock = core.Clock()

# Initialize components for Routine "wait"
waitClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Wait for instructions',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "internal_state"
internal_stateClock = core.Clock()
IS_slider = visual.Slider(win=win, name='IS_slider',
    size=(1000, 30), pos=(0,0), units=None,
    labels=None, ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
ISlabel1 = visual.TextStim(win=win, name='ISlabel1',
    text='default text',
    font='Arial',
    pos=(-500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISlabel2 = visual.TextStim(win=win, name='ISlabel2',
    text='default text',
    font='Arial',
    pos=(500, -43), height=25, wrapWidth=400, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
IS_text = visual.TextStim(win=win, name='IS_text',
    text='default text',
    font='Arial',
    pos=(0, 100), height=40, wrapWidth=1200, ori=0, 
    color='MidnightBlue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
IScount = 0
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
IS1_pre_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('internal_states.xlsx'),
    seed=None, name='IS1_pre_trials')
thisExp.addLoop(IS1_pre_trials)  # add the loop to the experiment
thisIS1_pre_trial = IS1_pre_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIS1_pre_trial.rgb)
if thisIS1_pre_trial != None:
    for paramName in thisIS1_pre_trial:
        exec('{} = thisIS1_pre_trial[paramName]'.format(paramName))

for thisIS1_pre_trial in IS1_pre_trials:
    currentLoop = IS1_pre_trials
    # abbreviate parameter names if possible (e.g. rgb = thisIS1_pre_trial.rgb)
    if thisIS1_pre_trial != None:
        for paramName in thisIS1_pre_trial:
            exec('{} = thisIS1_pre_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "internal_state"-------
    # update component parameters for each repeat
    IS_slider.reset()
    ISlabel1.setText(LabelL)
    ISlabel2.setText(LabelR)
    IS_text.setText(Question)
    win.mouseVisible = False
    
    IS_slider.marker.size=(.1,2)
    IS_slider.marker.color='Red'
    
    mouse.setPos((-500,0))
    IS_slider.markerPos=0
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    internal_stateComponents = [IS_slider, ISlabel1, ISlabel2, IS_text, mouse]
    for thisComponent in internal_stateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    internal_stateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "internal_state"-------
    while continueRoutine:
        # get current time
        t = internal_stateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=internal_stateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IS_slider* updates
        if IS_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_slider.frameNStart = frameN  # exact frame index
            IS_slider.tStart = t  # local t and not account for scr refresh
            IS_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_slider, 'tStartRefresh')  # time at next scr refresh
            IS_slider.setAutoDraw(True)
        
        # *ISlabel1* updates
        if ISlabel1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel1.frameNStart = frameN  # exact frame index
            ISlabel1.tStart = t  # local t and not account for scr refresh
            ISlabel1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel1, 'tStartRefresh')  # time at next scr refresh
            ISlabel1.setAutoDraw(True)
        
        # *ISlabel2* updates
        if ISlabel2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel2.frameNStart = frameN  # exact frame index
            ISlabel2.tStart = t  # local t and not account for scr refresh
            ISlabel2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel2, 'tStartRefresh')  # time at next scr refresh
            ISlabel2.setAutoDraw(True)
        
        # *IS_text* updates
        if IS_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_text.frameNStart = frameN  # exact frame index
            IS_text.tStart = t  # local t and not account for scr refresh
            IS_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_text, 'tStartRefresh')  # time at next scr refresh
            IS_text.setAutoDraw(True)
        x = mouse.getPos()[0]
        IS_slider.markerPos=500 + (x)
        
        #if mouse.getPressed()[0]:
        #    if IScount <= 5:
        #        IS1_pre_trials.addData('ISval', IS_slider.markerPos)
        #    else:
        #        IS2_post_trials.addData('ISval', IS_slider.markerPos)
        #    continueRoutine = False
            
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in internal_stateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "internal_state"-------
    for thisComponent in internal_stateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    IScount += 1
    
    if IScount <= 5:
        IS1_pre_trials.addData('ISval', (IS_slider.markerPos / 10))
    else:
        IS2_post_trials.addData('ISval', (IS_slider.markerPos / 10))
    
    core.wait(0.5)
    # store data for IS1_pre_trials (TrialHandler)
    # the Routine "internal_state" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IS1_pre_trials'


# ------Prepare to start Routine "wait"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
waitComponents = [text, key_resp]
for thisComponent in waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wait"-------
while continueRoutine:
    # get current time
    t = waitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=waitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait"-------
for thisComponent in waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trayno = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('outer_loop.xlsx'),
    seed=None, name='trayno')
thisExp.addLoop(trayno)  # add the loop to the experiment
thisTrayno = trayno.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrayno.rgb)
if thisTrayno != None:
    for paramName in thisTrayno:
        exec('{} = thisTrayno[paramName]'.format(paramName))

for thisTrayno in trayno:
    currentLoop = trayno
    # abbreviate parameter names if possible (e.g. rgb = thisTrayno.rgb)
    if thisTrayno != None:
        for paramName in thisTrayno:
            exec('{} = thisTrayno[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "tray_2"-------
    # update component parameters for each repeat
    tray_display.setText(TrayNo)
    start_ratings.keys = []
    start_ratings.rt = []
    # keep track of which components have finished
    tray_2Components = [tray_display, start_ratings, press_enter]
    for thisComponent in tray_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    tray_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "tray_2"-------
    while continueRoutine:
        # get current time
        t = tray_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=tray_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tray_display* updates
        if tray_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tray_display.frameNStart = frameN  # exact frame index
            tray_display.tStart = t  # local t and not account for scr refresh
            tray_display.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tray_display, 'tStartRefresh')  # time at next scr refresh
            tray_display.setAutoDraw(True)
        
        # *start_ratings* updates
        waitOnFlip = False
        if start_ratings.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_ratings.frameNStart = frameN  # exact frame index
            start_ratings.tStart = t  # local t and not account for scr refresh
            start_ratings.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_ratings, 'tStartRefresh')  # time at next scr refresh
            start_ratings.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(start_ratings.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_ratings.status == STARTED and not waitOnFlip:
            theseKeys = start_ratings.getKeys(keyList=['return'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *press_enter* updates
        if press_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            press_enter.frameNStart = frameN  # exact frame index
            press_enter.tStart = t  # local t and not account for scr refresh
            press_enter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_enter, 'tStartRefresh')  # time at next scr refresh
            press_enter.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tray_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tray_2"-------
    for thisComponent in tray_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "tray_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tastes.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "tastecup"-------
        # update component parameters for each repeat
        tray_display_2.setText(tray)
        start_ratings_2.keys = []
        start_ratings_2.rt = []
        # keep track of which components have finished
        tastecupComponents = [tray_display_2, start_ratings_2, press_enter_2, taste_instr]
        for thisComponent in tastecupComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        tastecupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "tastecup"-------
        while continueRoutine:
            # get current time
            t = tastecupClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=tastecupClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tray_display_2* updates
            if tray_display_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tray_display_2.frameNStart = frameN  # exact frame index
                tray_display_2.tStart = t  # local t and not account for scr refresh
                tray_display_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tray_display_2, 'tStartRefresh')  # time at next scr refresh
                tray_display_2.setAutoDraw(True)
            
            # *start_ratings_2* updates
            waitOnFlip = False
            if start_ratings_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_ratings_2.frameNStart = frameN  # exact frame index
                start_ratings_2.tStart = t  # local t and not account for scr refresh
                start_ratings_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_ratings_2, 'tStartRefresh')  # time at next scr refresh
                start_ratings_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(start_ratings_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if start_ratings_2.status == STARTED and not waitOnFlip:
                theseKeys = start_ratings_2.getKeys(keyList=['return'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    # a response ends the routine
                    continueRoutine = False
            
            # *press_enter_2* updates
            if press_enter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_enter_2.frameNStart = frameN  # exact frame index
                press_enter_2.tStart = t  # local t and not account for scr refresh
                press_enter_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_enter_2, 'tStartRefresh')  # time at next scr refresh
                press_enter_2.setAutoDraw(True)
            
            # *taste_instr* updates
            if taste_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                taste_instr.frameNStart = frameN  # exact frame index
                taste_instr.tStart = t  # local t and not account for scr refresh
                taste_instr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taste_instr, 'tStartRefresh')  # time at next scr refresh
                taste_instr.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tastecupComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "tastecup"-------
        for thisComponent in tastecupComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        core.wait(0.5)
        # the Routine "tastecup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "intense"-------
        # update component parameters for each repeat
        intense_slider.reset()
        CupNoLMS.setText(tray)
        mouse = event.Mouse(visible=False)
        
        intense_slider.marker.size=(2,.1);
        intense_slider.marker.color='Red';
        
        mouse.setPos((0,0))
        intense_slider.markerPos=0
        # keep track of which components have finished
        intenseComponents = [intense_slider, intense_instructions, CupNoLMS]
        for thisComponent in intenseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intenseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "intense"-------
        while continueRoutine:
            # get current time
            t = intenseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intenseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *intense_slider* updates
            if intense_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intense_slider.frameNStart = frameN  # exact frame index
                intense_slider.tStart = t  # local t and not account for scr refresh
                intense_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intense_slider, 'tStartRefresh')  # time at next scr refresh
                intense_slider.setAutoDraw(True)
            
            # *intense_instructions* updates
            if intense_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intense_instructions.frameNStart = frameN  # exact frame index
                intense_instructions.tStart = t  # local t and not account for scr refresh
                intense_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intense_instructions, 'tStartRefresh')  # time at next scr refresh
                intense_instructions.setAutoDraw(True)
            
            # *CupNoLMS* updates
            if CupNoLMS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CupNoLMS.frameNStart = frameN  # exact frame index
                CupNoLMS.tStart = t  # local t and not account for scr refresh
                CupNoLMS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CupNoLMS, 'tStartRefresh')  # time at next scr refresh
                CupNoLMS.setAutoDraw(True)
            x = mouse.getPos()[1]
            intense_slider.markerPos=(x//5)
            
            if mouse.getPressed()[0]:
                trials.addData('Intense', intense_slider.markerPos)
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intenseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intense"-------
        for thisComponent in intenseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        core.wait(0.5)
        # the Routine "intense" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "sweet"-------
        # update component parameters for each repeat
        sweet_slider.reset()
        CupNoSweet.setText(tray)
        mouse = event.Mouse(visible=False)
        
        sweet_slider.marker.size=(2,.1);
        sweet_slider.marker.color='Red';
        
        mouse.setPos((0,0))
        sweet_slider.markerPos=0
        # keep track of which components have finished
        sweetComponents = [sweet_slider, sweet_question, CupNoSweet]
        for thisComponent in sweetComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sweetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "sweet"-------
        while continueRoutine:
            # get current time
            t = sweetClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sweetClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sweet_slider* updates
            if sweet_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sweet_slider.frameNStart = frameN  # exact frame index
                sweet_slider.tStart = t  # local t and not account for scr refresh
                sweet_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sweet_slider, 'tStartRefresh')  # time at next scr refresh
                sweet_slider.setAutoDraw(True)
            
            # *sweet_question* updates
            if sweet_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sweet_question.frameNStart = frameN  # exact frame index
                sweet_question.tStart = t  # local t and not account for scr refresh
                sweet_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sweet_question, 'tStartRefresh')  # time at next scr refresh
                sweet_question.setAutoDraw(True)
            
            # *CupNoSweet* updates
            if CupNoSweet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CupNoSweet.frameNStart = frameN  # exact frame index
                CupNoSweet.tStart = t  # local t and not account for scr refresh
                CupNoSweet.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CupNoSweet, 'tStartRefresh')  # time at next scr refresh
                CupNoSweet.setAutoDraw(True)
            x = mouse.getPos()[1]
            sweet_slider.markerPos=(x//5)
            
            if mouse.getPressed()[0]:
                trials.addData('Sweet', sweet_slider.markerPos)
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sweetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sweet"-------
        for thisComponent in sweetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        core.wait(0.5)
        # the Routine "sweet" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "liking"-------
        # update component parameters for each repeat
        like_slider.reset()
        CupNoLHS.setText(tray)
        mouse = event.Mouse(visible=False)
        
        like_slider.marker.size=(2,.1);
        like_slider.marker.color='Red';
        
        mouse.setPos((0,0))
        like_slider.markerPos=0
        # keep track of which components have finished
        likingComponents = [like_slider, like_instructions, CupNoLHS]
        for thisComponent in likingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        likingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "liking"-------
        while continueRoutine:
            # get current time
            t = likingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=likingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *like_slider* updates
            if like_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                like_slider.frameNStart = frameN  # exact frame index
                like_slider.tStart = t  # local t and not account for scr refresh
                like_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(like_slider, 'tStartRefresh')  # time at next scr refresh
                like_slider.setAutoDraw(True)
            
            # *like_instructions* updates
            if like_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                like_instructions.frameNStart = frameN  # exact frame index
                like_instructions.tStart = t  # local t and not account for scr refresh
                like_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(like_instructions, 'tStartRefresh')  # time at next scr refresh
                like_instructions.setAutoDraw(True)
            
            # *CupNoLHS* updates
            if CupNoLHS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CupNoLHS.frameNStart = frameN  # exact frame index
                CupNoLHS.tStart = t  # local t and not account for scr refresh
                CupNoLHS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CupNoLHS, 'tStartRefresh')  # time at next scr refresh
                CupNoLHS.setAutoDraw(True)
            x = mouse.getPos()[1]
            like_slider.markerPos=(x//5)
            
            if mouse.getPressed()[0]:
                trials.addData('Like', like_slider.markerPos)
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in likingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "liking"-------
        for thisComponent in likingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        core.wait(0.5)
        # the Routine "liking" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        VAS_trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('vas_loop.xlsx'),
            seed=None, name='VAS_trials')
        thisExp.addLoop(VAS_trials)  # add the loop to the experiment
        thisVAS_trial = VAS_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVAS_trial.rgb)
        if thisVAS_trial != None:
            for paramName in thisVAS_trial:
                exec('{} = thisVAS_trial[paramName]'.format(paramName))
        
        for thisVAS_trial in VAS_trials:
            currentLoop = VAS_trials
            # abbreviate parameter names if possible (e.g. rgb = thisVAS_trial.rgb)
            if thisVAS_trial != None:
                for paramName in thisVAS_trial:
                    exec('{} = thisVAS_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "VAS"-------
            # update component parameters for each repeat
            vas_slider.reset()
            vas_question.setText(VASq)
            CupNo.setText(tray)
            win.mouseVisible = False
            
            vas_slider.marker.size=(.1,2)
            vas_slider.marker.color='Red'
            
            mouse_vas.setPos((-500,0))
            vas_slider.markerPos=0
            vas_label1.setText(VASLabelL)
            vas_label2.setText(VASLabelR)
            # setup some python lists for storing info about the mouse_vas
            gotValidClick = False  # until a click is received
            mouse_vas.mouseClock.reset()
            # keep track of which components have finished
            VASComponents = [vas_slider, vas_question, CupNo, vas_label1, vas_label2, mouse_vas]
            for thisComponent in VASComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            VASClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "VAS"-------
            while continueRoutine:
                # get current time
                t = VASClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=VASClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *vas_slider* updates
                if vas_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vas_slider.frameNStart = frameN  # exact frame index
                    vas_slider.tStart = t  # local t and not account for scr refresh
                    vas_slider.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vas_slider, 'tStartRefresh')  # time at next scr refresh
                    vas_slider.setAutoDraw(True)
                
                # *vas_question* updates
                if vas_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vas_question.frameNStart = frameN  # exact frame index
                    vas_question.tStart = t  # local t and not account for scr refresh
                    vas_question.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vas_question, 'tStartRefresh')  # time at next scr refresh
                    vas_question.setAutoDraw(True)
                
                # *CupNo* updates
                if CupNo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    CupNo.frameNStart = frameN  # exact frame index
                    CupNo.tStart = t  # local t and not account for scr refresh
                    CupNo.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(CupNo, 'tStartRefresh')  # time at next scr refresh
                    CupNo.setAutoDraw(True)
                x = mouse_vas.getPos()[0]
                vas_slider.markerPos= 500 + (x)
                
                #if mouse.getPressed()[0]:
                #    trials.addData('VAS', vas_slider.markerPos)
                #    continueRoutine = False
                
                # *vas_label1* updates
                if vas_label1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vas_label1.frameNStart = frameN  # exact frame index
                    vas_label1.tStart = t  # local t and not account for scr refresh
                    vas_label1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vas_label1, 'tStartRefresh')  # time at next scr refresh
                    vas_label1.setAutoDraw(True)
                
                # *vas_label2* updates
                if vas_label2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vas_label2.frameNStart = frameN  # exact frame index
                    vas_label2.tStart = t  # local t and not account for scr refresh
                    vas_label2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vas_label2, 'tStartRefresh')  # time at next scr refresh
                    vas_label2.setAutoDraw(True)
                # *mouse_vas* updates
                if mouse_vas.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_vas.frameNStart = frameN  # exact frame index
                    mouse_vas.tStart = t  # local t and not account for scr refresh
                    mouse_vas.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_vas, 'tStartRefresh')  # time at next scr refresh
                    mouse_vas.status = STARTED
                    prevButtonState = mouse_vas.getPressed()  # if button is down already this ISN'T a new click
                if mouse_vas.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_vas.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            continueRoutine = False                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in VASComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "VAS"-------
            for thisComponent in VASComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            VAS_trials.addData('VAS', (vas_slider.markerPos / 10))
            core.wait(0.5)
            # store data for VAS_trials (TrialHandler)
            # the Routine "VAS" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'VAS_trials'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trayno'


# ------Prepare to start Routine "wait"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
waitComponents = [text, key_resp]
for thisComponent in waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wait"-------
while continueRoutine:
    # get current time
    t = waitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=waitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait"-------
for thisComponent in waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
IS2_post_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('internal_states.xlsx'),
    seed=None, name='IS2_post_trials')
thisExp.addLoop(IS2_post_trials)  # add the loop to the experiment
thisIS2_post_trial = IS2_post_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIS2_post_trial.rgb)
if thisIS2_post_trial != None:
    for paramName in thisIS2_post_trial:
        exec('{} = thisIS2_post_trial[paramName]'.format(paramName))

for thisIS2_post_trial in IS2_post_trials:
    currentLoop = IS2_post_trials
    # abbreviate parameter names if possible (e.g. rgb = thisIS2_post_trial.rgb)
    if thisIS2_post_trial != None:
        for paramName in thisIS2_post_trial:
            exec('{} = thisIS2_post_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "internal_state"-------
    # update component parameters for each repeat
    IS_slider.reset()
    ISlabel1.setText(LabelL)
    ISlabel2.setText(LabelR)
    IS_text.setText(Question)
    win.mouseVisible = False
    
    IS_slider.marker.size=(.1,2)
    IS_slider.marker.color='Red'
    
    mouse.setPos((-500,0))
    IS_slider.markerPos=0
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    internal_stateComponents = [IS_slider, ISlabel1, ISlabel2, IS_text, mouse]
    for thisComponent in internal_stateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    internal_stateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "internal_state"-------
    while continueRoutine:
        # get current time
        t = internal_stateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=internal_stateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IS_slider* updates
        if IS_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_slider.frameNStart = frameN  # exact frame index
            IS_slider.tStart = t  # local t and not account for scr refresh
            IS_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_slider, 'tStartRefresh')  # time at next scr refresh
            IS_slider.setAutoDraw(True)
        
        # *ISlabel1* updates
        if ISlabel1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel1.frameNStart = frameN  # exact frame index
            ISlabel1.tStart = t  # local t and not account for scr refresh
            ISlabel1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel1, 'tStartRefresh')  # time at next scr refresh
            ISlabel1.setAutoDraw(True)
        
        # *ISlabel2* updates
        if ISlabel2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISlabel2.frameNStart = frameN  # exact frame index
            ISlabel2.tStart = t  # local t and not account for scr refresh
            ISlabel2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISlabel2, 'tStartRefresh')  # time at next scr refresh
            ISlabel2.setAutoDraw(True)
        
        # *IS_text* updates
        if IS_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IS_text.frameNStart = frameN  # exact frame index
            IS_text.tStart = t  # local t and not account for scr refresh
            IS_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IS_text, 'tStartRefresh')  # time at next scr refresh
            IS_text.setAutoDraw(True)
        x = mouse.getPos()[0]
        IS_slider.markerPos=500 + (x)
        
        #if mouse.getPressed()[0]:
        #    if IScount <= 5:
        #        IS1_pre_trials.addData('ISval', IS_slider.markerPos)
        #    else:
        #        IS2_post_trials.addData('ISval', IS_slider.markerPos)
        #    continueRoutine = False
            
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in internal_stateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "internal_state"-------
    for thisComponent in internal_stateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    IScount += 1
    
    if IScount <= 5:
        IS1_pre_trials.addData('ISval', (IS_slider.markerPos / 10))
    else:
        IS2_post_trials.addData('ISval', (IS_slider.markerPos / 10))
    
    core.wait(0.5)
    # store data for IS2_post_trials (TrialHandler)
    # the Routine "internal_state" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IS2_post_trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [done]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done.frameNStart = frameN  # exact frame index
        done.tStart = t  # local t and not account for scr refresh
        done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done, 'tStartRefresh')  # time at next scr refresh
        done.setAutoDraw(True)
    if done.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            done.tStop = t  # not accounting for scr refresh
            done.frameNStop = frameN  # exact frame index
            win.timeOnFlip(done, 'tStopRefresh')  # time at next scr refresh
            done.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
