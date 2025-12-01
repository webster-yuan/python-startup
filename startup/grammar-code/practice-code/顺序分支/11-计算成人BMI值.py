h,w=[float(x) for x in input().split()]
bmi=w/(h*h)
if bmi<18.5:
    word='Underweight'
elif 18.5<=bmi<24:
    word='Normal'
elif 24<=bmi<28:
    word='Overweight'
else:
    word='Obese'
print(format(bmi,'.1f'),end=' ')
print(word)