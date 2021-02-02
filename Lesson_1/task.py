
def foo(w,l,h):
    if w < 15 and l < 15 and h < 15:
        print('Box 1')
    elif (w > 15 and w < 50) or (h > 15 and h < 50) or (l > 15 and l < 50):
        print('Box 2')
    elif l > 200:
        print('Find a box for ski')
    else:
        print('Standart box 3')


foo(25, 36, 5)