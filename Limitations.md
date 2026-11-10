# Limitations

These analyses are deliberately limited in scope:

1. The pilot (Figures 1 to 5) examined one participant per dataset. Stages 2 and 3 cover all participants of Hyser (20) and putEMG-Force (44), but CEMHSEY results still come from one person.
2. Hyser and putEMG-Force provide individual finger forces, not thumb–index contact force.
3. CEMHSEY GESTURE provides gesture labels but no measured force.
4. The analyses cover selected tests rather than the complete physiological framework.
5. Learned neural-drive representations, in-context personalisation and the complete real-time robotic pipeline remain proposed research directions.
6. Cross-trial and cross-day comparisons are useful preliminary checks, but they do not establish clinical or robotic deployment performance.
7. The onset timing (Figure 1) rests on two onsets, one per trial: in the Hyser random task the force of the five fingers rarely returns to rest.
8. The confidence intervals of Figure 2 reflect variation over time within two recordings of one person, not variation between people. Figure 7 adds the variation between people.
9. Stage 2 uses the middle finger and two 25 s recordings per session. The delay of best prediction (Figure 6) combines the electromechanical delay with the slow dynamics of force: it is not an onset latency.
10. The tests across people in Figures 7 and 11 are not corrected for the number of horizons and phases compared.
11. putEMG-Force records force with a separate dynamometer at 200 Hz, and its alignment with the sEMG cannot be checked from the data. A delay of best prediction close to Hyser's (100 and 130 ms) argues against a large offset, but an offset of a few tens of milliseconds would shift the warning times of Figure 10 by the same amount.
12. In putEMG-Force the participants followed a visible force target and often started pressing before the target step, so the presses were anticipated rather than reactions to a cue. Detection is therefore scored against force onset, not against the target.
13. The putEMG-Force electrodes were used as recorded (monopolar). Other derivations, such as bipolar pairs along each band, may change the per-finger results.
14. The detector of Figure 10 is a fixed threshold on the three most active electrodes, referenced to rest and not trained on presses. It is a baseline for early detection with this electrode layout, not an upper bound.

The repository is intended to demonstrate my experimental reasoning.
