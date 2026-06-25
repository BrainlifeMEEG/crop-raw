# Crop Raw MEG/EEG Data

## Description

This Brainlife.io application crops raw MEG/EEG data to a specified time window. It takes a raw MNE-format data file and trims it to the interval `[tmin, tmax]` using MNE-Python's `raw.crop()` function.

The app generates:
- Cropped data in MNE-Python format
- Comprehensive HTML report comparing original and cropped data

## Inputs

### Input Files

- **meg.fif**: MNE-format MEG/EEG data file (required)

## Outputs

### Output Files

- **meg.fif**: Cropped MEG/EEG data file in MNE format
- **report_crop.html**: Interactive HTML report showing original and cropped data with power spectral density

## Configuration Parameters

- **tmin** (float | null): Start time in seconds for cropping. Set to `null` to keep from the beginning of the recording.
- **tmax** (float | null): End time in seconds for cropping. Set to `null` to keep until the end of the recording.

## Usage

### Running on Brainlife.io

1. Upload your MEG/EEG data file in MNE format (.fif)
2. Select the crop-raw app
3. Configure the time window:
   - Set `tmin` to the desired start time in seconds (or leave `null` for start of recording)
   - Set `tmax` to the desired end time in seconds (or leave `null` for end of recording)
4. Submit the task
5. Monitor task completion and review outputs in the report viewer

### Local Testing

```bash
# Update config.json with your data path and desired tmin/tmax
# Then run:
python main.py
```

## Technical Details

### Cropping Implementation

- Uses MNE-Python's `raw.crop(tmin, tmax)` method
- `tmin=null` defaults to the start of the recording (t=0)
- `tmax=null` defaults to the end of the recording
- Times are specified in seconds relative to the recording start
- The crop is applied in-place after loading (data is preloaded for efficiency)

### Report Generation

Uses MNE-Python's Report class to create an interactive HTML report with:
- Original data summary and PSD
- Cropped data summary and PSD

## Authors

- Maximilien Chaumon (https://github.com/dnacombo)

## Citations

Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2

## Funding Acknowledgement

brainlife.io is publicly funded. We kindly ask that you acknowledge the funding below in your code and publications.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
