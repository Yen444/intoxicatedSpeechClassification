import json
import os
import random

def split_file_name(path_to_file_list):
    # load json list file
    with open(path_to_file_list, 'r') as f:
        file_list = json.load(f)
    # shuffle the list
    print(len(file_list))
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

    with open("/users/yentran/sum2023/teamlab/file_name_split/train_list.json", mode="w", encoding="utf8") as f:
        json.dump(train_list, f, indent=4)
    with open("/users/yentran/sum2023/teamlab/file_name_split/val_list.json", mode="w", encoding="utf8") as f:
        json.dump(val_list, f, indent=4)
    with open("/users/yentran/sum2023/teamlab/file_name_split/test_list.json", mode="w", encoding="utf8") as f:
        json.dump(test_list, f, indent=4)


split_file_name('/users/yentran/sum2023/teamlab/file_name_split/list_files.json')