from flask import Flask, render_template, request
from my_app_formula.formulas_functions import Formula_for_metal_seam_perpendicular_to_the_seam as ffms, \
    Formula_for_metal_seam_in_the_plane_of_the_seam, \
    Formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces
from my_app_formula.matirials_for_calculations import Welded_joints
import pdfkit

app = Flask(__name__)


@app.route('/')
def home_page():
    """Главная страница сайта"""
    title = 'Радость конструктора!'
    return render_template('home_page.html', the_title=title)


# --- Блок "Контруктивный расчет"---
@app.route('/constructive_calculation/metal_constructions')
def calculation_metal_constructions() -> str:
    """Страница с расчетами для металлоконструкций"""
    title = 'Расчет металлоконструкций'
    return render_template('calculation_metal_constructions.html', the_title=title)


# @app.route('/constructive_calculation/concrete_constructions')
# def calculation_concrete_constructions():
#   """Страница с расчетами для железобетонных конструкций"""
#     title = 'Расчет железобетонных конструкций'
#     return render_template('calculation_concrete_constructions.html', the_title=title)

# @app.route('/constructive_calculation/wooden_constructions')
# def calculation_wooden_constructions():
#   """Страница с расчетами для конструкций из дерева"""
#   title = 'Расчет конструкций из дерева'
#   return render_template('calculation_wooden_constructions.html', the_title=title)


# ---Блок "Техническая документация"---

@app.route('/tech_documentation/metal_constructions/welded_joints')
def tech_doc_metal_constructions() -> str:
    """Страница с технической документацией для металлоконструкций"""
    title = 'СП-2017'
    return render_template('tech_doc_metal_constructions_welded_joints.html', the_title=title)


# @app.route('/tech_documentation/concrete_constructions')
# def tech_doc_concrete_constructions() -> str:
#    """Страница с технической документацией для железобетонных конструкций"""
#     title = 'СП-2017'
#     return render_template('tech_doc_concrete_constructions.html', the_title=title)
#
# @app.route('/tech_documentation/wooden_constructions')
# def tech_doc_wooden_constructions() -> str:
#   """Страница с технической документацией для конструкций из дерева"""
#     title = 'СП-2017'
#     return render_template('tech_doc_wooden_constructions.html', the_title=title)

# ---Блок "Личный кабинет"---

# @app.route('/user_coner')
# def user_coner() -> str:
#     """Страница с личным кабинетом пользователя"""
#     title = 'Личный кабинет'
#     return render_template('user_coner.html', the_title=title)

# ---Блок "Связаться с автором"---
@app.route('/feedback_form')
def feedback_form():
    """Форма для отправки сообщения администратору"""
    title = "Обратная связь"
    return render_template("feedback_form.html", the_title=title)


# ---Блок "Поиск"
# """Поиск по сайту через строку поиска"""

# ---Блок с формами для расчета металлоконструкций---

@app.route('/constructive_calculation/metal_constructions/form_moment_perpendicular_to_the_seam')
def form_moment_perpendicular_to_the_seam() -> str:
    """Форма для расчета сварного соединения c угловыми швами с моментом перепендикулярным шву"""
    title = 'Расчет сварного соединения'
    return render_template('form_moment_perpendicular_to_the_seam.html', the_title=title)


@app.route('/constructive_calculation/metal_constructions/form_moment_in_the_plane_of_the_seam')
def form_moment_in_the_plane_of_the_seam() -> str:
    """Форма для расчета сварного соединения c угловыми швами с моментом в плоскости шва"""
    title = 'Расчет сварного соединения'
    return render_template('form_moment_in_the_plane_of_the_seam.html', the_title=title)


@app.route('/constructive_calculation/metal_constructions/form_simultaneous_longitudinal_and_perpendicular_forces')
def form_simultaneous_longitudinal_and_perpendicular_forces() -> str:
    """Форма для расчета сварного соединения c угловыми швами при одновременном действии продольной и поперечной сил"""
    title = 'Расчет сварного соединения'
    return render_template('form_simultaneous_longitudinal_and_perpendicular_forces.html', the_title=title)


# ---Блок с формами для расчета железобетонных конструкций---


# ---Блок с формами для расчета конструкций из дерева---


# ---Блок с расчетами и результатами---

@app.route('/constructive_calculation/metal_constructions/result_moment_perpendicular_to_the_seam',
           methods=['GET', 'POST'])
def result_moment_perpendicular_to_the_seam() -> 'html':
    """Собирает данные формы и передает их в качестве аргументов в модуль formulas_functions.py, а затем выдает результаты расчетов"""
    big_b_f = request.form['big_b_f']
    big_b_z = request.form['big_b_z']
    h_w = request.form['h_w']
    t_w = request.form['t_w']
    b_f = request.form['b_f']
    h = request.form['h']
    big_m = request.form['big_m']
    electrode_type = request.form.get('select1')
    steel_type = request.form.get('select2')
    gamma_c = request.form['gamma_c']
    k_f = request.form['k_f']

    instance_for_welded_joints = Welded_joints(electrode_type, steel_type)  # Экземпляр для выбора электродов и стали
    big_r_wf = instance_for_welded_joints.big_r_wf() # Вызов функции для электродов
    big_r_un = instance_for_welded_joints.big_r_un() # Вызов функции для стали

    if type(big_r_wf) != int:
        return render_template("something_went_wrong.html",)
    elif type(big_r_un) != int:
        return render_template("something_went_wrong.html", )
    else:

        instance_for_ffms = ffms(big_b_f, h_w, t_w, b_f, h, big_m, big_r_wf,
                                 gamma_c, k_f, big_b_z, big_r_un)  # Экземпляр для расчета "по металлу шва"

        result1 = instance_for_ffms.big_i_f()
        result2 = instance_for_ffms.y_max()
        result3 = instance_for_ffms.big_w_f()
        result4 = instance_for_ffms.tau_f()
        result5 = instance_for_ffms.inequality()
        main_condition = instance_for_ffms.main_condition()
        main_notation = instance_for_ffms.main_notation()
        condition1 = instance_for_ffms.condition1()
        condition2 = instance_for_ffms.condition2()
        cond2_calc1 = instance_for_ffms.condition2_calc1()
        cond2_calc2 = instance_for_ffms.condition2_calc2()
        condition3 = instance_for_ffms.condition3()
        calc_big_r_wz = instance_for_ffms.big_r_wz()
        condition4 = instance_for_ffms.condition4()
        check_katet = instance_for_ffms.check_katet()
        check_main_condition = instance_for_ffms.check_main_condition()
        check_main_notation = instance_for_ffms.check_main_notation()

        title = 'Результаты вычислений'

        if float(condition4) <= 1:

            return render_template('result_moment_perpendicular_to_the_seam.html', the_title=title, the_big_b_f=big_b_f,
                                   the_big_b_z=big_b_z, the_h_w=h_w, the_t_w=t_w, the_b_f=b_f,
                                   the_h=h, the_big_m=big_m, the_big_r_wf=big_r_wf,
                                   the_big_r_un=big_r_un, the_gamma_c=gamma_c, the_k_f=k_f,
                                   the_electrode_type=electrode_type,
                                   the_steel_type=steel_type,

                                   the_result1=result1, the_result2=result2, the_result3=result3,
                                   the_result4=result4, the_result5=result5, the_main_condition=main_condition,
                                   the_main_notation=main_notation, the_condition1=condition1, the_condition2=condition2,
                                   the_condition3=condition3, the_cond2_calc1=cond2_calc1, the_cond2_calc2=cond2_calc2,
                                   the_big_r_wz=calc_big_r_wz, the_condition4=condition4, the_check_katet=check_katet,
                                   the_check_main_condition=check_main_condition,
                                   the_check_main_notation=check_main_notation)
        else:

            return render_template('ask_for_help.html',)


#
@app.route('/constructive_calculation/metal_constructions/result_moment_in_the_plane_of_the_seam',
           methods=['GET', 'POST'])
def result_moment_in_the_plane_of_the_seam() -> 'html':
    """Собирает данные формы и передает их в качестве аргументов в модуль formulas_functions.py, а затем выдает результаты расчетов"""
    big_b_f = request.form['big_b_f']
    big_b_z = request.form['big_b_z']
    big_m = request.form['big_m']
    electrode_type = request.form.get('select1')
    steel_type = request.form.get('select2')
    gamma_c = request.form['gamma_c']
    k_f = request.form['k_f']
    l_1 = request.form['l_1']
    l_2 = request.form['l_2']

    instance_for_welded_joints = Welded_joints(electrode_type, steel_type)  # Экземпляр для выбора электродов и стали
    big_r_wf = instance_for_welded_joints.big_r_wf()
    big_r_un = instance_for_welded_joints.big_r_un()

    if type(big_r_wf) != int:
        return render_template("something_went_wrong.html",)
    elif type(big_r_un) != int:
        return render_template("something_went_wrong.html", )
    else:
        instance_for_formula_for_metal_seam_in_the_plane_of_the_seam = Formula_for_metal_seam_in_the_plane_of_the_seam(
            big_b_f, big_m, big_r_wf, gamma_c, k_f, big_b_z, big_r_un, l_1, l_2)  # Экземпляр для класса "по металлу шва"

        # """Расчет значения big_r_wz"""
        calc_big_r_wz = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.big_r_wz()
        # """Расчет отношения для выбора сечения для расчетов(металл шва или граница сплавления)"""
        condition4 = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.condition4()
        # """Расчет значения центра тяжести периметра швов по оси х"""
        x_c = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.x_c()
        # """Расчет координаты точки А по оси х """
        point_a_coordinate_x = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.point_a_coordinate_x()
        # """Расчет координаты точки А по оси y """
        point_a_coordinate_y = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.point_a_coordinate_y()
        # """Коррекция длинны шва на 10 мм, согласно СНИП"""
        l_1_minus_10mm = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.l_1_minus_10mm()
        # """Расчет значения Ifx"""
        big_i_fx = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.big_i_fx()
        # """Расчет значения Ify"""
        big_i_fy = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.big_i_fy()
        # """Расчет расстояния от Хц до точки А"""
        length_from_x_c_to_a = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.length_from_x_c_to_a()
        # """Расчет главной формулы big_m/(big_w_f*big_r_wf*gamma_c)"""
        main_condition = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.main_condition()
        # """Условие, что результат главной формулы должен быть <= 1"""
        main_notation = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.main_notation()
        # """Расчет напряжения в шве"""
        tau_f = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.tau_f()
        # """Расчет отношения напряжения в шве к сопротивлению шва"""
        relation_tau_f_to_big_r_wf = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.relation_tau_f_to_big_r_wf()
        # """Определение оптимальной высоты катета шва"""
        check_katet = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.check_katet()
        # """Проверка условия главной формулы при подстановке оптимальной высоты катета шва"""
        check_main_condition = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.check_main_condition()
        # """Исходя из расчетов check_main_condition выдает заключение о соответствии условию главной формулы"""
        check_main_notation = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.check_main_notation()
        #  """Условие для выбора электродов для механизированной сварки для стали до 285 Н/мм2"""
        condition1 = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.condition1()
        # """Условие для выбора электродов для ручной сварки для стали до 285 Н/мм2"""
        condition2 = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.condition2()
        # """Расчет значения для condition2 для подстановки значения в текст отчета"""
        condition2_calc1 = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.condition2_calc1()
        # """Расчет значения для condition2 для подстановки значения в текст отчета"""
        condition2_calc2 = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.condition2_calc2()
        #  """Условие для выбора электродов для сварки для стали свыше 285 Н/мм2"""
        condition3 = instance_for_formula_for_metal_seam_in_the_plane_of_the_seam.condition3()

        if float(condition4) <= 1:

            return render_template('result_moment_in_the_plane_of_the_seam.html', the_big_b_f=big_b_f,
                                   the_big_b_z=big_b_z, the_big_m=big_m, the_big_r_wf=big_r_wf,
                                   the_big_r_un=big_r_un, the_gamma_c=gamma_c, the_k_f=k_f,
                                   the_electrode_type=electrode_type, the_steel_type=steel_type,
                                   the_l_1=l_1, the_l_2=l_2,

                                   the_main_condition=main_condition,
                                   the_main_notation=main_notation, the_condition1=condition1, the_condition2=condition2,
                                   the_condition3=condition3, the_cond2_calc1=condition2_calc1,
                                   the_cond2_calc2=condition2_calc2, the_big_r_wz=calc_big_r_wz, the_condition4=condition4,
                                   the_check_katet=check_katet, the_check_main_condition=check_main_condition,
                                   the_check_main_notation=check_main_notation, the_x_c=x_c,
                                   the_point_a_coordinate_x=point_a_coordinate_x,
                                   the_point_a_coordinate_y=point_a_coordinate_y,
                                   the_l_1_minus_10mm=l_1_minus_10mm, the_big_i_fx=big_i_fx, the_big_i_fy=big_i_fy,
                                   the_length_from_x_c_to_a=length_from_x_c_to_a, the_tau_f=tau_f,
                                   the_relation_tau_f_to_big_r_wf=relation_tau_f_to_big_r_wf, )




        else:
            return render_template("ask_for_help.html", )

@app.route('/constructive_calculation/metal_constructions/result_simultaneous_longitudinal_and_perpendicular_forces',
           methods=['GET', 'POST'])
def result_simultaneous_longitudinal_and_perpendicular_forces() -> 'html':
    """Собирает данные формы и передает их в качестве аргументов в модуль formulas_functions.py, а затем выдает результаты расчетов"""
    big_b_f = request.form['big_b_f']
    big_b_z = request.form['big_b_z']
    big_n = request.form['big_n']
    big_q = request.form['big_q']
    electrode_type = request.form.get('select1')
    steel_type = request.form.get('select2')
    gamma_c = request.form['gamma_c']
    k_f = request.form['k_f']
    l_1 = request.form['l_1']
    l_2 = request.form['l_2']

    instance_for_welded_joints = Welded_joints(electrode_type, steel_type)  # Экземпляр для выбора электродов и стали
    big_r_wf = instance_for_welded_joints.big_r_wf()
    big_r_un = instance_for_welded_joints.big_r_un()

    if type(big_r_wf) != int:
        return render_template("something_went_wrong.html",)
    elif type(big_r_un) != int:
        return render_template("something_went_wrong.html", )
    else:
        instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces = Formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces(
            big_b_f, big_n, big_q, big_r_wf, gamma_c, k_f, big_b_z, big_r_un, l_1,
            l_2)  # Экземпляр для класса "по металлу шва"

        # """Расчет значения big_r_wz"""
        calc_big_r_wz = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.big_r_wz()
        # """Расчет отношения для выбора сечения для расчетов(металл шва или граница сплавления)"""
        condition4 = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.condition4()
        # """Коррекция длинны шва на 10 мм, согласно СНИП"""
        l_1_minus_10mm = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.l_1_minus_10mm()
        # """Расчет площади шва"""
        big_a_w = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.big_a_w()
        # """Расчет напряжения в соединении от продольной силы N"""
        tau_n = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.tau_n()
        # """Расчет напряжения в соединении от продольной силы Q"""
        tau_q = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.tau_q()
        # """Расчет значения центра тяжести периметра швов по оси х"""
        x_c = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.x_c()
        # """Расчет координаты точки А по оси х """
        point_a_coordinate_x = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.point_a_coordinate_x()
        # """Расчет координаты точки А по оси y """
        point_a_coordinate_y = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.point_a_coordinate_y()
        # """Расчет значения Ifx"""
        big_i_fx = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.big_i_fx()
        # """Расчет значения Ify"""
        big_i_fy = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.big_i_fy()
        # """Расчет расстояния от Хц до точки А"""
        length_from_x_c_to_a = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.length_from_x_c_to_a()
        # """Расчет напряжения от момента."""
        tau_m_q = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.tau_m_q()
        # """Расчет косинуса а"""
        cos_a = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.cos_a()
        # """Расчет результирующего напряжения от действия поперечной силы Q"""
        tau_q_rez = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.tau_q_rez()
        # """Расчет синуса а"""
        sin_a = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.sin_a()
        # """Расчет косинуса фи"""
        cos_phi = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.cos_phi()
        # """Суммарное напряжение в шве"""
        tau_f = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.tau_f()
        # """Расчет главной формулы tau_f/big_r_wf*gamma_c)"""
        main_condition = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.main_condition()
        # """Условие, что результат главной формулы должен быть <= 1"""
        main_notation = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.main_notation()
        # """Определение оптимальной высоты катета шва"""
        check_katet = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.check_katet()
        # """Проверка условия главной формулы при подстановке оптимальной высоты катета шва"""
        check_main_condition = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.check_main_condition()
        # """Исходя из расчетов check_main_condition выдает заключение о соответствии условию главной формулы"""
        check_main_notation = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.check_main_notation()
        #  """Условие для выбора электродов для механизированной сварки для стали до 285 Н/мм2"""
        condition1 = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.condition1()
        # """Условие для выбора электродов для ручной сварки для стали до 285 Н/мм2"""
        condition2 = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.condition2()
        # """Расчет значения для condition2 для подстановки значения в текст отчета"""
        condition2_calc1 = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.condition2_calc1()
        # """Расчет значения для condition2 для подстановки значения в текст отчета"""
        condition2_calc2 = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.condition2_calc2()
        #  """Условие для выбора электродов для сварки для стали свыше 285 Н/мм2"""
        condition3 = instance_for_formula_for_metal_seam_simultaneous_longitudinal_and_perpendicular_forces.condition3()

        if float(condition4) <= 1:
        #
            return render_template('result_simultaneous_longitudinal_and_perpendicular_forces.html', the_big_b_f=big_b_f,
                                   the_big_b_z=big_b_z, the_big_n=big_n, the_big_q=big_q, the_big_r_wf=big_r_wf,
                                   the_big_r_un=big_r_un, the_gamma_c=gamma_c, the_k_f=k_f,
                                   the_electrode_type=electrode_type, the_steel_type=steel_type,
                                   the_l_1=l_1, the_l_2=l_2,

                                   the_main_condition=main_condition,
                                   the_main_notation=main_notation, the_condition1=condition1, the_condition2=condition2,
                                   the_condition3=condition3, the_cond2_calc1=condition2_calc1,
                                   the_cond2_calc2=condition2_calc2, the_big_r_wz=calc_big_r_wz, the_condition4=condition4,
                                   the_check_katet=check_katet, the_check_main_condition=check_main_condition,
                                   the_check_main_notation=check_main_notation, the_x_c=x_c,
                                   the_point_a_coordinate_x=point_a_coordinate_x,
                                   the_point_a_coordinate_y=point_a_coordinate_y,
                                   the_l_1_minus_10mm=l_1_minus_10mm, the_big_i_fx=big_i_fx, the_big_i_fy=big_i_fy,
                                   the_length_from_x_c_to_a=length_from_x_c_to_a, the_tau_f=tau_f, the_big_a_w=big_a_w,
                                   the_tau_n=tau_n, the_tau_q=tau_q, the_tau_m_q=tau_m_q, the_cos_a=cos_a,
                                   the_tau_q_rez=tau_q_rez,
                                   the_sin_a=sin_a, the_cos_phi=cos_phi, )
        else:
            return render_template("ask_for_help.html",)


@app.route('/trail')
def test():
    return render_template('ask_for_help.html')


# @app.route('/metall/pdf_report')
# def pdf_report():
#     title = 'Отчет в формате PDF'
#     conf = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
#     pdfkit.from_file('C:\\Users\\zaten\\PycharmProjects\\app_fromulas\\my_app_formula\\templates\\result_moment_perpendicular_to_the_seam.html',
#                      'result.pdf', configuration=conf)
#     return

if __name__ == '__main__':
    app.run(debug=True)
