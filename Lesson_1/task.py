
def foo(w,l,h):
    if  l > 200:
        print('Find a box for ski')
    elif (w > 15 and w < 50) or (h > 15 and h < 50) or (l > 15 and l < 50):
        print('Box 2')
    elif w < 15 and l < 15 and h < 15:
        print('Box 1')
    else:
        print('Standart box 3')


foo(45, 210, 15)