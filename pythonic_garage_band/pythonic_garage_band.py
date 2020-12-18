# class Band():
#     def __init__(self, name, members=None):
#         self.name = name
#         self.members = members
#         # self.band_name = band_name

#     def __str__(self):
#         return f"The band {self.name}"

#     def __repr__(self):
#         return f"Band instance. name={self.name}, members={self.members}"
    
#     def play_solos(self):
#         solos = []
#         for musician in self.members: 
#             solos.append(musician.play_solo())
#         return solos

#     @classmethod
#     def get_instrument(cls):
#         return Guitarist.instrument + Bassist.instrument + Drummer.instrument

#     @classmethod
#     def to_list(cls):
#         # return "{self.band_name}"
#         return []



# class Musician(Band):
#     pass

# class Guitarist(Band):
#     instrument = 'guitar'

#     def __init__(self, name='Guitar Guy'):
#         self.name = name

#     def __str__(self):
#         return f"My name is {self.name} and I play guitar"
    
#     def __repr__(self):
#         return f"Guitarist instance. Name = {self.name}"

#     @classmethod
#     def get_instrument(cls):
#         return cls.instrument

#     @staticmethod
#     def play_solo():
#         return "face melting guitar solo"

# class Bassist:
#     instrument = 'bass'

#     def __init__(self, name='Bassist Babe'):
#         self.name = name

#     def __str__(self):
#         return f"My name is {self.name} and I play bass"
    
#     def __repr__(self):
#         return f"Bassist instance. Name = {self.name}"
    
#     @classmethod
#     def get_instrument(cls):
#         return cls.instrument
    
#     @staticmethod
#     def play_solo():
#         return "bom bom buh bom"

# class Drummer:
#     instrument = 'drums'

#     def __init__(self, name='Drummer Dude'):
#         self.name = name

#     def __str__(self):
#         return f"My name is {self.name} and I play drums"
    
#     def __repr__(self):
#         return f"Drummer instance. Name = {self.name}"
    
#     @classmethod
#     def get_instrument(cls):
#         return cls.instrument

#     @staticmethod
#     def play_solo():
#         return "rattle boom crash"
















class Band():
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        # self.band_name = band_name
        Band.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    def play_solos(self):
        # solos = []
        # for musician in self.members: 
        #     solos.append(musician.play_solo())
        # return solos
        return[player.play_solo() for player in self.members]

    @classmethod
    def get_instrument(cls):
        return Guitarist.instrument + Bassist.instrument + Drummer.instrument

    @classmethod
    def to_list(cls):
        # return "{self.band_name}"
        return cls.instances



class Musician:
    def __init__(self, name, instrument: str=None):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    @classmethod
    def get_instrument(cls):
        return cls.instrument


class Guitarist(Musician):
    instrument = 'guitar'

    def __init__(self, name):
        super().__init(name)

    
    def __init__(self, name='Guitar Guy'):
        self.name = name

    @staticmethod
    def play_solo():
        return "face melting guitar solo"

class Bassist(Musician):
    instrument = 'bass'

    def __init__(self, name='Bassist Babe'):
        self.name = name
    
    @classmethod
    def get_instrument(cls):
        return cls.instrument
    
    @staticmethod
    def play_solo():
        return "bom bom buh bom"

class Drummer(Musician):
    instrument = 'drums'

    def __init__(self, name='Drummer Dude'):
        self.name = name
    
    @classmethod
    def get_instrument(cls):
        return cls.instrument

    @staticmethod
    def play_solo():
        return "rattle boom crash"










#to instanciate BAND
# if __name__ == "__main__": 
#     # band = Band("joe")
#     # print(repr(band))

#     # auto prints str
#     # musician = Musician('Joe', 'flute')

#     guitarist = Guitarist('Jane', 'guitar')
#     print(guitarist)
