import audiofile
import opensmile
import os
import json
import pandas as pd

def extract_one_file(file):
    features_LLDs = []
    features_functionals = []
    signal, sampling_rate = audiofile.read(file, always_2d=True)
    smile_1 = opensmile.Smile(feature_set="/home/users1/tranti/TL/lib64/python3.10/site-packages/opensmile/core/config/compare/ComParE_2016.conf", feature_level='lld')
    lld = smile_1.process_signal(signal, sampling_rate)
    smile_2 = opensmile.Smile(feature_set="/home/users1/tranti/TL/lib64/python3.10/site-packages/opensmile/core/config/compare/ComParE_2016.conf", feature_level='func')
    func = smile_2.process_signal(signal, sampling_rate)
    for col in lld:
        features_LLDs.append(lld[col].tolist())
    for col in func:
        features_functionals.append(func[col].tolist())
    # return list of features with len(list) = 65 + 6 = 71 features
    return features_LLDs, features_functionals


def main():
    """lld, func = extract_one_file('/Users/yentran/sum2023/teamLab/ALC/ses1006/0061006015_h_00.wav')
    lld.to_csv('lld_feature_compare_more_mfcc.csv')
    func.to_csv('func_feature_compare_more_mfcc.csv')
    print(lld)"""
    data_path = '/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/data/ALC'
    feature_llds = {}
    feature_funcs = {}

    for root, dirs, files in os.walk(data_path):
      for file in files:
        if file.endswith('h_00.wav'):
            print(file)
            codes = [x for x in file]
            label = ''.join(codes[3])
            label = 1 if label in ['1', '3'] else 0
            section = ''.join(codes[3:7])
            speaker = ''.join(codes[:3])
            promt = ''.join(codes[7:10])
            lld_feature, func_feature = extract_one_file(os.path.join(root, file))
            feature_llds[file] = {'label': label,
                                  'speaker': speaker,
                                  'section': section,
                                  'promt': promt,
                                  'features': lld_feature}
            feature_funcs[file] = {'label': label,
                                  'speaker': speaker,
                                  'section': section,
                                  'promt': promt,
                                  'features': func_feature}

    print('finishing feature extraction')
    with open('/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/feature_compare_65/lld_feature_compare_65.json', 'w') as f_lld:
        json.dump(feature_llds, f_lld, indent=4)
    with open('/mount/arbeitsdaten/studenten1/team-lab-phonetics/2023/student_directories/tran/feature_compare_65/func_feature_compare_65.json', 'w') as f_func:
        json.dump(feature_funcs, f_func, indent=4)
if __name__ == "__main__":
    main()