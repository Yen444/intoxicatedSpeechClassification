import json
import os
import numpy as np
import h5py

# split dataset into train, val, test set and convert to h5py -> lighter and easier to be loaded to pytorch dataset

def split_data(feature_set, dataset, name_list_file):
   root = '/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/teamlab'
   path_to_dataset = os.path.join(root, dataset)
   print(f'path to dataset: {path_to_dataset}')
   path_to_feature_set = os.path.join(root, feature_set)
   print(f'path to feature set: {path_to_feature_set}')
   path_to_split_name = os.path.join(root, name_list_file)
   print(f'path to split name: {path_to_split_name}')
   # load json dataset file
   with open(path_to_dataset, 'r') as f:
      dataset = json.load(f)
   # load json name list file
   train_list_path = os.path.join(path_to_split_name, 'train_list.json')
   val_list_path = os.path.join(path_to_split_name, 'val_list.json')
   test_list_path = os.path.join(path_to_split_name, 'test_list.json')
   """train_balanced_path = os.path.join(path_to_split_name, 'train_balanced_list_control.json')
   val_balanced_list_path = os.path.join(path_to_split_name, 'val_balanced_list_control.json')
   test_balanced_list_path = os.path.join(path_to_split_name, 'test_balanced_list_control.json')"""
   with open(train_list_path, 'r') as f:
      train_list = json.load(f)
   with open(val_list_path, 'r') as f:
      val_list = json.load(f)
   with open(test_list_path, 'r') as f:
      test_list = json.load(f)
   """with open(train_balanced_path, 'r') as f:
      train_balanced_list = json.load(f)
   with open(val_balanced_list_path, 'r') as f:
      val_balanced_list = json.load(f)
   with open(test_balanced_list_path, 'r') as f:
      test_balanced_list = json.load(f)"""
   # create train, val, test dict
   train_dict = {}
   val_dict = {}
   test_dict = {}
   train_balanced_dict = {}
   val_balanced_dict = {}
   test_balanced_dict = {}
   for i, file_name in enumerate(train_list):
      train_dict[file_name] = dataset[file_name]
   for i, file_name in enumerate(val_list):
      val_dict[file_name] = dataset[file_name]
   for i, file_name in enumerate(test_list):
      test_dict[file_name] = dataset[file_name]
   """for i, file_name in enumerate(train_balanced_list):
      train_balanced_dict[file_name] = dataset[file_name]
   for i, file_name in enumerate(val_balanced_list):
      val_balanced_dict[file_name] = dataset[file_name]
   for i, file_name in enumerate(test_balanced_list):
      test_balanced_dict[file_name] = dataset[file_name]"""
   
   # write to h5 file and store in corresponding feature set
   train_dict_path = os.path.join(path_to_feature_set, 'train_dict.h5')
   val_dict_path = os.path.join(path_to_feature_set, 'val_dict.h5')
   test_dict_path = os.path.join(path_to_feature_set, 'test_dict.h5')
   """train_balanced_dict_path = os.path.join(path_to_feature_set, 'train_balanced_dict.h5')
   val_balanced_dict_path = os.path.join(path_to_feature_set, 'val_balanced_dict.h5')
   test_balanced_dict_path = os.path.join(path_to_feature_set, 'test_balanced_dict.h5')"""
   
   with h5py.File(train_dict_path, 'w') as train_h5:
      train_h5.create_dataset("number_datasets", data=len(train_dict.keys()))
      for key_idx, key in enumerate(train_dict.keys()):
         value = train_dict[key]
         features = np.array(value['features'])
         label = int(value['label'])
         speaker = value["speaker"]
         promt = value["promt"]
         features = value['features']
         name = key
         grp = train_h5.create_group(f"dataset_{key_idx:07d}")
         grp.create_dataset("features", data=features)
         grp.create_dataset("label", data=label)
         grp.create_dataset("speaker", data=speaker)
         grp.create_dataset("promt", data=promt)
         grp.create_dataset("name", data=name)
   with h5py.File(val_dict_path, 'w') as val_h5:
      val_h5.create_dataset("number_datasets", data=len(val_dict.keys()))
      for key_idx, key in enumerate(val_dict.keys()):
         value = val_dict[key]
         features = np.array(value['features'])
         label = int(value['label'])
         speaker = value["speaker"]
         promt = value["promt"]
         features = value['features']
         name = key
         grp = val_h5.create_group(f"dataset_{key_idx:07d}")
         grp.create_dataset("features", data=features)
         grp.create_dataset("label", data=label)
         grp.create_dataset("speaker", data=speaker)
         grp.create_dataset("promt", data=promt)
         grp.create_dataset("name", data=name)
   with h5py.File(test_dict_path, 'w') as test_h5:
      test_h5.create_dataset("number_datasets", data=len(test_dict.keys()))
      for key_idx, key in enumerate(test_dict.keys()):
         value = test_dict[key]
         features = np.array(value['features'])
         label = int(value['label'])
         speaker = value["speaker"]
         promt = value["promt"]
         features = value['features']
         name = key
         grp = test_h5.create_group(f"dataset_{key_idx:07d}")
         grp.create_dataset("features", data=features)
         grp.create_dataset("label", data=label)
         grp.create_dataset("speaker", data=speaker)
         grp.create_dataset("promt", data=promt)
         grp.create_dataset("name", data=name)
   """with h5py.File(train_balanced_dict_path, 'w') as train_balanced_h5:
      train_balanced_h5.create_dataset("number_datasets", data=len(train_balanced_dict.keys()))
      for key_idx, key in enumerate(train_balanced_dict.keys()):
         value = train_balanced_dict[key]
         features = np.array(value['features'])
         label = int(value['label'])
         speaker = value["speaker"]
         promt = value["promt"]
         features = value['features']
         name = key
         grp = train_balanced_h5.create_group(f"dataset_{key_idx:07d}")
         grp.create_dataset("features", data=features)
         grp.create_dataset("label", data=label)
         grp.create_dataset("speaker", data=speaker)
         grp.create_dataset("promt", data=promt)
         grp.create_dataset("name", data=name)
   with h5py.File(test_balanced_dict_path, 'w') as test_balanced_h5:
      test_balanced_h5.create_dataset("number_datasets", data=len(test_balanced_dict.keys()))
      for key_idx, key in enumerate(test_balanced_dict.keys()):
         value = test_balanced_dict[key]
         features = np.array(value['features'])
         label = int(value['label'])
         speaker = value["speaker"]
         promt = value["promt"]
         features = value['features']
         name = key
         grp = test_balanced_h5.create_group(f"dataset_{key_idx:07d}")
         grp.create_dataset("features", data=features)
         grp.create_dataset("label", data=label)
         grp.create_dataset("speaker", data=speaker)
         grp.create_dataset("promt", data=promt)
         grp.create_dataset("name", data=name)
   with h5py.File(val_balanced_dict_path, 'w') as val_balanced_h5:
      val_balanced_h5.create_dataset("number_datasets", data=len(val_balanced_dict.keys()))
      for key_idx, key in enumerate(val_balanced_dict.keys()):
         value = val_balanced_dict[key]
         features = np.array(value['features'])
         label = int(value['label'])
         speaker = value["speaker"]
         promt = value["promt"]
         features = value['features']
         name = key
         grp = val_balanced_h5.create_group(f"dataset_{key_idx:07d}")
         grp.create_dataset("features", data=features)
         grp.create_dataset("label", data=label)
         grp.create_dataset("speaker", data=speaker)
         grp.create_dataset("promt", data=promt)
         grp.create_dataset("name", data=name)"""
   

# split for compare feature set 65 features
#split_data('feature_compare_65','feature_compare_65/lld_feature_compare_65.json', 'file_name_split')
# split for egemap feature set 41 features
split_data('feature_egemaps_41','feature_egemaps_41/lld_feature.json', 'file_name_split')
# split for compare feature set 41 features
#split_data('feature_compare_65','feature_egemaps_41/lld_feature.json', 'file_name_split')