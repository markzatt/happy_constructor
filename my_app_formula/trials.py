

# # import pdfkit

#
# from collections import Counter
# #
# # electrode_type = 'Э50, Э50А'
# #
# # elec_type_dict = {'Э42, Э42А': 180,
# #                   'Э46, Э46А': 200,
# #                   'Э50, Э50А': 215,
# #                   'Э60': 240,
# #                   'Э70': 280,
# #                   }
# #
# # for k, v in elec_type_dict.items():
# #     if electrode_type == k:
# #         big_r_wf = v
# #         # elec_type_dict[electrode_type] =
# #         print(big_r_wf)
# #
# # # conf = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
# # # pdfkit.from_file('trail.html', 'hello.pdf', configuration=conf)
# #
# # # b = 18
# # # h = 25.6
# # # w_z = b * (h ** 2 / 6)
# # # print(w_z)
# # # a = (75 * 10 ** 3) / (w_z * 1 * 162)
# # # print(a)
# # # i_z = w_z / (h / 2)
# # # print(i_z)
# #
# # x = 0.7 * (20 ** 3 * 1 / 12 + 2 * 29 * 1 * ((20 + 1) / 2) ** 2)
# # y = 0.7 * (2 * (29 ** 3 * 1 / 12 + 29 * 1 * (29 / 2 - 11) ** 2) + 20 * 1 * (11 + 1 / 2) ** 2)
# # r = 2 * (29 ** 3 * 1 / 12 + 29 * 1 * (29 / 2 - 11) ** 2)
# # u = 20 * 1 * (11 + 1 / 2) ** 2
# # z = 0.7 * (r + u)
# # print(x) # 4775.3
# # print(u) # 2645.0
# # print(z) # 5194.2
# # B = 18
# # H = 25.6
# # b = 8.7
# # h = 24
# # Iz = B*H ** 3 / 12 - 2 * (b*h ** 3 / 12)
# #
# # f = (11**2+10**2)**0.5
# # print(f)
#
# a = "вились даже опасные мечтатели. Руководимые не столько разумом, сколько движениям"
# b = list(a)
# print(b)
# c = Counter(b)
# print(c)
# sum = 0
# for i in b:
#     sum+=1
# print (sum)

from my_app_formula.matirials_for_calculations import Welded_joints

electrode_type = 'Э42, Э42А'
steel_type = 'С235 от 2 до 20 мм'

instance_for_welded_joints = Welded_joints(electrode_type, steel_type)  # Экземпляр для выбора электродов и стали
big_r_wf = str(instance_for_welded_joints.big_r_wf())
big_r_un = str(instance_for_welded_joints.big_r_un())
print(big_r_wf)
print(big_r_un)


print(type(electrode_type))

x = 1
if type(x) != str:
    print ("it's a number")