import pandas as pd

def generate_random_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        record = {
            '员工工号': f'100{i:03}',
            '货币类型': 'CNY',
            '层级': ['P6', 'P7', 'M3'][i % 3],
            '绩效': round(3.0 + (i % 5) * 0.25, 2),
            '盘点结果': ['高', '中', '低', '明日之星'][i % 4],
            '调薪前': 2000 + i * 100,
            '调薪后': 2100 + i * 100,
            '年奖': 3000 + i * 50,
            '项目奖金': 1000 + i * 20,
            '异地津贴': 500 + i * 10
        }
        data.append(record)
    return data

num_records = 100
data = generate_random_data(num_records)
df = pd.DataFrame(data)
output_file = 'last_year_salary_value.xlsx'
df.to_excel(output_file, index=false)

print(f"已生成 {num_records} 条测试数据并保存为 {output_file}")