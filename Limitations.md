# Limitations

**What was measured**

- Everything here is offline analysis of recordings made by other groups. Nothing was run in real time or on a robot, and acquisition, processing and actuation delays are not included.
- No dataset has what the question really needs: forearm HD-sEMG with thumb–index pinch force. Hyser and putEMG-Force give individual finger forces. WAY-EEG-GAL gives pinch grip force, but with five single sEMG channels and no thumb muscle. CEMHSEY GESTURE has no force at all, only cue labels.
- The pilot (Figures 1 to 5) is one person per dataset, and the CEMHSEY results stay that way.
- The models are linear (ridge regression on log RMS envelopes). Nonlinear or learned models may do better at forecasting and detection.

**Timing**

- In Hyser, force is stored at 100 Hz after a 10 Hz low-pass filter whose phase is not documented. Applied forward only, it would delay force by about 80 ms. The delays of best prediction (Figure 6) and the onset leads (Figure 1) may include part of that.
- The onset leads of Figure 1 come from two onsets of one person; in the random task the fingers rarely return to rest.
- putEMG-Force records force with a separate dynamometer at 200 Hz, and its alignment with the sEMG cannot be checked from the data. An offset of a few tens of milliseconds would shift the warning times of Figure 10 by the same amount.
- The delay of best prediction mixes the electromechanical delay with the slow rise and fall of force. It changed a lot between recordings of the same person (median 90 ms between the two Hyser trials, 80 ms between putEMG sessions), so it should not be read as a fixed property of a person.

**Detection**

- The detector is a threshold on rest-referenced activity, not trained on presses or grips. It is a baseline for these electrode layouts, not an upper bound.
- In putEMG-Force, rest is defined from the force, so false alarms are counted only while the hand is still. Other movements would add more, as CEMHSEY (Figure 5) and the reach in WAY-EEG-GAL (Figure 14) show.
- putEMG participants followed a visible force target and often started before the target step, so presses were anticipated rather than reactions. I score detection against force onset, not against the target.
- The putEMG-Force electrodes were used as recorded (monopolar). Bipolar pairs along each band might change the per-finger results.

**Forecast and statistics**

- One comparison per dataset is primary (force rising, 100 ms ahead, against the model's own estimate). The other phases, horizons and weight cases are exploratory, reported without p-values, and should be read as descriptions.
- Intervals within a person come from resampling time within a few recordings. Across people, only the primary comparison has an interval.
- In WAY-EEG-GAL, grip force is set to zero outside each grip using the authors' event times, which makes the time between grips easy to predict. That is why I also give R² over the grips alone (0.39 against 0.65).
- The WAY-EEG-GAL weight cases rest on about 7 s of rising grip force per person and case.

**Calibration across days**

- Hyser recordings are 25 s, so new-day budgets above 20 s could not be tested.
- All WAY-EEG-GAL series of a person come from one session, so that dataset does not test a new session.
- Calibrations weight all samples equally. A weighting that favours new data might change the putEMG-Force result that keeping old data hurts (Figure 12); I did not test it.
