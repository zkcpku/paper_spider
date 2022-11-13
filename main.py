import requests
import re

import pandas as pd

name = 'pldi'

years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
URL_DICT = {
                'icse': "https://dblp.org/db/conf/icse/icse{year}.html", 
                "ase": "https://dblp.org/db/conf/kbse/ase{year}.html", 
                "fse": "https://dblp.org/db/conf/sigsoft/fse{year}.html", 
                "saner": "https://dblp.org/db/conf/wcre/saner{year}.html",
                "icsme": "https://dblp.org/db/conf/icsm/icsme{year}.html",
                "icpc": "https://dblp.org/db/conf/iwpc/icpc{year}.html",
                "esem": "https://dblp.org/db/conf/esem/esem{year}.html",

                "pldi": "https://dblp.org/db/conf/pldi/pldi{year}.html",

                "nips": "https://dblp.org/db/conf/nips/neurips{year}.html",
                "icml": "https://dblp.org/db/conf/icml/icml{year}.html",
                "iclr": "https://dblp.org/db/conf/iclr/iclr{year}.html",
                "aaai": "https://dblp.org/db/conf/aaai/aaai{year}.html",
                "ijcai": "https://dblp.org/db/conf/ijcai/ijcai{year}.html",
                "kdd": "https://dblp.org/db/conf/kdd/kdd{year}.html",
                "www": "https://dblp.org/db/conf/www/www{year}.html",

                "acl": "https://dblp.org/db/conf/acl/acl{year}-1.html",
                "acl1": "https://dblp.org/db/conf/acl/acl{year}.html",
                "emnlp": "https://dblp.org/db/conf/emnlp/emnlp{year}-1.html",
                "emnlp1": "https://dblp.org/db/conf/emnlp/emnlp{year}.html",
                "naacl": "https://dblp.org/db/conf/naacl/naacl{year}.html"

            }

pd_dict = {"name": [], "year": [], "title": [], "link": []}

for year in years:
    url = URL_DICT[name].format(year=year)
    print(url)
    content = requests.get(url).content
    paper_names = re.findall(r'<span class="title" itemprop="name">(.+?)</span>', content.decode('utf-8'))
    for paper_name in paper_names:
        pd_dict["name"].append(name)
        pd_dict["year"].append(year)
        pd_dict["title"].append(paper_name)
        pd_dict["link"].append(url)

df = pd.DataFrame(pd_dict)
df.to_csv(f"{name}.csv", index=False)


