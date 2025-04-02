import numpy as np

def find_distance(x1,y1,z1,x2,y2,z2):
    """
    Calculates the distance between two 3D points.

    Args:
        points: 2 sets of 3D coordinates, x1,y1,z1,x2,y2,z2.

    Returns:
        A float value that represents the distance between the two points.
    """
    return np.sqrt(np.square(x2-x1)+np.square(y2-y1)+np.square(z2-z1))

def find_center(x_coords, y_coords,z_coords, weight_names):
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

    #following dict correlates atomic weight to all elements found in amino acids
    atomic_weight_dict = {'C': 12.011,
                          'O': 15.999,
                          'S': 32.065,
                          'H': 1.008,
                          'N': 14.007,
                          }
    
    #masses translates the elements in the residue with their corresponding weights
    masses = [atomic_weight_dict[weight_names.iloc[e]] for e in range(len(weight_names))]


    if len(masses) >= 5:
        #this will calculate the center of mass of the sidechain using formula:
        # CoM = m1*x1 + m2*x2 +...+ mn*xn / sum(masses)
        # were only using 4: to remove the influence of the backbone
        center_x = np.array(masses[4:]).dot(np.array(x_coords[4:])) / sum(masses[4:])
        center_y = np.array(masses[4:]).dot(np.array(y_coords[4:])) / sum(masses[4:])
        center_z = np.array(masses[4:]).dot(np.array(z_coords[4:])) / sum(masses[4:])
    else:
        #this is the case for Glycine, which has a hydrogen as a side chain opposing the Nitrogen
        # we will use the coordinates of the Nitrogen on the backbone to approximate the CoM
        center_x = x_coords.iloc[0]
        center_y = y_coords.iloc[0]
        center_z = z_coords.iloc[0]

    return center_x, center_y, center_z