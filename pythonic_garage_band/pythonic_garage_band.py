class Band():
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        # self.band_name = band_name

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    def play_solos(self):
        solos = []
        for musician in self.members: 
            solos.append(musician.play_solo())
        return solos

    @classmethod
    def get_instrument(cls):
        return Guitarist.instrument + Bassist.instrument + Drummer.instrument

    @classmethod
    def to_list(cls):
        # return "{self.band_name}"
        return []



class Musician(Band):
    pass

class Guitarist(Band):
    instrument = 'guitar'

    def __init__(self, name='Guitar Guy'):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @classmethod
    def get_instrument(cls):
        return cls.instrument

    @staticmethod
    def play_solo():
        return "face melting guitar solo"

class Bassist:
    instrument = 'bass'

    def __init__(self, name='Bassist Babe'):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    @classmethod
    def get_instrument(cls):
        return cls.instrument
    
    @staticmethod
    def play_solo():
        return "bom bom buh bom"

class Drummer:
    instrument = 'drums'

    def __init__(self, name='Drummer Dude'):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    @classmethod
    def get_instrument(cls):
        return cls.instrument

    @staticmethod
    def play_solo():
        return "rattle boom crash"