'''Contains function that classifies triangles'''

def classify_triangle(side_a: float, side_b: float, side_c: float):
    ''' 
    Return type of triangle based on side lengths

    Args:
        side_a (float): first side length
        side_b (float): second side length
        side_c (float): third side length
    
    Returns:
        triangle_type (str): equilateral, isosceles, scalene, right, or None
    '''
    sides = [side_a,side_b,side_c]
    sides = sorted(sides)

    for side in sides:
        if side <= 0:
            return None
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "Right"
    if sides[0] == sides[1]:
        if sides[1] == sides[2]:
            return "Equilateral"
        return "Isosceles"
    if sides[1] == sides[2]:
        return "Isosceles"
    return "Scalene"
