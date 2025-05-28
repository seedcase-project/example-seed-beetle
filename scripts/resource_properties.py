import seedcase_sprout as sp


def resource_properties_seed_beetles():
    """Contains the properties of the seed beetles resource."""
    return sp.ResourceProperties(
        name="seed-beetles",
        title="Seed beetle data",
        description="Some data on seed beetles.",
        schema=sp.TableSchemaProperties(
            fields=[
                sp.FieldProperties(
                    name="id",
                    title="ID",
                    description="Unique identifier for the record.",
                    type="integer",
                ),
                sp.FieldProperties(
                    name="name",
                    title="Name",
                    description="Name of the record.",
                    type="string",
                ),
            ],
            primary_key=["id"],
        ),
    )
