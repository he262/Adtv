import csv
import numpy as np
import pandas as pd
from pathlib import Path
from pytictoc import  TicToc
from urllib.parse import urlencode
from pandas import concat, read_csv
from behave import given, when, then
from pandas.testing import assert_series_equal
from pandas.testing import assert_frame_equal
import requests
import datetime
import time


from logging import basicConfig, DEBUG, info, debug
basicConfig(level=DEBUG, format="%(levelname)s %(asctime)s : %(message)s")


@given(u'the api url is {base_url}')
def step_impl(context,base_url:str):
    context.base_url = base_url

@given(u'I append the following parameters')
def step_impl(context):
    params = {}
    for row in context.table:
        params[row['param_name']] = row['param_value']
        context.url_with_params= f"{context.base_url}?{urlencode(params)}"
        
@when(u'I make an api request')
def step_impl(context):
    t = TicToc()
    t.tic()
    # start=datetime.datetime.now()
    response= requests.get(context.url_with_params,verify=False)
    # end=datetime.datetime.now()
    t.toc()
    # print("Response Time: ",end-start)
    print("NEW Elapsed Response Time: ",response.elapsed.total_seconds())
    context.api_response = response.content

@then(u'save api response in {CSV_File}')
def step_impl(context,CSV_File:str):
    # download_path= 'Kaushal.csv'
    download_path= CSV_File
    with open(Path(download_path),'wb') as csv_file:
        csv_file.write(context.api_response)
        context.download_path = download_path
        print(context.download_path)

@when(u'pivot api data at {CSV_File} and {after_pivot_data}')
def step_impl(context,CSV_File:str,after_pivot_data:str):
    api_df = pd.read_csv(CSV_File,na_filter=False,sep=';')
    df =api_df
    df = df.pivot(index=['stoxx_id','name','isin','sedol','ric','date'],columns="attribute",values="value")
    df.reset_index(inplace=True)
    df.columns = [''.join(col).strip() for col in df.columns.values]
    df.to_csv(Path(after_pivot_data),index=False)
