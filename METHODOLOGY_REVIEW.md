# Methodology review — static corrections without rerunning experiments

Review date: 17 November 2026. Scope: code reading and documentation only. The original recordings were **not downloaded or reprocessed** during this review. All existing figure images, saved JSON results and numerical estimates are preserved; nothing here certifies their numerical accuracy.

## What is supported by the implemented code

- The main sEMG signal path uses forward-only IIR filtering (`sosfilt`) and trailing RMS windows. The Hyser pilot also shows `sosfiltfilt) with a centred window as an **offline illustration** of how noncausal preprocessing alters apparent onset timing. No offline lead should be treated as deployable advance notice.
- Model coefficients and normalization/PCA parameters are generally fitted on designated calibration recordings. Later studies evaluate held-out recordings or series for predictions at **predefined** horizons (30, 50, 70, 100, 150 and 200 ms).
- The "own-estimate persistence" baseline is applicable to a system without a force sensor; measured-force persistence is an **offline** reference, not a deployable baseline.
- Recorded force is used for labels, scoring and evaluation-phase definitions; those retrospective labels do not feed directly into real-time prediction.

## Issues that remain in the published exploratory results

1. **Test-selected best delay (Figures 6, 9, 15).** The delay maximizing held-out R² is selected using the same held-out measurements whose maximum R² is reported. A descriptive peak in an observed delay curve is valid; the R² at that peak is optimistically selected. The peak delay is also not a direct estimate of electromechanical onset latency because slow force dynamics contribute. Corrected performance for a selected delay would require choosing delay on calibration/validation recordings and scoring it once on an untouched test. This has *not* been recalculated.
2. **Unsupervised test-recording QC in Hyser (Figures 1–3 and 6–8).** The pilot takes the union of flagged electrodes from both trial recordings, and the multisubject notebook similarly unions QC across both session-1 trials before comparing them. Although this does not inspect force labels, it uses test covariates to select channels. It does not establish a strictly deployment-like held-out protocol. Repeating QC on calibration data only is a separate analysis; existing results should retain this caveat.
3. **Pilot onset timing is based on two clean onsets from one participant (Figure 1).** The causal-envelope result demonstrates processing consistency, not real-time end-to-end latency. Confirmation time, timestamp convention, force acquisition/filtering and the complete compute/actuation stack matter. The zero-phase comparison is offline only.
4. **Different baseline scope.** Only the Hyser pilot implements the trend-extrapolation and reduced physiological baselines. Stages 2–4 focus on the forecast versus own-estimate and measured-force persistence. The limited and uneven baseline scope must be stated.
5. **putEMG-Force detector statistic (Figure 10).** `det_stat` standardizes each channel using calibration rest mean/SD and *at each time step* averages the largest three standardized channel values. This is a time-varying selection, **not** a fixed trio of electrodes. Thresholds 3/5/8 act on that mean of channel z-scores; they are not SDs of the detector's aggregated distribution. Treat the reported operating points as empirical choices, not calibrated family-wise false-alarm probabilities.
6. **Detection definitions.** putEMG-Force counts a hit for a firing from 300 ms before force onset up to the end of the press and counts rest firings separately; negative 'warning time' means the detector fired after onset. WAY-EEG-GAL labels firing relative to reach/contact using the authors' trial events. Neither establishes that a detected activation uniquely predicts a future pinch.
7. **Statistical uncertainty.** Block bootstrap intervals measure within-recording sampling variability, not between-person variability; cross-person Wilcoxon tests are exploratory. Multiple horizons, phases, weights and threshold settings were inspected without multiplicity control.
8. **Calibration times and transfer.** Claims of 10/20/120-second recalibration should distinguish the nominal count of selected labeled samples from actual collection/setup time and initial skip/window/horizon requirements. Results do not establish a production-ready short calibration protocol. Cross-session electrode reapplication and changing task conditions can dominate prediction quality.
9. **Retrospective stratification.** Centered force smoothing in `phase_labels` is used to define evaluation subsets. This is acceptable for retrospective error analysis but not deployable online segmentation and must be kept outside inference.
10. **Recording synchronization.** Public datasets may differ in acquisition clocks, resampling, reference force processing and event alignment. Forecast horizon should be interpreted with native sampling intervals and clock uncertainty in mind. This review has *not* independently verified all source-dataset timing definitions.

## No-rerun correction policy

The documentation changes in this branch clarify limitations and correct explanations without substituting new numbers for existing calculations. The old numerical results remain **exploratory**. A definitive numerical or causal validation would require re-executing the code on original recordings; this was not requested or performed.

### Files checked

- `hyser.ipynb` and `hyser_multisubject.ipynb`
- `putemg_force.ipynb`
- `way_eeg_gal.ipynb`
- `cemhsey.ipynb`
- `README.md`, `Limitations.md`, `Tests/Figure1.md` through `Tests/Figure15.md`, result summaries and download scripts.

### Suggested eventual follow-up (not part of this branch)

If numbers are revisited later: freeze input data and processing, select delays on calibration-only folds, ensure QC is fitted on calibration sessions, reserve a final untouched test, account for signal timestamps and total system latency, report participant-level uncertainty, and regenerate the affected JSON/figures together.
