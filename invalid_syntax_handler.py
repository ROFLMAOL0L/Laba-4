def check(n):
    n = n.lower()
    ns = '0123456789'
    fs = '+*/^'
    fsm = '-+*/^'
    N = n
    if ' ' in n:
        return ('Error: spaces not available')
    elif len(n.replace(' ','')) == 0:
        return ('Error: string is empty')
    elif n.count('(') != n.count(')'):
        if n.count('(') > n.count(')'):
            return ('Error: there are more opening brackets than closing brackets')
        else:
            return ('Error: there are more closing brackets than opening brackets')
    else:
        n = n.replace('sin(', '')
        n = n.replace('cos(', '')
        n = n.replace('log(', '')
        n = n.replace('lg(', '')
        n = n.replace('ln(', '')
        n = n.replace('x', '')
        n = n.replace('(', '')
        n = n.replace(')', '')
        n = n.replace('+', '')
        n = n.replace('-', '')
        n = n.replace('*', '')
        n = n.replace('/', '')
        n = n.replace('^', '')
        n = n.replace('0', '')
        n = n.replace('1', '')
        n = n.replace('2', '')
        n = n.replace('3', '')
        n = n.replace('4', '')
        n = n.replace('5', '')
        n = n.replace('6', '')
        n = n.replace('7', '')
        n = n.replace('8', '')
        n = n.replace('9', '')
        n = n.replace('.', '')
        n = n.replace(',', '')
        if len(n) == 0:
            n = N
            n = n.replace('**', '^')
            n = n.replace('x(', 'x*(')
            n = n.replace('0(', '0*(')
            n = n.replace('1(', '1*(')
            n = n.replace('2(', '2*(')
            n = n.replace('3(', '3*(')
            n = n.replace('4(', '4*(')
            n = n.replace('5(', '5*(')
            n = n.replace('6(', '6*(')
            n = n.replace('7(', '7*(')
            n = n.replace('8(', '8*(')
            n = n.replace('9(', '9*(')
            n = n.replace(')(', ')*(')
            n = n.replace('x-', 'x+-')
            n = n.replace('0-', '0+-')
            n = n.replace('1-', '1+-')
            n = n.replace('2-', '2+-')
            n = n.replace('3-', '3+-')
            n = n.replace('4-', '4+-')
            n = n.replace('5-', '5+-')
            n = n.replace('6-', '6+-')
            n = n.replace('7-', '7+-')
            n = n.replace('8-', '8+-')
            n = n.replace('9-', '9+-')
            n = n.replace(')-', ')+-')
            if n[0] in '+*/^).':
                return ('Error: invalid first symbol')
            elif n[-1] in '+-*/^(.':
                return ('Error: invalid last symbol')
            elif '--' in n:
                return ('Error: double minus not available')
            for i in range(len(n)-1):
                if (n[i] in fs) and (n[i+1] in fs): # ++ ** // ^^ etc
                    return ('Error: double function not available')
                elif (n[i] in fsm) and (n[i+1] == ')'): # -) +) *) /) ^)
                    return ('Error: the closing bracket or the character before it is incorrect')
                elif (n[i] == '(') and (n[i+1] in fs): # (+ (* (/ (^
                    return ('Error: the opening bracket or the character after it is incorrect')
                elif (n[i] in ns) and (n[i+1] == 'x'): # 0x 1x 2x etc
                    return ("Error: 'x' cannot be next to a digit")
                elif (n[i] == 'x') and (n[i+1] in ns): # x0 x1 x2 etc
                    return ('Error: digit cannot be next to "x"')
                elif (n[i] == '.') and ((n[i+1] not in ns) or (n[i-1] not in ns)): # x.4  4.x  ).4  4.( etc
                    return ('Error: the dot is in the wrong place')
                elif (n[i] == '(') and (n[i+1] == ')'): # ()
                    return ('Error: string cannot contain empty brackets')
                elif (n[i] == 'x') and (n[i+1] == 'x'): # xx
                    return ("Error: there can't be more than one 'x' in a row")
            return (n)
        else:
            return ('Error: found these invalid characters - ' + n)
