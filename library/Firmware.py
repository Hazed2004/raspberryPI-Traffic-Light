from gpiozero import LED
from time import sleep

RedLight = LED(25)
YellowLight = LED(8)
GreenLight = LED(7)

OnRedSignal = False
OnGreenSignal = False
OnYellowSignal = False
OnAllSignal = False
OffRedSignal = False
OffGreenSignal = False
OffYellowSignal = False
OffAllSignal = False
AutomateTrafficSignal = False

class LedController():
    def OnRed():
        RedLight.on()
        return
    def OffRed():
        RedLight.off()
        return
    def OnGreen():
        GreenLight.on()
        return
    def OffGreen():
        GreenLight.off()
        return
    def OnYellow():
        YellowLight.on()
        return
    def OffYellow():
        YellowLight.off()
        return
    def Onall():
        RedLight.on()
        YellowLight.on()
        GreenLight.on()
        return
    def Offall():
        RedLight.off()
        YellowLight.off()
        GreenLight.off()
    def AutomateTraffic():
        while AutomateTrafficSignal:
            RedLight.off()
            YellowLight.off()
            GreenLight.off()
            RedLight.on()
            sleep(100)
            RedLight.off()
            YellowLight.on()
            sleep(2)
            YellowLight.off()
            GreenLight.on()
            sleep(50)
            GreenLight.off()
        return
