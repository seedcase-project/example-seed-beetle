import polars as pl
import seedcase_sprout as sp

from scripts.package_properties import package_properties
from scripts.resource_properties_seed_beetle_metabolic_rate import (
    resource_properties_seed_beetle_metabolic_rate,
)


def main():
    """Pipeline for creating the seed beetle Data Package.

    Note: Make sure to run the following scripts before this pipeline to
    download and tidy the data:
    - `scripts/download-data.py`
    - `scripts/clean-data.py`
    The tidied data should then be available in `raw/data-ready.csv`.
    """
    # Create the properties script (will not be overwritten).
    sp.create_properties_script()

    # Load the tidied data from the CSV file.
    data = pl.read_csv(sp.PackagePath().root() / "raw" / "data-ready.csv")
    # Extract field properties.
    field_properties = sp.extract_field_properties(
        data=data,
    )
    # Create the resource properties script (will not be overwritten).
    sp.create_resource_properties_script(
        resource_name="seed-beetle-metabolic-rate",
        fields=field_properties,
    )

    # Write properties to `datapackage.json`.
    sp.write_properties(properties=package_properties)
    # Create text for a README of the data package.
    readme_text = sp.as_readme_text(package_properties)
    # Write the README text to a `README.md` file.
    sp.write_file(readme_text, sp.PackagePath().readme())

    # Write tidied data to batch.
    sp.write_resource_batch(
        data=data, resource_properties=resource_properties_seed_beetle_metabolic_rate
    )

    # Read in batch data file for the resource as a list.
    batch_data = sp.read_resource_batches(
        resource_properties=resource_properties_seed_beetle_metabolic_rate
    )
    # Join batch data into a single Polars DataFrame (and remove potential duplicates).
    joined_data = sp.join_resource_batches(
        data_list=batch_data,
        resource_properties=resource_properties_seed_beetle_metabolic_rate,
    )

    # Write the joined data to the resource.
    sp.write_resource_data(
        data=joined_data,
        resource_properties=resource_properties_seed_beetle_metabolic_rate,
    )


if __name__ == "__main__":
    main()
