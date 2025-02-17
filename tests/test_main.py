import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from BioContactMap.main import distance_and_contact_map

class TestDistanceAndContactMap(unittest.TestCase):

    @patch('BioContactMap.main.PandasPdb')
    @patch('BioContactMap.main.find_center')
    @patch('BioContactMap.main.find_distance')
    def test_distance_and_contact_map(self, mock_find_distance, mock_find_center, MockPdb):
        # Mock the PDB object
        mock_ppdb = MagicMock()
        mock_ppdb.df = {
            'ATOM': pd.DataFrame({
                'residue_number': [1, 1, 2, 2, 3, 3],
                'x_coord': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                'y_coord': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                'z_coord': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            })
        }
        MockPdb().fetch_pdb.return_value = mock_ppdb

        # Mock the helper functions
        mock_find_center.return_value = (0.5, 1.5, 2.5)  # Return mock center of mass coordinates
        mock_find_distance.return_value = 1.0  # Mock the distance function

        # Call the function with sample inputs
        pdb_id = 'test_pdb'
        threshold = 2.5
        center_df, heatmap, heatmap_thresh, fig, fig_thresh = distance_and_contact_map(pdb_id, threshold)

        # Assertions for the returned DataFrames
        self.assertIsInstance(center_df, pd.DataFrame)
        self.assertEqual(center_df.shape, (3, 4))  # 3 residues, 4 columns (Residue, X, Y, Z)
        self.assertIn('Residue', center_df.columns)
        self.assertIn('X', center_df.columns)
        self.assertIn('Y', center_df.columns)
        self.assertIn('Z', center_df.columns)

        self.assertIsInstance(heatmap, pd.DataFrame)
        self.assertEqual(heatmap.shape, (3, 3))  # Heatmap is a square matrix for 3 residues
        self.assertTrue(np.all(heatmap.values == 1.0))  # All distances should be 1.0, mock behavior

        self.assertIsInstance(heatmap_thresh, pd.DataFrame)
        self.assertEqual(heatmap_thresh.shape, (3, 3))
        self.assertTrue(np.all(heatmap_thresh.values == 1))  # Thresholded values (based on mock threshold)

        # Assertions for the plot objects
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(fig_thresh, plt.Figure)

        # Check that the plots are actually created
        plt.close(fig)  # Close to prevent plotting during testing
        plt.close(fig_thresh)

        # Ensure helper functions were called
        mock_find_center.assert_called()
        mock_find_distance.assert_called()

if __name__ == '__main__':
    unittest.main()