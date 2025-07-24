import seedcase_sprout as sp

resource_properties_metabolic_rate = sp.ResourceProperties(
    ## Required:
    name="metabolic-rate",
    title="Metabolic rate of the seed beetles",
    description=(
        """This dataset contains metabolic rate, respiratory quotient, body weight and
        ejaculate weight data from seed beetles with different mitonuclear genotypes."""
    ),
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
                title="Cycle",
                # format="",
                description=(
                    """Focal cycle in the respirometry. Note that the number one here
                    corresponds to the real cycle number two, as the first one was
                    removed as a burn-in. Original field name: `CYCLE`."""
                ),
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="o2_consumed",
                type="number",
                ## Optional
                title="O2 consumed",
                # format="",
                description="Original field name: `O2`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="co2_produced",
                type="number",
                ## Optional
                title="CO2 produced",
                # format="",
                description="Original field name: `CO2`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="respiratory_quotient",
                type="number",
                ## Optional
                title="Respiratory quotient",
                # format="",
                description="Original field name: `RQ`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="block",
                type="string",
                ## Optional
                title="Block",
                # format="",
                description="Experimental block. Original field name: `BLOCK`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="activity",
                type="number",
                ## Optional
                title="Activity",
                # format="",
                description="Original field name: `ACTIVITY`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="strain",
                type="string",
                ## Optional
                title="Strain",
                # format="",
                description="Line identity. Original field name: `STRAIN`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="mitochondrial_dna_lineage",
                type="string",
                ## Optional
                title="Mitochondrial DNA lineage",
                # format="",
                description="Original field name: `MT_DNA_HAPLOTYPE`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="nuclear_lineage",
                type="string",
                ## Optional
                title="Nuclear lineage",
                # format="",
                description="Original field name: `NC_GENOTYPE`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="mating_treatment",
                type="string",
                ## Optional
                title="Mating treatment",
                # format="",
                description="Mated or virgin. Original field name: `TREATMENT`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="coadaptation",
                type="integer",
                ## Optional
                title="Coadaptation",
                # format="",
                description=(
                    """Coadaptation of the mitochondrial and nuclear lineage genomes.
                    Original field name: `COEVOL`."""
                ),
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="virgin_body_weight",
                type="number",
                ## Optional
                title="Virgin body weight",
                # format="",
                description="Unit: g. Original field name: `W_V`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="body_weight_after_mating",
                type="number",
                ## Optional
                title="Body weight after mating",
                # format="",
                description=(
                    """Body weight after mating, prior to respirometry measurements.
                    Unit: g. Original field name: `W_M1`."""
                ),
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="mated_body_weight_after_respirometry",
                type="number",
                ## Optional
                title="Mated body weight after respirometry",
                # format="",
                description=(
                    """Mated male body weight after the respirometry, prior to second
                    mating. Unit: g. Original field name: `W_M1R`."""
                ),
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="ejaculate_weight_first_mating",
                type="number",
                ## Optional
                title="Ejaculate weight in the first mating",
                # format="",
                description="Unit: g. Original field name: `EJAC1`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="ejaculate_weight_second_mating",
                type="number",
                ## Optional
                title="Ejaculate weight in the second mating",
                # format="",
                description="Unit: g. Original field name: `EJAC2`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="copulation_duration_first_mating",
                type="number",
                ## Optional
                title="Copulation duration of the first mating",
                # format="",
                description="Unit: sec. Original field name: `COPULDUR_1`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="copulation_duration_second_mating",
                type="number",
                ## Optional
                title="Copulation duration of the second mating",
                # format="",
                description="Unit: sec. Original field name: `COPULDUR_2`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
            sp.FieldProperties(
                ## Required
                name="id",
                type="integer",
                ## Optional
                title="ID",
                # format="",
                description="Experimental subject identity. Original field name: `ID`.",
                # example="",
                # categories=[],
                # categories_ordered=False,
            ),
        ],
        ## Optional
        # fields_match=["equal"],
        primary_key=["id"],
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
