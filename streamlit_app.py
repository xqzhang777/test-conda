import streamlit as st
import torch
import iotbx.ccp4_map

"Hello from conda"

def test_hmmer():
    import subprocess
    subprocess.call('hmmsearch', shell=True)

test_hmmer()

b = st.button("Click me")

if b:
  st.balloons()

