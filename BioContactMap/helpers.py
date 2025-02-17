import numpy as np

def find_distance(x1,y1,z1,x2,y2,z2):
    """
    Calculates the distance between two 3D points.

    Args:
        points: 2 sets of 3D coordinates, x1,y1,z1,x2,y2,z2.

    Returns:
        d: A float value that represents the distance between the two points.
    """
    
    d = np.sqrt(np.square(x2-x1)+np.square(y2-y1)+np.square(z2-z1))
    return d

def find_center(x_coords, y_coords,z_coords):
    """
    Calculates the center point of a list of 3D coordinates.

    Args:
        x_coords: list of x values
        y_coords: list of y values
        z_coords: list of z values

    Returns:
        center_x: mean x value
        center_y: mean y value
        center_z :mean z value

    Assert: for future unittesting min_x<center_x<max_x + len(x_coords)==len(y_coords)
    """

    center_x = sum(x_coords) / len(x_coords)
    center_y = sum(y_coords) / len(y_coords)
    center_z = sum(z_coords) / len(z_coords)
    
    return center_x, center_y, center_z