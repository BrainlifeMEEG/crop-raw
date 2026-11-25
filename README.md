<h1 align="center">Crop raw data</h1>

<p align="center">
  Crops continuous MEG/EEG data (MNE raw FIF) to a time window between tmin and tmax seconds with MNE-Python raw.crop.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.940"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.940-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Crops continuous MEG/EEG data (MNE raw FIF) to a time window between tmin and tmax seconds with MNE-Python raw.crop.**

Loads the raw recording and keeps only the interval [tmin, tmax] (from the start or to the end when either is empty), saving raw.fif. Use it to drop unwanted parts of a recording, such as the period before the task starts, before further processing.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/raw` |
| **Outputs** | `neuro/meeg/mne/raw` |
| **Container** | `brainlifemeeg/mne:1.12.1` |
| **Resources** | 4 CPUs · 20 GB memory |
| **Run it** | [doi.org/10.25663/brainlife.app.940](https://doi.org/10.25663/brainlife.app.940) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `raw` | `neuro/meeg/mne/raw` | yes | Continuous MEG/EEG recording (MNE raw FIF). |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/raw` | Cropped data |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `tmin` | number |  | Start time of the raw data to use in seconds (must be >= 0). |
| `tmax` | number |  | End time of the raw data to use in seconds (cannot exceed data duration). If None (default), the current end of the data is used. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.940](https://doi.org/10.25663/brainlife.app.940), choose `neuro/meeg/mne/raw` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/raw`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlifemeeg/mne:1.12.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "mne": "/path/to/raw/mne",
       "tmin": "<number>",
       "tmax": "<number>"
   }
   ```

3. Run `./main`.

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `tmin` | float \| null | `null` | Start time in seconds for cropping (must be >= 0). If `null`, the data are kept from the beginning of the recording. |
| `tmax` | float \| null | `null` | End time in seconds for cropping (cannot exceed data duration). If `null`, the data are kept until the end of the recording. |

## Local Testing

```bash
# Update config.json with your data path and desired tmin/tmax
# Then run:
python main.py
```

## Cropping Implementation

- Uses MNE-Python's `raw.crop(tmin, tmax)` method
- `tmin=null` defaults to the start of the recording (t=0)
- `tmax=null` defaults to the end of the recording
- Times are specified in seconds relative to the recording start
- The crop is applied in-place after loading (data is preloaded for efficiency)

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Crop raw data. brainlife.io App. [doi:10.25663/brainlife.app.940](https://doi.org/10.25663/brainlife.app.940)
- Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Maximilien Chaumon (https://github.com/dnacombo)

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
