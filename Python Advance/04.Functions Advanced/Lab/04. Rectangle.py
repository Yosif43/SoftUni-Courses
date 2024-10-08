def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    result = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return result

print(rectangle(2, 10))
print(rectangle("2", 10))