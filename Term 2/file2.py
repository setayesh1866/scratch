def get_info():
    return input('Enter ur information:("name family age")\n').split()


info = get_info() 


template = f"""Name {info[0]}
Last: {info[1]}
Age: {info[2]}
*******************
"""
file = open('name.txt', 'a')
file.write(template)
file.close()