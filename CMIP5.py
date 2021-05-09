import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import numpy as np
import hvplot.xarray
import hvplot
import holoviews as hv
import holoviews.plotting.mpl
import base64


st.set_page_config(
     #page_title="CMIP6 climate variables",
     #layout="wide",
     initial_sidebar_state="expanded",
      )


dictdel = pd.read_csv('CMIP5_files_short.csv')
@st.cache
def load_data():
	df = pd.concat(dictdel.values(), ignore_index=True)
	return df
data = load_data()
st.write(data)
	
	##########################
csv = data.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
st.markdown("## Download the table:")
st.markdown(href, unsafe_allow_html=True)	
	###########################
	
