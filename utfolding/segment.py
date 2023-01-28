#! /usr/bin/env python3

# chord length = 2*radius sin(center-angle/2)
# Sagitta = r+- sqrt(radius^2 - half_chord_length)
import math

NUMBER_OF_SEGMENTS = 10
RADIUS = 50

center_angle = 180 - 2 * 360 / NUMBER_OF_SEGMENTS


def chord_length(radius: int | float, center_angle: int | float) -> float:
    radian = math.radians(center_angle)
    return 2 * radius * math.sin(radian / 2)


def rise_from_height(
    outer_height: int | float, inner_height: int | float, radius: int | float
) -> float:
    """get the rise value using the inner and outer height of the segment, and the radius of the pipe"""
    higher = max(outer_height, inner_height)
    lower = min(outer_height, inner_height)
    return (higher - lower) / (radius * 2)


def rise_from_angle(
    outer_height: int | float, angle: int | float, radius: int | float
) -> list[float]:
    """get the rise value using the angle and outer height of the segment, and the radius of the pipe"""
    return


def get_x(n_segments: int, radius: int | float) -> list:
    """Get a list of x points from the left most point in a circle, where the
    segments meet the radius
    """
    x = []
    single_angle = 360 / n_segments
    for n in range(n_segments + 1):
        chord_angle = n * single_angle
        chord = chord_length(radius, chord_angle)
        chord_diff = radius * 2 - chord
        x.append(chord_diff)
        # x.insert(-n, chord_diff)

    return x


def list_of_points(x_list: list, y_rise: int | float) -> list:
    y_list = []
    for x in x_list:
        y_list.append(x * y_rise)

    return zip(x_list, y_list)


def get_x_list(total_segments: int, radius: int | float) -> list:
    """Get a list of x points from the left most point in a circle, where the
    segments meet the radius
    """
    x = []
    # we are calculating x from a quarter of a circle, and the angle has to be
    # symetrical
    angle = 2 * (360 / total_segments)
    for n in range(total_segments):
        # the remaining angle on each side corresponds with x
        remaining_angle = 180 - angle * n
        # remove half the chord length from the radius and we are left with the
        # distance from the left edge to x
        remaining_x = radius - chord_length(radius, remaining_angle) / 2
        x.append(remaining_x)
    x.append(0)
    return x


class Segment:
    def __init__(self) -> None:
        pipe_radius = self.pipe_radius

    pipe_radius = diameter / 2
    diameter = pipe_radius / 2


"""
for each segment length
    new_x = radius - chord_length / 2
    next point = (cum_segment_len, clip(x))
    add line from previous point to next point
"""
