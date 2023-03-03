import streamlit as st
import pandas as pd


@st.cache
def load_data(fp: str) -> pd.DataFrame:
    return pd.read_csv(fp)

