import sys, time                    # Built-in Library
from fractions import Fraction

import RPi.GPIO as GPIO
import picamera
import picamera.array


class RaspberryPi:
    def __init__(self, led_pin):
        # led_pin 使用 GPIO.BCM 編碼
        try:
            self.camera_obj = picamera.PiCamera()
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(led_pin, GPIO.OUT)
            self.pwm = GPIO.PWM(led_pin, 200)
            self.pwm.start(100)                 # initial pwm to set off
        except Exception as e:
            print("Launch Error: ", e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(self.camera_obj, picamera.PiCamera):
            self.camera_obj.stop_preview()
            self.camera_obj.close()
            self.pwm.stop()
            GPIO.cleanup()

    def setting_camera(self, framerate = 10, exposure_mode = "off", shutter_speed = 10**5, iso = 100, awb_mode = "off", awb_gains = (Fraction(128, 128), Fraction(128, 128))):
        self.camera_obj.framerate = framerate
        self.camera_obj.shutter_speed = shutter_speed
        self.camera_obj.iso = iso
        time.sleep(2)   # Camera Warm-up
        self.camera_obj.exposure_mode = exposure_mode
        self.camera_obj.awb_mode = awb_mode
        self.camera_obj.awb_gains = awb_gains

    def show_camera_setting(self):
        if isinstance(self.camera_obj, picamera.PiCamera):
            print("Exposure Mode = ", self.camera_obj.exposure_mode)
            print("Shutter Speed = ", self.camera_obj.shutter_speed)
            print("Exposure Speed = ", self.camera_obj.exposure_speed)
            print("ISO = ", self.camera_obj.iso)
            print("FrameRate = ", self.camera_obj.framerate)
            print("Digital Gain = ", self.camera_obj.digital_gain)
            print("Analog Gain = ", self.camera_obj.analog_gain)
            print("AWB Mode = ", self.camera_obj.awb_mode)
            print("AWB Gain = ", self.camera_obj.awb_gains)
            print("Still Status = ", self.camera_obj.still_stats)
        else:
            print("Error: Camera need to initialize first")

    def set_led_intensity(self, duty_cycle):
        duty_cycle = 0 if duty_cycle < 0 else duty_cycle
        duty_cycle = 100 if duty_cycle > 100 else duty_cycle
        if isinstance(self.pwm, GPIO.PWM):
            self.pwm.start(duty_cycle)

    def capture_raw_data(self, file_name):
        # 大概需要近20秒
        with picamera.array.PiBayerArray(self.camera_obj) as stream:
            self.camera_obj.capture(stream, 'jpeg', bayer=True)
            output = stream.demosaic()
            with open(file_name, 'wb') as f:
                output.tofile(f)

    def preview(self):
        # Preview 測試後應該不影響capture_raw_date
        self.camera_obj.start_preview()
        time.sleep(2)

    def stop_preview(self):
        self.camera_obj.stop_preview()


if __name__ == "__main__":
    with RaspberryPi(led_pin=12) as control:
        control.setting_camera()
        for i in range(11):
            control.set_led_intensity(i*10)
            # control.preview()
            control.capture_raw_data("test.class_" + str(i))











