#!/usr/bin/env python

from mozscape import Mozscape
import argparse
import csv
import sys
import pandas as pd

client = Mozscape(
    'my-access-id',
    'my-secret-key')

# The links API has more columns to specify, as well as sort, scope, etc.
links = client.links(
    'ENTER URL', scope='page_to_page', sort='page_authority',
    filters=['internal'], targetCols=Mozscape.UMCols.url)
	

## PUT ABOVE INTO A PANDAS DATAFRAME ##
#df = pd.DataFrame(authorities.items())
df = pd.DataFrame(links)
df = df.rename(columns={
	'upa': 'Page Authority', 
	'uu': 'URL'})

print(df)
df.to_excel('mozLinks.xls', index=False)
# use xlsx to stop limiting of row export - check csv module


anchorTermResults = client.anchorText(
		'ENTER_URL',
		 cols=Mozscape.ATCols.freeCols2)

df2 = pd.DataFrame(anchorTermResults)
df2 = df2.rename(columns={
	'apuemp': 'External Mozrank passed', 
	'apuimp': 'Internal Mozrank Passed', 
	'apuiu': 'Internal Pages Linking', 
	'aput': 'Term'})
print(df2)

df2.to_excel('anchors.xls', index=False)
# print(df)


"""
default metrics when doing print(mozMetrics)

uu == canonical form of URL
ut == meta title
us == http status code
upa == page authority
ueid == equity of external links?
ulc == time last crawled returned in epoch format (epochconverter.com/)
umrp == 10 point score of Mozrank
umrr == Mozrank raw score
fmrp == subdomain mozRank 10 point score
fmrr == above raw score
pda == domain authority

"""

