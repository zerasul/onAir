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
        if settings.mode == network.AP_IF:
            self.create_ap()
        else:
            self.create_sta()

    def create_sta(self):
        if settings.mode == network.AP_IF:
            raise ConnectionError('Invalid mode')

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

    def create_ap(self):
        if settings.mode == network.STA_IF:
            raise ConnectionError('Invalid Mode')
        self.station.active(True)
        self.station.config(essid=settings.wifi_ssid, password=settings.wifi_password, authmode=3)
        config = self.station.ifconfig()
        print(config)
        self.connected=True
        self.currentIp = config[0]

    def getcurrent_ip(self):
        if not self.connected:
            raise ConnectionError('Not Connected; run Connect First')
        return self.currentIp
