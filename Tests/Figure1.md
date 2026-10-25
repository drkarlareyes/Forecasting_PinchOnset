![Figure 1: sEMG comes before force (T1)](figures/figure1.png)

The left panel shows an example press, comparing aggregate activity derived from 251 HD-sEMG electrodes with the measured change in finger force from rest.
The right panel zooms in on the beginning of the press to compare the timing of the two signals.

An onset was defined offline as the first point at which the respective signal remained above the rest noise threshold (rest mean + 5 standard deviations) for at least 50 ms.

- Trial 2: sEMG onset preceded force onset by 51 ms.
- Trial 1: The corresponding difference was 42 ms.

These observations suggest a measurable window of neuromuscular activity before the detected mechanical force onset. 
This is one reason short horizon forecasting may be possible and motivates testing whether the lead is repeatable across participants and contraction types.

However these are retrospective onset measurements from selected trials, not a real time forecasting result. 
The definition of onset and signal processing can influence the measured difference. 
Acquisition, filtering, inference, communication and actuation delays must be accounted for before claiming useful lead time for a robot.
