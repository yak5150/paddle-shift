import pandas as pd

data = pd.read_csv('fsae_michigan18_&_madformulateam_mft02_evo_&_Yak_5150_&_stint_3.csv')
data = data[data['Lap'] > 0]

lap_group = data.groupby('Lap')

shifts = []
times = []

for lap, lap_data in lap_group:
    gear_column = lap_data['Gear']
    time_column = lap_data['Time']
    lap_shifts = []
    lap_times = []

    last_non_zero_gear = None
    last_shift_time = 0.0

    for gear in gear_column:
        if gear != 0:
            if last_non_zero_gear is not None:
                if gear > last_non_zero_gear:
                    lap_shifts.append(1)
                elif gear < last_non_zero_gear:
                    lap_shifts.append(0)
                lap_times.append(last_shift_time)
                last_shift_time = 0.0
            last_non_zero_gear = gear
        else:
            last_shift_time += 0.05 #sampling frequency

    shifts.extend(lap_shifts)
    times.extend(lap_times)

Standard_Shifts = len(shifts)
Standard_Times = len(times)

Standard_Shift = ','.join(str(shift) for shift in shifts)
Standard_Time = ','.join(str(time) for time in times)

print("#define Standard_Shifts", Standard_Shifts)
print("#define Standard_Times", Standard_Times)
print("const int Standard_Shift[] = {", Standard_Shift, "};")
print("const float Standard_Time[] = {", Standard_Time, "};")