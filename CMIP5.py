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

st.sidebar.title('CMIP5 ETH files')

st.sidebar.markdown('**How many files are available from ETH? Which variables? At which temporal resolutions? From how many models? I hope this app makes our lives a bit easier when working with CMIP5 files!**')
#tabletype = st.sidebar.radio('', ['Search CMIP6 variables', 'Filter CMIP6 variables', 'Delivered variables', 'Interactive plots'])


#dictdel = pd.read_csv('streamlit_CMIP5_short.csv')
#@st.cache(allow_output_mutation=True, max_entries=10, ttl=30)
#def load_data():
#	return dictdel

#dict1 = pd.read_excel('CMIP6_MIP_tables.xlsx', sheet_name = None)

@st.cache
def load_data():
    dictdel = pd.read_csv('streamlit_CMIP5_short.csv')
    return dictdel

data = load_data()
	

exp = st.multiselect('Experiment', data['experiment'].unique())
f_data = data[(data['experiment'].isin(exp))]
tem = st.multiselect('Temporal resolution', f_data['temp_res'].unique())
f_data2 = f_data[(f_data['temp_res'].isin(tem))]
var = st.multiselect('Variable', f_data2['variable'].unique())
f_data3 = f_data2[(f_data2['variable'].isin(var))]


if len(f_data3)>0:
	st.write(f_data3)
	st.write(str(len(f_data3)) + " files with " + str(len(f_data3["model"].unique())) + " models")
	##########################
	csv = f_data3.to_csv(index=False)
	b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
	href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
	st.markdown("## Download the table:")
	st.markdown(href, unsafe_allow_html=True)	
	###########################
elif len(f_data2)>0:
	st.write(f_data2)
	st.write(str(len(f_data2)) + " files with " + str(len(f_data2["variable"].unique())) + " variables from " + str(len(f_data2["model"].unique())) + " models")
	##########################
	#csv = f_data2.to_csv(index=False)
	#b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
	#href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
	#st.markdown("## Download the table:")
	#st.markdown(href, unsafe_allow_html=True)	
	###########################
elif len(f_data)>0:
	st.write(f_data)
	st.write(str(len(f_data)) + " files with " + str(len(f_data["variable"].unique())) + " variables from " + str(len(f_data["model"].unique())) + " models")
	##########################
	#csv = f_data.to_csv(index=False)
	#b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
	#href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
	#st.markdown("## Download the table:")
	#st.markdown(href, unsafe_allow_html=True)	
	###########################
else:
	st.write(data)
	st.write(str(len(data)) + " files with " + str(len(data["variable"].unique())) + " variables from " + str(len(data["model"].unique())) + " models")






