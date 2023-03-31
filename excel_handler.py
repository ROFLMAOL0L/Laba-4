#x = [-6,-4,-2,0,2,4,6,8,10,12]
#y = [2,1,4,2,-4,4,6,8,4,2]
#n = 'какая-то формула'
def deix(x, y, n): #data entry in xlsx
    if (not isinstance(x, list)) and (not isinstance(y, list)):
        return(print('ошибка, y и x не являются списками'))
    elif not isinstance(x, list):
        return(print('ошибка, x не является списком'))
    elif not isinstance(y, list):
        return(print('ошибка, y не является списком'))
    elif (len(x) == 0) and (len(y) == 0):
        return(print('ошибка, длины списков х и у равны 0'))
    elif len(x) == 0:
        return(print('ошибка, длина списка х равна 0'))
    elif len(y) == 0:
        return(print('ошибка, длина списка у равна 0'))
    elif len(x) != len(y):
        return(print('ошибка, длины списков х и у не равны'))
    elif not isinstance(n, str):
        return(print('ошибка, n не является строкой'))
    elif (n == '') or (n == ' '):
        return(print('ошибка, n является пустой строкой'))
    else:
        #print(x)
        #print(y)
        #print(n)
        xlname = input('введите имя xlsx файла - ')
        from openpyxl import Workbook
        from openpyxl.chart import LineChart, Reference
        wb = Workbook()
        ws = wb.active
        ws.append(['x', 'y'])
        for i in range(len(x)):
            ws.append([x[i], y[i]])
        values = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(y)+1)
        categor = Reference(ws, min_col=1, min_row=2, max_row=len(x)+1)
        chart = LineChart()
        chart.add_data(values, titles_from_data=True)
        chart.set_categories(categor)
        chart.title = f'y = {n}'
        chart.style = 1
        chart.x_axis.title = "ось X"
        chart.y_axis.title = "ось Y"
        chart.width = 43
        chart.height = 23
        ws.add_chart(chart, "D2")
        wb.save(f'{xlname}.xlsx')
        return(print('файл xlsx создан'))
#deix(x, y, n)

