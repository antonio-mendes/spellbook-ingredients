import os
import sys

from write_to_dune import write_to_dune
from dump_spellbook_resources_to_csv import dump_spellbook_resources_to_csv


def main(api_key, spellbook_path, csv_path):
    dump_spellbook_resources_to_csv(spellbook_path, csv_file_path)
    write_to_dune(api_key, csv_file_path)


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        raise ('Usage: python main.py API_KEY MANIFEST_PATH [CSV_FILE_PATH]')
        exit(1)

    api_key = sys.argv[1]
    spellbook_path = sys.argv[2]
    csv_file_path = sys.argv[3] if len(sys.argv) == 4 else os.path.join(
        os.getcwd(), "spellbook_resource_name_dump.csv")
    main(api_key, spellbook_path, csv_file_path)
