from pathlib import Path
from pprint import pprint

import seedcase_sprout.core as sp

properties = sp.PackageProperties(
    title=(
        "Complex mito-nuclear interactions and metabolic costs of mating "
        "in male seed beetles"
    ),
    description=(
        "Data from the 2015 on metabolic rate, respiratory quotient, body "
        "weight and ejaculate weight data from seed beetles with different "
        "mito-nuclear genotypes."
    ),
)

package_path = Path(__file__).resolve().parent.parent / "datapackage.json"

updated_package_properties = sp.edit_package_properties(
    path=package_path,
    properties=properties,  # sp.PackageProperties(name="male-seed-beetle"),
)

package_path = sp.write_package_properties(
    properties=updated_package_properties, path=package_path
)
