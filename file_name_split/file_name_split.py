import json
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd

np.random.seed(0)
def split_file_name(path_to_file_list):
    # load json list file
    file_list = []
    with open(path_to_file_list, 'r') as f:
        full_list = json.load(f)
    # shuffle the list
    for name in full_list:
        codes = [x for x in name]
        label = ''.join(codes[3])
        if label in ['1', '2', '3', '4']:
            file_list.append(name)
    
    with open("/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/final_list_file.json", mode="w", encoding="utf8") as f:
        json.dump(file_list, f, indent=4)

    print(f'len old list with control: {len(full_list)}')
    print(f'len final list without control: {len(file_list)}')
    random.shuffle(file_list)
    # calculate the number of samples for each split
    num_samples = len(file_list)
    num_train = int(num_samples * 0.8)
    num_val = int(num_samples * 0.1)
    
    # create three new list for training, validation, and testing
    train_list = list()
    val_list = list()
    test_list = list()
    # iterate over the shuffled keys and add each key-value pair to the appropriate dictionary
    for i, key in enumerate(file_list):
        if i < num_train:
            train_list.append(key)
        elif i < num_train + num_val:
            val_list.append(key)
        else:
            test_list.append(key)

    with open("/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/train_list.json", mode="w", encoding="utf8") as f:
        json.dump(train_list, f, indent=4)
    with open("/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/val_list.json", mode="w", encoding="utf8") as f:
        json.dump(val_list, f, indent=4)
    with open("/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/test_list.json", mode="w", encoding="utf8") as f:
        json.dump(test_list, f, indent=4)
    
    print(f'len train list: {len(train_list)}')
    print(f'len val list: {len(val_list)}')
    print(f'len test list: {len(test_list)}')

def split_file_name_with_control(path_to_file_list):
    # load json list file
    with open(path_to_file_list, 'r') as f:
        full_list = json.load(f)
    # shuffle the list

    print(f'len old list with control: {len(full_list)}')
    random.shuffle(full_list)
    # calculate the number of samples for each split
    num_samples = len(full_list)
    num_train = int(num_samples * 0.8)
    num_val = int(num_samples * 0.1)
    
    # create three new list for training, validation, and testing
    train_list_control = list()
    val_list_control = list()
    test_list_control = list()
    # iterate over the shuffled keys and add each key-value pair to the appropriate dictionary
    for i, key in enumerate(full_list):
        if i < num_train:
            train_list_control.append(key)
        elif i < num_train + num_val:
            val_list_control.append(key)
        else:
            test_list_control.append(key)

    with open("/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/train_list_control.json", mode="w", encoding="utf8") as f:
        json.dump(train_list_control, f, indent=4)
    with open("/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/val_list_control.json", mode="w", encoding="utf8") as f:
        json.dump(val_list_control, f, indent=4)
    with open("/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/test_list_control.json", mode="w", encoding="utf8") as f:
        json.dump(test_list_control, f, indent=4)
    
    print(f'len train list: {len(train_list_control)}')
    print(f'len val list: {len(val_list_control)}')
    print(f'len test list: {len(test_list_control)}')

def read_table(file='/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/data/ALC/TABLE/SESSEXT.TBL'):
    data_frame = pd.read_table(file)
    speakers = data_frame['SCD'].tolist()
    sex = data_frame['SEX'].tolist()
    states = data_frame['ACC'].tolist()
    ages = data_frame['AGE'].tolist()
    
    correct_speaker = {'596': 7, '507': 12, '048': 6, '513': 10, '591': 7, '534': 8, '549': 7, '038': 11, '550': 5, '022': 8, '006': 6, '563': 17, '041': 8, '071': 9, '025': 8, '090': 6, '554': 5, '526': 5, '061': 7, '013': 6, '517': 6, '039': 6, '078': 14, '046': 5, '080': 9, '570': 6, '034': 9, '059': 7, '574': 9, '546': 6, '037': 5, '520': 10, '007': 8, '515': 9, '502': 8, '558': 6, '101': 7, '583': 5, '542': 6, '077': 5, '552': 10, '518': 12, '536': 8, '072': 6, '531': 4, '020': 5, '568': 8, '582': 6, '537': 6}
    a_c_states = []
    a_c_sex = []
    for key, val in correct_speaker.items():
        idx = speakers.index(int(key))
        state = states[idx]
        s = sex[idx]
        a_c_states.append(state)
        a_c_sex.append(s)
    print({i:a_c_states.count(i) for i in set(a_c_states)})
    print({i:a_c_sex.count(i) for i in set(a_c_sex)})
def extract_control():
    path_to_file_list = '/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/list_files.json'
    control_list = []
    with open(path_to_file_list, 'r') as f:
        full_list = json.load(f)
    # shuffle the list
    for name in full_list:
        codes = [x for x in name]
        label = ''.join(codes[3])
        if label in ['5', '6']:
            control_list.append(name)
    print(len(control_list))
    with open('/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/control_list_only.json', 'w') as f:
        json.dump(control_list, f, indent=4)

def count_data(list_file):
    with open(list_file, "r") as f:
        list = json.load(f)
    drunk = 0
    sober = 0
    read_a = ['001','003', '004', '006', '007', '008','009', '011', '012', '013', '015', '016', '017', '019','020','021','023','024','029','030'] #read numbers, address, words, sentences, credit card numbers, auto numbers
    spontaneous_a = ['002', '014', '005','010','018'] # talk about holiday (dialogues, mono)
    command_control_a = ['022','025','026','027','028'] #tell a story basing on picture, talk with leiter about that picture, gien a situation and give instruction for sb to do sth

    read_na = ['001','003','004','006','007','008','009','011','012','013','015', '016', '017', '019','020','021','023','024','026','027','028', '031','032','033','035','036','037','039','040','041','044','050','051','052','056','057','058','059','060']
    spontaneous_na = ['002','014','022','034', '005', '010', '018','025','030','038'] #experience Trinkversuch
    command_control_na = ['042','043','045','046','047','048','049','053','054','055']
    
    promt_dict = {'read': 0, 'spontaneous':0, 'command_control':0}
    promt_dict_a = {'read': 0, 'spontaneous':0, 'command_control':0}
    promt_dict_na = {'read': 0, 'spontaneous':0, 'command_control':0}

    speakers = []
    for name in list:
        codes = [x for x in name]
        promt = ''.join(codes[7:10])
        speaker = ''.join(codes[:3])
        speakers.append(speaker)
        sec = codes[3]
        if sec in ['1','3']:
            drunk += 1
            if promt in read_a:
                promt_dict['read'] += 1
                promt_dict_a['read'] += 1
            elif promt in spontaneous_a:
                promt_dict['spontaneous'] += 1
                promt_dict_a['spontaneous'] += 1
            else:
                promt_dict['command_control'] += 1
                promt_dict_a['command_control'] += 1
        else:
            sober += 1
            if promt in read_na:
                promt_dict['read'] += 1
                promt_dict_na['read'] += 1
            elif promt in spontaneous_na:
                promt_dict['spontaneous'] += 1
                promt_dict_na['spontaneous'] += 1
            else:
                promt_dict['command_control'] += 1
                promt_dict_na['command_control'] += 1
    speaker_dict = {i: speakers.count(i) for i in set(speakers)}
    return drunk, sober, promt_dict, promt_dict_a, promt_dict_na, speaker_dict



#split_file_name_with_control('/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/list_files.json')
#split_file_name('/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/final_list_file.json')
"""drunk, sober, promt_dict, promt_dict_a, promt_dict_na, speaker_dict = count_data('/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab/file_name_split/test_list_control.json')
print(drunk)
print(sober)
print(promt_dict)
print(promt_dict_a)
print(promt_dict_na)
print(len(speaker_dict))"""
#extract_control()
read_table()

