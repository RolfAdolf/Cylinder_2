class Parlgram():
    """In this class we define simple
    constraints. It is easier to represent 
    them as parallelograms. In our 
    simple task version we assume that 
    parallelogram only has constant nominal values
    and no parameters.
    ABC - boundaries.
    a_1, a_2 - Ox boundaries.
    b_1, b_2 - Oy boundaries.
    c_1, c_2 - Oz boundaries.
    """
    def __init__(self, ABC):
        self.a_1 = ABC[0]
        self.a_2 = ABC[1]
        self.b_1 = ABC[2]
        self.b_2 = ABC[3]
        self.c_1 = ABC[4]
        self.c_2 = ABC[5]
