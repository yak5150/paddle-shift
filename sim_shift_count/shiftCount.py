import pandas as pd

data = pd.read_csv('fsae_michigan18_&_madformulateam_mft02_evo_&_Yak_5150_&_stint_3.csv')

lap_group = data.groupby('Lap')

shifts_per_lap = {}

for lap, lap_data in lap_group:
    gear_column = lap_data['Gear']

    up_shifts = 0
    down_shifts = 0
    last_non_zero_gear = None
    for gear in gear_column:
        if gear != 0:
            if last_non_zero_gear is not None:
                if gear > last_non_zero_gear:
                    up_shifts += 1
                elif gear < last_non_zero_gear:
                    down_shifts += 1
            last_non_zero_gear = gear

    shifts_per_lap[lap] = {'up_shifts': up_shifts, 'down_shifts': down_shifts}

for lap, shifts in shifts_per_lap.items():
    print(f"Lap {lap}: {shifts['up_shifts']} upshifts - {shifts['down_shifts']} downshifts")