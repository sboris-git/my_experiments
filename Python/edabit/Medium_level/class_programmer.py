class Programer:
    '''
    I want you to create a class called programmer. It has a sallary value, work_hours value,
and a __ del __ (self) function. __ del __ (self) returns ()"oof, " + str(sallary) + ", " + str(work_hours))
when the object is destroyed using del obj. sallary and work_hours will be in the constructor.
Varibales in a class are defined with self.name = value.

        prog = programer(25000, 5)
        prog.sallary ➞ 25000
        prog.work_hours ➞ 5
        del prog ➞ "oof, 25000, 5"
        # By the __ del __ function.
    '''

    def __init__(self, sallary, work_hours):
        self.sallary = sallary
        self.work_hours = work_hours

    def __del__(self):
        return print("oof, " + str(self.sallary) + ", " + str(self.work_hours))
    '''
    def __lt__(self, other):
        if not isinstance(other, Programer):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.sallary < other.sallary and self.work_hours < other.work_hours

    def __eq__(self, other):
        if not isinstance(other, Programer):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.sallary == other.sallary and self.work_hours == other.work_hours
    '''
    '''If you use the functools.total_ordering decorator, you only need to implement e.g. the __lt__ and __eq__ methods:

    from functools import total_ordering
    
    @total_ordering
    class Point(object):
        def __lt__(self, other):
            ...
    
        def __eq__(self, other):
    '''

    '''Also, define a function that will compare two programmers (their sallary and work_hours).
    If their sallary is equal, then work_hours is compared, they will allways be different.
    Return the programmer that is worse.'''
    def compare(self, other):
        if self.sallary < other.sallary:
            return self
        elif self.sallary > other.sallary:
            return other
        else:
            if self.sallary == other.sallary:
                if self.work_hours < other.work_hours:
                    return self
                else:
                    return other


prog = Programer(10000, 8)
prog2 = Programer(50000, 5)

print(prog.sallary)  # ➞ 25000
print(prog.work_hours)  # ➞ 5
print(prog.compare(prog2))
del prog  # ➞ "oof, 25000, 5"

'''

Notes
Only base functions are pre-written in the code tab. You need to complete them and possibly add a few arguments.
Variables are defined inside the __ init __ function.
In most cases __ del __ isn't used to return values (but it's not possible to check print output).
'''