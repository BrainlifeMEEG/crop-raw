"""
Crop raw MEG/EEG data to a specified time window.

This app loads raw neuroimaging data and crops it to a time window
defined by tmin and tmax parameters. It produces a report comparing
the original and cropped data duration.

Inputs
------
mne : str
    Path to the input MNE-format MEG/EEG data file (MNE .fif format).

Outputs
-------
meg.fif : str
    Cropped MEG/EEG data file in MNE format.
report_crop.html : str
    Interactive HTML report showing original and cropped data information.
"""

# Copyright (c) 2026 brainlife.io
#
# Crop raw MEG/EEG data to a specified time window.
#
# Authors:
# - Maximilien Chaumon (https://github.com/dnacombo)

import sys
import os
import mne
import matplotlib.pyplot as plt

# Add brainlife_utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    create_product_json,
    add_info_to_product,
    add_raw_info_to_product,
    ensure_output_dirs
)

# Setup environment
setup_matplotlib_backend()
config = load_config()

ensure_output_dirs('out_dir')

# == LOAD DATA ==
fname = config['mne']
raw = mne.io.read_raw_fif(fname, preload=True)
raw_orig = raw.copy()

tmin = config['tmin']
tmax = config['tmax']

# == CROP DATA ==
raw.crop(tmin=tmin, tmax=tmax)

# == SAVE CROPPED DATA ==
raw.save('out_dir/meg.fif', overwrite=True)

# == CREATE PRODUCT.JSON ==
product_items = []

orig_duration = raw_orig.times[-1] - raw_orig.times[0]
crop_duration = raw.times[-1] - raw.times[0]

tmin_str = str(tmin) if tmin is not None else "start"
tmax_str = str(tmax) if tmax is not None else "end"
add_info_to_product(product_items, f"Cropped to: {tmin_str} - {tmax_str} s", 'success')
add_info_to_product(product_items, f"Original duration: {orig_duration:.3f} s")
add_info_to_product(product_items, f"Cropped duration: {crop_duration:.3f} s")

add_info_to_product(product_items, "Original Data:")
add_raw_info_to_product(product_items, raw_orig)

add_info_to_product(product_items, "Cropped Data:")
add_raw_info_to_product(product_items, raw)

create_product_json(product_items)
