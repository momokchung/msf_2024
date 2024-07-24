import msf_2024
import numpy as np
import pytest

def test_build_bond_list():
    coordinates = np.array([
        [ 1  , 1  , 1  ],
        [ 2.4, 1  , 1  ],
        [-0.4, 1  , 1  ],
        [ 1  , 1  , 2.4],
        [ 1  , 1  ,-0.4],
    ])
    bonds = msf_2024.build_bond_list(coordinates)
    assert len(bonds) == 4
    for bond_length in bonds.values():
        assert bond_length == pytest.approx(1.4)
