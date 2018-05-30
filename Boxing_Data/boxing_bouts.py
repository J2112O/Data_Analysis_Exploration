#!/usr/bin/python3.6
import csv


def main():
    '''
    file = ('clean_bouts_out.csv')
    with open(file, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        data_set = [row for row in csv_reader]
        print(data_set[2])

    path = r'/home/bigdaddy/Practice_Data/bouts_out_new.csv'
    with open(path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        data_set = []
        new_file = open('clean_bouts_out.csv', 'w')
        writer = csv.writer(new_file)
        for row in csv_reader:
            if any(row in (None, "") for row in csv_reader):
                writer.writerow(Null)
        age_A = int(row[0])
        age_B = int(row[1])
        height_A = int(row[2])
        height_B = int(row[3])
        reach_A = int(row[4])
        reach_B = int(row[5])
        stance_A = str(row[6])
        stance_B = str(row[7])
        weight_A = int(row[8])
        weight_B = int(row[9])
        won_A = int(row[10])
        won_B = int(row[11])
        lost_A = int(row[12])
        lost_B = int(row[13])
        drawn_A = int(row[14])
        drawn_B = int(row[15])
        kos_A = int(row[16])
        kos_B = int(row[17])
        result = str(row[18])
        decision = str(row[19])
        judge1_A = int(row[20])
        judge1_B = int(row[21])
        judge2_A = int(row[22])
        judge2_B = int(row[23])
        judge3_A = int(row[24])
        judge3_B = int(row[25])
        data_set.append([age_A, age_B, height_A, height_B, reach_A, reach_B, stance_A, stance_B, weight_A, weight_B, won_A, won_B, lost_A, lost_B, drawn_A, drawn_B, kos_A, kos_B, result, decision, judge1_A, judge1_B, judge2_A, judge2_B, judge3_A, judge3_B])

    new_file = open('clean_bouts_out.csv', 'w')
    writer = csv.writer(new_file)
    writer.writerow(["age_A", "age_B", "height_A", "height_B", "reach_A", "reach_B", "stance_A", "stance_B", "weight_A", "weight_B", "won_A", "won_B", "lost_A", "lost_B", "drawn_A", "drawn_B", "kos_A", "kos_B", "result", "decision", "judge1_A", "judge1_B", "judge2_A", "judge2_B", "judge3_A", "judge3_B"])
    for i in range(len(data_set)):
        clean_row = data_set[i]
        clean_age_A = clean_row[0]
        clean_age_B = clean_row[1]
        clean_height_A = clean_row[2]
        clean_height_B = clean_row[3]
        clean_reach_A = clean_row[4]
        clean_reach_B = clean_row[5]
        clean_stance_A = clean_row[6]
        clean_stance_B = clean_row[7]
        clean_weight_A = clean_row[7]
        clean_weight_B = clean_row[9]
        clean_won_A = clean_row[10]
        clean_won_B = clean_row[11]
        clean_lost_A = clean_row[12]
        clean_lost_B = clean_row[13]
        clean_drawn_A = clean_row[14]
        clean_drawn_B = clean_row[15]
        clean_kos_A = clean_row[16]
        clean_kos_B = clean_row[17]
        clean_result = clean_row[18]
        clean_decision = clean_row[19]
        clean_judge1_A = clean_row[20]
        clean_judge1_B = clean_row[21]
        clean_judge2_A = clean_row[22]
        clean_judge2_B = clean_row[23]
        clean_judge3_A = clean_row[24]
        clean_judge3_B = clean_row[25]
        writer.writerow([clean_age_A, clean_age_B, clean_height_A, clean_height_B, clean_reach_A, clean_reach_B, clean_stance_A, clean_stance_B, clean_weight_A, clean_weight_B, clean_won_A, clean_won_B, clean_lost_A, clean_lost_B, clean_drawn_A, clean_drawn_B, clean_kos_A, clean_kos_B, clean_result, clean_decision, clean_judge1_A, clean_judge1_B, clean_judge2_A, clean_judge2_B, clean_judge3_A, clean_judge3_B])
'''


if __name__ == '__main__':
    main()
