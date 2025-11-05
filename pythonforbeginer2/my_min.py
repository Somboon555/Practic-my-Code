def my_min(iterable1,iterable2):
    if len(iterable1) < len(iterable2):
        resoult=[]
        my_pop=len(iterable2)-len(iterable1)
        for _  in my_pop:
            iterable2=iterable2.pop()
    for i in len(iterable1):
        resoult=(iterable1[i],iterable2[i])
    else     :
        resoult=[]
        my_pop=len(iterable1)-len(iterable2)
        for _  in my_pop:
            iterable1=iterable1.pop()
    for i in len(iterable2):
        resoult=(iterable1[i],iterable2[i])
