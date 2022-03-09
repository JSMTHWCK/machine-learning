from cProfile import label
import matplotlib.pyplot as plt
from knn import KNC
x = [
[0.14 , 0.14 , 0.28 , 0.44 ],
[0.10 , 0.18 , 0.28 , 0.44 ],
[0.12 , 0.10 , 0.33 , 0.45 ],
[0.10 , 0.25 , 0.25 , 0.40 ],
[0.00 , 0.10 , 0.40 , 0.50 ],   
[0.00 , 0.20 , 0.40 , 0.40 ],
[0.02 , 0.08 , 0.45 , 0.45 ],
[0.10 , 0.15 , 0.35 , 0.40 ],
[0.10 , 0.08 , 0.35 , 0.47 ],
[0.00 , 0.05 , 0.30 , 0.65 ],
[0.20 , 0.00 , 0.40 , 0.40 ],
[0.25 , 0.10 , 0.30 , 0.35 ],
[0.22 , 0.15 , 0.50 , 0.13 ],
[0.15 , 0.20 , 0.35 , 0.30 ],
[0.22 , 0.00 , 0.40 , 0.38 ],
[0.05 , 0.12 , 0.28 , 0.55 ],
[0.14 , 0.27 , 0.31 , 0.28 ],
[0.15 , 0.23 , 0.30 , 0.32 ],
[0.20 , 0.10 , 0.30 , 0.40 ]
]
print(len(x))
cookie_type = ['Shortbread','Shortbread', 'Shortbread', 'Shortbread', 'Sugar', 'Sugar', 'Sugar', 'Sugar', 'Sugar' , 'Sugar', 'Fortune', 'Fortune', 'Fortune', 'Fortune', 'Fortune', 'Shortbread', 'Shortbread', 'Shortbread', 'Shortbread']
print(len(cookie_type))
cookie_totals = {}
for item in cookie_type:
    if item not in cookie_totals:
        cookie_totals[item] = 1
    else:
        cookie_totals[item] += 1
print(cookie_totals)
label = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
fin = []
file = open('knn_text.txt',"w")

#for each k
accuracy_per_k = []
for k in range(1,15):
    accuracy_per_out = []
    #for each leave one out
    for out in range(0,len(x)):
        x_copy = x[:out] + x[out+1:]
        cookie_copy = cookie_type[:out] + cookie_type[out+1:]
        knc = KNC(k)
        knc.fit(x_copy,cookie_copy)
        knc.classify(x[out])
        #file.write("k is " + str(k) + '\n')
        #file.write("cookie type is " + cookie_type[out] + '\n')
        #file.write("guessed cookie type is " + knc.classify(x[out]) + '\n')
        if knc.classify(x[out]) == cookie_type[out]:
            accuracy_per_out.append(1)
        else:
            accuracy_per_out.append(0)
        if k == 18:
            file.write(str(knc.classify(x[out],all_classification=True)) + '\n')
        #file.write('\n')
    acc = 0
    for item in accuracy_per_out:
        acc += item
    acc /= len(accuracy_per_out)
    accuracy_per_k.append(acc)
print(accuracy_per_k)
print(len(accuracy_per_out))

plt.scatter([i for i in range(len(accuracy_per_k))],accuracy_per_k)
plt.savefig('loocv.png')
        




