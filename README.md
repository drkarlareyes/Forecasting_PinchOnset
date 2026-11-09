# Forecasting finger force and pinch onsets from forearm HD-sEMG

Muscle electrical activity starts before the force it produces. This repository tests how far that lead can be used: can a model predict finger force tens of milliseconds ahead with information that goes beyond simply repeating the last value, and how do early pinch detection and false pinches trade off?

I approach the problem as an evaluation framework of eight tests (T1 to T8). The analyses here run five of them on public HD-sEMG data. Each figure takes one test and checks whether its result would change a modelling decision. These are exploratory analyses with one participant per dataset: they show what each test can reveal, not general performance.

## Key results

| Figure | Test | Question | Result on public data |
|---|---|---|---|
| [1](Tests/Figure1.md) | T1 | Does EMG lead force, and by how much? | With causal processing, EMG crossed the rest threshold 22 and 41 ms before force (two trials). A real-time detector with 10 ms confirmation fired 13 and 32 ms before force; with 50 ms confirmation, after force had started. |
| [2](Tests/Figure2.md) | T2 | Does a forecast beat persistence, and when? | Against repeating its own last estimate (the deployable baseline), the EMG forecast was at most 2.6 points of a typical press better, and during force rise the 95% interval included zero at every horizon. Repeating the measured force, which needs a force sensor, won at 30 ms in every phase and up to 150 ms during holds. |
| [3](Tests/Figure3.md) | T5 | Which calibration data identify the model? | Steady force left the EMG-to-force delay poorly identified (fit changed by 0.035 R² across 0 to 150 ms); changing force constrained it (0.16 to 0.25). A mixed calibration predicted best or as well (R² 0.70 and 0.78). |
| [4](Tests/Figure4.md) | T4 | Can the task schedule alone look like anticipation? | Time since trial start alone predicted cued muscle activity with R² 0.77 to 0.91, and self-paced activity not at all (−0.03 and −0.18). |
| [5](Tests/Figure5.md) | T7, T8 | Where do false pinches come from? | A pinch detector calibrated on pinch and rest flagged rest 0.4% of the time but hand closing 99% and wrist extension 79%. On another day, after the electrodes were re-applied, it detected 0 of 10 pinches. |

Each linked page explains the figure, the method and its limits.

## Approach

- **Causal processing.** At time *t* a model only sees EMG up to *t*, and the onset timing uses the same causal processing. Normalisation, components, weights and thresholds come from calibration data only.
- **Calibrate on one recording, test on another,** in both directions.
- **Four baselines** for every forecast: the model's own last estimate (deployable persistence), the last measured force (offline reference), trend extrapolation, and a reduced physiological model.
- **Reduced physiological model.** Activation follows a neural drive estimate *u* as da/dt = (u − a)/τ, with separate time constants for rise and relaxation, and force is F(t + d) = b + k·aᵖ with an electromechanical delay *d*.
- **Results split by phase** (force rising, steady, falling), because good performance during holds can hide poor anticipation.

## Leakage checklist

| Step | Fitted on | Uses samples after *t*? |
|---|---|---|
| sEMG features and activity (band-pass, RMS) | none | No: causal filter and trailing window, confirmed by a look-ahead test in `hyser.ipynb` |
| Electrode exclusion | each trial separately | No labels used; both trials flagged the same five electrodes |
| z-score, PCA, ridge weights and penalty | calibration recording | Penalty chosen by blocked cross-validation with a gap |
| Trend damping, physiological model | calibration recording | No |
| Phase labels (rising, steady, falling) | measured force of the test recording | Yes, but only to split the evaluation, never as model input |
| Error scale | test recording | Same divisor for every model |
| Baseline 2 (measured force) | none | No, but it needs a force sensor |

## The eight tests

| Test | Question |
|---|---|
| T1 | Does sEMG contain information before force changes? |
| T2 | Does a forecast beat persistence and trend at the same horizon? |
| T3 | Does recent sEMG carry the useful information (older-EMG ablation)? |
| T4 | Is the forecast exploiting the task schedule instead of sEMG (cue-only control)? |
| T5 | Do holds, ramps or mixed calibrations personalise the model best? |
| T6 | Do physiological constraints or learned representations improve on simpler models? |
| T7 | How early can pinches be detected before false pinches become unacceptable? |
| T8 | Do the results survive new sessions, electrode shifts, wrist movement and real processing delays? |

## Repository

| Path | Content |
|---|---|
| `hyser.ipynb` | Hyser analyses: Figures 1, 2 and 3 |
| `cemhsey.ipynb` | CEMHSEY analyses (with a Hyser comparison): Figures 4 and 5 |
| `Tests/` | One page per figure with its explanation |
| `figures/` | Figure images |
| `results/` | Numbers behind the figures (JSON) |
| `Limitations.md` | What these analyses cannot show |

## How to run

1. Download the data (not included here, see below) into a `data/` folder.
2. `pip install -r requirements.txt`
3. Set `HYSER_DIR` and `CEM_DIR` in the first cell of each notebook (or as environment variables), then run all cells from the repository folder. `hyser.ipynb` takes about a minute; `cemhsey.ipynb` takes a few minutes the first time while it extracts features from the CEMHSEY files.

## Data

**Hyser** (PhysioNet `hd-semg` 2.0.0). Forearm HD-sEMG from 20 participants, 256 electrodes in four 8 × 8 grids over the extensor and flexor muscles (2048 Hz), with the force of the five fingers (100 Hz). Used here: subject 1, session 1, random task, trials 1 and 2 (self-paced finger presses).

- Jiang X, Dai C, Liu X, Fan J. Open Access Dataset and Toolbox of High-Density Surface Electromyogram Recordings (version 2.0.0). PhysioNet (2023). https://doi.org/10.13026/hxan-pe94
- Jiang X, et al. Open access dataset, toolbox and benchmark processing results of high-density surface electromyogram recordings. *IEEE Transactions on Neural Systems and Rehabilitation Engineering* 29, 1035–1046 (2021). https://doi.org/10.1109/TNSRE.2021.3082551
- Licence: Open Data Commons Attribution License v1.0.

**CEMHSEY** (ConsecutivE Multi-day High-density Surface ElectromyographY). 320-channel forearm HD-sEMG (five 8 × 8 grids, 2048 Hz) over 11 consecutive days, with electrodes re-applied each day. Used here: GESTURE sub-dataset (11 cued hand and wrist gestures, no force), subject 1, days 1 and 2, five trials per day.

- Yang S, Li D, Chen C, Zhu X. Dataset: CEMHSEY, Part II. Zenodo (2025). https://doi.org/10.5281/zenodo.14272463
- Yang S, Chen C, Li D, Zhu X. A consecutive multi-day high-density surface electromyography dataset comprising 7 grasps and 11 gestures. *Scientific Data* 12, 1420 (2025). https://doi.org/10.1038/s41597-025-05733-y

## Author

Karla Miriam Reyes Leiva, PhD. Biomedical engineer working on physiological signal processing, wearable and radar sensing, and machine learning. ORCID [0000-0002-3269-0830](https://orcid.org/0000-0002-3269-0830)

Code: MIT licence. The datasets belong to their authors; please cite them if you use them.
