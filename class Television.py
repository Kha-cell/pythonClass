class Television:
    def _init_(self):
        self.is_on = False
        self.channel = 0
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, channel):
        if self.is_on and 1 <= channel <= 100:
            self.channel = channel

    def increase_volume(self):
        if self.is_on and self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.is_on and self.volume > 0:
            self.volume -= 1

    def get_status(self):
        return {
            "is_on": self.is_on,
            "channel": self.channel if self.is_on else None,
            "volume": self.volume if self.is_on else None
        }