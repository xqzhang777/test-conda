import sys
import os
import shutil
from pathlib import Path

"Hello from conda"

if Path("/home/appuser").exists():
    # essential to avoid cctbx import errors
    target = Path("/home/appuser/venv/share/cctbx")
    if not target.exists():
        target.symlink_to("/home/appuser/.conda/share/cctbx")

    sys.path += ["/home/appuser/venv/lib/python3.9/lib-dynload"]
    os.environ["PATH"] += os.pathsep + "/home/appuser/.conda/bin"


import streamlit as st
import torch
import iotbx.ccp4_map
    
    

b = st.button("Click me")

if b:
  st.balloons()

