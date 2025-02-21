import unittest

from television import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.tv = Television()

    def test_initial_state(self):
        self.assertFalse(self.tv.is_on)
        self.assertIsNone(self.tv.channel)
        self.assertIsNone(self.tv.volume)

    def test_turn_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)
    def test_turn_off(self):
        self.tv.turn_off()
        self.assertFalse(self.tv.is_on)
    def test_increase_volume(self):
        self.assertFalse(self.tv.is_on)
        self.assertFalse(self.tv.is_on)
        self.tv.increase_volume()

    def test_decrease_volume(self):
        self.assertTrue(self.tv.is_off)
        self.assertTrue(self.tv.is_off)
        self.tv.decrease_volume()
    def test_set_channel(self):
        self.assertTrue(self.tv.is_on)
        self.assertFalse(self.tv.is_off)
        self.tv.set_channel(5)