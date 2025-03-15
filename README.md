# Polygon Area Calculator

## Description
This project implements a `Rectangle` class and a `Square` class using object-oriented programming principles. The `Square` class is a subclass of `Rectangle` and inherits its methods and attributes. The implementation allows for calculating various properties of rectangles and squares such as area, perimeter, diagonal, and visual representation.

## Classes

### Rectangle
The `Rectangle` class is initialized with `width` and `height` attributes and includes the following methods:

- `set_width(width)`: Sets the width of the rectangle
- `set_height(height)`: Sets the height of the rectangle
- `get_area()`: Returns the area (width * height)
- `get_perimeter()`: Returns the perimeter (2 * width + 2 * height)
- `get_diagonal()`: Returns the diagonal ((width² + height²)^0.5)
- `get_picture()`: Returns a string representation of the shape using lines of '*'
- `get_amount_inside(shape)`: Returns how many times the passed shape fits inside this rectangle

When a `Rectangle` is represented as a string, it looks like: `'Rectangle(width=5, height=10)'`

### Square
The `Square` class is a subclass of `Rectangle`. When a `Square` object is created, a single side length is passed in, which is stored as both the `width` and `height` attributes from the `Rectangle` class.

Additional methods for the `Square` class:
- `set_side(side)`: Sets both width and height to the given side length
- The inherited `set_width` and `set_height` methods update both dimensions to maintain a square

When a `Square` is represented as a string, it looks like: `'Square(side=9)'`

## Usage Example

```python
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

## Output
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

## Testing
The code includes comprehensive tests to validate the implementation against all specified requirements. Run the script directly to execute all tests and see the example usage output.

## Requirements
- Python 3.x

## Notes
- The `get_picture()` method will return "Too big for picture." if the width or height is larger than 50.
- The `get_amount_inside()` method calculates how many times another shape can fit inside without rotations.
