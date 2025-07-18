import seedcase_sprout as sp

resource_properties_seed_beetle_metabolic_rate = sp.ResourceProperties(
    ## Required:
    name="seed-beetle-metabolic-rate",
    title="",
    description="",
    ## Optional:
    type="table",
    format="parquet",
    mediatype="application/parquet",
    schema=sp.TableSchemaProperties(
        ## Required
        fields=[
            sp.FieldProperties(
                ## Required
                name="cycle",
                type="integer",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="o2_consumed",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="co2_produced",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="respiratory_quotient",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="block",
                type="string",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="activity",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="strain",
                type="string",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="mitochondrial_dna_lineage",
                type="string",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="nuclear_lineage",
                type="string",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="mating_treatment",
                type="string",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="coadaptation",
                type="integer",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="virgin_body_weight",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="body_weight_after_mating",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="mated_body_weight_after_respirometry",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="ejaculate_weight_first_mating",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="ejaculate_weight_second_mating",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="copulation_duration_first_mating",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="copulation_duration_second_mating",
                type="number",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="id",
                type="integer",
                ## Optional
                # title="",
                # format="",
                # description="",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
        ],
        ## Optional
        # fields_match=["equal"],
        # primary_key=[""],
        # unique_keys=[[""]],
        # foreign_keys=[
        #     sp.TableSchemaForeignKeyProperties(
        #         ## Required
        #         fields=[""],
        #         reference=sp.ReferenceProperties(
        #             ## Required
        #             resource="",
        #             fields=[""],
        #         ),
        #     ),
        # ],
    ),
    # sources=[
    #     sp.SourceProperties(
    #         ## Required:
    #         title="",
    #         ## Optional:
    #         path="",
    #         email="",
    #         version="",
    #     ),
    # ],
)