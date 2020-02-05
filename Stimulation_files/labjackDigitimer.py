#from labjack import u6

import u6

import time



# since the scanner's TLL pulses are fed into channel 1 in both the Biopac and the EyeTracker's Voltage Pro board

# I'll call what's really channel 2 on the peripherals channel 1 for the purposes of this class

BIOPAC_CHANNELS = [1,2,3,4,5,6,7]

EYETRACKER_CHANNELS = [9,10,11,12,13,14,15]

DIGITIMER_CHANNELS=[0]



BIOPAC_DEVICE_ID = 0

EYETRACKER_DEVICE_ID = 1

DIGITIMER_DEVICE_ID = 2



DIGITAL_CHANNEL_DIRECTION_OUTPUT = 1

ON_STATE = 1

OFF_STATE = 0



class LabJackBIC:

    def __init__(self):

		# create an instance of the LabJack driver which will do all the communication	

        self.jack = u6.U6()
        # print(self.jack.configU6())



    def connect(self):

        iscompleted = False

        nbattempts = 0

        while not(iscompleted) and nbattempts<1000:#while iscompleted is false and nb<1000   will be doing this constantly

            try:

                nbattempts = nbattempts +1

                #print ('Attempt nb ' + str(nbattempts))

                self.jack = u6.U6()

                iscompleted = True

            except:

                print('Pb with labjack initialisation nb '+ str(nbattempts))

                time.sleep(0.01)

        if not(iscompleted): #if iscompleted  equals false   which would give true he 

            raise IOError('Labjack could not connect')

    

		# the FIO0-FIO7 inputs are flexible, meaning they can be analog or digital, so ensure

		# they are all digital by sending a zero for the FIO Analog parameter

		# self.jack.configIO(FIOAnalog = 0)



		# now set all the channels to output, since each digital IO channel supports input and output

        for channel in BIOPAC_CHANNELS:

            #self.jack.getFeedback(u6.BitDirWrite(channel,DIGITAL_CHANNEL_DIRECTION_OUTPUT))

            self.sendMsg(u6.BitDirWrite(channel,DIGITAL_CHANNEL_DIRECTION_OUTPUT))

        for channel in EYETRACKER_CHANNELS:

            #self.jack.getFeedback(u6.BitDirWrite(channel,DIGITAL_CHANNEL_DIRECTION_OUTPUT))

            self.sendMsg(u6.BitDirWrite(channel,DIGITAL_CHANNEL_DIRECTION_OUTPUT))

        for channel in DIGITIMER_CHANNELS:

            #self.jack.getFeedback(u6.BitDirWrite(channel, DIGITAL_CHANNEL_DIRECTION_OUTPUT))

            self.sendMsg(u6.BitDirWrite(channel, DIGITAL_CHANNEL_DIRECTION_OUTPUT))



    def channelOn(self, device, channelNo):

		# make sure the channelNo is valid

        if channelNo < 0 or channelNo > len(BIOPAC_CHANNELS):

            raise ValueError('Invalid channel number passed to the LabJackBIC channelOn method: $i' %(channelNo))



		# based on which device is being used, determine the channel number to pass to the driver

        channel = None

        if device == BIOPAC_DEVICE_ID:

            channel = BIOPAC_CHANNELS[channelNo]

        elif device == EYETRACKER_DEVICE_ID:

            channel = EYETRACKER_CHANNELS[channelNo]

        elif device == DIGITIMER_DEVICE_ID:

            channel = DIGITIMER_CHANNELS[channelNo]

        else:

            raise ValueError('Invalid Device ID passed to the LabJackBIC channelOn method: %i' %(device))



		# set the given channel to the On state

        #self.jack.getFeedback(u6.BitStateWrite(IONumber=channel, State=ON_STATE))

        self.sendMsg(u6.BitStateWrite(IONumber=channel, State=ON_STATE))

    def channelOff(self, device, channelNo):

		# make sure the channelNo is valid

        if channelNo < 0 or channelNo > len(BIOPAC_CHANNELS):

            raise ValueError('Invalid channel number passed to the LabJackBIC channelOff method: $i' %(channelNo))

		# based on which device is being used, determine the channel number to pass to the driver

        channel = None

        if device == BIOPAC_DEVICE_ID:

            channel = BIOPAC_CHANNELS[channelNo]

        elif device == EYETRACKER_DEVICE_ID:

            channel = EYETRACKER_CHANNELS[channelNo]

        elif device == DIGITIMER_DEVICE_ID:

            channel = DIGITIMER_CHANNELS[channelNo]

        else:

            raise ValueError('Invalid Device ID passed to the LabJackBIC channelOff method: %i' %(device))



		# set the given channel to the On state

        #self.jack.getFeedback(u6.BitStateWrite(IONumber=channel, State=OFF_STATE))

        self.sendMsg(u6.BitStateWrite(IONumber=channel, State=OFF_STATE))

    def channelPulseOn(self, device,channelNo):

	    # make sure the channelNo is valid

        if channelNo < 0 or channelNo > len(BIOPAC_CHANNELS):

            raise ValueError('Invalid channel number passed to the LabJackBIC channelOff method: $i' %(channelNo))

		# based on which device is being used, determine the channel number to pass to the driver

        channel = None

        if device == BIOPAC_DEVICE_ID:

            channel = BIOPAC_CHANNELS[channelNo]

        elif device == EYETRACKER_DEVICE_ID:

            channel = EYETRACKER_CHANNELS[channelNo]

        elif device == DIGITIMER_DEVICE_ID:

            channel = DIGITIMER_CHANNELS[channelNo]

        else:

            raise ValueError('Invalid Device ID passed to the LabJackBIC channelOff method: %i' %(device))

		# set the given channel to the On state

        self.sendMsg(u6.BitStateWrite(IONumber=channel, State=ON_STATE))

        time.sleep(0.5)

        self.sendMsg(u6.BitStateWrite(IONumber=channel, State=OFF_STATE))

	

    def clearChannels(self, device):

		# based on which device is being used, determine the channel number to pass to the driver

        channels = None

        if device == BIOPAC_DEVICE_ID:

            channels = BIOPAC_CHANNELS

        elif device == EYETRACKER_DEVICE_ID:

            channels = EYETRACKER_CHANNELS

        elif device == DIGITIMER_DEVICE_ID:

            channels = DIGITIMER_CHANNELS

        else:

            raise ValueError('Invalid Device ID passed to the LabJackBIC clearChannels method: %i' %(device))



		# set the given channel to the On state

        for channel in channels:

            #self.jack.getFeedback(u6.BitStateWrite(IONumber=channel, State=OFF_STATE))

            self.sendMsg(u6.BitStateWrite(IONumber=channel, State=OFF_STATE))

   



    def sendMsg(self, msg):

        

        iscompleted = False

        nbattempts = 0

        while not(iscompleted) and nbattempts<1000:

            try:

                nbattempts = nbattempts +1

                self.jack.getFeedback(msg)

                iscompleted = True

            except:

                print('Pb with labjack feedback nb '+ str(nbattempts))

                #time.sleep(0.01)

        if not(iscompleted):

            raise IOError('Labjack could not get feedback')

















