def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] +=1
        else:
            count_dict[item] =1
    return count_dict
input_string = input("Nhập danh sách các từ , cách nhau bằng dấu cách:")
word_lis = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_lis)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)
       