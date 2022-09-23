import csv

def fix_csv():
    resolved_triage = []
    with open("C:\\Users\\HP\\Desktop\\New folder\\a.csv", "r", encoding='utf-8') as csv_f, open("C:\\Users\\HP\\Desktop\\New folder\\a_fixed.csv",'w', encoding='utf-8') as to_csv:
        csv_reader = csv.reader(csv_f, delimiter="\t")
        csv_writer = csv.writer(to_csv, delimiter=',')
        for row in csv_reader:
            csv_writer.writerow(row)
fix_csv()