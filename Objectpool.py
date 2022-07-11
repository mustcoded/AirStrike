class Objectpool(object):

    def __init__(self, size):

        self.size = size
        self.count = 0
        self.elist = [None]*size

    def recycle(self, item):

        if (self.count  < self.size):
            self.elist[self.count] = item
            self.count += 1

    def obtain(self):

        if (self.count > 0):
            self.count -= 1
            self.item = self.elist[self.count]
            self.elist[self.count] = None
            self.item.missile_count = 1
            self.item.hit = False
            return self.item

    def obtain_missile(self, x, y): # get the missile object from the pool

        if (self.count > 0):
            self.count -= 1
            self.item = self.elist[self.count]
            self.elist[self.count] = None
            self.item.x = x
            self.item.y = y
            self.item.on = True

            return self.item

    def getSize(self):

        return self.count

