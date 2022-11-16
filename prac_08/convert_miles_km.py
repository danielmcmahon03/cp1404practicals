"""
CP1404 - Practical 8
Converting Miles to Kilometres and Vice Versa
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609


class ConvertMilesToKilometres(App):
    kilometres = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, text):
        """Handle calculation of miles to kilometres."""
        miles = change_str_to_float(text)
        self.kilometres = str(miles * MILES_TO_KM)

    def handle_increment(self, text, change):
        """Adds or removes one from total."""
        miles = change_str_to_float(text) + change
        self.root.ids.input_distance.text = str(miles)


def change_str_to_float(text):
    try:
        return float(text)
    except ValueError:
        return 0.0


ConvertMilesToKilometres().run()
