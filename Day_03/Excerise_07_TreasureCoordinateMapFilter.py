# Treasure Coordinate Map filter
coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
valid_coords = [coords for coords in coords if coords[0]>=0 and coords[1]>=0]
print(valid_coords)