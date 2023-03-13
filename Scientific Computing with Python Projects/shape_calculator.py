class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*self.width+2*self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return 'Too big for picture'
        else:
            return ''.join(['*' if i<self.width-1 else '*\n' for j in range(self.height) for i in range(self.width)])
    def get_amount_inside(self,other_shape):
        if other_shape.width > self.width or other_shape.height > self.height:
            return 0
        hor_fit = self.width//other_shape.width
        ver_fit = self.height//other_shape.height
        return hor_fit*ver_fit
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

# subclass      
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)
    def set_side(self,side):
        self.height = side
        self.width = side
    def set_width(self,side):
        self.set_side(side)
    def set_height(self,side):
        self.set_side(side)
    def __str__(self):
        return f'Square(side={self.height})'