import os
import json
import random
import h5py
root = root = '/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran'
train_list_path = os.path.join(root, 'teamlab/file_name_split/train_list_control.json')
val_list_path = os.path.join(root,'teamlab/file_name_split/val_list_control.json')
test_list_path = os.path.join(root,'teamlab/file_name_split/test_list_control.json')

# balanced path
train_balanced_list_path = os.path.join(root, 'teamlab/file_name_split/train_balanced_list_control.json')
val_balanced_list_path = os.path.join(root,'teamlab/file_name_split/val_balanced_list_control.json')
test_balanced_list_path = os.path.join(root,'teamlab/file_name_split/test_balanced_list_control.json')

def create_balanced_dataset(in_path, out_path):
   with open(in_path) as f:
      imbalanced_list = json.load(f)
   drunk = []
   sober = []
   balanced_list = []

   for name in imbalanced_list:
      codes = [x for x in name]
      if codes[3] in ['1', '3']:
         drunk.append(name)
      else:
         sober.append(name)
   random.shuffle(drunk)
   random.shuffle(sober)
   for i in range(len(drunk)):
      balanced_list.append(drunk[i])
      balanced_list.append(sober[i])
   random.shuffle(balanced_list)
   print(f'len old list: {len(imbalanced_list)}')
   print(f'len balanced list: {len(balanced_list)}')

  
   with open(out_path, 'w') as f:
      json.dump(balanced_list, f, indent=4)

create_balanced_dataset(train_list_path, train_balanced_list_path)
create_balanced_dataset(val_list_path, val_balanced_list_path)
create_balanced_dataset(test_list_path, test_balanced_list_path)



        


