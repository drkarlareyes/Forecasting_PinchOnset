![Figure 3: Calibration Calibration: steady versus changing force (T5)](../figures/figure4.png)

From a calibration trial, an equal number of labeled samples was selected from steady force, changing force or mixed segments. 
The two tested calibration budgets were approximately 5.8 s and 2.1 s. 
Model fitting was done on one trial and evaluated on the other, in both directions.

(a) examines how the goodness of fit changes when the assumed EMG to force delay varies from 0 to 150 ms. 
(b) shows prediction performance (R²) on the independent trial using different calibration sample selections.

The figure shows that there is delay identifiability: With steady force samples, the fit varied by only about 0.035 R² across candidate delays. 
Changing-force samples produced a more pronounced variation of approximately 0.16–0.25 R².

Steady samples gave R² = 0.65 and 0.79, compared with 0.56 and 0.70 from changing force samples. 
Mixed samples gave 0.70 and 0.78 across the two directions.

Steady-force samples can provide a useful estimate of force magnitude, 
while changing force samples help constrain temporal parameters.
This motivates testing short mixed protocols rather than assuming that ramps alone are optimal.

The limitation is that samples were selected retrospectively from existing recordings; 
these are not separately collected, user guided calibration sessions. 
