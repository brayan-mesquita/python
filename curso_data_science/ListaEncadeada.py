class ItemLista:
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.nextItem = None
    def __repr__(self):
        return '%s' % (self.data, self.nextItem)

