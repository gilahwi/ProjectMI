from mynltk.newstuff import cheer
from mynltk.newstuff2 import cheer2


class Cheers:

    def three_times(self):
        cheer()
        cheer()
        cheer()
        cheer2()

    def doing_good(self):
        print('Keep up the good work!')

    def all_caps(self, string):
        print(string.upper())
        return string.upper()


Cheers.three_times(Cheers)
Cheers.doing_good(Cheers)
Cheers.all_caps(Cheers, 'pineapple')
