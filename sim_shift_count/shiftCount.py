import pandas as pd

data = pd.read_csv('fsae_michigan18_&_madformulateam_mft02_evo_&_Yak_5150_&_stint_3.csv')
data = data[data['Lap'] > 0]

gear_column = data['Gear']
time_column = data['Time [s]']

shifts = []
times = []

last_non_zero_gear = None
last_shift_time = 75.35

for i in range(len(gear_column)):
    gear = gear_column.iloc[i]
    time = time_column.iloc[i]

    if gear != 0:
        if last_non_zero_gear is not None:
            if gear > last_non_zero_gear:
                shifts.append(1)  # Upshift
            elif gear < last_non_zero_gear:
                shifts.append(0)  # Downshift
            if gear != last_non_zero_gear:
                # print(f"Gear: {gear}, Time: {time}, Last Gear: {last_non_zero_gear}, Last Shift Time: {last_shift_time}")
                times.append(time - last_shift_time)
                last_shift_time = time
        last_non_zero_gear = gear

Standard_Shifts = len(shifts)
Standard_Times = len(times)

Standard_Shift = ','.join(str(shift) for shift in shifts)
Standard_Time = ','.join(str(round(time, 2)) for time in times)

print("#define Standard_Shifts", Standard_Shifts)
print("#define Standard_Times", Standard_Times)
print("const int Standard_Shift[] = {", Standard_Shift, "};")
print("const float Standard_Time[] = {", Standard_Time, "};")