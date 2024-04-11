import pandas as pd

data = pd.read_csv('fsae_michigan18_&_madformulateam_mft02_evo_&_Yak_5150_&_stint_3.csv')

grouped_data = data.groupby('Lap')

shifts_per_lap = {}

for lap, lap_data in grouped_data:
    shifts = sum(1 for i in range(1, len(lap_data)) if lap_data['Gear'].iloc[i] != lap_data['Gear'].iloc[i-1])
    shifts_per_lap[lap] = shifts

for lap, shifts in shifts_per_lap.items():
        print(f"Lap {lap}: {shifts} shifts")