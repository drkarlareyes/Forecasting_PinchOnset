# Forecasting_PinchOnset
Supporting documentation for scientific approach

This REPO shows proof of concept tests of my experimental plan on two public datasets, with one subject measurements taken from each. 

Each figure takes one test from the plan, runs it on real HD-sEMG, and checks whether it gives an answer that would change a decision.


## Data

**Hyser** (PhysioNet `hd-semg`, version 2.0.0). High-density surface EMG from the forearm of 20 participants, recorded with 256 electrodes (four 8 × 8 grids over the extensor and flexor muscles, 2048 Hz) together with the force of the five fingers (100 Hz). I used the random task of subject 1, session 1, trials 1 and 2, in which the participant pressed the fingers freely, without cues.

- Dataset: Jiang X, Dai C, Liu X, Fan J. Open Access Dataset and Toolbox of High-Density Surface Electromyogram Recordings (version 2.0.0). PhysioNet (2023). https://doi.org/10.13026/hxan-pe94
- Licence: Open Data Commons Attribution License v1.0.

**CEMHSEY** (ConsecutivE Multi-day High-density Surface ElectromyographY). 320-channel HD-sEMG from the forearm (five 8 × 8 grids, 2048 Hz), recorded over 11 consecutive days, with the electrodes removed and re-applied each day. I used the GESTURE sub-dataset (11 cued hand and wrist gestures, 10 s each with rest in between, no force recording), subject 1, days 1 and 2, five trials per day. GESTURE is in Part II of the dataset.

- Dataset: Yang S, Li D, Chen C, Zhu X. Dataset: CEMHSEY (ConsecutivE Multi-day High-density Surface ElectromyographY), Part II. Zenodo (2025). https://doi.org/10.5281/zenodo.14272463

The data are not included in this repository. 
