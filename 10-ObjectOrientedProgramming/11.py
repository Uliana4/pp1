class tv():
    def __init__(self):
        self.is_on == False
        self.channel = 1
        self.channels=[]
    
    def turn_on(self):
            self.is_on=True
    def turn_off(self):
            self.channel_on=False
    def show_status(self):
        if self.is_on:
            print(f'tv on, numer kanalu: {self.channel}')
        else:
            print('TV is off')
    def set_channel(self, channel):
        self.channel=channel

    def set_channels(self, channels_list):
        self.channels_list= channels_list
    def show_channels(self):
        print(self.channels_list)

tv.show_status()
tv.set_channels(['tvp4'])