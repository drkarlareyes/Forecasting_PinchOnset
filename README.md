# Forecasting finger force and pinch onsets from forearm HD-sEMG

Muscle electrical activity starts before the force it produces. This repository tests how far that lead can be used: can a model predict finger force tens of milliseconds ahead with information that goes beyond simply repeating the last value, and how do early pinch detection and false pinches trade off?

I use eight research questions (T1–T8) to organise exploratory analyses of four public-data stages. The repository implements subsets of these tests, not a completed or deployment-validated system.

1. **Pilot, one participant per dataset** (Figures 1 to 5): five of the tests on Hyser and CEMHSEY, to see what each test can reveal.
2. **Hyser, all 20 participants** (Figures 6 to 8): the timing and forecast tests repeated on everyone, plus a day-to-day test with the electrodes placed again.
3. **putEMG-Force, all 44 participants** (Figures 9 to 12): the same tests on a second dataset recorded in another lab, plus a press detector scored on about 90 presses from rest per person.
4. **WAY-EEG-GAL, all 12 participants** (Figures 13 to 15): thumb–index grip force during whole reach, grasp, lift and release movements, with unexpected weight changes.

## Key results

### Stage 1 · Pilot, one participant per dataset

| Figure | T | Question | Result on public data |
|---|---|---|---|
| [1](Tests/Figure1.md) | Test 1 | Does EMG lead force, and by how much? | With causal processing, EMG crossed the rest threshold 22 and 41 ms before force (two trials). A *causally processed offline detector* with 10 ms confirmation fired 13 and 32 ms before the reference force threshold; with 50 ms confirmation it fired after. These timings exclude complete acquisition, computation and robotic actuation latency. |
| [2](Tests/Figure2.md) | Test 2 | Does a forecast beat persistence, and when? | Against repeating its own last estimate (the deployable baseline), the EMG forecast was at most 2.6 points of a typical press better, and during force rise the 95% interval included zero at every horizon. Repeating the measured force, which needs a force sensor, won at 30 ms in every phase and up to 150 ms during holds. |
| [3](Tests/Figure3.md) | Test 5 | Which calibration data identify the model? | Steady force left the EMG-to-force delay poorly identified (fit changed by 0.035 R² across 0 to 150 ms); changing force constrained it (0.16 to 0.25). A mixed calibration predicted best or as well (R² 0.70 and 0.78). |
| [4](Tests/Figure4.md) | Test 4 | Can the task schedule alone look like anticipation? | Time since trial start alone predicted cued muscle activity with R² 0.77 to 0.91, and self-paced activity not at all (−0.03 and −0.18). |
| [5](Tests/Figure5.md) | Test 7, Test 8 | Where do false pinches come from? | A pinch detector calibrated on pinch and rest flagged rest 0.4% of the time but hand closing 99% and wrist extension 79%. On another day, after the electrodes were re-applied, it detected 0 of 10 pinches. |

### Stage 2 · Hyser, all 20 participants

| Figure | T | Question | Result on public data |
|---|---|---|---|
| [6](Tests/Figure6.md) | Test 1 | How far ahead does sEMG carry information about force? | In all 19 participants with an active middle finger, the maximum of the held-out delay profile occurred at a positive delay (test-selected, descriptive): median 130 ms (IQR 105 to 195 ms; 70 ms for the pilot participant). R² on the other trial rose from 0.18 at 0 ms to 0.36 at each person's best delay (medians). |
| [7](Tests/Figure7.md) | Test 2 | Does the forecast beat persistence across people? | Against repeating its own estimate, the forecast's median gain during force rise was 1.4 points of a typical press at 100 ms and 3.3 to 3.7 points at 150 to 200 ms (Wilcoxon p ≤ 0.001), clear within 10 of 19 people at 150 to 200 ms. Repeating the measured force still won up to 100 ms in every phase and at all horizons during holds. |
| [8](Tests/Figure8.md) | Test 8, Test 5 | Does a calibration survive to the next day? | No. A day-1 model fell from a median R² of 0.39 (same-day calibration) to −0.07 on day 2. Rescaling the sEMG on day 2 without force reached only 0.11. Adding 10 to 20 s of day-2 data with force to the day-1 data recovered 0.32 to 0.35; day-2 data alone needed 20 s to match. |

### Stage 3 · putEMG-Force, all 44 participants

| Figure | T | Question | Result on public data |
|---|---|---|---|
| [9](Tests/Figure9.md) | Test 1 | Does the delay of best prediction replicate? | The maximum held-out delay-profile score occurred at a positive delay for all 44 participants (median 100 ms, IQR 90–140 ms; Hyser: 130 ms). The reported R² at the maximum (0.41 versus 0.40 at zero delay) is optimistic because the best delay was chosen on test data. |
| [10](Tests/Figure10.md) | Test 1, Test 7, Test 8 | Can a detector see a press before force starts? | Rarely. At 5 SD and 25 ms, a rest-referenced sEMG detector caught 30% of presses with 0.44 false alarms per minute, a median of 540 ms after force onset, and none before it. The most sensitive setting caught 82% but raised 15 false alarms per minute (random firing would catch 52%), and 13% before force onset. Ring and little finger presses were caught most often (62%), thumb presses least (8%). The next session gave similar numbers. |
| [11](Tests/Figure11.md) | Test 2 | Does the forecast beat persistence in a second dataset? | In the same direction as Hyser, but smaller: during force rise the median gain over repeating its own estimate was 0.4 points of a typical press at 100 ms (clear in 37 of 44 participants) and 0.6 at 200 ms. During release the forecast was worse up to 100 ms. |
| [12](Tests/Figure12.md) | Test 8, Test 5 | Does a calibration survive to the next session? | No. R² fell from 0.46 (same-session calibration) to −0.75. Unlike Hyser, keeping the session-1 data hurt: new-session data alone reached 0.20 with 20 s and 0.36 with 120 s; session 1 plus the same new data reached −0.12 and 0.15. |

### Stage 4 · WAY-EEG-GAL, all 12 participants

| Figure | T | Question | Result on public data |
|---|---|---|---|
| [13](Tests/Figure13.md) | Test 1 | When do the arm and hand muscles become active relative to finger contact? | The shoulder and forearm muscles switched on 60 to 140 ms before the hand started moving. The first dorsal interosseous switched on 82 ms after the hand started moving, about 820 ms before contact, at a low level; its main burst came after contact (halfway to its peak at 105 ms, grip force at 225 ms). |
| [14](Tests/Figure14.md) | Test 7, Test 1 | Does a pinch detector stay quiet during the reach? | Not at useful settings. On the two finger muscles (flexor digitorum, first dorsal interosseous), a sensitive detector (3 SD, 10 ms) had fired before the last 200 ms preceding contact in 85% of trials, with 4.1 false alarms per minute at rest. A stricter one (5 SD, 25 ms) was rarely on at rest or during the reach, but first fired after contact (median 113 ms) or not at all in 76% of trials. At no setting did more than 8% of trials first fire in the last 200 ms before contact. |
| [15](Tests/Figure15.md) | Test 1, Test 2 | Does the forecast help with grip force and unexpected weights? | The highest held-out delay-profile R² occurred at a median 125 ms (IQR 88–152 ms). The small difference between R² at zero delay (0.65) and the test-selected maximum (0.66) is descriptive, not unbiased model-selection performance. During force rise the forecast was worse than its own estimate up to 70 ms and better at 150 to 200 ms (0.4 and 0.9 points of a typical grip). A heavier object than in the previous trial made no clear difference; a lighter one lowered the gain at every horizon. |

Each linked page explains the figure, the method and its limits.

### Interpretation of reported numbers

The figures and JSON results are **existing exploratory outputs; they have not been recalculated after this documentation review**. A reviewer should know:

- **Test-selected best delays.** Figures 6, 9 and 15 identify the delay maximizing R² on held-out recordings. These positive peak delays describe the observed profiles; reporting R² at their maxima is optimistically selected. A reliable estimate of a *chosen* delay would require selecting it using calibration data only, followed by an untouched test.
- **Electrode QC.** The Hyser pilot and 20-participant analysis combine unsupervised quality flags from both recordings in a test pair before fitting. This uses information from the test recording (even though no force labels are used), so these splits are not strictly held out. In putEMG-Force, electrode QC is based on the first-session calibration recording.
- **Latency and detection.** The signal filtering and envelopes used in the forecast are causal. This alone does not establish usable lead after acquisition, computation, inference, confirmation, and actuation delays. The Hyser pilot's zero-phase filtering is shown only as an *offline timing comparison*.
- **Uncertainty.** Participant-level summaries and moving-block intervals are exploratory. Reported p-values cover multiple horizons and phases without multiplicity correction; within-participant block intervals do not quantify between-person generalization.
- **Metrics.** Evaluation uses force-derived phase labels and test-recording force scales only to score predictions, not as model inputs. The last *measured* force is an offline reference baseline requiring a force sensor; the last *estimated* force is the deployment-relevant persistence baseline when a force sensor is unavailable.

For exact implementation choices and unresolved issues, see [Methodology review](METHODOLOGY_REVIEW.md) and [Limitations](Limitations.md).

## Approach

- **Causal processing.** Forecast and detector signals use forward-only filtering and trailing windows; the Hyser zero-phase trace is an explicit offline comparison. Learned scalers and model weights use calibration recordings, except for the test-informed electrode QC in the Hyser notebooks described above. The few numerical look-ahead spot checks are not an exhaustive latency audit.
- **Cross-recording tests.** Models are calibrated on one recording and scored on another; the Hyser electrode QC and best-delay selection mean that not every comparison is a strictly untouched test.
- **Baselines.** The pilot compares four baselines: last estimated force, last measured force (offline-only), trend extrapolation and a reduced physiological model. Stages 2–4 compare the first two persistence baselines; the latter two were **not** rerun at scale.
- **Reduced physiological model.** Activation follows a neural drive estimate *u* as da/dt = (u − a)/τ, with separate time constants for rise and relaxation, and force is F(t + d) = b + k·aᵖ with an electromechanical delay *d*.
- **Results split by phase** (force rising, steady, falling), because good performance during holds can hide poor anticipation.
- **Detection scored against force onset** (stage 3) or movement phases (stage 4). In stage 3 the detector averages the *three largest per-channel standardized activity values at each time sample*; they are not three fixed electrodes, and the thresholds are in per-electrode standardized units, not SDs of that aggregate statistic.

## Leakage checklist

| Step | Fitted on | Uses samples after *t*? |
|---|---|---|
| sEMG features and activity (band-pass, RMS) | fixed filter coefficients | Uses forward-only filters and trailing windows; each notebook includes limited look-ahead checks, not a comprehensive timing audit |
| Electrode exclusion | Hyser: both calibration and test recordings in stages 1–2; putEMG-Force: session-1 calibration recording | **Hyser has test-covariate leakage** (unsupervised QC flags from held-out recordings); no force labels are used in electrode exclusion |
| z-score, PCA, ridge weights and penalty | calibration recording | Penalty chosen by blocked cross-validation with a gap |
| Trend damping, physiological model | calibration recording | No |
| Phase labels (rising, steady, falling) | measured force of the test recording | Yes, but only to split the evaluation, never as model input |
| Detector rest levels | calibration recording | No |
| Force onsets and rest periods | measured force of the test recording | Yes, but only to score the detector, never as its input |
| Trial events and movement phases (stage 4) | the dataset authors' event times | Yes, but only to define the grip force target, split the evaluation and score the detector, never as model input |
| Error scale | test recording | Same divisor for every model |
| Baseline 2 (measured force) | none | No, but it needs a force sensor |

## Eight research questions (some not yet implemented)

| Test | Question |
|---|---|
| Test 1 | Does sEMG contain information before force changes? |
| Test 2 | Does a forecast beat persistence and trend at the same horizon? |
| Test 3 | Does recent sEMG carry the useful information (older-EMG ablation)? **Not implemented** |
| Test 4 | Is the forecast exploiting the task schedule instead of sEMG (cue-only control)? |
| Test 5 | Do holds, ramps or mixed calibrations personalize the model best? |
| Test 6 | Do physiological constraints or learned representations improve on simpler models? **Not fully evaluated beyond pilot physiological baseline** |
| Test 7 | How early can pinches be detected before false pinches become unacceptable? |
| Test 8 | Do the results survive new sessions, electrode shifts, wrist movement and real processing delays? |

## Repository

| Path | Content |
|---|---|
| `hyser.ipynb` | Hyser pilot, one participant: Figures 1, 2 and 3 |
| `hyser_multisubject.ipynb` | Hyser, all 20 participants: Figures 6, 7 and 8 |
| `download_hyser.py` | Downloads the Hyser files used by both notebooks |
| `putemg_force.ipynb` | putEMG-Force, all 44 participants: Figures 9 to 12 |
| `download_putemg_force.py` | Downloads the putEMG-Force recordings |
| `way_eeg_gal.ipynb` | WAY-EEG-GAL, all 12 participants: Figures 13 to 15 |
| `download_way_eeg_gal.py` | Downloads the WAY-EEG-GAL files |
| `cemhsey.ipynb` | CEMHSEY analyses (with a Hyser comparison): Figures 4 and 5 |
| `Tests/` | One page per figure with its explanation |
| `figures/` | Figure images |
| `results/` | Numbers behind the figures (JSON) |
| `Limitations.md` | What these analyses cannot show |
| `METHODOLOGY_REVIEW.md` | Static audit, reproducibility status, and issues requiring new analyses |

## How to run

1. Download the data (not included here, see below) into a `data/` folder. For Hyser, `python download_hyser.py` gets the random task of all 20 participants, both sessions (about 2 GB, into `data/hyser/`). For putEMG-Force, `python download_putemg_force.py` gets the force recordings of all 44 participants (about 20 GB, into `data/putemg_force/`). For WAY-EEG-GAL, `python download_way_eeg_gal.py` gets the 12 participant files (10.3 GB, into `data/way_eeg_gal/`).
2. `pip install -r requirements.txt`
3. Set `HYSER_DIR`, `HYSER_RANDOM`, `PUTEMG_FORCE`, `WAY_EEG_GAL` and `CEM_DIR` in the first cell of each notebook (or as environment variables), then run all cells from the repository folder. `hyser.ipynb` takes about a minute; `hyser_multisubject.ipynb` takes about 15 s per participant the first time and keeps the results of each person in `results/multisubject/`; `putemg_force.ipynb` takes about 25 s per participant the first time and keeps them in `results/putemg/`; `way_eeg_gal.ipynb` takes about 20 s per participant the first time and keeps them in `results/way/`; `cemhsey.ipynb` takes a few minutes the first time while it extracts features from the CEMHSEY files.

## Datasets 

**Hyser** (PhysioNet `hd-semg` 2.0.0). Forearm HD-sEMG from 20 participants, 256 electrodes in four 8 × 8 grids over the extensor and flexor muscles (2048 Hz), with the force of the five fingers (100 Hz). Used here: random task (self-paced finger presses), trials 1 and 2. Stage 1: subject 1, session 1. Stage 2: subjects 1 to 20, sessions 1 and 2, recorded on separate days.

- Jiang X, Dai C, Liu X, Fan J. Open Access Dataset and Toolbox of High-Density Surface Electromyogram Recordings (version 2.0.0). PhysioNet (2023). https://doi.org/10.13026/hxan-pe94
- Jiang X, et al. Open access dataset, toolbox and benchmark processing results of high-density surface electromyogram recordings. *IEEE Transactions on Neural Systems and Rehabilitation Engineering* 29, 1035–1046 (2021). https://doi.org/10.1109/TNSRE.2021.3082551
- Licence: Open Data Commons Attribution License v1.0.

**putEMG-Force** (Biomedical Engineering group, Poznan University of Technology). 24 monopolar electrodes in three bands of eight around the right forearm (5120 Hz) and the force of each finger on a hand dynamometer (200 Hz), from 44 participants in two sessions at least a week apart, with the bands placed again. Used here: all force recordings (`repeats_long`, `sequential`, `repeats_short`), in which the participant follows a force target with the thumb, the index, the middle, the ring and little fingers together, or all fingers.

- putEMG and putEMG-Force datasets. https://biolab.put.poznan.pl/putemg-dataset/
- Kaczmarek P, Mańkowski T, Tomczyński J. putEMG—A surface electromyography hand gesture recognition dataset. *Sensors* 19, 3548 (2019). https://doi.org/10.3390/s19163548
- Licence: CC BY-NC 4.0.

**WAY-EEG-GAL** (Umeå University). 12 participants grasped an object between thumb and index finger, lifted it, held it and put it back, in 9 series of 28 or 34 trials each (3,528 trials with sEMG and force); the weight (165, 330 or 660 g) and the contact surface (sandpaper, suede or silk) changed between trials without warning. sEMG of five muscles (anterior deltoid, brachioradialis, flexor digitorum, common extensor digitorum, first dorsal interosseous) at 4 kHz, force and torque of the index and thumb contact plates at 500 Hz, and event times for each trial. The EEG in the dataset is not used here.

- Luciw MD, Jarocka E, Edin BB. Multi-channel EEG recordings during 3,936 grasp and lift trials with varying weight and friction. *Scientific Data* 1, 140047 (2014). https://doi.org/10.1038/sdata.2014.47
- Dataset: figshare collection. https://doi.org/10.6084/m9.figshare.988376
- Licence: CC BY 4.0.

**CEMHSEY** (ConsecutivE Multi-day High-density Surface ElectromyographY). 320-channel forearm HD-sEMG (five 8 × 8 grids, 2048 Hz) over 11 consecutive days, with electrodes re-applied each day. Used here: GESTURE sub-dataset (11 cued hand and wrist gestures, no force), subject 1, days 1 and 2, five trials per day.

- Yang S, Li D, Chen C, Zhu X. Dataset: CEMHSEY, Part II. Zenodo (2025). https://doi.org/10.5281/zenodo.14272463
- Yang S, Chen C, Li D, Zhu X. A consecutive multi-day high-density surface electromyography dataset comprising 7 grasps and 11 gestures. *Scientific Data* 12, 1420 (2025). https://doi.org/10.1038/s41597-025-05733-y

## Author

Karla Miriam Reyes Leiva, PhD. Biomedical engineer working on physiological signal processing, wearable and radar sensing, and machine learning. ORCID [0000-0002-3269-0830](https://orcid.org/0000-0002-3269-0830)

Code: MIT licence. The datasets belong to their authors; please cite them if you use them.
