#!/usr/bin/env python
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables from .env file and fetch the REDCAP_TOKEN
load_dotenv()

token = os.getenv("REDCAP_TOKEN")
if not token:
    raise ValueError("REDCAP_TOKEN not found in environment variables")

# Get the directory where the script is located
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "raw"
output_file = folder_path / "data-from-redcap.csv"

data = {
    "token": token,
    "content": "record",
    "action": "export",
    "format": "csv",
    "type": "flat",
    "csvDelimiter": ";",
    "fields[0]": "redcap_id",
    "fields[1]": "cycle",
    "fields[2]": "o2_consumed",
    "fields[3]": "co2_produced",
    "fields[4]": "respiratory_quotient",
    "fields[5]": "block",
    "fields[6]": "activity",
    "fields[7]": "strain",
    "fields[8]": "mitochondrial_dna_lineage",
    "fields[9]": "nuclear_lineage",
    "fields[10]": "mating_treatment",
    "fields[11]": "coadaptation",
    "fields[12]": "virgin_body_weight",
    "fields[13]": "body_weight_after_mating",
    "fields[14]": "mated_body_weight_after_respirometry",
    "fields[15]": "ejaculate_weight_first_mating",
    "fields[16]": "ejaculate_weight_second_mating",
    "fields[17]": "copulation_duration_first_mating",
    "fields[18]": "copulation_duration_second_mating",
    "rawOrLabel": "label",
    "rawOrLabelHeaders": "label",
    "exportCheckboxLabel": "false",
    "exportSurveyFields": "false",
    "exportDataAccessGroups": "false",
    "returnFormat": "json",
}
imported_data = requests.post("https://redcap.au.dk/api/", data=data)

if imported_data.status_code == 200:
    output_file.write_text(imported_data.text, encoding="utf-8")
else:
    print("Error retrieving data, status code:", imported_data.status_code)
