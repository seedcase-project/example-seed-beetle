import seedcase_sprout as sp

from scripts.properties import properties


def main():
    """Pipeline for creating the seed beetle Data Package."""
    # Create the properties script in the default location.
    sp.create_properties_script()
    # Write properties to `datapackage.json`.
    sp.write_properties(properties=properties)
    # Create text for a README of the data package.
    readme_text = sp.as_readme_text(properties)
    # Write the README text to a `README.md` file.
    sp.write_file(readme_text, sp.PackagePath().readme())


if __name__ == "__main__":
    main()
