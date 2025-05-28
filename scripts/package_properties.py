from textwrap import dedent

import seedcase_sprout as sp

from .resource_properties import resource_properties

properties = sp.PackageProperties.from_default(
    name="male-seed-beetle",
    title=(
        "Complex mitonuclear interactions and metabolic costs of mating "
        "in male seed beetles"
    ),
    description=dedent("""
        Data from the 2015 on metabolic rate, respiratory quotient, body
        weight and ejaculate weight data from seed beetles with different
        mitonuclear genotypes.

        This repository shows how to use the Seedcase Sprout tools on a data set
        of seed beetle data. The data is from a study by [Immonen et al.
        (2015)](https://onlinelibrary.wiley.com/doi/10.1111/jeb.12789) and is
        available on [Zenodo](https://zenodo.org/records/4932381).
    """),
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
    resources=[resource_properties],
)
