#x = [-6,-4,-2,0,2,4,6,8,10,12]
#y = [2,1,4,2,-4,4,6,8,4,2]
#n = 'какая-то формула'
#xlname = 'название файла'
def deix(x, y, n, file_name): #data entry in xlsx
    if (not isinstance(x, list)) and (not isinstance(y, list)):
        return('Error: y and x are not lists')
    elif not isinstance(x, list):
        return('Error: x is not a list')
    elif not isinstance(y, list):
        return('Error: y is not a list')
    elif (len(x) == 0) and (len(y) == 0):
        return('Error: the lengths of x and y lists are 0')
    elif len(x) == 0:
        return('Error: list length x is 0')
    elif len(y) == 0:
        return('Error: list length y is 0')
    elif len(x) != len(y):
        return('Error: lists x and y are not the same length')
    elif not isinstance(n, str):
        return('Error: n is not a string')
    elif (n == '') or (n == ' '):
        return('Error: n is an empty string')
    elif not isinstance(file_name, str):
        return('Error: file_name is not a string')
    elif (file_name == '') or (file_name == ' '):
        return('Error: file_name is an empty string')
    else:
        #print(x)
        #print(y)
        #print(n)
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
        wb.save(f'{file_name}.xlsx')
        return('Success')
#deix(x, y, n)

