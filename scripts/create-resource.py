# For pretty printing of output
from pathlib import Path
from pprint import pprint

# TODO: This could be a wrapper helper function instead
# To be able to write multiline strings without indentation
from textwrap import dedent

import seedcase_sprout.core as sp

# Set the folder path for raw-data
package_path = Path(__file__).resolve().parent.parent

file_path = package_path / "data-raw/data-ready.csv"

resource_properties = sp.extract_resource_properties(data_path=file_path)
pprint(resource_properties)

print(sp.check_resource_properties(resource_properties))

# sp.create_resource_structure(path=sp.path_resources(path=package_path))

# sp.create_resource_properties(
#     path=sp.path_properties(path=package_path), properties=resource_properties
# )

# pprint(sp.read_properties(sp.path_properties(path=package_path)))

# sp.write_resource_batch_data(
#     data_path=file_path, resource_properties=resource_properties
# )
# print(sp.path_resource_batch_files(1, path=package_path))

# sp.build_resource_parquet(
#     raw_files=sp.path_resource_batch_files(1, path=package_path),
#     path=sp.path_resource_data(1, path=package_path),
# )

# readme_text = sp.as_readme_text(
#     properties=sp.read_properties(sp.path_properties(path=package_path))
# )

# sp.write_file(
#     text=readme_text,
#     path=sp.path_readme(path=package_path)
# )
