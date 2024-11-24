import math
class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r
    def povrsina (self):
        return math.pi * (self.r**2)

krug = Krug(10)
print (f"Opseg kruga je: {krug.opseg()}")
print (f"Povrsina kruga je: {krug.povrsina()}")