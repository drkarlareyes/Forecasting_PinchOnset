# Forecasting pinch force from forearm sEMG

Can forearm sEMG tell a robotic hand that a pinch is coming, early enough to be useful? I tested this offline on four public datasets, 77 people in total: Hyser (20), putEMG-Force (44), WAY-EEG-GAL (12) and CEMHSEY (1).

**Short answer**

- sEMG starts before force, but with causal processing not by much: 22 and 54 ms in the two pilot trials. Force in that dataset is sampled at 100 Hz and filtered in a way that is not fully documented, so I don't read this as a latency.
- A forecast 100 ms ahead beats the model's own current estimate while force rises, but only a little: by 1.4 points of a typical press in Hyser and 0.4 in putEMG-Force, and not at all in the reach-to-grasp task of WAY-EEG-GAL.
- A threshold detector on the sEMG caught at most 11% of presses before force onset (median across people), and only at settings with several false alarms per minute at rest. During a reach it fired long before the hand touched anything.
- A calibration does not survive putting the electrodes back on. The new session needs tens of seconds of data with force.

All of this is offline analysis of recordings. Nothing was run on a robot.

## Hyser, 20 people (Figures 6 to 8)

Self-paced finger presses recorded with 256 electrodes over the forearm: two 25 s trials per session, two sessions on different days. I calibrate on one trial, test on the other, and model the middle finger (active in 19 of the 20 people).

**How far ahead.** The delay at which the sEMG predicts force best, chosen inside the calibration trial, had a median of 150 ms (IQR 98 to 210 ms) and changed a lot from one trial to the next. On the other trial it raised R² from 0.19 at 0 ms to 0.32 (medians). Part of this delay may come from how the force was filtered before it was stored, see [Figure 1](notes/Figure1.md). [Figure 6](notes/Figure6.md)

**Forecast.** One comparison is primary in every dataset: the forecast 100 ms ahead while force rises, against repeating the model's own current estimate. The median gain was 1.4 points of a typical press (95% CI 0.6 to 4.2). It was positive in 17 of 19 people, but each person's own interval was clearly above zero in only 5. At 150 and 200 ms the gain was larger, 3.2 and 3.7 points. Repeating the measured force, which needs a force sensor, was still better up to 150 ms while force rose and at every horizon during holds and release. [Figure 7](notes/Figure7.md)

**Next day.** A day-1 model fell from R² 0.41 (calibrated on the same day) to −0.17. Rescaling the sEMG on the new day without force helped little (0.07 to 0.10). With force, 20 s of the new day got back to 0.36 alone and 0.38 together with day 1. [Figure 8](notes/Figure8.md)

## putEMG-Force, 44 people (Figures 9 to 12)

A second lab: 24 electrodes in three bands around the forearm, presses of each finger following a force target, two sessions at least a week apart.

**How far ahead.** Here choosing a delay on the calibration recording did not help on the test recordings: R² was 0.40 at 0 ms and 0.40 at the chosen delay (median 95 ms, IQR 20 to 190 ms). [Figure 9](notes/Figure9.md)

**Detection.** The detector fires when its output (the three highest per-electrode z-scores at each millisecond, averaged) stays above a percentile of its own rest output in the calibration recording. At the most sensitive setting it caught 76% of presses with 11 false alarms per minute at rest; firing at random at that rate would catch 44%. Only 11% of presses were caught before force onset. At 0.7 false alarms per minute it caught 32%, a median of 0.5 s after force onset. Ring and little finger presses were caught most often, thumb presses least. [Figure 10](notes/Figure10.md)

**Forecast.** Primary comparison: median gain 0.4 points (95% CI 0.3 to 0.5; above zero in 39 of 44 people). Small, but in almost everyone. During release the forecast was worse than its own estimate up to 100 ms. [Figure 11](notes/Figure11.md)

**Next session.** R² fell from 0.46 to −0.75. Unlike Hyser, keeping the session-1 data made things worse: new-session data alone reached 0.26 with 40 s and 0.36 with 120 s. [Figure 12](notes/Figure12.md)

## WAY-EEG-GAL, 12 people (Figures 13 to 15)

Reach, grasp an object between thumb and index finger, lift, hold, put back; 3,528 trials with five arm and hand muscles. The weight changes between trials without warning.

**Muscle onsets.** The shoulder and forearm muscles switched on 60 to 140 ms before the hand moved. The first dorsal interosseous switched on 82 ms after the hand started moving, about 820 ms before contact, at a low level; its main burst came after contact. [Figure 13](notes/Figure13.md)

**Detection.** On the two finger muscles, the detector's first firing in a trial came either during the reach, around a second before contact, or after contact. At no threshold did more than 9% of trials first fire in the last 200 ms before contact. [Figure 14](notes/Figure14.md)

**Grip force.** The force plates also pick up the experimenter handling the object between trials, so I set grip force to zero outside each grip, using the authors' event times. That makes the gaps easy to predict: R² of the force estimate was 0.65 over whole series but 0.39 over the grips alone. The delay chosen on the calibration series (median 125 ms) raised R² from 0.65 to 0.66. Primary comparison: −0.16 points (95% CI −0.54 to 0.05; above zero in 4 of 12), so no gain at 100 ms. At 150 and 200 ms the gain was positive (0.4 and 0.9 points). A lighter object than in the previous trial lowered the gain at every horizon in nearly every person. [Figure 15](notes/Figure15.md)

## Pilot, one person per dataset (Figures 1 to 5)

Before running everyone, I tried each question on Hyser subject 1 and CEMHSEY subject 1 to see what it could show.

- **Timing.** With causal processing, sEMG onset came 22 and 54 ms before force onset in the two trials; a detector that needs 50 ms above threshold fires after force has started in one of them. Force is stored at 100 Hz, so onsets are resolved to 10 ms, and the dataset says it was low-pass filtered at 10 Hz without saying how. Applied forward only, that filter would delay force by about 80 ms. [Figure 1](notes/Figure1.md)
- **Baselines.** The pilot compares the forecast with four baselines: its own current estimate, the measured force, a trend of the estimate and a reduced physiological model. Against its own estimate it gained at most 2.6 points, and during force rise the 95% interval included zero at every horizon. The trend chose no trend on calibration, so it matched the first baseline. [Figure 2](notes/Figure2.md)
- **Calibration data.** With the same number of samples, steady force left the model's delay poorly identified and changing force constrained it, but steady force predicted the other trial better. A random mix did about as well as the best of the two. [Figure 3](notes/Figure3.md)
- **Cue-only control.** In CEMHSEY, where movements follow a fixed schedule, time since trial start alone predicted muscle activity with R² 0.77 to 0.91. In self-paced Hyser it predicted nothing. Cued datasets can make a model look anticipatory when it is only learning the schedule. [Figure 4](notes/Figure4.md)
- **False pinches.** A pinch detector calibrated on pinch and rest flagged 0.5% of rest, but 99.8% of hand closing and 84% of wrist extension. On the next day, with the electrodes put back on, it detected 0 of 10 pinches. [Figure 5](notes/Figure5.md)

## How the numbers were made

- **Causal features.** Band-pass filter and trailing RMS, so a feature at time *t* only uses sEMG up to *t*. Each notebook checks this by cutting the recording after *t* and recomputing.
- **Calibrate on one recording, test on another.** Everything that is fitted comes from the calibration recording only: which electrodes to keep, normalisation, principal components, ridge weights and penalty, the delay, and the detector's rest levels and thresholds.
- **Baselines.** Four in the pilot. In the three multi-person stages, two: the model's own current estimate (what a system without a force sensor can use) and the measured force (an offline reference, it needs a sensor).
- **Errors** are RMS errors in % of a typical press (the 95th percentile of the force change in the test recording), so gains are in percentage points of a typical press.
- **Statistics.** One primary comparison per dataset: force rising, 100 ms ahead, against the model's own estimate. Rising force is where anticipation would matter, and 100 ms is in the range of controller delays usually considered acceptable for myoelectric prostheses (Farrell and Weir, *IEEE TNSRE* 15:111, 2007). It gets a 95% interval from resampling people and a Wilcoxon test. Everything else is exploratory and reported as medians, IQRs and counts of people, without p-values. Intervals within a person come from a moving-block bootstrap with 1 s blocks drawn inside each recording.
- **Phases** (rising, steady, falling force) come from the measured force and are only used to split the scores.
- **Calibration budgets** on a new day count everything from the start of the recording to the last sample used, including the first second and the forecast horizon.

## Signals and timing

| Dataset | sEMG | Force | What limits the timing |
|---|---|---|---|
| Hyser | 256 electrodes, 2048 Hz | five fingers, 100 Hz | 10 ms sampling; 10 Hz low-pass of unknown phase |
| putEMG-Force | 24 electrodes, 5120 Hz | ten strain gauges, 200 Hz | separate device; alignment with the sEMG cannot be checked from the data |
| WAY-EEG-GAL | 5 muscles, 4 kHz | thumb and index plates, 500 Hz | force taken 2 ms before each feature time |
| CEMHSEY | 320 electrodes, 2048 Hz | none, labels from the cue schedule | 100 ms windows |

[Limitations.md](Limitations.md) lists what these analyses cannot show.

## Repository

| Path | Content |
|---|---|
| `hyser.ipynb` | Hyser pilot, one person: Figures 1 to 3 |
| `cemhsey.ipynb` | CEMHSEY, one person, with a Hyser comparison: Figures 4 and 5 |
| `hyser_multisubject.ipynb` | Hyser, all 20 people: Figures 6 to 8 |
| `putemg_force.ipynb` | putEMG-Force, all 44 people: Figures 9 to 12 |
| `way_eeg_gal.ipynb` | WAY-EEG-GAL, all 12 people: Figures 13 to 15 |
| `download_*.py` | Download the Hyser, putEMG-Force and WAY-EEG-GAL files |
| `notes/` | One page per figure: what it shows, how it was made, the numbers |
| `figures/`, `results/` | Figure images and the numbers behind them (JSON, with package versions) |

## How to run

1. Get the data (not included here): `python download_hyser.py` (about 2 GB), `python download_putemg_force.py` (about 20 GB), `python download_way_eeg_gal.py` (10.3 GB). CEMHSEY is on Zenodo (link below).
2. `pip install -r requirements.txt` (versions as used for the results; Python 3.10).
3. Point `HYSER_DIR`, `HYSER_RANDOM`, `PUTEMG_FORCE`, `WAY_EEG_GAL` and `CEM_DIR` to the data, as environment variables or in the first cell of each notebook, and run the notebooks from the repository folder. `CEM_CACHE` sets where `cemhsey.ipynb` keeps the features it extracts. The multi-person notebooks keep each person's results in `results/multisubject/`, `results/putemg/` and `results/way/`, and only process new people when run again.

## Data

**Hyser** (PhysioNet `hd-semg` 2.0.0). Random task (self-paced finger presses), trials 1 and 2. Pilot: subject 1, session 1. All people: subjects 1 to 20, sessions 1 and 2.

- Jiang X, Dai C, Liu X, Fan J. Open Access Dataset and Toolbox of High-Density Surface Electromyogram Recordings (version 2.0.0). PhysioNet (2023). https://doi.org/10.13026/hxan-pe94
- Jiang X, et al. Open access dataset, toolbox and benchmark processing results of high-density surface electromyogram recordings. *IEEE Transactions on Neural Systems and Rehabilitation Engineering* 29, 1035–1046 (2021). https://doi.org/10.1109/TNSRE.2021.3082551
- Licence: Open Data Commons Attribution License v1.0.

**putEMG-Force** (Poznan University of Technology). All force recordings (`repeats_long`, `sequential`, `repeats_short`) of the 44 participants.

- putEMG and putEMG-Force datasets. https://biolab.put.poznan.pl/putemg-dataset/
- Kaczmarek P, Mańkowski T, Tomczyński J. putEMG—A surface electromyography hand gesture recognition dataset. *Sensors* 19, 3548 (2019). https://doi.org/10.3390/s19163548
- Licence: CC BY-NC 4.0.

**WAY-EEG-GAL** (Umeå University). sEMG of five muscles, contact plate forces and the authors' event times; the EEG is not used.

- Luciw MD, Jarocka E, Edin BB. Multi-channel EEG recordings during 3,936 grasp and lift trials with varying weight and friction. *Scientific Data* 1, 140047 (2014). https://doi.org/10.1038/sdata.2014.47
- Dataset: figshare collection. https://doi.org/10.6084/m9.figshare.988376
- Licence: CC BY 4.0.

**CEMHSEY**. GESTURE sub-dataset (11 cued gestures, no force), subject 1, days 1 and 2, five trials per day.

- Yang S, Li D, Chen C, Zhu X. Dataset: CEMHSEY, Part II. Zenodo (2025). https://doi.org/10.5281/zenodo.14272463
- Yang S, Chen C, Li D, Zhu X. A consecutive multi-day high-density surface electromyography dataset comprising 7 grasps and 11 gestures. *Scientific Data* 12, 1420 (2025). https://doi.org/10.1038/s41597-025-05733-y

Karla Miriam Reyes Leiva · [drkarlareyes.github.io](https://drkarlareyes.github.io) · ORCID [0000-0002-3269-0830](https://orcid.org/0000-0002-3269-0830) · Code under the MIT licence; the datasets belong to their authors.
