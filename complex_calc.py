
def calc(a,b,op):
    try:
        match op:
            case '+':
                msg_text = a + b
            case '-':
                msg_text = a - b
            case '/':
                msg_text = a / b
            case '*':
                msg_text = a * b
    except Exception as ex:
        msg_text = 'На ноль делить нельзя!'

    return msg_text