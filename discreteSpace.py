
class DiscreteSpace:
    
    def __init__(self):
        self.dim = None
        self.space = None
        self.spaceDict = {}
        
    def setSpace(self, space=None):  
        
        if not space is None:
            assert isinstance(space, list)
            assert len(space) > 0
            self.dim = len(space)
            self.space = space
            self.spaceDict = {int(_): space[_] for _ in range(self.dim)}  
