import pandas as pd
import re
import os
import sys




keywords = ['code gen', 'synthesis', "program gen", "generate program"]

def filter_paper(paper_pd, keyword):
    paper_pd = paper_pd[paper_pd['title'].str.contains(keyword, case=False)]
    return paper_pd

if __name__ == '__main__':
    for keyword in keywords:
        paper_pd = pd.read_csv('all.csv')
        paper_pd = filter_paper(paper_pd, keyword)
        paper_pd.to_csv("filter/" + keyword + '.csv', index=False)

