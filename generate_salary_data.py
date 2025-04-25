import pandas as pd

# 定义员工基础信息（从输入的Excel文件中提取）
data = [
    {"工号": "189806", "姓名": "马萍(玟七)", "层级": "M3"},
    {"工号": "22833", "姓名": "李俊锋", "层级": "P7"},
    {"工号": "20424", "姓名": "张祎", "层级": "P6"},
    {"工号": "27781", "姓名": "罗昊天", "层级": "P6"},
    {"工号": "18962", "姓名": "曹帅", "层级": "P7"},
    {"工号": "18679", "姓名": "刘奇", "层级": "P6"}
]

# 生成测试数据
def generate_test_data(employee_data):
    test_data = []
    for emp in employee_data:
        if emp['层级'] == 'P6':
            base_salary = 20000
        elif emp['层级'] == 'P7':
            base_salary = 30000
        else:  # M3
            base_salary = 40000
        
        record = {
            '员工工号': emp['工号'],
            '姓名': emp['姓名'],
            '货币类型': 'CNY',
            '层级': emp['层级'],
            '绩效': round(3.0 + (employee_data.index(emp) % 5) * 0.25, 2),
            '盘点结果': ['高', '中', '低', '明日之星'][employee_data.index(emp) % 4],
            '调薪前': base_salary,
            '调薪后': base_salary * 1.1,
            '年奖': base_salary * 0.5,
            '项目奖金': base_salary * 0.1,
            '异地津贴': 500
        }
        test_data.append(record)
    return test_data

# 主函数
def main():
    employee_data = data
    test_data = generate_test_data(employee_data)
    df = pd.DataFrame(test_data)
    output_file = './去年薪酬总价值.xlsx'
    df.to_excel(output_file, index=false)
    print(f'已生成 {len(test_data)} 条真实员工测试数据并保存为 {output_file}')

if __name__ == "__main__":
    main()