import seedcase_sprout as sp

from scripts.resource_properties import resource_properties_seed_beetles

properties = sp.PackageProperties.from_default(
    name="male-seed-beetle",
    title=(
        "Complex mitonuclear interactions and metabolic costs of mating "
        "in male seed beetles"
    ),
    description=(
        "Data from the 2015 on metabolic rate, respiratory quotient, body "
        "weight and ejaculate weight data from seed beetles with different "
        "mitonuclear genotypes."
    ),
    contributors=[
        sp.ContributorProperties(
            title="Elina Immonen",
            path="https://www.uu.se/en/contact-and-organisation/staff?query=N12-1639",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Johanna Liljestrand-Rönn",
            path="https://www.uu.se/en/contact-and-organisation/staff?query=N2-1345",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Christopher Watson",
            path="https://www.uu.se/en/department/ecology-and-genetics/research/evolutionary-biology/immonen-lab",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="David Berger",
            path="https://www.uu.se/en/contact-and-organisation/staff?query=N11-2446",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Göran Arnqvist",
            path="https://www.uu.se/en/contact-and-organisation/staff?query=N1-1284",
            roles=["creator"],
        ),
    ],
    sources=[
        sp.SourceProperties(
            title=(
                "Complex mitonuclear interactions and metabolic costs of mating "
                "in male seed beetles"
            ),
            path="https://zenodo.org/record/4932381",
        )
    ],
    licenses=[
        sp.LicenseProperties(
            name="CCO_1.0",
            path="https://creativecommons.org/publicdomain/zero/1.0/legalcode",
            title="CCO 1.0 UNIVERSAL",
        )
    ],
    resources=[resource_properties_seed_beetles()],
)


# Create the path to the package

sp.write_package_properties(properties=properties)
