{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d0f6708b-229d-413a-adba-07a14bc05945",
   "metadata": {},
   "source": [
    "### Custom Project from PSET2 for Github \n",
    "\n",
    "Created by: Clement Chai\n",
    "\n",
    "Date: 05/26/2025\n",
    "Updated on: 06/14/2025\n",
    "\n",
    "---\n",
    "\n",
    "#####  -Requires `validate_and_extract_log()` function and `manufacturelog.py` files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a058a396-8d95-4df5-bdea-ab54cd00fae7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "\n",
    "import os\n",
    "import sys\n",
    "import argparse\n",
    "import json\n",
    "import csv\n",
    "import io\n",
    "\n",
    "# importing existing files\n",
    "from manufacturelog import validate_and_extract_log\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ceb3167-7154-445d-a8ac-c6d1ad168bae",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Creates an ArgumentParser object named 'parser'\n",
    "parser = argparse.ArgumentParser(\n",
    "    description=\"Parse manufacturing logs into structured batches\"\n",
    ")                   \n",
    "\n",
    "# Declaring a required positional arugment ('input')\n",
    "parser.add_argument(\n",
    "    \"input\",\n",
    "    help=\"Path to log file or raw log string\"\n",
    ")                            \n",
    "\n",
    "# Declaring an optional -o/--output flag with limited valid values and a default.\n",
    "parser.add_argument(\n",
    "    \"-o\", \"--output\",\n",
    "    choices=[\"json\", \"csv\"],\n",
    "    default=\"json\",\n",
    "    help=\"Format of the output (default: json)\"\n",
    ")\n",
    "\n",
    "# defining an optional argument that lets user decide where to save the results.\n",
    "parser.add_argument(\n",
    "    \"-f\", \"--outfile\",\n",
    "    help=\"Filename to write results to (defaults to stdout)\"\n",
    ")\n",
    "\n",
    "# Parse the command-line arguments and store them in the `args` namespace\n",
    "args = parser.parse_args()\n",
    "\n",
    "\n",
    "# Determine whether args.input refers to a file on disk\n",
    "if os.path.isfile(args.input):\n",
    "    \n",
    "    # if it's a file path, it opens and read contents\n",
    "    with open(args.input, 'r') as fh:\n",
    "        log_string = fh.read().strip()\n",
    "        \n",
    "    # if it's not a file path, so assume it's raw log text\n",
    "else:\n",
    "    log_string = args.input\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0475edac-2772-4288-af70-9dd528ee3c77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# At this point, `result` is a list of dicts, e.g.:\n",
    "# [{'Batch ID':'1234','Product Code':'AB','Quantity':50,'Date':'20230908'}, ...]\n",
    "\n",
    "# 1) Handle invalid cases\n",
    "if result == \"invalid\":\n",
    "    sys.exit(\"Error: the provided log string is invalid.\")\n",
    "\n",
    "# 2) Serialize to the chosen format\n",
    "if args.output == \"json\":\n",
    "    # Convert Python list-of-dicts into a pretty-printed JSON string\n",
    "    serialized = json.dumps(result, indent=2)\n",
    "else:\n",
    "    # Build a CSV in memory\n",
    "    # 2a) Use the keys of the first dict as column headings\n",
    "    keys = result[0].keys()  \n",
    "    # 2b) Create a StringIO buffer to hold CSV text\n",
    "    buffer = io.StringIO()  \n",
    "    # 2c) Create a DictWriter, telling it the column order\n",
    "    writer = csv.DictWriter(buffer, fieldnames=keys)\n",
    "    writer.writeheader()         # write \"Batch ID,Product Code,Quantity,Date\"\n",
    "    writer.writerows(result)     # write each batch as one CSV row\n",
    "    serialized = buffer.getvalue()  # extract the full CSV text\n",
    "\n",
    "\n",
    "# 3) Output\n",
    "if args.outfile:\n",
    "    # If user passed “-f filename”, write the serialized text into that file\n",
    "    with open(args.outfile, 'w') as out_fh:\n",
    "        out_fh.write(serialized)\n",
    "else:\n",
    "    # Otherwise, send the serialized text to standard output (the console)\n",
    "    print(serialized)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c29c4da2-b817-4ae9-b641-d5e2c9bf11ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'Batch ID': '1323', 'Product Code': 'BD', 'Quantity': 1234, 'Date': '20210919'}]\n",
      "[\n",
      "  {\n",
      "    \"Batch ID\": \"1234\",\n",
      "    \"Product Code\": \"AB\",\n",
      "    \"Quantity\": 50,\n",
      "    \"Date\": \"20230908\"\n",
      "  }\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "!python logcli.py \"B1234PABQ50D20230908\"  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "81e31808-cb3b-4af1-bc5a-767db0c81637",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'Batch ID': '1323', 'Product Code': 'BD', 'Quantity': 1234, 'Date': '20210919'}]\n",
      "Batch ID,Product Code,Quantity,Date\n",
      "\n",
      "1234,AB,50,20230908\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!python logcli.py \"B1234PABQ50D20230908\" -o csv  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5ea289c0-0c5f-4cd8-abac-98cca5679be3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing sample_log.txt\n"
     ]
    }
   ],
   "source": [
    "%%writefile sample_log.txt\n",
    "B1323PBDQ1234D20210919\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a55996fc-4d6c-4d55-a746-d6f32c7bc531",
   "metadata": {},
   "outputs": [],
   "source": [
    "!python logcli.py sample_log.txt -f out.json\n",
    "\n",
    "!type out.json   \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "049b67ab-f643-4579-a1b1-8211bd220180",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'Batch ID': '1323', 'Product Code': 'BD', 'Quantity': 1234, 'Date': '20210919'}]\n",
      "Batch ID,Product Code,Quantity,Date\n",
      "\n",
      "1323,BD,1234,20210919\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!python logcli.py sample_log.txt -o csv -f out.csv\n",
    "!type out.csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41dd1d5e-191c-459f-93bb-b1bb550ecf42",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
