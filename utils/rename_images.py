import os

os.chdir('/Users/pipbbaale/Documents/SchoolSite/images')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_title = f_name.replace(',','_').replace('-','_').replace(' ','_')    

    # f_title = f_title.strip()

    # print('{}{}'.format(f_title, f_ext))

    # new_name = ('{}{}'.format(f_title, f_ext))
    # os.rename(f, new_name)