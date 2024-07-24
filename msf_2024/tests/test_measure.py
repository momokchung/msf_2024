import msf_2024
import numpy as np
import pytest

def test_calculate_angle():
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])
    angle = msf_2024.calculate_angle(r1, r2, r3)
    expected_angle = np.pi / 2
    assert angle == pytest.approx(expected_angle)