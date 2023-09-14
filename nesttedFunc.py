def outerFunc():
    first_name ='vetri'
    def innerFunc():
        last_name = 'vel'
        name =first_name+last_name
        return name
    return innerFunc
ob = outerFunc()
print(ob())