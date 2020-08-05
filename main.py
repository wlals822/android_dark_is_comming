# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import re


android_dir = "/Users/user/Audio-Android/app/src/main/res/layout/"
colors_dir = "/Users/user/Audio-Android/app/src/main/res/values/colors.xml"
test_layout_name = "fragment_ranking.xml"
color_res_pattern = "(?<=@color/)[a-z,_, 0-9]*"


def open_layout_file():
    layout_file = open(android_dir + test_layout_name, "r")
    file_string = layout_file.read()
    reg_result = re.findall(color_res_pattern, file_string)
    print("layout have colors: {}".format(reg_result))
    return reg_result


# color 값이 직접 들어있는 경우만 찾을 수 있다.
def find_color(res_id):
    find_value_pattern = '(?<="{}">)#[a-z, 0-9]*'.format(res_id)
    color_file = open(colors_dir, "r").read()
    result = re.findall(find_value_pattern, color_file)
    if len(result) == 0:
        print("{}의 값은 이중 refernce입니다.".format(res_id))
    else:
        print("{}의 값은 {}입니다.".format(res_id, result))

def find_dark_color(color_code):



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target_keys = open_layout_file()
    for key in target_keys:
        find_color(key)

