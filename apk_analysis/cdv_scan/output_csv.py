"""
    Input: 
        a dictionary of apk names,
        a dictionary of apis,
        a dictionary of permissions,
        a dictionary of plugin_declaration,
        the output directory path
    Output: csv files
        cordova_API.csv
        cordova_PERMISSION.csv
        cordova_FEATURE.csv
        cordova_FEATURE.csv
        cordova_PLUGIN_DECLARATION.csv
"""
import pandas as pd
import copy
from pathlib import Path


def create_csv_dir(dir_output):
    # create directory for csv output if it not exists
    Path(dir_output).mkdir(parents=True, exist_ok=True)


def output_csv(d_apk_name, d_int_api, d_int_permission, d_plugin_declare_all, d_plugin_permission_declare_all, dir_output):
    # concate api and permission, and output as a csv file
    # Todo: add class(Benign 0; Malicious: 1) for each apk
    print_title("Output CSV file")
    create_csv_dir(dir_output)
    features = ["API", "PERMISSION", "FEATURE", "PLUGIN_DECLARATION", "PLUGIN_PERMISSION_DECLARATION"]
    for feature in features:
        output_csv_feature(
            d_apk_name, d_int_api, d_int_permission, d_plugin_declare_all, d_plugin_permission_declare_all, dir_output, feature
        )
    # d_apk_name = {'apk_name': [apk1, apk2, ...]}
    print(f"Total number of APKs: {len(list(d_apk_name.values())[0])}")    # first value


def output_csv_feature(d_apk_name, d_int_api, d_int_permission, d_plugin_declare_all, d_plugin_permission_declare_all, dir_output, feature):
    d_apk = copy.deepcopy(d_apk_name)
    # print three different types of files:
    # API, PERMISSION and FEATURE (API+PERMISSION)
    if feature in ["API", "FEATURE"]:
        d_apk.update(d_int_api)
    if feature in ["PERMISSION", "FEATURE"]:
        d_apk.update(d_int_permission)
    if feature == "PLUGIN_DECLARATION":
        d_apk.update(d_plugin_declare_all)
    if feature == "PLUGIN_PERMISSION_DECLARATION":
        d_apk.update(d_plugin_permission_declare_all)
    output_path = dir_output + f"cordova_{feature}.csv"
    output_csv_file(d_apk, output_path, f"{feature}")


def output_csv_file(d_apk, output_path, feature):
    # output a single file
    try:
        df_results = pd.DataFrame(data=d_apk)
        df_results.to_csv(output_path, index=False)
        # print(d_apk_name)
        print(f"Output Path: {output_path}")
        print(f"Total number of {feature}: {len(df_results.columns)-1}\n")

    except Exception as e:
        print(e)


def print_title(title=""):
    # print break line with title
    # ============== title =============
    total_len = 100
    if title:
        decoration = "#" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)
    else:
        print("#" * 101)