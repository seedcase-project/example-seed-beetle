import seedcase_sprout as sp

from scripts.package_properties import properties

# Create the path to the package
if __name__ == "__main__":
    sp.write_package_properties(properties=properties)
    text = sp.as_readme_text(properties)
    sp.write_file(text, sp.PackagePath().readme())
