import random

class Coin():  # general class for everything
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):
        for key, value in kwargs.items():
            setattr(self,key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self. rusty_color
    def rust(self):
        self.color = self.rusty_color
    def __del__(self):
        print('coin spent')
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    def clean(self):
        self.color = self.clean_color

class One_Pence(Coin):  # inherit from coin and gets all method
    def __init__(self):  # go inside init function for each child class then inside our init function we get parents constructor to do rest of setup
        data = {
            'original_value': 0.01,
            'clean_color': 'bronze',
            'rusty_color': 'brownish',
            'num_edges': 1,
            'diameter': 20.3,
            'thickness': 1.52,
            'mass': 3.56
        }
        super().__init__(**data)

class Two_Pence(Coin):  # inherit from coin and gets all method
    def __init__(self):  # go inside init function for each child class then inside our init function we get parents constructor to do rest of setup
        data = {
            'original_value': 0.02,
            'clean_color': 'bronze',
            'rusty_color': 'brownish',
            'num_edges': 1,
            'diameter': 25.9,
            'thickness': 1.85,
            'mass': 7.12
        }
        super().__init__(**data)


class Five_Pence(Coin):  # inherit from coin and gets all method
    def __init__(self):  # go inside init function for each child class then inside our init function we get parents constructor to do rest of setup
        data = {
            'original_value': 0.05,
            'clean_color': 'silver',
            'rusty_color': None,
            'num_edges': 1,
            'diameter': 18.0,
            'thickness': 1.77,
            'mass': 3.25
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color

class Pound(Coin):  # inherit from coin and gets all method
    def __init__(self):  # go inside init function for each child class then inside our init function we get parents constructor to do rest of setup
        data = {
            'original_value': 1.00,
            'clean_color': 'gold',
            'rusty_color': 'greenish',
            'num_edges': 1,
            'diameter': 22.5,
            'thickness': 3.15,
            'mass': 9.5
        }
        super().__init__(**data)
one_pound_coin = Pound()
print(one_pound_coin.value)
print(one_pound_coin.heads)
print(one_pound_coin.flip())
print(one_pound_coin.color)
one_pound_coin.rust()
print(one_pound_coin.color)

