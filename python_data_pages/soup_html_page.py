
import os
from bs4 import BeautifulSoup

dir="F:\\Data\\officeallay_Encounters_sep_17_22"
class soup_html_page_class:
    def html_page(directory_path):
        subfolders = [f.path for f in os.scandir(directory_path) if f.is_dir()]
        for direc in subfolders:
            a = direc.split('\\')
            pid = a[len(a) - 1]
            file_ = direc + '\\index.htm'
            # for filename in os.listdir(directory):
            #     f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(file_):
                soup = BeautifulSoup(open(file_, encoding="utf8"), "html.parser")
                tables = soup.findAll("table", {"id": "encounters"})
                # rows = tables[1].findChildren(['tr']) #for documents read
                rows = tables[0].findChildren(['tr']) #for encounters read
                i = 0
                for row in rows:
                    cells = row.findChildren('td')
                    d = ""
                    for cell in cells:
                        if cell == '<td>' or "\n" in cell:
                            if cell.text.find(".pdf") == -1:
                                continue
                        value = cell.text
                        # p=("The value in this cell is %s" % value.replace('< td>', '').replace("\n", '').replace('< tr>', ''))
                        p = (value.replace('< tr>', ''))
                        d = d + p + "|"
                    print(d)
                    if i != 0:
                        file_object = open('C:\\Users\\HP\\Desktop\\New folder\\a.csv', 'a')
                        file_object.write(pid + '|' + d + '\n')
                    i = i + 1
soup_html_page_class.html_page(directory_path=dir)