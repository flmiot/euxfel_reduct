import os
import yaml

base = r'2699_81'

base_files = os.listdir(base)

for i in range(1, 104+1):
    folder_name = r'2699_{:0>3d}'.format(i)

    try:
        os.mkdir(folder_name)
    except Exception as e:
        print(e)

    for f in base_files:
        with open(os.path.join(base, f), 'rb') as file:
            b = file.read()

        with open(os.path.join(folder_name, f), 'wb') as file:
            file.write(b)


    with open(os.path.join(base, '01_filter.yml'), 'r') as file:
        config = yaml.load(file.read(), Loader = yaml.SafeLoader)
    config['directory'] = r'/pnfs/xfel.eu/exfel/archive/XFEL/raw/FXE/202022/p002699/r{:0>4d}/'.format(i)
    with open(os.path.join(folder_name, '01_filter.yml'), 'w+') as file:
        yaml.dump(config, file, default_flow_style=False)


    with open(os.path.join(base, 'Makefile'), 'r') as file:
        l = list(file.readlines())

    print(l)
    l[2] = 'SCRATCH = /home/$(USER)/scratch/tmp/{}\n'.format(folder_name)

    with open(os.path.join(folder_name, 'Makefile'), 'w+') as file:
        file.write("".join(l))

    print(l)
