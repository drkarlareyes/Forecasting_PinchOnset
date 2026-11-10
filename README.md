# Forecasting finger force and pinch onsets from forearm HD-sEMG

Muscle electrical activity starts before the force it produces. This repository tests how far that lead can be used: can a model predict finger force tens of milliseconds ahead with information that goes beyond simply repeating the last value, and how do early pinch detection and false pinches trade off?

I approach the problem as an evaluation framework of eight tests (T1 to T8), run on public sEMG data in three stages. Each figure takes one test and checks whether its result would change a modelling decision.

1. **Pilot, one participant per dataset** (Figures 1 to 5): five of the tests on Hyser and CEMHSEY, to see what each test can reveal.
2. **Hyser, all 20 participants** (Figures 6 to 8): the timing and forecast tests repeated on everyone, plus a day-to-day test with the electrodes placed again.
3. **putEMG-Force, all 44 participants** (Figures 9 to 12): the same tests on a second dataset recorded in another lab, plus a press detector scored on about 90 presses from rest per person.

## Key results

### Stage 1 · Pilot, one participant per dataset

| Figure | Test | Question | Result on public data |
|---|---|---|---|
| [1](Tests/Figure1.md) | T1 | Does EMG lead force, and by how much? | With causal processing, EMG crossed the rest threshold 22 and 41 ms before force (two trials). A real-time detector with 10 ms confirmation fired 13 and 32 ms before force; with 50 ms confirmation, after force had started. |
| [2](Tests/Figure2.md) | T2 | Does a forecast beat persistence, and when? | Against repeating its own last estimate (the deployable baseline), the EMG forecast was at most 2.6 points of a typical press better, and during force rise the 95% interval included zero at every horizon. Repeating the measured force, which needs a force sensor, won at 30 ms in every phase and up to 150 ms during holds. |
| [3](Tests/Figure3.md) | T5 | Which calibration data identify the model? | Steady force left the EMG-to-force delay poorly identified (fit changed by 0.035 R² across 0 to 150 ms); changing force constrained it (0.16 to 0.25). A mixed calibration predicted best or as well (R² 0.70 and 0.78). |
| [4](Tests/Figure4.md) | T4 | Can the task schedule alone look like anticipation? | Time since trial start alone predicted cued muscle activity with R² 0.77 to 0.91, and self-paced activity not at all (−0.03 and −0.18). |
| [5](Tests/Figure5.md) | T7, T8 | Where do false pinches come from? | A pinch detector calibrated on pinch and rest flagged rest 0.4% of the time but hand closing 99% and wrist extension 79%. On another day, after the electrodes were re-applied, it detected 0 of 10 pinches. |

### Stage 2 · Hyser, all 20 participants

| Figure | Test | Question | Result on public data |
|---|---|---|---|
| [6](Tests/Figure6.md) | T1 | How far ahead does sEMG carry information about force? | In all 19 participants with an active middle finger, the causal sEMG features predicted force best some time ahead rather than now: median 130 ms (IQR 105 to 195 ms; 70 ms for the pilot participant). R² on the other trial rose from 0.18 at 0 ms to 0.36 at each person's best delay (medians). |
| [7](Tests/Figure7.md) | T2 | Does the forecast beat persistence across people? | Against repeating its own estimate, the forecast's median gain during force rise was 1.4 points of a typical press at 100 ms and 3.3 to 3.7 points at 150 to 200 ms (Wilcoxon p ≤ 0.001), clear within 10 of 19 people at 150 to 200 ms. Repeating the measured force still won up to 100 ms in every phase and at all horizons during holds. |
| [8](Tests/Figure8.md) | T8, T5 | Does a calibration survive to the next day? | No. A day-1 model fell from a median R² of 0.39 (same-day calibration) to −0.07 on day 2. Rescaling the sEMG on day 2 without force reached only 0.11. Adding 10 to 20 s of day-2 data with force to the day-1 data recovered 0.32 to 0.35; day-2 data alone needed 20 s to match. |

### Stage 3 · putEMG-Force, all 44 participants

| Figure | Test | Question | Result on public data |
|---|---|---|---|
| [9](Tests/Figure9.md) | T1 | Does the delay of best prediction replicate? | Yes: median 100 ms (IQR 90 to 140 ms), positive in all 44 participants (Hyser: 130 ms). Here looking ahead raised R² only from 0.40 to 0.41 (medians), against 0.18 to 0.36 in Hyser. |
| [10](Tests/Figure10.md) | T1, T7, T8 | Can a detector see a press before force starts? | Rarely. At 5 SD and 25 ms, a rest-referenced sEMG detector caught 30% of presses with 0.44 false alarms per minute, a median of 540 ms after force onset, and none before it. The most sensitive setting caught 82% but raised 15 false alarms per minute (random firing would catch 52%), and 13% before force onset. Ring and little finger presses were caught most often (62%), thumb presses least (8%). The next session gave similar numbers. |
| [11](Tests/Figure11.md) | T2 | Does the forecast beat persistence in a second dataset? | In the same direction as Hyser, but smaller: during force rise the median gain over repeating its own estimate was 0.4 points of a typical press at 100 ms (clear in 37 of 44 participants) and 0.6 at 200 ms. During release the forecast was worse up to 100 ms. |
| [12](Tests/Figure12.md) | T8, T5 | Does a calibration survive to the next session? | No. R² fell from 0.46 (same-session calibration) to −0.75. Unlike Hyser, keeping the session-1 data hurt: new-session data alone reached 0.20 with 20 s and 0.36 with 120 s; session 1 plus the same new data reached −0.12 and 0.15. |

Each linked page explains the figure, the method and its limits.

## Approach

- **Causal processing.** At time *t* a model only sees EMG up to *t*, and the onset timing uses the same causal processing. Normalisation, components, weights and thresholds come from calibration data only.
- **Calibrate on one recording, test on another,** in both directions.
- **Four baselines** for every forecast: the model's own last estimate (deployable persistence), the last measured force (offline reference), trend extrapolation, and a reduced physiological model.
- **Reduced physiological model.** Activation follows a neural drive estimate *u* as da/dt = (u − a)/τ, with separate time constants for rise and relaxation, and force is F(t + d) = b + k·aᵖ with an electromechanical delay *d*.
- **Results split by phase** (force rising, steady, falling), because good performance during holds can hide poor anticipation.
- **Detection scored against force onset,** with false alarms counted at rest and rest levels taken from a calibration recording (stage 3).

## Leakage checklist

| Step | Fitted on | Uses samples after *t*? |
|---|---|---|
| sEMG features and activity (band-pass, RMS) | none | No: causal filter and trailing window, confirmed by a look-ahead test in `hyser.ipynb` and `putemg_force.ipynb` |
| Electrode exclusion | each trial (stage 1) or session 1 (stages 2 and 3) | No labels used |
| z-score, PCA, ridge weights and penalty | calibration recording | Penalty chosen by blocked cross-validation with a gap |
| Trend damping, physiological model | calibration recording | No |
| Phase labels (rising, steady, falling) | measured force of the test recording | Yes, but only to split the evaluation, never as model input |
| Detector rest levels | calibration recording | No |
| Force onsets and rest periods | measured force of the test recording | Yes, but only to score the detector, never as its input |
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
| `hyser.ipynb` | Hyser pilot, one participant: Figures 1, 2 and 3 |
| `hyser_multisubject.ipynb` | Hyser, all 20 participants: Figures 6, 7 and 8 |
| `download_hyser.py` | Downloads the Hyser files used by both notebooks |
| `putemg_force.ipynb` | putEMG-Force, all 44 participants: Figures 9 to 12 |
| `download_putemg_force.py` | Downloads the putEMG-Force recordings |
| `cemhsey.ipynb` | CEMHSEY analyses (with a Hyser comparison): Figures 4 and 5 |
| `Tests/` | One page per figure with its explanation |
| `figures/` | Figure images |
| `results/` | Numbers behind the figures (JSON) |
| `Limitations.md` | What these analyses cannot show |

## How to run

1. Download the data (not included here, see below) into a `data/` folder. For Hyser, `python download_hyser.py` gets the random task of all 20 participants, both sessions (about 2 GB, into `data/hyser/`). For putEMG-Force, `python download_putemg_force.py` gets the force recordings of all 44 participants (about 20 GB, into `data/putemg_force/`).
2. `pip install -r requirements.txt`
3. Set `HYSER_DIR`, `HYSER_RANDOM`, `PUTEMG_FORCE` and `CEM_DIR` in the first cell of each notebook (or as environment variables), then run all cells from the repository folder. `hyser.ipynb` takes about a minute; `hyser_multisubject.ipynb` takes about 15 s per participant the first time and keeps the results of each person in `results/multisubject/`; `putemg_force.ipynb` takes about 25 s per participant the first time and keeps them in `results/putemg/`; `cemhsey.ipynb` takes a few minutes the first time while it extracts features from the CEMHSEY files.

## Data

**Hyser** (PhysioNet `hd-semg` 2.0.0). Forearm HD-sEMG from 20 participants, 256 electrodes in four 8 × 8 grids over the extensor and flexor muscles (2048 Hz), with the force of the five fingers (100 Hz). Used here: random task (self-paced finger presses), trials 1 and 2. Stage 1: subject 1, session 1. Stage 2: subjects 1 to 20, sessions 1 and 2, recorded on separate days.

- Jiang X, Dai C, Liu X, Fan J. Open Access Dataset and Toolbox of High-Density Surface Electromyogram Recordings (version 2.0.0). PhysioNet (2023). https://doi.org/10.13026/hxan-pe94
- Jiang X, et al. Open access dataset, toolbox and benchmark processing results of high-density surface electromyogram recordings. *IEEE Transactions on Neural Systems and Rehabilitation Engineering* 29, 1035–1046 (2021). https://doi.org/10.1109/TNSRE.2021.3082551
- Licence: Open Data Commons Attribution License v1.0.

**putEMG-Force** (Biomedical Engineering group, Poznan University of Technology). 24 monopolar electrodes in three bands of eight around the right forearm (5120 Hz) and the force of each finger on a hand dynamometer (200 Hz), from 44 participants in two sessions at least a week apart, with the bands placed again. Used here: all force recordings (`repeats_long`, `sequential`, `repeats_short`), in which the participant follows a force target with the thumb, the index, the middle, the ring and little fingers together, or all fingers.

- putEMG and putEMG-Force datasets. https://biolab.put.poznan.pl/putemg-dataset/
- Kaczmarek P, Mańkowski T, Tomczyński J. putEMG—A surface electromyography hand gesture recognition dataset. *Sensors* 19, 3548 (2019). https://doi.org/10.3390/s19163548
- Licence: CC BY-NC 4.0.

**CEMHSEY** (ConsecutivE Multi-day High-density Surface ElectromyographY). 320-channel forearm HD-sEMG (five 8 × 8 grids, 2048 Hz) over 11 consecutive days, with electrodes re-applied each day. Used here: GESTURE sub-dataset (11 cued hand and wrist gestures, no force), subject 1, days 1 and 2, five trials per day.

- Yang S, Li D, Chen C, Zhu X. Dataset: CEMHSEY, Part II. Zenodo (2025). https://doi.org/10.5281/zenodo.14272463
- Yang S, Chen C, Li D, Zhu X. A consecutive multi-day high-density surface electromyography dataset comprising 7 grasps and 11 gestures. *Scientific Data* 12, 1420 (2025). https://doi.org/10.1038/s41597-025-05733-y

## Author

Karla Miriam Reyes Leiva, PhD. Biomedical engineer working on physiological signal processing, wearable and radar sensing, and machine learning. ORCID [0000-0002-3269-0830](https://orcid.org/0000-0002-3269-0830)

Code: MIT licence. The datasets belong to their authors; please cite them if you use them.
