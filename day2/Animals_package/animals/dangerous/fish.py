class Fish:
    def __init__(self):
        '''Constructor for this class'''       
        self.members = ['Cod', 'Tilapia', 'Catfish']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s' % member)
