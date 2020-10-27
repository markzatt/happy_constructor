class Formula_for_metal_seam_perpendicular_to_the_seam:
    """Расчет прочности сварного соединения по металлу шва - момент перпендикулярен плоскости шва"""

    def __init__(self, big_b_f: float, h_w: float, t_w: float, b_f: float, h: float, big_m: float, big_r_wf: float,
                 gamma_c: float, k_f: float, big_b_z: float, big_r_un: float) -> float:
        self.k_f = k_f
        self.big_b_f = big_b_f
        self.h_w = h_w
        self.t_w = t_w
        self.b_f = b_f
        self.h = h
        self.big_m = big_m
        self.big_r_wf = big_r_wf
        self.gamma_c = gamma_c
        self.big_b_z = big_b_z
        self.big_r_un = big_r_un

    def big_i_f(self) -> float:
        big_i_f = float(self.big_b_f) * (
                (2 * float(self.h_w) ** 3 * float(self.k_f) / 12) + 2 * float(self.b_f) * float(self.k_f) * (
                (float(self.h) + float(self.k_f)) / 2) ** 2 + 2 * (float(self.b_f) - float(self.t_w)) * float(
            self.k_f) * ((float(self.h_w) - float(self.k_f)) / 2) ** 2)
        return round(big_i_f, 1)

    def y_max(self) -> float:
        """Расчитывает значение y_max"""
        y_max = float(self.h) / 2 + float(self.k_f)
        return y_max

    def big_w_f(self) -> float:
        """Расчитывает значение big_w_f"""
        big_w_f = float(self.big_i_f()) / float(self.y_max())
        return round(big_w_f, 1)

    def tau_f(self) -> float:
        """Расчитывает значение tau_f"""
        tau_f = float(self.big_m) * 10 ** 3 / float(self.big_w_f())
        return round(tau_f, 1)

    def inequality(self):
        """Расчитывает отношение tau_f к big_r_wf"""
        inequality = float(self.tau_f()) / float(self.big_r_wf)
        return round(inequality, 1)

    def main_condition(self):
        """Расчет главной формулы big_m/(big_w_f*big_r_wf*gamma_c)"""
        value = (float(self.big_m) * 10 ** 3 / (float(self.big_w_f()) * float(self.big_r_wf)) * float(self.gamma_c))
        return round(value, 1)

    def main_notation(self):
        """Условие, что результат главной формулы должен быть <= 1"""
        if float(self.main_condition()) <= 1:
            main_notation = 'выполняется! Прочность по металлу шва достаточна!'
        else:
            main_notation = 'не выполняется! Электроды (либо высота катета) выбраны неверно!'
        return main_notation

    def big_r_wz(self) -> float:
        """Расчет значения big_r_wz"""
        big_r_wz = 0.45 * float(self.big_r_un)
        return round(big_r_wz, 1)

    def condition1(self):
        """Условие для выбора электродов для механизированной сварки для стали до 285 Н/мм2"""
        if float(self.big_r_wf) > float(self.big_r_wz()):
            notation1 = 'выполняется!'
        else:
            notation1 = 'не выполняется! Электроды выбраны неверно!'
        return notation1

    def condition2(self):
        """Условие для выбора электродов для ручной сварки для стали до 285 Н/мм2"""
        if 1.1 * float(self.big_r_wz()) <= float(self.big_r_wf) <= float(self.big_r_wz()) * float(
                self.big_b_z) / float(self.big_b_f):
            notation2 = 'выполняется!'
        else:
            notation2 = 'не выполняется! Электроды выбраны неверно!'
        return notation2

    def condition2_calc1(self):
        """Расчет значения для condition2 для подстановки значения в текст отчета"""
        cond2_res1 = 1.1 * float(self.big_r_wz())
        return round(cond2_res1, 1)

    def condition2_calc2(self):
        """Расчет значения для condition2 для подстановки значения в текст отчета"""
        cond2_res2 = float(self.big_r_wz()) * float(self.big_b_z) / float(self.big_b_f)
        return round(cond2_res2, 1)

    def condition3(self):
        """Условие для выбора электродов для сварки для стали свыше 285 Н/мм2"""
        if float(self.big_r_wz()) <= float(self.big_r_wf) <= float(self.big_r_wz()) * float(self.big_b_z) / float(
                self.big_b_f):
            notation3 = 'выполняется!'
        else:
            notation3 = 'не выполняется! Электроды выбраны неверно!'
        return notation3

    def condition4(self):
        """Расчет отношения для выбора сечения для расчетов(металл шва или граница сплавления)"""
        cond4_res = (float(self.big_b_f) * float(self.big_r_wf)) / (float(self.big_b_z) * float(self.big_r_wz()))
        return round(cond4_res, 1)

    def check_katet(self):
        """Расчет оптимальной высоты катета шва"""
        k_f = 1
        big_i_f = float(self.big_b_f) * (
                (2 * float(self.h_w) ** 3 * float(k_f) / 12) + 2 * float(self.b_f) * float(k_f) * (
                (float(self.h) + float(k_f)) / 2) ** 2 + 2 * (float(self.b_f) - float(self.t_w)) * float(
            k_f) * ((float(self.h_w) - float(k_f)) / 2) ** 2)
        y_max = float(self.h) / 2 + float(k_f)
        big_w_f = float(big_i_f) / float(y_max)
        tau_f = float(self.big_m) * 10 ** 3 / float(big_w_f)
        katet_height = float(tau_f) / float(self.big_r_wf)
        return round(katet_height, 1)

    def check_main_condition(self):
        """Проверка условия главной формулы при подстановке оптимальной высоты катета шва"""
        k_f = float(self.check_katet())
        big_i_f = float(self.big_b_f) * (
                (2 * float(self.h_w) ** 3 * float(k_f) / 12) + 2 * float(self.b_f) * float(k_f) * (
                (float(self.h) + float(k_f)) / 2) ** 2 + 2 * (float(self.b_f) - float(self.t_w)) * float(
            k_f) * ((float(self.h_w) - float(k_f)) / 2) ** 2)
        y_max = float(self.h) / 2 + float(k_f)
        big_w_f = float(big_i_f) / float(y_max)
        check_main_condition = (
                float(self.big_m) * 10 ** 3 / (float(big_w_f) * float(self.big_r_wf)) * float(self.gamma_c))
        return round(check_main_condition, 1)

    def check_main_notation(self):
        """Исходя из расчетов check_main_condition выдает заключение о соответствии условию главной формулы"""
        if float(self.check_main_condition()) <= 1:
            check_main_notation = 'выполняется! Прочность по металлу шва достаточна!'
        else:
            check_main_notation = 'не выполняется! Электроды (либо высота катета) выбраны неверно!'
        return check_main_notation


# Экземпляр класса
a = Formula_for_metal_seam_perpendicular_to_the_seam(big_b_f=0.9, h_w=24, t_w=0.6, b_f=18, h=25.6, big_m=75,
                                                     big_r_wf=215, gamma_c=1,
                                                     k_f=1, big_b_z=0.9, big_r_un=360)


# print(a.big_i_f())
# print(a.y_max())
# print(a.big_w_f())
# print(a.tau_f())
# print(a.inequality())
# print(a.main_condition())
# print(a.condition2())
# print(a.big_r_wz())
# print(a.check_katet())

# class Formula_for_fusion_border:
#     """Расчет сварного соединения по границе сплавления"""
#
#     def __init__(self, big_b_z: float, h_w: float, t_w: float, h: float, big_m: float, big_r_wz: float,
#                  gamma_c: float, k_f: float) -> float:
#         self.k_f = k_f
#         self.big_b_z = big_b_z
#         self.h_w = h_w
#         self.t_w = t_w
#
#         self.h = h
#         self.big_m = big_m
#         self.big_r_wz = big_r_wz
#         self.gamma_wz = gamma_wz
#         self.gamma_c = gamma_c
#
#     def big_i_z(self) -> float:
#         big_i_z = float(self.big_b_z) * (
#                 (2 * float(self.h_w) ** 3 * float(self.k_f) / 12) + 2 * float(self.b_z) * float(self.k_f) * (
#                 (float(self.h) + float(self.k_f)) / 2) ** 2 + 2 * (float(self.b_z) - float(self.t_w)) * float(
#             self.k_f) * (
#                         (float(self.h_w) - float(self.k_f)) / 2) ** 2)
#         return big_i_z
#
#     def y_max(self) -> float:
#         y_max = float(self.h) / 2 + float(self.k_f)
#         return y_max
#
#     def big_w_z(self) -> float:
#         big_w_z = float(self.big_i_z()) / float(self.y_max())
#         return big_w_z
#
#     def tau_z(self) -> float:
#         tau_z = float(self.big_m) * 10 ** 3 / float(self.big_w_z())
#         return tau_z
#
#     def inequality(self):
#         inequality = float(self.tau_z()) / float(self.big_r_wz) * float(self.gamma_wz) * float(self.gamma_c)
#
#         return inequality
#
#
# a = Formula_for_fusion_border(big_b_z=0.9, h_w=24, t_w=0.6, b_z=18, h=25.6, big_m=75, big_r_wz=215, gamma_c=1,
#                               gamma_wz=1, k_f=1)
# # print(a.big_i_z())
# # print(a.y_max())
# # print(a.big_w_z())
# # print(a.tau_z())
# # print(a.inequality())

class Formula_for_metal_seam_in_the_plane_of_the_seam:
    """Расчет прочности сварного соединения по металлу шва - момент в плоскости шва"""

    def __init__(self, big_b_f: float, big_m: float, big_r_wf: float,
                 gamma_c: float, k_f: float, big_b_z: float, big_r_un: float, l_1: float, l_2: float) -> float:
        self.k_f = k_f
        self.big_b_f = big_b_f
        self.big_m = big_m
        self.big_r_wf = big_r_wf
        self.gamma_c = gamma_c
        self.big_b_z = big_b_z
        self.big_r_un = big_r_un
        self.l_1 = l_1
        self.l_2 = l_2

    def big_r_wz(self) -> float:
        """Расчет значения big_r_wz"""
        big_r_wz = 0.45 * float(self.big_r_un)
        return round(big_r_wz, 1)

    def condition4(self):
        """Расчет отношения для выбора сечения для расчетов(металл шва или граница сплавления)"""
        cond4_res = (float(self.big_b_f) * float(self.big_r_wf)) / (float(self.big_b_z) * float(self.big_r_wz()))
        return round(cond4_res, 1)

    def x_c(self):
        """Расчет значения центра тяжести периметра швов по оси х"""
        x_c = (float(self.l_1) ** 2 - 0.5 * float(self.l_2) * float(self.k_f)) / (2 * float(self.l_1) + float(self.l_2))
        return round(x_c, 0)

    def point_a_coordinate_x(self):
        """Расчет координаты точки А по оси х """
        x_a = float(self.l_1) - float(self.x_c())
        return round(x_a, 1)

    def point_a_coordinate_y(self):
        """Расчет координаты точки А по оси у"""
        y_a = float(self.l_2) / 2
        return round(y_a, 1)

    def l_1_minus_10mm(self):
        """Коррекция длинны шва на 10 мм, согласно СНИП"""
        correction = float(self.l_1) - 1
        return round(correction, 1)

    def big_i_fx(self):
        """Расчет значения Ifx"""
        big_i_fx = float(self.big_b_f) * (
                float(self.l_2) ** 3 * float(self.k_f) / 12 + 2 * float(self.l_1_minus_10mm()) * float(self.k_f) * (
                (float(self.l_2) + float(self.k_f)) / 2) ** 2)
        return round(big_i_fx, 1)

    def big_i_fy(self):
        """Расчет значения Ify"""
        big_i_fy = float(self.big_b_f) * (2 * (float(self.l_1_minus_10mm()) ** 3 * float(self.k_f) / 12 +
                                               float(self.l_1_minus_10mm()) * float(self.k_f) * (
                                                       float(self.l_1_minus_10mm()) / 2 -
                                                       float(self.x_c())) ** 2) + float(self.l_2) * float(
            self.k_f) * (float(self.x_c()) + float(self.k_f)
                         / 2) ** 2)
        return round(big_i_fy, 1)

    def length_from_x_c_to_a(self):
        """Расчет расстояния от Хц до точки А"""
        length_from_x_c_to_a = (float(self.point_a_coordinate_x()) ** 2 + float(
            self.point_a_coordinate_y()) ** 2) ** 0.5
        return round(length_from_x_c_to_a, 1)

    def main_condition(self):
        """Расчет главной формулы big_m/(big_w_f*big_r_wf*gamma_c)"""
        value = float(self.big_m) * 10 ** 3 * float(self.length_from_x_c_to_a()) / ((
                                                                                            float(
                                                                                                self.big_i_fx()) + float(
                                                                                        self.big_i_fy())) * float(
            self.big_r_wf) * float(self.gamma_c))
        return round(value, 1)

    def main_notation(self):
        """Условие, что результат главной формулы должен быть <= 1"""
        if float(self.main_condition()) <= 1:
            main_notation = 'выполняется! Прочность по металлу шва достаточна!'
        else:
            main_notation = 'не выполняется! Электроды (либо высота катета) выбраны неверно!'
        return main_notation

    def tau_f(self):
        """Расчет напряжения в шве"""
        tau_f = float(self.big_m) * 10 ** 3 * float(self.length_from_x_c_to_a()) / (float(self.big_i_fx()) + float(
            self.big_i_fy()))
        return round(tau_f, 0)

    def relation_tau_f_to_big_r_wf(self):
        """Расчет отношения напряжения в шве к сопротивлению шва"""
        relation_tau_f_to_big_r_wf = float(self.tau_f()) / float(self.big_r_wf)
        return round(relation_tau_f_to_big_r_wf, 1)

    def check_katet(self):
        """Определение оптимальной высоты катета шва"""
        k_f = 1
        x_c = (float(self.l_1) ** 2 - 0.5 * float(self.l_2) * float(k_f)) / (2 * float(self.l_1) + float(self.l_2))
        x_a = float(self.l_1) - float(x_c)
        y_a = float(self.l_2) / 2
        length_from_x_c_to_a = (float(x_a) ** 2 + float(y_a) ** 2) ** 0.5
        big_i_fx = float(self.big_b_f) * (
                float(self.l_2) ** 3 * float(k_f) / 12 + 2 * float(self.l_1_minus_10mm()) * float(k_f) * (
                (float(self.l_2) + float(k_f)) / 2) ** 2)

        big_i_fy = float(self.big_b_f) * (2 * (float(self.l_1_minus_10mm()) ** 3 * float(k_f) / 12 +
                   float(self.l_1_minus_10mm()) * float(k_f) * (float(self.l_1_minus_10mm()) / 2 -
                   float(x_c) ** 2) + float(self.l_2) * float(k_f) * (float(x_c) + float(k_f) / 2) ** 2))

        tau_f = float (self.big_m) * 10 ** 3 * float(length_from_x_c_to_a) / (float(big_i_fx) + float(big_i_fy))

        check_katet = (float(tau_f)/ float(self.big_r_wf)) + 0.01
        return round(check_katet, 1)

    def check_main_condition(self):
        """Проверка условия главной формулы при подстановке оптимальной высоты катета шва"""
        k_f = float(self.check_katet())
        x_c = (float(self.l_1) ** 2 - 0.5 * float(self.l_2) * float(k_f)) / (2 * float(self.l_1) + float(self.l_2))
        x_a = float(self.l_1) - float(x_c)
        y_a = float(self.l_2) / 2
        length_from_x_c_to_a = (float(x_a) ** 2 + float(y_a) ** 2) ** 0.5
        big_i_fx = float(self.big_b_f) * (
                float(self.l_2) ** 3 * float(k_f) / 12 + 2 * float(self.l_1_minus_10mm()) * float(k_f) * (
                (float(self.l_2) + float(k_f)) / 2) ** 2)
        big_i_fy = float(self.big_b_f) * (2 * (float(self.l_1_minus_10mm()) ** 3 * float(k_f) / 12 +
                                               float(self.l_1_minus_10mm()) * float(k_f) * (
                                                       float(self.l_1_minus_10mm()) / 2 - float(
                                                   x_c)) ** 2) + float(self.l_2) * float(k_f) * (
                                                  float(x_c) + float(k_f) / 2) ** 2)
        check_main_condition = float(self.big_m) * 10 ** 3 * float(length_from_x_c_to_a) / ((
                    float(big_i_fx) + float(big_i_fy)) * float(self.big_r_wf) * float(self.gamma_c))
        return round(check_main_condition, 1)

    def check_main_notation(self):
        """Исходя из расчетов check_main_condition выдает заключение о соответствии условию главной формулы"""
        if float(self.check_main_condition()) <= 1:
            check_main_notation = 'выполняется! Прочность по металлу шва достаточна!'
        else:
            check_main_notation = 'не выполняется! Электроды (либо высота катета) выбраны неверно!'
        return check_main_notation

    def condition1(self):
        """Условие для выбора электродов для механизированной сварки для стали до 285 Н/мм2"""
        if float(self.big_r_wf) > float(self.big_r_wz()):
            notation1 = 'выполняется!'
        else:
            notation1 = 'не выполняется! Электроды выбраны неверно!'
        return notation1

    def condition2(self):
        """Условие для выбора электродов для ручной сварки для стали до 285 Н/мм2"""
        if 1.1 * float(self.big_r_wz()) <= float(self.big_r_wf) <= float(self.big_r_wz()) * float(
                self.big_b_z) / float(self.big_b_f):
            notation2 = 'выполняется!'
        else:
            notation2 = 'не выполняется! Электроды выбраны неверно!'
        return notation2

    def condition2_calc1(self):
        """Расчет значения для condition2 для подстановки значения в текст отчета"""
        cond2_res1 = 1.1 * float(self.big_r_wz())
        return round(cond2_res1, 1)

    def condition2_calc2(self):
        """Расчет значения для condition2 для подстановки значения в текст отчета"""
        cond2_res2 = float(self.big_r_wz()) * float(self.big_b_z) / float(self.big_b_f)
        return round(cond2_res2, 1)

    def condition3(self):
        """Условие для выбора электродов для сварки для стали свыше 285 Н/мм2"""
        if float(self.big_r_wz()) <= float(self.big_r_wf) <= float(self.big_r_wz()) * float(self.big_b_z) / float(
                self.big_b_f):
            notation3 = 'выполняется!'
        else:
            notation3 = 'не выполняется! Электроды выбраны неверно!'
        return notation3


b = Formula_for_metal_seam_in_the_plane_of_the_seam(big_b_f=0.7, big_m=55, big_r_wf=200, gamma_c=1,
                                                    k_f=1, big_b_z=0.7, big_r_un=370, l_1=30, l_2=20)






class Formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces:
    """Расчет прочности сварного соединения по металлу шва на одновременное действие продольной и поперечной сил"""

    def __init__(self, big_b_f: float, big_n: float, big_q, big_r_wf: float,
                 gamma_c: float, k_f: float, big_b_z: float, big_r_un: float, l_1: float, l_2: float) -> float:
        self.k_f = k_f
        self.big_b_f = big_b_f
        self.big_n = big_n
        self. big_q = big_q
        self.big_r_wf = big_r_wf
        self.gamma_c = gamma_c
        self.big_b_z = big_b_z
        self.big_r_un = big_r_un
        self.l_1 = l_1
        self.l_2 = l_2

    def big_r_wz(self) -> float:
        """Расчет значения big_r_wz"""
        big_r_wz = 0.45 * float(self.big_r_un)
        return round(big_r_wz, 1)

    def condition4(self):
        """Расчет отношения для выбора сечения для расчетов(металл шва или граница сплавления)"""
        cond4_res = (float(self.big_b_f) * float(self.big_r_wf)) / (float(self.big_b_z) * float(self.big_r_wz()))
        return round(cond4_res, 1)

    def l_1_minus_10mm(self):
        """Коррекция длинны шва на 10 мм, согласно СНИП"""
        correction = float(self.l_1) - 1
        return round(correction, 1)

    def big_a_w(self):
        """Расчет площади шва"""
        big_a_w = (2 * float(self.l_1_minus_10mm()) + float(self.l_2)) * float(self.k_f) * float(self.big_b_f)
        return round(big_a_w, 1)

    def tau_n(self):
        """Расчет напряжения в соединении от продольной силы N"""
        tau_n = float(self.big_n) * 10 / float(self.big_a_w())
        return round(tau_n, 1)

    def tau_q(self):
        """Расчет напряжения в соединении от продольной силы Q"""
        tau_q = float(self.big_q) * 10 / float(self.big_a_w())
        return round(tau_q, 1)

    def x_c(self):
        """Расчет значения центра тяжести периметра швов по оси х"""
        x_c = (float(self.l_1) ** 2 - 0.5 * float(self.l_2) * float(self.k_f)) / (2 * float(self.l_1) + float(self.l_2))
        return round(x_c, 0)

    def point_a_coordinate_x(self):
        """Расчет координаты точки А по оси х """
        x_a = float(self.l_1) - float(self.x_c())
        return round(x_a, 1)

    def point_a_coordinate_y(self):
        """Расчет координаты точки А по оси у"""
        y_a = float(self.l_2) / 2
        return round(y_a, 1)

    def big_i_fx(self):
        """Расчет значения Ifx"""
        big_i_fx = float(self.big_b_f) * (
                float(self.l_2) ** 3 * float(self.k_f) / 12 + 2 * float(self.l_1_minus_10mm()) * float(self.k_f) * (
                (float(self.l_2) + float(self.k_f)) / 2) ** 2)
        return round(big_i_fx, 1)

    def big_i_fy(self):
        """Расчет значения Ify."""
        big_i_fy = float(self.big_b_f) * (2 * (float(self.l_1_minus_10mm()) ** 3 * float(self.k_f) / 12 +
                                               float(self.l_1_minus_10mm()) * float(self.k_f) * (
                                                       float(self.l_1_minus_10mm()) / 2 -
                                                       float(self.x_c())) ** 2) + float(self.l_2) * float(
            self.k_f) * (float(self.x_c()) + float(self.k_f)
                         / 2) ** 2)
        return round(big_i_fy, 1)

    def length_from_x_c_to_a(self):
        """Расчет расстояния от Хц до точки А."""
        length_from_x_c_to_a = (float(self.point_a_coordinate_x()) ** 2 + float(
            self.point_a_coordinate_y()) ** 2) ** 0.5
        return round(length_from_x_c_to_a, 1)

    def tau_m_q(self):
        """Расчет напряжения от момента."""
        tau_m_q = float(self.big_q) * 10 ** 3 * float(self.length_from_x_c_to_a()) / (float(self.big_i_fx()) + float(
            self.big_i_fy()))
        return round(tau_m_q, 1)

    def cos_a(self):
        """Расчет косинуса а"""
        cos_a = (float(self.l_1) - float(self.x_c())) / float(self.length_from_x_c_to_a())
        return round(cos_a, 2)

    def tau_q_rez(self):
        """Расчет результирующего напряжения от действия поперечной силы Q"""
        tau_q_rez = ((float(self.tau_q())**2 + float(self.tau_m_q())**2) + 2 * float(self.tau_q()) *
                     float(self.tau_m_q()) * float(self.cos_a())) ** 0.5
        return round(tau_q_rez, 1)

    def sin_a(self):
        """Расчет синуса а"""
        sin_a = 0.5 * float(self.l_2) / float(self.length_from_x_c_to_a())
        return round(sin_a, 2)

    def cos_phi(self):
        """Расчет косинуса фи"""
        cos_phi = float(self.tau_m_q()) * float(self.sin_a()) / ((float(self.tau_m_q()) * float(self.sin_a()))**2 +
                  (float(self.tau_m_q()) * float(self.cos_a()) + float(self.tau_q())) ** 2) ** 0.5
        return round(cos_phi, 2)

    def tau_f(self):
        """Суммарное напряжение в шве"""
        tau_f = (float(self.tau_n()) ** 2 + float(self.tau_q_rez()) ** 2 + 2 * float(self.tau_n()) *
                 float(self.tau_q_rez()) * float(self.cos_phi())) ** 0.5
        return round(tau_f, 1)

    def main_condition(self):
        """Расчет главной формулы big_m/(big_w_f*big_r_wf*gamma_c)"""
        value = float(self.tau_f() / float(self.big_r_wf) * float(self.gamma_c))
        return round(value, 1)

    def main_notation(self):
        """Условие, что результат главной формулы должен быть <= 1"""
        if float(self.main_condition()) <= 1:
            main_notation = 'выполняется! Прочность по металлу шва достаточна!'
        else:
            main_notation = 'не выполняется! Электроды (либо высота катета) выбраны неверно!'
        return main_notation

    def relation_tau_f_to_big_r_wf(self):
        """Расчет отношения напряжения в шве к сопротивлению шва"""
        relation_tau_f_to_big_r_wf = float(self.tau_f()) / float(self.big_r_wf)
        return round(relation_tau_f_to_big_r_wf, 1)



    def check_katet(self):
        """Определение оптимальной высоты катета шва"""
        k_f = 1
        big_a_w = (2 * float(self.l_1_minus_10mm()) + float(self.l_2)) * float(k_f) * float(self.big_b_f)
        tau_n = float(self.big_n) * 10 / float(big_a_w)
        tau_q = float(self.big_n) * 10 / float(big_a_w)
        x_c = (float(self.l_1) ** 2 - 0.5 * float(self.l_2) * float(k_f)) / (2 * float(self.l_1) + float(self.l_2))
        x_a = float(self.l_1) - float(x_c)
        y_a = float(self.l_2) / 2
        length_from_x_c_to_a = (float(x_a) ** 2 + float(y_a) ** 2) ** 0.5

        big_i_fx = float(self.big_b_f) * (
                float(self.l_2) ** 3 * float(k_f) / 12 + 2 * float(self.l_1_minus_10mm()) * float(k_f) * (
                (float(self.l_2) + float(k_f)) / 2) ** 2)
        big_i_fy = float(self.big_b_f) * (2 * (float(self.l_1_minus_10mm()) ** 3 * float(k_f) / 12 +
                                               float(self.l_1_minus_10mm()) * float(k_f) * (
                                                       float(self.l_1_minus_10mm()) / 2 -
                                                       float(x_c)) ** 2) + float(self.l_2) * float(k_f) * (
                                                  float(x_c) + float(k_f)
                                                  / 2) ** 2)
        tau_m_q = float(self.big_q) * 10 ** 3 * float(length_from_x_c_to_a) / (float(big_i_fx) + float(
            big_i_fy))
        cos_a = (float(self.l_1) - float(x_c)) / float(length_from_x_c_to_a)
        tau_q_rez = ((float(tau_q) ** 2 + float(tau_m_q) ** 2) + 2 * float(tau_q) *
                     float(tau_m_q) * float(cos_a)) ** 0.5
        sin_a = 0.5 * float(self.l_2) / float(length_from_x_c_to_a)
        cos_phi = float(tau_m_q) * float(sin_a) / ((float(tau_m_q) * float(sin_a)) ** 2 +
                                                                 (float(tau_m_q) * float(cos_a) + float(
                                                                     tau_q)) ** 2) ** 0.5
        tau_f = (float(tau_n) ** 2 + float(tau_q_rez) ** 2 + 2 * float(tau_n) *
                 float(tau_q_rez) * float(cos_phi)) ** 0.5

        check_katet = (float(tau_f)/ float(self.big_r_wf)) + 0.025
        return round(check_katet, 1)


    def check_main_condition(self):
        """Проверка условия главной формулы при подстановке оптимальной высоты катета шва"""
        k_f = float(self.check_katet())
        big_a_w = (2 * float(self.l_1_minus_10mm()) + float(self.l_2)) * float(k_f) * float(self.big_b_f)
        tau_n = float(self.big_n) * 10 / float(big_a_w)
        tau_q = float(self.big_n) * 10 / float(big_a_w)
        x_c = (float(self.l_1) ** 2 - 0.5 * float(self.l_2) * float(k_f)) / (2 * float(self.l_1) + float(self.l_2))
        x_a = float(self.l_1) - float(x_c)
        y_a = float(self.l_2) / 2
        length_from_x_c_to_a = (float(x_a) ** 2 + float(y_a) ** 2) ** 0.5

        big_i_fx = float(self.big_b_f) * (
                float(self.l_2) ** 3 * float(k_f) / 12 + 2 * float(self.l_1_minus_10mm()) * float(k_f) * (
                (float(self.l_2) + float(k_f)) / 2) ** 2)
        big_i_fy = float(self.big_b_f) * (2 * (float(self.l_1_minus_10mm()) ** 3 * float(k_f) / 12 +
                                               float(self.l_1_minus_10mm()) * float(k_f) * (
                                                       float(self.l_1_minus_10mm()) / 2 -
                                                       float(x_c)) ** 2) + float(self.l_2) * float(k_f) * (
                                                  float(x_c) + float(k_f)
                                                  / 2) ** 2)
        tau_m_q = float(self.big_q) * 10 ** 3 * float(length_from_x_c_to_a) / (float(big_i_fx) + float(
            big_i_fy))
        cos_a = (float(self.l_1) - float(x_c)) / float(length_from_x_c_to_a)
        tau_q_rez = ((float(tau_q) ** 2 + float(tau_m_q) ** 2) + 2 * float(tau_q) *
                     float(tau_m_q) * float(cos_a)) ** 0.5
        sin_a = 0.5 * float(self.l_2) / float(length_from_x_c_to_a)
        cos_phi = float(tau_m_q) * float(sin_a) / ((float(tau_m_q) * float(sin_a)) ** 2 +
                                                   (float(tau_m_q) * float(cos_a) + float(
                                                       tau_q)) ** 2) ** 0.5
        tau_f = (float(tau_n) ** 2 + float(tau_q_rez) ** 2 + 2 * float(tau_n) *
                 float(tau_q_rez) * float(cos_phi)) ** 0.5

        check_main_condition = float(tau_f) / (float(self.big_r_wf) * float(self.gamma_c))
        return round(check_main_condition, 1)

    def check_main_notation(self):
        """Исходя из расчетов check_main_condition выдает заключение о соответствии условию главной формулы"""
        if float(self.check_main_condition()) <= 1:
            check_main_notation = 'выполняется! Прочность по металлу шва достаточна!'
        else:
            check_main_notation = 'не выполняется! Электроды (либо высота катета) выбраны неверно!'
        return check_main_notation

    def condition1(self):
        """Условие для выбора электродов для механизированной сварки для стали до 285 Н/мм2"""
        if float(self.big_r_wf) > float(self.big_r_wz()):
            notation1 = 'выполняется!'
        else:
            notation1 = 'не выполняется! Электроды выбраны неверно!'
        return notation1

    def condition2(self):
        """Условие для выбора электродов для ручной сварки для стали до 285 Н/мм2"""
        if 1.1 * float(self.big_r_wz()) <= float(self.big_r_wf) <= float(self.big_r_wz()) * float(
                self.big_b_z) / float(self.big_b_f):
            notation2 = 'выполняется!'
        else:
            notation2 = 'не выполняется! Электроды выбраны неверно!'
        return notation2

    def condition2_calc1(self):
        """Расчет значения для condition2 для подстановки значения в текст отчета"""
        cond2_res1 = 1.1 * float(self.big_r_wz())
        return round(cond2_res1, 1)

    def condition2_calc2(self):
        """Расчет значения для condition2 для подстановки значения в текст отчета"""
        cond2_res2 = float(self.big_r_wz()) * float(self.big_b_z) / float(self.big_b_f)
        return round(cond2_res2, 1)

    def condition3(self):
        """Условие для выбора электродов для сварки для стали свыше 285 Н/мм2"""
        if float(self.big_r_wz()) <= float(self.big_r_wf) <= float(self.big_r_wz()) * float(self.big_b_z) / float(
                self.big_b_f):
            notation3 = 'выполняется!'
        else:
            notation3 = 'не выполняется! Электроды выбраны неверно!'
        return notation3


с = Formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces(big_b_f=0.7, big_n=100, big_q=38, big_r_wf=200, gamma_c=1,
                                                    k_f=1, big_b_z=0.7, big_r_un=370, l_1=30, l_2=20)

