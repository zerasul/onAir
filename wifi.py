import settings
import network


class Wifi:

    station = None
    connected = False
    currentIp = '0.0.0.0'

    def __init__(self):
        if settings.mode is None:
            raise ConnectionError('No Wifi Mode in Settings')
        self.station = network.WLAN(settings.mode)

    def connect(self):

        if self.station.isconnected():
            print("Already connected")
            self.connected = True
            self.currentIp = self.station.ifconfig()[0]
            return
        self.station.active(True)
        self.station.connect(settings.wifi_ssid, settings.wifi_password)
        while not self.station.isconnected():
            pass
        print("Connection successful")
        self.connected=True
        config = self.station.ifconfig()
        print(config)
        self.currentIp = config[0]

    def getcurrent_ip(self):
        if not self.connected:
            raise ConnectionError('Not Connected; run Connect First')
        return self.currentIp
