import numpy as np

def random_unit_vector():
    theta = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, np.pi)
    x = np.cos(theta) * np.sin(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(phi)
    return np.array([x, y, z])

def shift_atom_position(atom_position, cell_params, shift_distance):
    unit_vector = random_unit_vector()
    cartesian_position = atom_position[0]*cell_params[0] + atom_position[1]*cell_params[1] + atom_position[2]*cell_params[2]
    displacement_vector = unit_vector * shift_distance
    new_cartesian_position = cartesian_position + displacement_vector
    new_relative_position = np.linalg.solve(cell_params.T, new_cartesian_position)
    return new_relative_position

# Define your crystal cell parameters
a = np.array([7.9740500450,0.0000000000,0.0000000000])
b = np.array([0.0000000000,9.2076396942,0.0000000000])
c = np.array([0.0000000000,0.0000000000,8.6286020279])

# Define the relative atom location
atom_location = np.array([0.111111111,0.555555555,0.583333333])

# Shift the atom's position by 0.15 angstroms in a random direction
shift_distance = 0.15
cell_params = np.vstack((a, b, c))
new_atom_location = shift_atom_position(atom_location, cell_params, shift_distance)

print("Original atom location:", atom_location)
print("New atom location:", new_atom_location)
