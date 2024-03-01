from nicegui import ui
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
from matplotlib import pyplot as plt
import csv
import json
import pickle

data_file = 'data.pickle'

try:
    with open(data_file, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    # 如果文件不存在，创建默认值
    data = {
        'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0,
        'b1': 0, 'b2': 0, 'b3': 0, 'b4': 0, 'b5': 0, 'b6': 0,
        'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0,
        'd1': 0, 'd2': 0, 'd3': 0, 'd4': 0, 'd5': 0,
        'e1': 0, 'e2': 0, 'e3': 0, 'e4': 0, 'e5': 0,
        'a11': 0, 'a12': 0, 'a13': 0, 'a14': 0, 'a15': 0,
        'b11': 0, 'b12': 0, 'b13': 0, 'b14': 0, 'b15': 0, 'b16': 0,
        'c11': 0, 'c12': 0, 'c13': 0, 'c14': 0, 'c15': 0,
        'd11': 0, 'd12': 0, 'd13': 0, 'd14': 0, 'd15': 0,
        'e11': 0, 'e12': 0, 'e13': 0, 'e14': 0, 'e15': 0,
        'g1': 0, 'g2': 0, 'g3': 0, 'g4': 0, 'g5': 0,
    }



def ui_main():


    fa1 = 0
    fa2 = 0
    fa3 = 0
    fa4 = 0
    fa5 = 0
    fb1 = 0
    fb2 = 0
    fb3 = 0
    fb4 = 0
    fb5 = 0
    fb6 = 0
    fc1 = 0
    fc2 = 0
    fc3 = 0
    fc4 = 0
    fc5 = 0
    fd1 = 0
    fd2 = 0
    fd3 = 0
    fd4 = 0
    fd5 = 0
    fe1 = 0
    fe2 = 0
    fe3 = 0
    fe4 = 0
    fe5 = 0
    ra1 = 0
    ra2 = 0
    ra3 = 0
    ra4 = 0
    ra5 = 0
    rb1 = 0
    rb2 = 0
    rb3 = 0
    rb4 = 0
    rb5 = 0
    rb6 = 0
    rc1 = 0
    rc2 = 0
    rc3 = 0
    rc4 = 0
    rc5 = 0
    rd1 = 0
    rd2 = 0
    rd3 = 0
    rd4 = 0
    rd5 = 0
    re1 = 0
    re2 = 0
    re3 = 0
    re4 = 0
    re5 = 0
    gg1 = 0
    gg2 = 0
    gg3 = 0
    gg4 = 0
    gg5 = 0
    with ui.grid(columns=2).classes('w-[80%] self-center row'):
        with ui.tabs().classes('col-auto self-center').props('vertical') as tabs:
            func0 = ui.tab("个人展示").style('color:blue')
            func3 = ui.tab('个人平均分').style('color:purple')
            func1 = ui.tab('统计').style('color:#2CAC32')
            func2 = ui.tab('更新').style('color:orange')
        with ui.tab_panels(tabs, value=func0).classes('col self-center'):
            with ui.tab_panel(func0):

                # 原始数据
                categories = ['夏天','陈玲','潘洁','刘宇','苏志辉','蔡宏','邢佳庆','易俊希','张欣然',
                              '孙黎明','于希平','薛文','陈夏颖','袁滢','伊雅淞','郭增林','赵明','姜少珍',
                              '罗丹','秦玲玫','王政杰','於宇','朱朋朋','马昊雨','余柳冰','袁森超']
                jingdu_data = [ra1,ra2,ra3,ra4,ra5,rb1,rb2,rb3,rb4,rb5,rb6,rc1,rc2,rc3,rc4,rc5,rd1,rd2,rd3,rd4,rd5,re1,re2,re3,re4,re5]
                fandu_data = [fa1,fa2,fa3,fa4,fa5,fb1,fb2,fb3,fb4,fb5,fb6,fc1,fc2,fc3,fc4,fc5,fd1,fd2,fd3,fd4,fd5,fe1,fe2,fe3,fe4,fe5]

                chart = ui.highchart({
                    'title': {'text': '个人总积分排行榜（蓝色）'},
                    'chart': {'type': 'bar'},
                    'xAxis': {
                        'categories': categories
                    },
                    'yAxis': {
                        'tickInterval': 0.5,  # 在这里设置您想要的Y轴步长
                    },
                    'series': [
                        {'name': '精读文献数', 'data': jingdu_data, 'color': 'blue'},
                        {'name': '泛读文献数', 'data': fandu_data, 'color': '#C0C0C0'},
                    ],
                }).classes('w-full h-full')





                def on_change1_click():
                    fa1 = a1.value
                    fa2 = a2.value
                    fa3 = a3.value
                    fa4 = a4.value
                    fa5 = a5.value
                    fb1 = b1.value
                    fb2 = b2.value
                    fb3 = b3.value
                    fb4 = b4.value
                    fb5 = b5.value
                    fb6 = b6.value
                    fc1 = c1.value
                    fc2 = c2.value
                    fc3 = c3.value
                    fc4 = c4.value
                    fc5 = c5.value
                    fd1 = d1.value
                    fd2 = d2.value
                    fd3 = d3.value
                    fd4 = d4.value
                    fd5 = d5.value
                    fe1 = e1.value
                    fe2 = e2.value
                    fe3 = e3.value
                    fe4 = e4.value
                    fe5 = e5.value

                    ra1 = a11.value
                    ra2 = a12.value
                    ra3 = a13.value
                    ra4 = a14.value
                    ra5 = a15.value
                    rb1 = b11.value
                    rb2 = b12.value
                    rb3 = b13.value
                    rb4 = b14.value
                    rb5 = b15.value
                    rb6 = b16.value
                    rc1 = c11.value
                    rc2 = c12.value
                    rc3 = c13.value
                    rc4 = c14.value
                    rc5 = c15.value
                    rd1 = d11.value
                    rd2 = d12.value
                    rd3 = d13.value
                    rd4 = d14.value
                    rd5 = d15.value
                    re1 = e11.value
                    re2 = e12.value
                    re3 = e13.value
                    re4 = e14.value
                    re5 = e15.value

                    gg1 = g1.value
                    gg2 = g2.value
                    gg3 = g3.value
                    gg4 = g4.value
                    gg5 = g5.value
                    categories = ['夏天','陈玲','潘洁','刘宇','苏志辉','蔡宏','邢佳庆','易俊希','张欣然','孙黎明','于希平','薛文','陈夏颖','袁滢','伊雅淞','郭增林','赵明','姜少珍','罗丹','秦玲玫','王政杰','於宇','朱朋朋','马昊雨','余柳冰','袁森超']
                    jingdu_data = [ra1, ra2, ra3, ra4, ra5, rb1, rb2, rb3, rb4, rb5, rb6, rc1, rc2, rc3, rc4, rc5, rd1,
                                   rd2, rd3, rd4, rd5, re1, re2, re3, re4, re5]
                    fandu_data = [fa1, fa2, fa3, fa4, fa5, fb1, fb2, fb3, fb4, fb5, fb6, fc1, fc2, fc3, fc4, fc5, fd1,
                                  fd2, fd3, fd4, fd5, fe1, fe2, fe3, fe4, fe5]



                    sorted_indices = np.argsort(jingdu_data)[::-1]  # 获取排序后的索引，[::-1]表示降序排列
                    sorted_categories = [categories[i] for i in sorted_indices]
                    sorted_recommend_data = [fandu_data[i] for i in sorted_indices]
                    sorted_vote_data = [jingdu_data[i] for i in sorted_indices]
                    chart.options['xAxis']['categories'] = sorted_categories
                    chart.options['series'][0]['data'] = sorted_vote_data
                    chart.options['series'][1]['data'] = sorted_recommend_data
                    chart.update()


                button3 = ui.button('按精读数排名',on_click=on_change1_click)


                def on_change2_click():
                    fa1 = a1.value
                    fa2 = a2.value
                    fa3 = a3.value
                    fa4 = a4.value
                    fa5 = a5.value
                    fb1 = b1.value
                    fb2 = b2.value
                    fb3 = b3.value
                    fb4 = b4.value
                    fb5 = b5.value
                    fb6 = b6.value
                    fc1 = c1.value
                    fc2 = c2.value
                    fc3 = c3.value
                    fc4 = c4.value
                    fc5 = c5.value
                    fd1 = d1.value
                    fd2 = d2.value
                    fd3 = d3.value
                    fd4 = d4.value
                    fd5 = d5.value
                    fe1 = e1.value
                    fe2 = e2.value
                    fe3 = e3.value
                    fe4 = e4.value
                    fe5 = e5.value

                    ra1 = a11.value
                    ra2 = a12.value
                    ra3 = a13.value
                    ra4 = a14.value
                    ra5 = a15.value
                    rb1 = b11.value
                    rb2 = b12.value
                    rb3 = b13.value
                    rb4 = b14.value
                    rb5 = b15.value
                    rb6 = b16.value
                    rc1 = c11.value
                    rc2 = c12.value
                    rc3 = c13.value
                    rc4 = c14.value
                    rc5 = c15.value
                    rd1 = d11.value
                    rd2 = d12.value
                    rd3 = d13.value
                    rd4 = d14.value
                    rd5 = d15.value
                    re1 = e11.value
                    re2 = e12.value
                    re3 = e13.value
                    re4 = e14.value
                    re5 = e15.value

                    gg1 = g1.value
                    gg2 = g2.value
                    gg3 = g3.value
                    gg4 = g4.value
                    gg5 = g5.value
                    categories = ['夏天','陈玲','潘洁','刘宇','苏志辉','蔡宏','邢佳庆','易俊希','张欣然','孙黎明','于希平','薛文','陈夏颖','袁滢','伊雅淞','郭增林','赵明','姜少珍','罗丹','秦玲玫','王政杰','於宇','朱朋朋','马昊雨','余柳冰','袁森超']
                    jingdu_data = [ra1, ra2, ra3, ra4, ra5, rb1, rb2, rb3, rb4, rb5, rb6, rc1, rc2, rc3, rc4, rc5, rd1,
                                   rd2, rd3, rd4, rd5, re1, re2, re3, re4, re5]
                    fandu_data = [fa1, fa2, fa3, fa4, fa5, fb1, fb2, fb3, fb4, fb5, fb6, fc1, fc2, fc3, fc4, fc5, fd1,
                                  fd2, fd3, fd4, fd5, fe1, fe2, fe3, fe4, fe5]


                    sorted_indices = np.argsort(fandu_data)[::-1]  # 获取排序后的索引，[::-1]表示降序排列
                    sorted_categories = [categories[i] for i in sorted_indices]
                    sorted_recommend_data = [fandu_data[i] for i in sorted_indices]
                    sorted_vote_data = [jingdu_data[i] for i in sorted_indices]
                    chart.options['xAxis']['categories'] = sorted_categories
                    chart.options['series'][0]['data'] = sorted_vote_data
                    chart.options['series'][1]['data'] = sorted_recommend_data
                    chart.update()


                button4 = ui.button('按泛读数排名',on_click=on_change2_click)







            with ui.tab_panel(func3):


                pinjingdu_data = [ra1 / gg1 if gg1 != 0 else 0,
                                  ra2 / gg1 if gg1 != 0 else 0,
                                  ra3 / gg1 if gg1 != 0 else 0,
                                  ra4 / gg1 if gg1 != 0 else 0,
                                  ra5 / gg1 if gg1 != 0 else 0,
                                  rb1 / gg2 if gg2 != 0 else 0,
                                  rb2 / gg2 if gg2 != 0 else 0,
                                  rb3 / gg2 if gg2 != 0 else 0,
                                  rb4 / gg2 if gg2 != 0 else 0,
                                  rb5 / gg2 if gg2 != 0 else 0,
                                  rb6 / gg2 if gg2 != 0 else 0,
                                  rc1 / gg3 if gg3 != 0 else 0,
                                  rc2 / gg3 if gg3 != 0 else 0,
                                  rc3 / gg3 if gg3 != 0 else 0,
                                  rc4 / gg3 if gg3 != 0 else 0,
                                  rc5 / gg3 if gg3 != 0 else 0,
                                  rd1 / gg4 if gg4 != 0 else 0,
                                  rd2 / gg4 if gg4 != 0 else 0,
                                  rd3 / gg4 if gg4 != 0 else 0,
                                  rd4 / gg4 if gg4 != 0 else 0,
                                  rd5 / gg4 if gg4 != 0 else 0,
                                  re1 / gg5 if gg5 != 0 else 0,
                                  re2 / gg5 if gg5 != 0 else 0,
                                  re3 / gg5 if gg5 != 0 else 0,
                                  re4 / gg5 if gg5 != 0 else 0,
                                  re5 / gg5 if gg5 != 0 else 0
                                  ]
                pinfandu_data = [fa1 / gg1 if gg1 != 0 else 0,
                                 fa2 / gg1 if gg1 != 0 else 0,
                                 fa3 / gg1 if gg1 != 0 else 0,
                                 fa4 / gg1 if gg1 != 0 else 0,
                                 fa5 / gg1 if gg1 != 0 else 0,
                                 fb1 / gg2 if gg2 != 0 else 0,
                                 fb2 / gg2 if gg2 != 0 else 0,
                                 fb3 / gg2 if gg2 != 0 else 0,
                                 fb4 / gg2 if gg2 != 0 else 0,
                                 fb5 / gg2 if gg2 != 0 else 0,
                                 fb6 / gg2 if gg2 != 0 else 0,
                                 fc1 / gg3 if gg3 != 0 else 0,
                                 fc2 / gg3 if gg3 != 0 else 0,
                                 fc3 / gg3 if gg3 != 0 else 0,
                                 fc4 / gg3 if gg3 != 0 else 0,
                                 fc5 / gg3 if gg3 != 0 else 0,
                                 fd1 / gg4 if gg4 != 0 else 0,
                                 fd2 / gg4 if gg4 != 0 else 0,
                                 fd3 / gg4 if gg4 != 0 else 0,
                                 fd4 / gg4 if gg4 != 0 else 0,
                                 fd5 / gg4 if gg4 != 0 else 0,
                                 fe1 / gg5 if gg5 != 0 else 0,
                                 fe2 / gg5 if gg5 != 0 else 0,
                                 fe3 / gg5 if gg5 != 0 else 0,
                                 fe4 / gg5 if gg5 != 0 else 0,
                                 fe5 / gg5 if gg5 != 0 else 0
                                 ]

                chart2 = ui.highchart({
                    'title': {'text': '个人平均积分排行榜（紫色）'},
                    'chart': {'type': 'bar'},
                    'xAxis': {'categories': categories},
                    'yAxis': {
                        'tickInterval': 0.25,  # 在这里设置您想要的Y轴步长
                    },
                    'series': [
                        {'name': '精读文献数', 'data': pinjingdu_data, 'color': 'purple'},
                        {'name': '泛读文献数', 'data': pinfandu_data, 'color': '#C0C0C0'},
                    ],
                }).classes('w-full h-full')

                def on_change5_click():
                    fa1 = a1.value
                    fa2 = a2.value
                    fa3 = a3.value
                    fa4 = a4.value
                    fa5 = a5.value
                    fb1 = b1.value
                    fb2 = b2.value
                    fb3 = b3.value
                    fb4 = b4.value
                    fb5 = b5.value
                    fb6 = b6.value
                    fc1 = c1.value
                    fc2 = c2.value
                    fc3 = c3.value
                    fc4 = c4.value
                    fc5 = c5.value
                    fd1 = d1.value
                    fd2 = d2.value
                    fd3 = d3.value
                    fd4 = d4.value
                    fd5 = d5.value
                    fe1 = e1.value
                    fe2 = e2.value
                    fe3 = e3.value
                    fe4 = e4.value
                    fe5 = e5.value

                    ra1 = a11.value
                    ra2 = a12.value
                    ra3 = a13.value
                    ra4 = a14.value
                    ra5 = a15.value
                    rb1 = b11.value
                    rb2 = b12.value
                    rb3 = b13.value
                    rb4 = b14.value
                    rb5 = b15.value
                    rb6 = b16.value
                    rc1 = c11.value
                    rc2 = c12.value
                    rc3 = c13.value
                    rc4 = c14.value
                    rc5 = c15.value
                    rd1 = d11.value
                    rd2 = d12.value
                    rd3 = d13.value
                    rd4 = d14.value
                    rd5 = d15.value
                    re1 = e11.value
                    re2 = e12.value
                    re3 = e13.value
                    re4 = e14.value
                    re5 = e15.value

                    gg1 = g1.value
                    gg2 = g2.value
                    gg3 = g3.value
                    gg4 = g4.value
                    gg5 = g5.value
                    categories = ['夏天','陈玲','潘洁','刘宇','苏志辉','蔡宏','邢佳庆','易俊希','张欣然','孙黎明','于希平','薛文','陈夏颖','袁滢','伊雅淞','郭增林','赵明','姜少珍','罗丹','秦玲玫','王政杰','於宇','朱朋朋','马昊雨','余柳冰','袁森超']


                    pinjingdu_data = [ra1 / gg1 if gg1 != 0 else 0,
                                      ra2 / gg1 if gg1 != 0 else 0,
                                      ra3 / gg1 if gg1 != 0 else 0,
                                      ra4 / gg1 if gg1 != 0 else 0,
                                      ra5 / gg1 if gg1 != 0 else 0,
                                      rb1 / gg2 if gg2 != 0 else 0,
                                      rb2 / gg2 if gg2 != 0 else 0,
                                      rb3 / gg2 if gg2 != 0 else 0,
                                      rb4 / gg2 if gg2 != 0 else 0,
                                      rb5 / gg2 if gg2 != 0 else 0,
                                      rb6 / gg2 if gg2 != 0 else 0,
                                      rc1 / gg3 if gg3 != 0 else 0,
                                      rc2 / gg3 if gg3 != 0 else 0,
                                      rc3 / gg3 if gg3 != 0 else 0,
                                      rc4 / gg3 if gg3 != 0 else 0,
                                      rc5 / gg3 if gg3 != 0 else 0,
                                      rd1 / gg4 if gg4 != 0 else 0,
                                      rd2 / gg4 if gg4 != 0 else 0,
                                      rd3 / gg4 if gg4 != 0 else 0,
                                      rd4 / gg4 if gg4 != 0 else 0,
                                      rd5 / gg4 if gg4 != 0 else 0,
                                      re1 / gg5 if gg5 != 0 else 0,
                                      re2 / gg5 if gg5 != 0 else 0,
                                      re3 / gg5 if gg5 != 0 else 0,
                                      re4 / gg5 if gg5 != 0 else 0,
                                      re5 / gg5 if gg5 != 0 else 0
                                      ]
                    pinfandu_data = [fa1 / gg1 if gg1 != 0 else 0,
                                     fa2 / gg1 if gg1 != 0 else 0,
                                     fa3 / gg1 if gg1 != 0 else 0,
                                     fa4 / gg1 if gg1 != 0 else 0,
                                     fa5 / gg1 if gg1 != 0 else 0,
                                     fb1 / gg2 if gg2 != 0 else 0,
                                     fb2 / gg2 if gg2 != 0 else 0,
                                     fb3 / gg2 if gg2 != 0 else 0,
                                     fb4 / gg2 if gg2 != 0 else 0,
                                     fb5 / gg2 if gg2 != 0 else 0,
                                     fb6 / gg2 if gg2 != 0 else 0,
                                     fc1 / gg3 if gg3 != 0 else 0,
                                     fc2 / gg3 if gg3 != 0 else 0,
                                     fc3 / gg3 if gg3 != 0 else 0,
                                     fc4 / gg3 if gg3 != 0 else 0,
                                     fc5 / gg3 if gg3 != 0 else 0,
                                     fd1 / gg4 if gg4 != 0 else 0,
                                     fd2 / gg4 if gg4 != 0 else 0,
                                     fd3 / gg4 if gg4 != 0 else 0,
                                     fd4 / gg4 if gg4 != 0 else 0,
                                     fd5 / gg4 if gg4 != 0 else 0,
                                     fe1 / gg5 if gg5 != 0 else 0,
                                     fe2 / gg5 if gg5 != 0 else 0,
                                     fe3 / gg5 if gg5 != 0 else 0,
                                     fe4 / gg5 if gg5 != 0 else 0,
                                     fe5 / gg5 if gg5 != 0 else 0
                                     ]



                    sorted_indices2 = np.argsort(pinjingdu_data)[::-1]  # 获取排序后的索引，[::-1]表示降序排列
                    sorted_categories2 = [categories[i] for i in sorted_indices2]
                    sorted_recommend_data2 = [pinfandu_data[i] for i in sorted_indices2]
                    sorted_vote_data2 = [pinjingdu_data[i] for i in sorted_indices2]
                    chart2.options['xAxis']['categories'] = sorted_categories2
                    chart2.options['series'][0]['data'] = sorted_vote_data2
                    chart2.options['series'][1]['data'] = sorted_recommend_data2
                    chart2.update()

                button5= ui.button('按精读数排名', on_click=on_change5_click)

                def on_change6_click():
                    fa1 = a1.value
                    fa2 = a2.value
                    fa3 = a3.value
                    fa4 = a4.value
                    fa5 = a5.value
                    fb1 = b1.value
                    fb2 = b2.value
                    fb3 = b3.value
                    fb4 = b4.value
                    fb5 = b5.value
                    fb6 = b6.value
                    fc1 = c1.value
                    fc2 = c2.value
                    fc3 = c3.value
                    fc4 = c4.value
                    fc5 = c5.value
                    fd1 = d1.value
                    fd2 = d2.value
                    fd3 = d3.value
                    fd4 = d4.value
                    fd5 = d5.value
                    fe1 = e1.value
                    fe2 = e2.value
                    fe3 = e3.value
                    fe4 = e4.value
                    fe5 = e5.value

                    ra1 = a11.value
                    ra2 = a12.value
                    ra3 = a13.value
                    ra4 = a14.value
                    ra5 = a15.value
                    rb1 = b11.value
                    rb2 = b12.value
                    rb3 = b13.value
                    rb4 = b14.value
                    rb5 = b15.value
                    rb6 = b16.value
                    rc1 = c11.value
                    rc2 = c12.value
                    rc3 = c13.value
                    rc4 = c14.value
                    rc5 = c15.value
                    rd1 = d11.value
                    rd2 = d12.value
                    rd3 = d13.value
                    rd4 = d14.value
                    rd5 = d15.value
                    re1 = e11.value
                    re2 = e12.value
                    re3 = e13.value
                    re4 = e14.value
                    re5 = e15.value

                    gg1 = g1.value
                    gg2 = g2.value
                    gg3 = g3.value
                    gg4 = g4.value
                    gg5 = g5.value
                    categories = ['夏天','陈玲','潘洁','刘宇','苏志辉','蔡宏','邢佳庆','易俊希','张欣然','孙黎明','于希平','薛文','陈夏颖','袁滢','伊雅淞','郭增林','赵明','姜少珍','罗丹','秦玲玫','王政杰','於宇','朱朋朋','马昊雨','余柳冰','袁森超']

                    pinjingdu_data = [ra1 / gg1 if gg1 != 0 else 0,
                                      ra2 / gg1 if gg1 != 0 else 0,
                                      ra3 / gg1 if gg1 != 0 else 0,
                                      ra4 / gg1 if gg1 != 0 else 0,
                                      ra5 / gg1 if gg1 != 0 else 0,
                                      rb1 / gg2 if gg2 != 0 else 0,
                                      rb2 / gg2 if gg2 != 0 else 0,
                                      rb3 / gg2 if gg2 != 0 else 0,
                                      rb4 / gg2 if gg2 != 0 else 0,
                                      rb5 / gg2 if gg2 != 0 else 0,
                                      rb6 / gg2 if gg2 != 0 else 0,
                                      rc1 / gg3 if gg3 != 0 else 0,
                                      rc2 / gg3 if gg3 != 0 else 0,
                                      rc3 / gg3 if gg3 != 0 else 0,
                                      rc4 / gg3 if gg3 != 0 else 0,
                                      rc5 / gg3 if gg3 != 0 else 0,
                                      rd1 / gg4 if gg4 != 0 else 0,
                                      rd2 / gg4 if gg4 != 0 else 0,
                                      rd3 / gg4 if gg4 != 0 else 0,
                                      rd4 / gg4 if gg4 != 0 else 0,
                                      rd5 / gg4 if gg4 != 0 else 0,
                                      re1 / gg5 if gg5 != 0 else 0,
                                      re2 / gg5 if gg5 != 0 else 0,
                                      re3 / gg5 if gg5 != 0 else 0,
                                      re4 / gg5 if gg5 != 0 else 0,
                                      re5 / gg5 if gg5 != 0 else 0
                                      ]
                    pinfandu_data = [fa1 / gg1 if gg1 != 0 else 0,
                                     fa2 / gg1 if gg1 != 0 else 0,
                                     fa3 / gg1 if gg1 != 0 else 0,
                                     fa4 / gg1 if gg1 != 0 else 0,
                                     fa5 / gg1 if gg1 != 0 else 0,
                                     fb1 / gg2 if gg2 != 0 else 0,
                                     fb2 / gg2 if gg2 != 0 else 0,
                                     fb3 / gg2 if gg2 != 0 else 0,
                                     fb4 / gg2 if gg2 != 0 else 0,
                                     fb5 / gg2 if gg2 != 0 else 0,
                                     fb6 / gg2 if gg2 != 0 else 0,
                                     fc1 / gg3 if gg3 != 0 else 0,
                                     fc2 / gg3 if gg3 != 0 else 0,
                                     fc3 / gg3 if gg3 != 0 else 0,
                                     fc4 / gg3 if gg3 != 0 else 0,
                                     fc5 / gg3 if gg3 != 0 else 0,
                                     fd1 / gg4 if gg4 != 0 else 0,
                                     fd2 / gg4 if gg4 != 0 else 0,
                                     fd3 / gg4 if gg4 != 0 else 0,
                                     fd4 / gg4 if gg4 != 0 else 0,
                                     fd5 / gg4 if gg4 != 0 else 0,
                                     fe1 / gg5 if gg5 != 0 else 0,
                                     fe2 / gg5 if gg5 != 0 else 0,
                                     fe3 / gg5 if gg5 != 0 else 0,
                                     fe4 / gg5 if gg5 != 0 else 0,
                                     fe5 / gg5 if gg5 != 0 else 0
                                     ]



                    sorted_indices2 = np.argsort(pinfandu_data)[::-1]  # 获取排序后的索引，[::-1]表示降序排列
                    sorted_categories2 = [categories[i] for i in sorted_indices2]
                    sorted_recommend_data2 = [pinfandu_data[i] for i in sorted_indices2]
                    sorted_vote_data2 = [pinjingdu_data[i] for i in sorted_indices2]
                    chart2.options['xAxis']['categories'] = sorted_categories2
                    chart2.options['series'][0]['data'] = sorted_vote_data2
                    chart2.options['series'][1]['data'] = sorted_recommend_data2
                    chart2.update()

                button6 = ui.button('按泛读数排名', on_click=on_change6_click)


            with ui.tab_panel(func1):
                categories = ['夏天','陈玲','潘洁','刘宇','苏志辉','蔡宏','邢佳庆','易俊希','张欣然','孙黎明','于希平','薛文','陈夏颖','袁滢','伊雅淞','郭增林','赵明','姜少珍','罗丹','秦玲玫','王政杰','於宇','朱朋朋','马昊雨','余柳冰','袁森超']
                jingdu_data = [ra1, ra2, ra3, ra4, ra5, rb1, rb2, rb3, rb4, rb5, rb6, rc1, rc2, rc3, rc4, rc5, rd1, rd2,
                               rd3, rd4, rd5, re1, re2, re3, re4, re5]
                fandu_data = [fa1, fa2, fa3, fa4, fa5, fb1, fb2, fb3, fb4, fb5, fb6, fc1, fc2, fc3, fc4, fc5, fd1, fd2,
                              fd3, fd4, fd5, fe1, fe2, fe3, fe4, fe5]

                # 过滤掉值为0的数据
                filtered_data = [(name, value) for name, value in zip(categories, jingdu_data) if value != 0]
                # 分离过滤后的数据
                categories_filtered, jingdu_data_filtered = zip(*filtered_data) if filtered_data else ((), ())

                # 创建 Highchart
                piechart = ui.highchart({
                    'title': {'text': '个人精读文献占比'},
                    'chart': {'type': 'pie'},
                    'series': [{
                        'name': '推荐文献数',
                        'data': [{'name': name, 'y': value} for name, value in zip(categories_filtered, jingdu_data_filtered)],
                    }],
                }).classes('w-full h-84')

                filtered_data2 = [(name, value) for name, value in zip(categories, fandu_data) if value != 0]
                categories_filtered2, fandu_data_filtered = zip(*filtered_data2) if filtered_data2 else ((), ())
                piechart2 = ui.highchart({
                    'title': {'text': '个人泛读文献占比'},
                    'chart': {'type': 'pie'},
                    'series': [{
                        'name': '泛读文献数',
                        'data': [{'name': name, 'y': value} for name, value in zip(categories_filtered2, fandu_data_filtered)],
                    }],
                }).classes('w-full h-84')









            with ui.tab_panel(func2):
                with ui.row():

                    with ui.column():
                        a1 = ui.number(label='夏天泛读文献数', value=data['a1'], format='%.2f')
                        a2 = ui.number(label='陈玲泛读文献数', value=data['a2'], format='%.2f')
                        a3 = ui.number(label='潘洁泛读文献数', value=data['a3'], format='%.2f')
                        a4 = ui.number(label='刘宇泛读文献数', value=data['a4'], format='%.2f')
                        a5 = ui.number(label='苏志辉泛读文献数', value=data['a5'], format='%.2f')
                    with ui.column():
                        b1 = ui.number(label='蔡宏泛读文献数', value=data['b1'], format='%.2f')
                        b2 = ui.number(label='邢佳庆泛读文献数', value=data['b2'], format='%.2f')
                        b3 = ui.number(label='易俊希泛读文献数', value=data['b3'], format='%.2f')
                        b4 = ui.number(label='张欣然泛读文献数', value=data['b4'], format='%.2f')
                        b5 = ui.number(label='孙黎明泛读文献数', value=data['b5'], format='%.2f')
                        b6 = ui.number(label='于希平泛读文献数', value=data['b6'], format='%.2f')
                    with ui.column():
                        c1 = ui.number(label='薛文泛读文献数', value=data['c1'], format='%.2f')
                        c2 = ui.number(label='陈夏颖泛读文献数', value=data['c2'], format='%.2f')
                        c3 = ui.number(label='袁滢泛读文献数', value=data['c3'], format='%.2f')
                        c4 = ui.number(label='伊雅淞泛读文献数', value=data['c4'], format='%.2f')
                        c5 = ui.number(label='郭增林泛读文献数', value=data['c5'], format='%.2f')
                    with ui.column():
                        d1 = ui.number(label='赵明泛读文献数', value=data['d1'], format='%.2f')
                        d2 = ui.number(label='姜少珍泛读文献数', value=data['d2'], format='%.2f')
                        d3 = ui.number(label='罗丹泛读文献数', value=data['d3'], format='%.2f')
                        d4 = ui.number(label='秦玲玫泛读文献数', value=data['d4'], format='%.2f')
                        d5 = ui.number(label='王政杰泛读文献数', value=data['d5'], format='%.2f')
                    with ui.column():
                        e1 = ui.number(label='於宇泛读文献数', value=data['e1'], format='%.2f')
                        e2 = ui.number(label='朱朋朋泛读文献数', value=data['e2'], format='%.2f')
                        e3 = ui.number(label='马昊雨泛读文献数', value=data['e3'], format='%.2f')
                        e4 = ui.number(label='余柳冰泛读文献数', value=data['e4'], format='%.2f')
                        e5 = ui.number(label='袁森超泛读文献数', value=data['e5'], format='%.2f')

                with ui.row():
                    with ui.column():
                        ui.label("   ")
                        ui.label("   ")
                        a11 = ui.number(label='夏天精读数', value=data['a11'], format='%.2f')
                        a12 = ui.number(label='陈玲精读数', value=data['a12'], format='%.2f')
                        a13 = ui.number(label='潘洁精读数', value=data['a13'], format='%.2f')
                        a14 = ui.number(label='刘宇精读数', value=data['a14'], format='%.2f')
                        a15 = ui.number(label='苏志辉精读数', value=data['a15'], format='%.2f')
                    with ui.column():
                        ui.label("   ")
                        ui.label("   ")
                        b11 = ui.number(label='蔡宏精读数', value=data['b11'], format='%.2f')
                        b12 = ui.number(label='邢佳庆精读数', value=data['b12'], format='%.2f')
                        b13 = ui.number(label='易俊希精读数', value=data['b13'], format='%.2f')
                        b14 = ui.number(label='张欣然精读数', value=data['b14'], format='%.2f')
                        b15 = ui.number(label='孙黎明精读数', value=data['b15'], format='%.2f')
                        b16 = ui.number(label='于希平精读数', value=data['b16'], format='%.2f')
                        ui.label("   ")
                        ui.label("   ")
                        ui.label("   ")
                        ui.label("   ")
                    with ui.column():
                        ui.label("   ")
                        ui.label("   ")
                        c11 = ui.number(label='薛文精读数', value=data['c11'], format='%.2f')
                        c12 = ui.number(label='陈夏颖精读数', value=data['c12'], format='%.2f')
                        c13 = ui.number(label='袁滢精读数', value=data['c13'], format='%.2f')
                        c14 = ui.number(label='伊雅淞精读数', value=data['c14'], format='%.2f')
                        c15 = ui.number(label='郭增林精读数', value=data['c15'], format='%.2f')
                    with ui.column():
                        ui.label("   ")
                        ui.label("   ")
                        d11 = ui.number(label='赵明精读数', value=data['d11'], format='%.2f')
                        d12 = ui.number(label='姜少珍精读数', value=data['d12'], format='%.2f')
                        d13 = ui.number(label='罗丹精读数', value=data['d13'], format='%.2f')
                        d14 = ui.number(label='秦玲玫精读数', value=data['d14'], format='%.2f')
                        d15 = ui.number(label='王政杰精读数', value=data['d15'], format='%.2f')
                    with ui.column():
                        ui.label("   ")
                        ui.label("   ")
                        e11 = ui.number(label='於宇精读数', value=data['e11'], format='%.2f')
                        e12 = ui.number(label='朱朋朋精读数', value=data['e12'], format='%.2f')
                        e13 = ui.number(label='马昊雨精读数', value=data['e13'], format='%.2f')
                        e14 = ui.number(label='余柳冰精读数', value=data['e14'], format='%.2f')
                        e15 = ui.number(label='袁森超精读数', value=data['e15'], format='%.2f')

                with ui.row():
                    with ui.row():
                        g1 = ui.number(label='group A轮转次数', value=data['g1'], format='%.2f')
                        g2 = ui.number(label='group B轮转次数', value=data['g2'], format='%.2f')
                        g3 = ui.number(label='group C轮转次数', value=data['g3'], format='%.2f')
                        g4 = ui.number(label='group D轮转次数', value=data['g4'], format='%.2f')
                        g5 = ui.number(label='group E轮转次数', value=data['g5'], format='%.2f')


                def on_end_button_click():
                    fa1 = a1.value
                    fa2 = a2.value
                    fa3 = a3.value
                    fa4 = a4.value
                    fa5 = a5.value
                    fb1 = b1.value
                    fb2 = b2.value
                    fb3 = b3.value
                    fb4 = b4.value
                    fb5 = b5.value
                    fb6 = b6.value
                    fc1 = c1.value
                    fc2 = c2.value
                    fc3 = c3.value
                    fc4 = c4.value
                    fc5 = c5.value
                    fd1 = d1.value
                    fd2 = d2.value
                    fd3 = d3.value
                    fd4 = d4.value
                    fd5 = d5.value
                    fe1 = e1.value
                    fe2 = e2.value
                    fe3 = e3.value
                    fe4 = e4.value
                    fe5 = e5.value

                    ra1 = a11.value
                    ra2 = a12.value
                    ra3 = a13.value
                    ra4 = a14.value
                    ra5 = a15.value
                    rb1 = b11.value
                    rb2 = b12.value
                    rb3 = b13.value
                    rb4 = b14.value
                    rb5 = b15.value
                    rb6 = b16.value
                    rc1 = c11.value
                    rc2 = c12.value
                    rc3 = c13.value
                    rc4 = c14.value
                    rc5 = c15.value
                    rd1 = d11.value
                    rd2 = d12.value
                    rd3 = d13.value
                    rd4 = d14.value
                    rd5 = d15.value
                    re1 = e11.value
                    re2 = e12.value
                    re3 = e13.value
                    re4 = e14.value
                    re5 = e15.value

                    gg1 = g1.value
                    gg2 = g2.value
                    gg3 = g3.value
                    gg4 = g4.value
                    gg5 = g5.value


                    categories = ['夏天','陈玲','潘洁','刘宇','苏志辉','蔡宏','邢佳庆','易俊希',
                                  '张欣然','孙黎明','于希平','薛文','陈夏颖','袁滢','伊雅淞','郭增林','赵明','姜少珍',
                                  '罗丹','秦玲玫','王政杰','於宇','朱朋朋','马昊雨','余柳冰','袁森超']
                    jingdu_data = [ra1, ra2, ra3, ra4, ra5, rb1, rb2, rb3, rb4, rb5, rb6, rc1, rc2, rc3, rc4, rc5, rd1,
                                   rd2, rd3, rd4, rd5, re1, re2, re3, re4, re5]
                    fandu_data = [fa1, fa2, fa3, fa4, fa5, fb1, fb2, fb3, fb4, fb5, fb6, fc1, fc2, fc3, fc4, fc5, fd1,
                                  fd2, fd3, fd4, fd5, fe1, fe2, fe3, fe4, fe5]
                    pinjingdu_data = [ra1 / gg1 if gg1 != 0 else 0,
                                      ra2 / gg1 if gg1 != 0 else 0,
                                      ra3 / gg1 if gg1 != 0 else 0,
                                      ra4 / gg1 if gg1 != 0 else 0,
                                      ra5 / gg1 if gg1 != 0 else 0,
                                      rb1 / gg2 if gg2 != 0 else 0,
                                      rb2 / gg2 if gg2 != 0 else 0,
                                      rb3 / gg2 if gg2 != 0 else 0,
                                      rb4 / gg2 if gg2 != 0 else 0,
                                      rb5 / gg2 if gg2 != 0 else 0,
                                      rb6 / gg2 if gg2 != 0 else 0,
                                      rc1 / gg3 if gg3 != 0 else 0,
                                      rc2 / gg3 if gg3 != 0 else 0,
                                      rc3 / gg3 if gg3 != 0 else 0,
                                      rc4 / gg3 if gg3 != 0 else 0,
                                      rc5 / gg3 if gg3 != 0 else 0,
                                      rd1 / gg4 if gg4 != 0 else 0,
                                      rd2 / gg4 if gg4 != 0 else 0,
                                      rd3 / gg4 if gg4 != 0 else 0,
                                      rd4 / gg4 if gg4 != 0 else 0,
                                      rd5 / gg4 if gg4 != 0 else 0,
                                      re1 / gg5 if gg5 != 0 else 0,
                                      re2 / gg5 if gg5 != 0 else 0,
                                      re3 / gg5 if gg5 != 0 else 0,
                                      re4 / gg5 if gg5 != 0 else 0,
                                      re5 / gg5 if gg5 != 0 else 0
                                      ]
                    pinfandu_data = [fa1 / gg1 if gg1 != 0 else 0,
                                     fa2 / gg1 if gg1 != 0 else 0,
                                     fa3 / gg1 if gg1 != 0 else 0,
                                     fa4 / gg1 if gg1 != 0 else 0,
                                     fa5 / gg1 if gg1 != 0 else 0,
                                     fb1 / gg2 if gg2 != 0 else 0,
                                     fb2 / gg2 if gg2 != 0 else 0,
                                     fb3 / gg2 if gg2 != 0 else 0,
                                     fb4 / gg2 if gg2 != 0 else 0,
                                     fb5 / gg2 if gg2 != 0 else 0,
                                     fb6 / gg2 if gg2 != 0 else 0,
                                     fc1 / gg3 if gg3 != 0 else 0,
                                     fc2 / gg3 if gg3 != 0 else 0,
                                     fc3 / gg3 if gg3 != 0 else 0,
                                     fc4 / gg3 if gg3 != 0 else 0,
                                     fc5 / gg3 if gg3 != 0 else 0,
                                     fd1 / gg4 if gg4 != 0 else 0,
                                     fd2 / gg4 if gg4 != 0 else 0,
                                     fd3 / gg4 if gg4 != 0 else 0,
                                     fd4 / gg4 if gg4 != 0 else 0,
                                     fd5 / gg4 if gg4 != 0 else 0,
                                     fe1 / gg5 if gg5 != 0 else 0,
                                     fe2 / gg5 if gg5 != 0 else 0,
                                     fe3 / gg5 if gg5 != 0 else 0,
                                     fe4 / gg5 if gg5 != 0 else 0,
                                     fe5 / gg5 if gg5 != 0 else 0
                                     ]


                    # 修改图表
                    sorted_indices = np.argsort(jingdu_data)[::-1]  # 获取排序后的索引，[::-1]表示降序排列
                    sorted_categories = [categories[i] for i in sorted_indices]
                    sorted_recommend_data = [fandu_data[i] for i in sorted_indices]
                    sorted_vote_data = [jingdu_data[i] for i in sorted_indices]
                    chart.options['xAxis']['categories'] = sorted_categories
                    chart.options['series'][0]['data'] = sorted_vote_data
                    chart.options['series'][1]['data'] = sorted_recommend_data
                    chart.update()

                    sorted_indices2 = np.argsort(pinjingdu_data)[::-1]  # 获取排序后的索引，[::-1]表示降序排列
                    sorted_categories2 = [categories[i] for i in sorted_indices2]
                    sorted_recommend_data2 = [pinfandu_data[i] for i in sorted_indices2]
                    sorted_vote_data2 = [pinjingdu_data[i] for i in sorted_indices2]
                    chart2.options['xAxis']['categories'] = sorted_categories2
                    chart2.options['series'][0]['data'] = sorted_vote_data2
                    chart2.options['series'][1]['data'] = sorted_recommend_data2
                    chart2.update()

                    filtered_data = [(name, value) for name, value in zip(categories, jingdu_data) if value != 0]
                    categories_filtered, jingdu_data_filtered = zip(*filtered_data) if filtered_data else ((), ())
                    piechart.options['series'][0]['data'] = [{'name': name, 'y': value} for name, value in
                                                             zip(categories_filtered, jingdu_data_filtered)]
                    piechart.update()

                    filtered_data2 = [(name, value) for name, value in zip(categories, fandu_data) if value != 0]
                    categories_filtered2, fandu_data_filtered = zip(*filtered_data2) if filtered_data2 else ((), ())
                    piechart2.options['series'][0]['data'] = [{'name': name, 'y': value} for name, value in
                                                             zip(categories_filtered2, fandu_data_filtered)]
                    piechart2.update()

                    def save_data():
                        data['a1'] = a1.value
                        data['a2'] = a2.value
                        data['a3'] = a3.value
                        data['a4'] = a4.value
                        data['a5'] = a5.value
                        data['b1'] = b1.value
                        data['b2'] = b2.value
                        data['b3'] = b3.value
                        data['b4'] = b4.value
                        data['b5'] = b5.value
                        data['b6'] = b6.value
                        data['c1'] = c1.value
                        data['c2'] = c2.value
                        data['c3'] = c3.value
                        data['c4'] = c4.value
                        data['c5'] = c5.value
                        data['d1'] = d1.value
                        data['d2'] = d2.value
                        data['d3'] = d3.value
                        data['d4'] = d4.value
                        data['d5'] = d5.value
                        data['e1'] = e1.value
                        data['e2'] = e2.value
                        data['e3'] = e3.value
                        data['e4'] = e4.value
                        data['e5'] = e5.value

                        data['a11'] = a11.value
                        data['a12'] = a12.value
                        data['a13'] = a13.value
                        data['a14'] = a14.value
                        data['a15'] = a15.value
                        data['b11'] = b11.value
                        data['b12'] = b12.value
                        data['b13'] = b13.value
                        data['b14'] = b14.value
                        data['b15'] = b15.value
                        data['b16'] = b16.value
                        data['c11'] = c11.value
                        data['c12'] = c12.value
                        data['c13'] = c13.value
                        data['c14'] = c14.value
                        data['c15'] = c15.value
                        data['d11'] = d11.value
                        data['d12'] = d12.value
                        data['d13'] = d13.value
                        data['d14'] = d14.value
                        data['d15'] = d15.value
                        data['e11'] = e11.value
                        data['e12'] = e12.value
                        data['e13'] = e13.value
                        data['e14'] = e14.value
                        data['e15'] = e15.value

                        data['g1'] = g1.value
                        data['g2'] = g2.value
                        data['g3'] = g3.value
                        data['g4'] = g4.value
                        data['g5'] = g5.value

                        with open(data_file, 'wb') as file:
                            pickle.dump(data, file)

                    save_data()



                button2 = ui.button('更改', on_click=on_end_button_click)









ui_main()
ui.run()
