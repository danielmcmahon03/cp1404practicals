from musician import Musician


class Band(Musician):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
