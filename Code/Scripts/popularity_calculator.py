# pop(a) = pos(a) * nut(a) / [{ pos(a)+neg(a) } * {nut(a)+nut(b)}]
import xlrd
import matplotlib.pyplot as plt
# find popularity based on an hour
# algo,
#
# read all cells
# drop the text column
# group based on hour
# calulate len of pos neg and nut
# plot the date on matplotlib
# x-axis = day and hour
# y-axis = popularity


def calculate_popularity(pos_a=0,nut_a=0,neg_a=0,nut_b=0)-> float:
    popularity = (pos_a)/(pos_a+neg_a)
    popularity *= (nut_a)/(nut_a+nut_b)
    return popularity


def freq_of_popularity(list_of_num)->dict:
    """

    :param list_of_num:
    :return: return the frequency of -1, 1 and 0
    """
    freq = {}
    freq['neg'] = list_of_num.count(-1)
    freq['pos'] = list_of_num.count(1)
    freq['nut'] = list_of_num.count(0)
    return freq




