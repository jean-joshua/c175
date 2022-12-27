import matplotlib .pyplot as plt
import psutil as p
app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count + 1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('Name : ', Name, '- - cpu_usage : ',cpu_usage)
        app_name_dict.update({Name:cpu_usage})
        keymax = max(app_name_dict,key=app_name_dict.get)
        print(keymax)
        keymin = min(app_name_dict,key=app_name_dict.get)
        name_list = [keymax,keymin]
        print(name_list)
        app=app_name_dict.values()
        maxapp = max(app)
        print(maxapp)
        minapp = min(app)
        print(minapp)
        max_min_list = [maxapp,minapp]
        print(max_min_list)

plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("Usage")
plt.bar(name_list, max_min_list, width=0.6, color=("blue","red"))
plt.show