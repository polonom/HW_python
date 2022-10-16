mult='*'
div='/'
plus='+'
minus='-'
power = '**'

def split_evaluation(evaluation):
    evaluation = evaluation.replace(' ', '')
    eval_lst = []
    num = ''
    sign = ''
    for char in evaluation:
        if char.isdigit():
            if sign != '':
                eval_lst.append(sign)
                sign = ''
            num = num + char
        else:
            if num != '':
                eval_lst.append(num)
                num = ''
            sign = sign + char
    eval_lst.append(num)
    return eval_lst


def is_in_lst(lst_for_search, searched_els_lst):
    return any((e in lst_for_search for e in searched_els_lst))


def make_eval_by_signs(lst, signs_lst):
    res = 0
    i = 0
    while True:
        if not is_in_lst(lst, signs_lst):
            break
        else:
            cur_e = lst[i]
            prev_e = lst[i - 1]
            next_e = lst[i + 1]
            if cur_e in signs_lst:
                if cur_e == power:
                    res = float(prev_e) ** float(next_e)
                elif cur_e == mult:
                    res = float(prev_e) * float(next_e)
                elif cur_e == div:
                    res = float(prev_e) / float(next_e)
                elif cur_e == plus:
                    res = float(prev_e) + float(next_e)
                else:
                    res = float(prev_e) - float(next_e)
                lst[i] = str(res)
                lst.pop(i + 1)
                lst.pop(i - 1)
                i = 0
            else:
                i += 1
    return lst


def make_eval(evaluation):
    eval_lst = split_evaluation(evaluation)
    if is_in_lst(eval_lst, [power]):
        eval_lst = make_eval_by_signs(eval_lst, [power])
    if is_in_lst(eval_lst, [mult, div]):
        eval_lst = make_eval_by_signs(eval_lst, [mult, div])
    if is_in_lst(eval_lst, [plus, minus]):
        eval_lst = make_eval_by_signs(eval_lst, [plus, minus])
    return eval_lst[0]


my_evaluation = input("Введите уравнение: ")
print(my_evaluation)
print(split_evaluation(my_evaluation))
print(make_eval(my_evaluation))
