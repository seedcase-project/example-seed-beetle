# For pretty printing of output
from pathlib import Path
from pprint import pprint

# TODO: This could be a wrapper helper function instead
# To be able to write multiline strings without indentation
from textwrap import dedent

import seedcase_sprout.core as sp

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
file_path = resource_dir / "data-raw/data-ready.csv"
package_path = resource_dir

resource_properties = sp.extract_resource_properties(data_path=file_path)
# pprint(resource_properties)

# print(sp.check_resource_properties(resource_properties))

sp.create_resource_structure(path=sp.path_resources(path=package_path))

sp.create_resource_properties(
    path=sp.path_properties(path=package_path), properties=resource_properties
)

pprint(sp.read_properties(sp.path_properties(path=package_path)))
