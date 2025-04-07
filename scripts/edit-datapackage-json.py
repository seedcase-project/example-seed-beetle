from pathlib import Path

import seedcase_sprout.core as sp

package_path = Path(__file__).resolve().parent.parent

current_properties = sp.read_properties(
    path=sp.PackagePath(package_path).properties(),
)

updated_properties = sp.PackageProperties(
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

updated_package_properties = sp.update_package_properties(
    current_properties=current_properties,
    update_properties=updated_properties,
)

sp.write_package_properties(
    properties=updated_package_properties,
    path=sp.PackagePath(package_path).properties(),
)
