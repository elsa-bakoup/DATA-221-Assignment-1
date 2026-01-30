def circle_area_coverage(radius_of_circle1, radius_of_circle2):

    if not isinstance(radius_of_circle1, int) or not isinstance(radius_of_circle2, int) \
            or radius_of_circle1 <= 0 or radius_of_circle2 <= 0:
        return "Invalid input, both radii must be positive integers."

    area_circle_1 = 3.14 * (radius_of_circle1**2)
    area_circle_2 = 3.14 * (radius_of_circle2**2)

    smaller = min(area_circle_1, area_circle_2)
    larger = max(area_circle_1, area_circle_2)

    return (smaller / larger) * 100
