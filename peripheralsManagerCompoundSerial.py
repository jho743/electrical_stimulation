#import labjackDigitimer_except
#from labjackDigitimer_except import *
import labjackDigitimer
from labjackDigitimer import *

# list of constants/ events from the trial that will be marked in the physio recordings
# STIM_CHANNELS = [1,2,3] #indicates if a stim has started, and what stim
# BLOCK_CHANNELS = [4,5,6]  #indicates when a block (one condition) has started, and what block
SOUND_CHANNEL = 0  # marks when shock happened
SINGLECS_CHANNEL = 1
COMPOUNDCS_CHANNEL = 2
CSPLUS_CHANNEL = 3
CSMINUS_CHANNEL = 4
CONDTRIPLET_CHANNELS = [5, 6]

# Wrapper class around the LabJackBIC which establishes a mapping between channels and script events such as run on/off, cs_cue on/off


class PeripheralsManager:
    def __init__(self, enableBioPac=True, enableEyeTracker=False, enableDigitimer=True):
        # create a LabJackBIC to communicate with the Peripherals
        self.labjack = LabJackBIC()
        self.enableBioPac = enableBioPac
        self.enableEyeTracker = enableEyeTracker
        self.enableDigitimer = enableDigitimer

    def initialize(self):

        self.labjack.connect()
        # clear the channels for both the Biopac and EyeTracker
        if self.enableBioPac:
            self.labjack.clearChannels(BIOPAC_DEVICE_ID)
        if self.enableEyeTracker:
            self.labjack.clearChannels(EYETRACKER_DEVICE_ID)
        if self.enableDigitimer:
            self.labjack.clearChannels(DIGITIMER_DEVICE_ID)

#	def blockOn(self, thecode):
#
#		stringBin = "%03i" % (int(bin(thecode)[2:]))
#
#		for i in xrange(len(BLOCK_CHANNELS)):
#			if int(stringBin[-(i+1)]):
#				if self.enableBioPac:
#					self.labjack.channelOn(BIOPAC_DEVICE_ID, BLOCK_CHANNELS[i])
#				if self.enableEyeTracker:
#					self.labjack.channelOn(EYETRACKER_DEVICE_ID, BLOCK_CHANNELS[i])
#			else:
#				if self.enableBioPac:
#					self.labjack.channelOff(BIOPAC_DEVICE_ID, BLOCK_CHANNELS[i])
#				if self.enableEyeTracker:
#					self.labjack.channelOff(EYETRACKER_DEVICE_ID, BLOCK_CHANNELS[i])
#
#	def blockOff(self):
#
#		for i in xrange(len(BLOCK_CHANNELS)):
#			if self.enableBioPac:
#				self.labjack.channelOff(BIOPAC_DEVICE_ID, BLOCK_CHANNELS[i])
#			if self.enableEyeTracker:
#				self.labjack.channelOff(EYETRACKER_DEVICE_ID, BLOCK_CHANNELS[i])

#	def stimOn(self, thecode):
#
#		stringBin = "%03i" % (int(bin(thecode)[2:]))
#
#		for i in xrange(len(STIM_CHANNELS)):
#			if int(stringBin[-(i+1)]):
#				if self.enableBioPac:
#					self.labjack.channelOn(BIOPAC_DEVICE_ID, STIM_CHANNELS[i])
#				if self.enableEyeTracker:
#					self.labjack.channelOn(EYETRACKER_DEVICE_ID, STIM_CHANNELS[i])
#			else:
#				if self.enableBioPac:
#					self.labjack.channelOff(BIOPAC_DEVICE_ID, STIM_CHANNELS[i])
#				if self.enableEyeTracker:
#					self.labjack.channelOff(EYETRACKER_DEVICE_ID, STIM_CHANNELS[i])
#
#	def stimOff(self):
#
#		for i in xrange(len(STIM_CHANNELS)):
#			if self.enableBioPac:
#				self.labjack.channelOff(BIOPAC_DEVICE_ID, STIM_CHANNELS[i])
#			if self.enableEyeTracker:
#				self.labjack.channelOff(EYETRACKER_DEVICE_ID, STIM_CHANNELS[i])

    def shockOn(self):

        if self.enableBioPac:
            self.labjack.channelOn(BIOPAC_DEVICE_ID, SOUND_CHANNEL)
        if self.enableEyeTracker:
            self.labjack.channelOn(EYETRACKER_DEVICE_ID, SOUND_CHANNEL)
        if self.enableDigitimer:
            self.labjack.channelOn(DIGITIMER_DEVICE_ID, SOUND_CHANNEL)

    def shockOff(self):

        if self.enableBioPac:
            self.labjack.channelOff(BIOPAC_DEVICE_ID, SOUND_CHANNEL)
        if self.enableEyeTracker:
            self.labjack.channelOff(EYETRACKER_DEVICE_ID, SOUND_CHANNEL)
        if self.enableDigitimer:
            self.labjack.channelOff(DIGITIMER_DEVICE_ID, SOUND_CHANNEL)

    def singleCSOn(self):
        # print "this is singleCS channel:", SINGLECS_CHANNEL
        if self.enableBioPac:
            self.labjack.channelOn(BIOPAC_DEVICE_ID, SINGLECS_CHANNEL)
        if self.enableEyeTracker:
            self.labjack.channelOn(EYETRACKER_DEVICE_ID, SINGLECS_CHANNEL)

    def singleCSOff(self):

        if self.enableBioPac:
            self.labjack.channelOff(BIOPAC_DEVICE_ID, SINGLECS_CHANNEL)
        if self.enableEyeTracker:
            self.labjack.channelOff(EYETRACKER_DEVICE_ID, SINGLECS_CHANNEL)

    def compoundCSOn(self):
        # print "this is Compound channel:", COMPOUNDCS_CHANNEL
        if self.enableBioPac:
            self.labjack.channelOn(BIOPAC_DEVICE_ID, COMPOUNDCS_CHANNEL)
        if self.enableEyeTracker:
            self.labjack.channelOn(EYETRACKER_DEVICE_ID, COMPOUNDCS_CHANNEL)

    def compoundCSOff(self):
        if self.enableBioPac:
            self.labjack.channelOff(BIOPAC_DEVICE_ID, COMPOUNDCS_CHANNEL)
        if self.enableEyeTracker:
            self.labjack.channelOff(EYETRACKER_DEVICE_ID, COMPOUNDCS_CHANNEL)

    def CSPlusOn(self):
        # print "this is CSPLUS channel:", CSPLUS_CHANNEL
        if self.enableBioPac:
            self.labjack.channelOn(BIOPAC_DEVICE_ID, CSPLUS_CHANNEL)
        if self.enableEyeTracker:
            self.labjack.channelOn(EYETRACKER_DEVICE_ID, CSPLUS_CHANNEL)

    def CSPlusOff(self):
	    if self.enableBioPac:
	        self.labjack.channelOff(BIOPAC_DEVICE_ID, CSPLUS_CHANNEL)
	    if self.enableEyeTracker:
	        self.labjack.channelOff(EYETRACKER_DEVICE_ID, CSPLUS_CHANNEL)

    def CSMinusOn(self):
        # print "this is CSMINUS channel:", CSMINUS_CHANNEL
	    if self.enableBioPac:
	        self.labjack.channelOn(BIOPAC_DEVICE_ID, CSMINUS_CHANNEL)
	    if self.enableEyeTracker:
	        self.labjack.channelOn(EYETRACKER_DEVICE_ID, CSMINUS_CHANNEL)

    def CSMinusOff(self):
	    if self.enableBioPac:
	        self.labjack.channelOff(BIOPAC_DEVICE_ID, CSMINUS_CHANNEL)
	    if self.enableEyeTracker:
	        self.labjack.channelOff(EYETRACKER_DEVICE_ID, CSMINUS_CHANNEL)

    def CondTripletOn(self, thecode):

        #stringBin = "%03i" % (int(bin(thecode)[2:]))

        # for i in xrange(len(CONDTRIPLET_CHANNELS)):
        # print thecode, "this is the code"#int(stringBin[-(i+1)]) ,"what channel?"
        if thecode == 1:  # int(stringBin[-(i+1)]):
            # print int(stringBin[-(i+1)])," this is channel for COndTriplet"
            # print "using channel 0 for condTriplet", CONDTRIPLET_CHANNELS[0]
            if self.enableBioPac:
                self.labjack.channelOn(
                    BIOPAC_DEVICE_ID, CONDTRIPLET_CHANNELS[0])
            if self.enableEyeTracker:
                self.labjack.channelOn(
                    EYETRACKER_DEVICE_ID, CONDTRIPLET_CHANNELS[0])
        else:

            # print "using channel 1 for condTriplet", CONDTRIPLET_CHANNELS[1]
            if self.enableBioPac:
                self.labjack.channelOn(
                    BIOPAC_DEVICE_ID, CONDTRIPLET_CHANNELS[1])
            if self.enableEyeTracker:
                self.labjack.channelOn(
                    EYETRACKER_DEVICE_ID, CONDTRIPLET_CHANNELS[1])

    def CondTripletOff(self, thecode):
        if thecode == 1:  # for i in xrange(len(CONDTRIPLET_CHANNELS)):
            if self.enableBioPac:
                self.labjack.channelOff(
                    BIOPAC_DEVICE_ID, CONDTRIPLET_CHANNELS[0])
            if self.enableEyeTracker:
                self.labjack.channelOff(
                    EYETRACKER_DEVICE_ID, CONDTRIPLET_CHANNELS[0])
        else:  # for i in xrange(len(CONDTRIPLET_CHANNELS)):
            if self.enableBioPac:
                self.labjack.channelOff(
                    BIOPAC_DEVICE_ID, CONDTRIPLET_CHANNELS[1])
            if self.enableEyeTracker:
                self.labjack.channelOff(
                    EYETRACKER_DEVICE_ID, CONDTRIPLET_CHANNELS[1])


# Wrapper class around the LabJackBIC which establishes a mapping between channels and script events such as run on/off, cs_cue on/off
class PeripheralsManager_dummy:
    def __init__(self, enableBioPac=True, enableEyeTracker=False, enableDigitimer=True):
        print('Creating Dummy Labjack')

    def blockOn(self, thecode):

        stringBin = "%03i" % (int(bin(thecode)[2:]))
        print('Block On' + stringBin)

    def blockOff(self):
        print('Block Off')

    def stimOn(self, thecode):

        stringBin = "%03i" % (int(bin(thecode)[2:]))
        print('Stim On' + stringBin)

    def stimOff(self):
        print('Stim Off')

    def shockOn(self):
        print('Shock On')

    def shockOff(self):
        print('Shock Off')
