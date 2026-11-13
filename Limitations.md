# Limitations

These analyses are deliberately limited in scope:

1. The pilot (Figures 1 to 5) examined one participant per dataset. Stages 2 to 4 cover all participants of Hyser (20), putEMG-Force (44) and WAY-EEG-GAL (12), but CEMHSEY results still come from one person.
2. Hyser and putEMG-Force provide individual finger forces, not thumb–index contact force. WAY-EEG-GAL provides thumb–index grip force, but with five sEMG channels (one per muscle, no thumb muscle) instead of forearm HD-sEMG.
3. CEMHSEY GESTURE provides gesture labels but no measured force.
4. The analyses cover selected tests rather than the complete physiological framework.
5. Learned neural-drive representations, in-context personalisation and the complete real-time robotic pipeline remain proposed research directions.
6. Cross-trial and cross-day comparisons are useful preliminary checks, but they do not establish clinical or robotic deployment performance.
7. The onset timing (Figure 1) rests on two onsets, one per trial: in the Hyser random task the force of the five fingers rarely returns to rest.
8. The confidence intervals of Figure 2 reflect variation over time within two recordings of one person, not variation between people. Figure 7 adds the variation between people.
9. Stage 2 uses the middle finger and two 25 s recordings per session. The delay of best prediction (Figure 6) combines the electromechanical delay with the slow dynamics of force: it is not an onset latency.
10. The tests across people in Figures 7, 11 and 15 are not corrected for the number of horizons, phases and weight cases compared.
11. putEMG-Force records force with a separate dynamometer at 200 Hz, and its alignment with the sEMG cannot be checked from the data. A delay of best prediction close to Hyser's (100 and 130 ms) argues against a large offset, but an offset of a few tens of milliseconds would shift the warning times of Figure 10 by the same amount.
12. In putEMG-Force the participants followed a visible force target and often started pressing before the target step, so the presses were anticipated rather than reactions to a cue. Detection is therefore scored against force onset, not against the target.
13. The putEMG-Force electrodes were used as recorded (monopolar). Other derivations, such as bipolar pairs along each band, may change the per-finger results.
14. The detector of Figure 10 is a fixed threshold on the three most active electrodes, referenced to rest and not trained on presses. It is a baseline for early detection with this electrode layout, not an upper bound. The same applies to Figure 14, where it uses two muscles.
15. All WAY-EEG-GAL series of a participant were recorded in one session, so stage 4 does not test new sessions. The detector's rest level comes from the first series of the same session.
16. In the WAY-EEG-GAL series with surface changes, the contact plates also record the experimenter handling the object between trials. Grip force is therefore taken only from just before first contact to just after release, using the dataset's event times.
17. The onsets of Figure 13 use a threshold of 3 SD over a short rest period before the cue (0.3 to 1 s). Activity before contact includes the reach and the shaping of the hand, so it cannot be attributed to the pinch alone.
18. The weight-change comparisons of Figure 15 rest on about 7 s of rising grip force per participant and case.

The repository is intended to demonstrate my experimental reasoning.
