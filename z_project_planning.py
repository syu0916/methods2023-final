import sys
import fileinput

def main():
    print("hello")

    pat_set = set()
    line_count = 0
    for patient in fileinput.input("../../0_data/synthea_covid_10k/patients.csv"):
        line_count += 1
        if line_count == 1:
            continue

        line_arr = patient.split(",")
        pat_set.add(line_arr[0])

    covid_map = {}
    line_count = 0
    for line in fileinput.input("../../0_data/synthea_covid_10k/careplans.csv"):
        line_count += 1
        if line_count == 1:
            continue

        line_arr = line.split(",")

        if line_arr[8].strip() == "COVID-19":
            covid_map[line_arr[3]] =  True
    print(covid_map)
    # print(pat_set)

    overlap = 0
    for key in covid_map.keys():
        if key in pat_set:
            overlap += 1

    print(f' size of covid map: {len(covid_map)} in comparison to number of patients: {len(pat_set)}')
    print(f'the amount of overlap is {overlap}')





main()