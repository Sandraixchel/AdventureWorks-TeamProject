import pandas as pd
import matplotlib.pyplot as plt

#What is the relationship between sick leave and Job Title (PersonType)? 

df_employee_leave_department = pd.read_csv('INTERIM PROJECT/Question4/JobTitle_Leave_Department.csv')

#print(df_employee_leave_department)

df_employee_leave_department['Average'] = df_employee_leave_department['total_sick_hours']/df_employee_leave_department['total_employee']

#print(df_employee_leave_department)


sorted_by_avg = df_employee_leave_department[['JobTitle', 'Average']].sort_values(by='Average', ascending=False)


# plt.scatter(df_employee_leave_department['JobTitle'], df_employee_leave_department['Average'])
# plt.xticks(rotation = 85)
# plt.show()

print(sorted_by_avg)

# top_25 = sorted_by_avg.head(25)

# plt.barh(top_25['JobTitle'], top_25['Average'])
# plt.xlim(50,70)
# plt.show()


# sorted_by_avg_dep = df_employee_leave_department[['Department', 'Average']].sort_values(by='Average', ascending=False)

# plt.bar(sorted_by_avg_dep['Department'], sorted_by_avg_dep['Average'])
# plt.xticks(rotation=45)
# plt.show()

