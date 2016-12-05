def get_intersections(cars_x, cars_y, cars_width=None, cars_height=None,
                      cars_is_circular=False):
    """
    Computes for a list of cars, which of them intersect each other.

    Note: the cars are currently approximated by rectangles or circles.

    The arguments 'cars_x' and 'cars_y' are two lists of center locations
    of the rectangles/circles. The optional arguments 'cars_width' and
    'cars_height' are two list of the widths and heights of the cars. By
    default, these default to lists containing 2s (for unit squares/circles).
    The optional argument 'cars_is_circular' is a list containing a boolean
    value for each car, indicating whether it's a circle (True).
    For simplicity, this argument can also be passed a boolean value, in which
    case it will be converted to a list of that value, one for each car.
    """
    result = []

    if cars_width is None:
        cars_width = [2] * len(cars_x)

    if cars_height is None:
        cars_height = cars_width[:]

    if not isinstance(cars_is_circular, list):
        cars_is_circular = [cars_is_circular] * len(cars_x)

    for i in range(len(cars_x)):
        for j in range(len(cars_x)):
            if j <= i:
                continue

            car_x = cars_x[i]
            other_car_x = cars_x[j]

            car_y = cars_y[i]
            other_car_y = cars_y[j]

            halfwidth = cars_width[i] / 2
            other_halfwidth = cars_width[j] / 2

            halfheight = cars_height[i] / 2
            other_halfheight = cars_height[j] / 2

            car_is_circular = cars_is_circular[i]
            other_car_is_circular = cars_is_circular[j]

            def sqr(x):
                return x * x

            if car_is_circular and other_car_is_circular:
                if sqr(car_x - other_car_x) + sqr(car_y - other_car_y) < \
                   sqr(halfwidth + other_halfwidth):
                    result.append((i, j))
            elif not car_is_circular and not other_car_is_circular:
                max_distance_width = halfwidth + other_halfwidth
                max_distance_height = halfheight + other_halfheight
                if abs(car_x - other_car_x) < max_distance_width and \
                   abs(car_y - other_car_y) < max_distance_height:
                    result.append((i, j))
            else:
                if car_is_circular and not other_car_is_circular:
                    car_x, other_car_x = other_car_x, car_x
                    car_y, other_car_y = other_car_y, car_y
                    halfwidth, other_halfwidth = other_halfwidth, halfwidth
                    halfheight, other_halfheight = other_halfheight, halfheight
                    car_is_circular, other_car_is_circular = \
                        other_car_is_circular, car_is_circular

                found_intersection = False

                # Step 1: point-in-circle test of corners
                corners = [(car_x - halfwidth, car_y - halfheight),
                           (car_x - halfwidth, car_y + halfheight),
                           (car_x + halfwidth, car_y - halfheight),
                           (car_x + halfwidth, car_y + halfheight)]
                for corner_x, corner_y in corners:
                    if sqr(corner_x - other_car_x) + \
                       sqr(corner_y - other_car_y) < sqr(other_halfwidth):
                        result.append((i, j))
                        found_intersection = True
                        break

                if found_intersection:
                    continue

                # Step 2: point-in-rectangle test of extremes of circle
                extremes = [(other_car_x - other_halfwidth, other_car_y),
                            (other_car_x + other_halfwidth, other_car_y),
                            (other_car_x, other_car_y - other_halfheight),
                            (other_car_x, other_car_y + other_halfheight)]

                # Add center-point, which detects fully overlapping shapes.
                # In case the sizes are equivalent, the extremes do not fall
                # inside the rectangle.
                extremes += [(other_car_x, other_car_y)]

                for extrema_x, extrema_y in extremes:
                    if car_x - halfwidth < extrema_x < car_x + halfwidth and \
                       car_y - halfheight < extrema_y < car_y + halfheight:
                        result.append((i, j))
                        break

    return result
