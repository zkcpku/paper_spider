import requests
import re

import pandas as pd

name = 'pacmpl'

volumes = {
    "tse": [42, 43, 44, 45, 46, 47, 48],
    "tosem": [25, 26, 27, 28, 29, 30, 31],
    "pacmpl": [1, 2, 3, 4, 5, 6]
}
URL_DICT = {
                "tse": "https://dblp.org/db/journals/tse/tse{year}.html",
                "tosem": "https://dblp.org/db/journals/tosem/tosem{year}.html",

                "pacmpl": "https://dblp.org/db/journals/pacmpl/pacmpl{year}.html"
            }

# pacmpl包含oopsla

pd_dict = {"name": [], "year": [], "title": [], "link": []}

for year in volumes[name]:
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


