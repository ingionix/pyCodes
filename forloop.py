
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
temps = week_temps_f.split(",")
sum_temps = 0.0
for temp in range(len(temps)):
    sum_temps += float(temps[temp])
sum_temps / len(temps)