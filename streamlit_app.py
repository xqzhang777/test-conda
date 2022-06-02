import streamlit as st
import torch
#import cctbx

"Hello from conda"

def test_hmmer():
    import subprocess
    subprocess.call('hmmsearch', shell=True)

test_hmmer()

b = st.button("Click me")

if b:
  st.balloons()

