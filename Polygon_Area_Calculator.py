class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if (self.height and self.width) > 50:
            return "Too big for picture."
        output = ""
        for i in range(self.height):
            output += "*" * self.width +"\n"
        return output

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.height})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)





# rect = Rectangle(5, 10)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect.get_picture())
# print(rect)
#
sq = Square(9)
print(sq.get_area())
print(sq)
sq.set_width(3)
print(sq.get_diagonal())
print(sq)