import os
import csv
import json


def dump_spellbook_resources_to_csv(manifest_path, csv_path):
    manifest_file = f'{manifest_path}target/manifest.json'
    print(manifest_file)
    if os.path.exists(manifest_file):
        with open(manifest_file) as f:
            manifest = json.load(f)
    else:
        raise Exception(
            "Manifest file not found! Make sure you ran `dbt compile` first.")
        exit(1)

    # Extract the names of all the tables that are resources to Spells
    resource_names = []
    for source_table in manifest['sources']:
        clean_source_table = source_table.replace('source.spellbook.', '')
        resource_names.append(clean_source_table)

    if len(resource_names) == 0:
        raise Exception('No resources found!')
        exit(1)

    # Write to CSV
    fieldnames = ['spellbook_dependencies']
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        _ = writer.writerow(fieldnames)
        for name in resource_names:
            _ = writer.writerow([name])
