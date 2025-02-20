import re
from pathlib import Path

import janitor.polars  # noqa: F401
import polars as pl

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

# Transform from tab sep to comma sep
with open(folder_path / "data.tsv", "r") as tsv:
    with open(folder_path / "data-ready.csv", "w") as csv:
        for line in tsv:
            content = re.sub("\t", ",", line)
            csv.write(content)

# Pull in data
df = pl.read_csv(folder_path / "data-ready.csv", infer_schema_length=100_000)

block_mapping = {1: "Block 1", 2: "Block 2", 3: "Block 3"}

treatment_map = {"V": "Virgin", "M": "Mating"}

df = (
    df.with_columns(
        pl.col("TREATMENT").replace_strict(treatment_map),
        pl.col("BLOCK").replace_strict(block_mapping, return_dtype=pl.Utf8),
    )
    .clean_names()
    .rename(
        {
            "o2": "o2_consumed",
            "co2": "co2_produced",
            "rq": "respiratory_quotient",
            "mt_dna_haplotype": "mitochondrial_dna_lineage",
            "nc_genotype": "nuclear_lineage",
            "treatment": "mating_treatment",
            "coevol": "coadaptation",
            "w_v": "virgin_body_weight",
            "w_m1": "body_weight_after_mating",
            "w_m1r": "mated_body_weight_after_respirometry",
            "ejac1": "ejaculate_weight_first_mating",
            "ejac2": "ejaculate_weight_second_mating",
            "copuldur_1": "copulation_duration_first_mating",
            "copuldur_2": "copulation_duration_second_mating",
        }
    )
)

df.write_csv(folder_path / "data-ready.csv")

df.glimpse()
