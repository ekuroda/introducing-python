class Bear():
    def eat(self):
        return 'berries'


class Rabbit():
    def eat(self):
        return 'clover'


class Octothorpe():
    def eat(self):
        return 'camplers'


for eater in [Bear(), Rabbit(), Octothorpe()]:
    print(eater.eat())
