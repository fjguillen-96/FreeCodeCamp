class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Set the width of the rectangle
    def set_width(self,width):
        self.width = width

    # Set the height of the rectangle
    def set_height(self,height):
        self.height = height

    # Calculate the area of the rectangle
    def get_area(self):
        return self.width*self.height

    # Calculate the perimeter of the rectangle
    def get_perimeter(self):
        return 2*self.width+2*self.height

    # Calculate the diagonal of the rectangle
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Generate a string representation of the rectangle as a picture
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return 'Too big for picture'
        else:
            return ''.join(['*' if i<self.width-1 else '*\n' for j in range(self.height) for i in range(self.width)])

    # Calculate how many times another shape can fit inside the rectangle
    def get_amount_inside(self,other_shape):
        if other_shape.width > self.width or other_shape.height > self.height:
            return 0
        hor_fit = self.width//other_shape.width
        ver_fit = self.height//other_shape.height
        return hor_fit*ver_fit

    # String representation of the rectangle
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

# Subclass for square, inherits from Rectangle      
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)

    # Set the side length of the square
    def set_side(self,side):
        self.height = side
        self.width = side

    # Override set_width to set the side length of the square
    def set_width(self,side):
        self.set_side(side)

    # Override set_height to set the side length of the square
    def set_height(self,side):
        self.set_side(side)

    # String representation of the square
    def __str__(self):
        return f'Square(side={self.height})'
