class Cylinder():
    """The Cylinder class, 
    which we use to define 
    surfaces of this type.
    R - base radius,
    h - height,
    I = [x0, y0, z0] - base center.
    """
    def __init__(self, R = 0, h = 0, I = [0, 0, 0]):
        self.R = R
        self.h = h
        self.x_0 = I[0]
        self.y_0 = I[1]
        self.z_0 = I[2]
