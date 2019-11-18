#Led depend
import RPi.GPIO as GPIO

#Camera depend
import time
from fractions import Fraction
import picamera

with picamera.PiCamera() as camera:
    # PiCamera(resolution = (1280, 720), framerate = 30)
    # but when capture in bayer parameter, the resolution setting will be ignored
    with picamera.array.PiBayerArray(camera) as stream:
        camera.framerate = 10
        camera.shutter_speed = 100000 # (us)
        # shutter_speed should not greater than 1/framerate
        camera.iso = 100
        
        time.sleep(2) # initialize camera
        camera.exposure_mode = 'off'
        camera.awb_mode = 'off'
        print(camera.awb_gains)
        camera.awb_gains = (Fraction(128,128), Fraction(128,128))
        print(camera.awb_gains)
        
        time.sleep(2)
        camera.start_preview()
        GPIO.setmode(GPIO.BCM)
        # GPIO.BCM 是使用 GPIO後的數字來為Pin腳編號
        # GPIO.BOARD 是使用Pin# 編號
        # GPIO 02 <=> Pin 03, GPIO 12 <=> Pin 32
        GPIO.setup(12, GPIO.OUT)
        pwm = GPIO.PWM(12, 200)             # 200Hz frequency.   GPIO.PWM(pin, frequency)
        pwm.start(100)                      # dutycycle = 100 - N.
        image_name = 'G_0.data'

        time.sleep(5)
        camera.stop_preview()
        
        print("ExposureMode=%s" %(camera.exposure_mode))
        print("Shutter Speed = %d" %(camera.shutter_speed))
        print("Exposure Speed = %d" %(camera.exposure_speed))
        print("ISO =%f" %(camera.iso))
        print("FrameRate=%f" %(camera.framerate))
        print("Digi Gain=%f" %(float(camera.digital_gain)))
        print("Analog Gain=%f" %(float(camera.analog_gain)))
        print("AWB Mode=%s" %camera.awb_mode)
        print("AWB Gain =%f, %f" %camera.awb_gains)
        print("Still Status =%d" %camera.still_stats)
        print('Capture Image: %s' %(image_name))
        #camera.capture(image_name);
        
        print(camera.awb_gains)

        camera.capture(stream, 'jpeg', bayer=True)
        print(stream.demosaic().shape)
        #output = (stream.demosaic() >> 2).astype(np.uint8)
        output= stream.demosaic()
        with open(image_name, 'wb') as f:
            output.tofile(f)
        
        pwm.stop()
        GPIO.cleanup()
        
print('Done!!!')





