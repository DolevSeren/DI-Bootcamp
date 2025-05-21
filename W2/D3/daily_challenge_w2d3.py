import math
import turtle

class Circle:
    def __init__(self, *, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must specify either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Circle):
            return self.radius != other.radius
        return NotImplemented

# --- Example usage ---
print("=== Circle Attributes & Arithmetic ===")
c1 = Circle(radius=5)
c2 = Circle(diameter=10)

print(c1)                        # Circle(radius=5.00, diameter=10.00, area=78.54)
print("c2 radius:", c2.radius)  # 5.0
print("c2 diameter:", c2.diameter)
print("c2 area:", c2.area)

c3 = c1 + c2
print("c3 radius:", c3.radius)  # 10.0

print("c1 > c2?", c1 > c2)      # False
print("c1 == c2?", c1 == c2)    # True

print("\n=== Sorted Circles ===")
circle_list = [Circle(radius=3), Circle(radius=1), Circle(radius=7)]
circle_list.sort()
for circle in circle_list:
    print(circle)

# --- Bonus: Turtle drawing of sorted circles ---
def draw_circle(circle, x_offset=0):
    turtle.penup()
    turtle.goto(x_offset, -circle.radius)
    turtle.pendown()
    turtle.circle(circle.radius)

print("\n=== Drawing Circles with Turtle ===")
turtle.speed(1)
sorted_circles = sorted([Circle(radius=30), Circle(radius=10), Circle(radius=50)])
x = -150
for circ in sorted_circles:
    draw_circle(circ, x_offset=x)
    x += circ.diameter + 10

turtle.done()
