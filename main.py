import seedcase_sprout as sp

from scripts.properties import properties


def main():
    """Pipeline for creating the seed beetle Data Package."""
    # Create the properties script in the default location.
    sp.create_properties_script()
    # Write properties to `datapackage.json`.
    sp.write_properties(properties=properties)


if __name__ == "__main__":
    main()
