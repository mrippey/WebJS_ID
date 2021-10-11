# WebJS_ID

Identify websites running suspicious JavaScript code using the PublicWWW API.

## Usage

WebJS_ID supports the following:

```bash
webjs_id.py -h
Examples:
         python webjs_id.py -q 'path to provided JSON configuration file'
         python webjs_id.py -o 'path to file to write results to'
         python webjs_id.py -c 'write output to csv file identified with -o option'

optional arguments:
  -h, --help                    show this help message and exit
  -q QUERY_FILE, --query_file   path to JSON file
  -o OUTPUT_TYPE, --output_file Output file to write
  -c CSV --csv                  Output data to csv


# TODO:

WebJS_ID currently only prints to stdout. Some queries can return a large amount of results, funcitionality for writing to a csv file, or regular text file
will be included at a later date.
