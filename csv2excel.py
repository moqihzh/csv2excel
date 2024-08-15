import sys

import pandas as pd


def csv2excel(file_path: str):
    if file_path:
        lines = pd.read_csv(file_path)
        if sys.platform == 'win32':
            file_name = file_path.split('\\')[-1].split('.')[0]
        elif sys.platform == 'linux':
            file_name = file_path.split('/')[-1].split('.')[0]
        pd.DataFrame(lines).to_excel(f'./{file_name}.xlsx', sheet_name='Sheet1', index=False)
        return "转换成功"
    else:
        print('文件名为空,请重新输入')


if __name__ == '__main__':
    file_path = sys.argv[1:]
    csv2excel(file_path)
