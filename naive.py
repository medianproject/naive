# Alter code zum testen
import numpy as np
import streamlit as st

# title
st.title("Median Calculator", anchor=False)

# uer entry
userEntry=st.sidebar.number_input("Select random iterations (min=1, max=10)", min_value=1, max_value=20,value=5, step=1)

# fix random intervall border [-10000,10000]
lowerBorder=-10
upperBorder=lowerBorder*(-1)

# generate random numbers & sort them
numberList=np.random.randint(lowerBorder,upperBorder,size=userEntry)
numberListSort=sorted(numberList) # nicht gut weil O(n log(n)) hier AVL balancierte bäume nutzen
n=len(numberListSort)

# Calculate median for odd and even case
medianList=[]
for i in range(len(numberListSort)):
    if (len(numberListSort[:i+1]))%2==0:
        myMedian=(numberListSort[len(numberListSort[:i+1])//2-1]+ # // ist die Gauß Klammer (abrunden) ⌊x⌋=max{k€Z: k<=x}
                  numberListSort[len(numberListSort[:i+1])//2])/2
    else:
        myMedian=numberListSort[len(numberListSort[:i+1])//2] # hier prüfen ob i oder i+1
    medianList.append(myMedian)

# Format the numbers in UI to be user friendly
numberListSort=[int(i) for i in numberListSort]
medianList=[round(float(i),2) for i in medianList]

# user output
st.write(f"Random numbers unsorted: {numberList}")
st.write(f"Random numbers sorted: {numberListSort}")
st.write(f"Median values: {medianList}")
st.line_chart(medianList, x_label="Iterations", y_label="Median values") 
