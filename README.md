# BioContactMap
![coverage](https://img.shields.io/badge/coverage-100%10green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

BioContactMap is a Python package designed for calculating distance and contact maps from protein structure data. It computes the distances between the centers of mass of each residue in a provided PDB file and generates both a distance matrix and a binary contact map.

## Features
- Compute the center of mass for each residue in a PDB file.
- Generate a distance map between residues.
- Create a thresholded contact map based on a user-defined distance cutoff.
- Visualize the distance and contact maps with heatmaps using Seaborn.

## Installation

### Prerequisites
To use this package, you'll need the following dependencies:
- Python 3.6+
- `biopandas` ==0.5.1
- `matplotlib` ==3.7.2
- `seaborn`==0.13.2
- `numpy`==1.24.3
- `pandas`==1.5.3

### Steps
1. Clone the repository:

```
   git clone https://github.com/yourusername/BioContactMap.git
   cd BioContactMap
```

2. Create a Virtual Environment:
```
	python -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install Required Dependencies:
```
	pip install -r requirements.txt
```

## Usage
You can use the distance_and_contact_map function to calculate and visualize distance and contact maps. Here's a basic example:
```
from BioContactMap.main import distance_and_contact_map

# Define the PDB ID and distance threshold (in Angstroms)

pdb_id = '1ABC'  # Example PDB ID
threshold = 8   # Threshold for contact map in Angstroms


# Call the function

center_df, heatmap, heatmap_thresh, fig, fig_thresh = distance_and_contact_map(pdb_id, threshold)

# You can now use `fig` and `fig_thresh` to show the distance and contact maps

fig.show()
fig_thresh.show()
```

## Functions

### `distance_and_contact_map(pdb, threshold)`
- **Description**: This function computes the distance matrix and contact map for the protein structure provided by the PDB ID. It calculates the center of mass for each residue, computes the pairwise distances between the residues, and generates both a distance matrix and a thresholded contact map based on the provided distance threshold.
  
- **Arguments**:
  - `pdb` (str): The PDB ID or a PDB file containing the protein structure.
  - `threshold` (float): A distance threshold in Angstroms, used to define contacts between residues. Residues within this distance are considered in contact.
  
- **Returns**:
  - `center_df` (DataFrame): A DataFrame containing the center of mass coordinates (X, Y, Z) for each residue.
  - `heatmap` (DataFrame): A DataFrame representing the distance matrix between the residues, with the distances in Angstroms.
  - `heatmap_thresh` (DataFrame): A binary DataFrame representing the thresholded contact map. Values are `1` if residues are in contact (distance <= threshold) and `0` otherwise.
  - `fig` (matplotlib.figure.Figure): A heatmap figure visualizing the distance matrix using Seaborn.
  - `fig_thresh` (matplotlib.figure.Figure): A heatmap figure visualizing the thresholded contact map.

### `find_center(x_coords, y_coords, z_coords)`
- **Description**: This function calculates the center of mass for a residue based on its atomic coordinates (X, Y, Z). It averages the coordinates of all atoms in the residue to obtain the center of mass.

- **Arguments**:
  - `x_coords` (list): A list of x-coordinates for the atoms of the residue.
  - `y_coords` (list): A list of y-coordinates for the atoms of the residue.
  - `z_coords` (list): A list of z-coordinates for the atoms of the residue.

- **Returns**:
  - `x_center` (float): The x-coordinate of the center of mass for the residue.
  - `y_center` (float): The y-coordinate of the center of mass for the residue.
  - `z_center` (float): The z-coordinate of the center of mass for the residue.

### `find_distance(x1, y1, z1, x2, y2, z2)`
- **Description**: This function calculates the Euclidean distance between two points in 3D space, given their (x, y, z) coordinates.

- **Arguments**:
  - `x1, y1, z1` (float): The coordinates of the first point.
  - `x2, y2, z2` (float): The coordinates of the second point.

- **Returns**:
  - `distance` (float): The Euclidean distance between the two points.


## Contributing
We welcome contributions to the BioContactMap project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add feature').
5. Push your changes to your fork (git push origin feature-branch).
6. Submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- **BioPandas**: For handling PDB data.
- **Seaborn**: For beautiful heatmap visualizations.
- **NumPy and Pandas**: For data manipulation and analysis.



