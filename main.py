import pymorphy2
import json


class Mess:
    def __init__(self):
        self.sort = ''
        self.time_create = None


morph = pymorphy2.MorphAnalyzer()
str = ''

with open("dataset_hack.json", "r") as write_file:
    str = write_file.read()


def serealize_data(mass_js):
    mass_retern = []
    for mes in mass_js:
        mes_arr = mes.split()
        # print(mes_arr)
        mass_retern.append(mes_arr)
    return mass_retern


zn_pr = [",", ".", "/", "?", "!", "-", ":", "(", ")"]


def del_zn_pripen(mass):
    morph = pymorphy2.MorphAnalyzer()
    ret_array = []
    for char in mass:
        if char[-1] in zn_pr:
            buf = char[0:-1]
            ret_array.append(morph.parse(buf)[0].normal_form)
        elif char[0] in zn_pr:
            buf = char[1:]
            ret_array.append(morph.parse(buf)[0].normal_form)
        else:
            ret_array.append(morph.parse(char)[0].normal_form)
            continue

    return ret_array


json_format = json.JSONDecoder()
js = json_format.decode(str)

array_mess = []
for mes in js:
    array_mess.append(mes['message'])
buf = []
array1 = serealize_data(array_mess)
array2 = []
for ar in array1:
    array2 = del_zn_pripen(ar)
    buf.append(array2)
print(buf)


# buf - массив с данными
# _____________________________________________

деньги_категория = 0

confirmed_категория = 0
confirmed_деньги_категория = 0
cancelled_категория = 0
cancelled_деньги_категория = 0
sorted_категория = 0
sorted_деньги = 0
lost_категории = 0
lost_зависли_деньги_категория = 0
refunding_категория = 0
refunding_деньги_категория = 0
started_категория = 0
started_деньги_категоория = 0
started_ПР_категория = 0
submitted_категория = 0
submitted_деньги_категория = 0
rejected_категория = 0
rejected_ПР_катешгория = 0
rejected_деньги_категория = 0


