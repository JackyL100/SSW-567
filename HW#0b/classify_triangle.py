def classify_triangle(a: float, b: float, c: float):
    '''
    Return type of triangle based on side lengths

    Args:
        a (float): first side length
        b (float): second side length
        c (float): third side length
    
    Returns:
        triangle_type (str): what type of triangle is made with the given side lengths, either: equilateral, isosceles, scalene, or right. Returns None for an invalid triangle
    '''
    sides = [a,b,c]
    sides = sorted(sides)

    for side in sides:
        if side <= 0:
            return None
    
    if (sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2):
        return "Right"
    if (sides[0] == sides[1]):
        if (sides[1] == sides[2]):
            return "Equilateral"
        else:
            return "Isosceles"
    else:
        if (sides[1] == sides[2]):
            return "Isosceles"
    return "Scalene"