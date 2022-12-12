class TV():
    def __init__(self):
        self.is_on=False
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is of")

tv1= TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.show_status()
    