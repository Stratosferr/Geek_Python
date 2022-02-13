import json

with open("5_7.txt", "r", encoding='utf-8') as company_file:
    profit_all = 0
    company_cnt = 0
    output_dict = {}
    for company in company_file:
        company_list = company.split()
        profit = int(company_list[2]) - int(company_list[3])
        output_dict[company_list[0]] = profit
        if profit >= 0:
            profit_all += profit
            company_cnt += 1
    output_list = [output_dict, {"average_profit": profit_all / company_cnt}]

with open('5_7.json', 'w+', encoding='utf-8') as f:
    json.dump(output_list, f, indent=2, ensure_ascii=False)

