import csv
import sys
from model import PricingEngine


file = sys.argv[1]

# Run script by typing "python run.py data.csv" into your terminal, where data.csv is your data file
# Opens up data file, sets headers, and puts each line item through pricing model
with open(file, 'rb') as f:
    reader = csv.reader(f)
    headers = []
    for i, row in enumerate(reader):
        if i == 0:
            headers = [header.replace(' ', '_').lower() for header in row]
        else:
            line_item = {}
            for j in range(len(headers)):
                line_item[headers[j]] = row[j]
            PricingEngine(**line_item).print_cost()
