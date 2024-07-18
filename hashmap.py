import secrets
import string
import random
import matplotlib.pyplot as plt
import numpy as np
import statistics

class Node:
    def __init__(self,key,value):
        self.value=value
        self.next=None
        self.key=key

class HashMap:
    def __init__(self,m):
        self.arr=[None]*(m+1)
        self.m=m
    
    def calcHash(self,key):
        sum=0
        mul=1
        for i in range(0,len(key)):
            mul = 1 if i % 4 == 0 else mul * 256
            sum+=ord(key[i])*mul
        
        return (int)(abs(sum)%self.m)
    
    def insert(self,key,value):
        hashValue=self.calcHash(key)
        temp=Node(key,value)
        curr=self.arr[hashValue]
        if(curr==None):
            self.arr[hashValue]=temp
        else:
            self.increaseKey(key,value,curr,temp)
    
    def increaseKey(self,key,value,curr,temp):
        while(curr!=None):
                if(curr.key==key):
                    curr.value+=value
                    break
                elif(curr.next==None):
                    curr.next=temp
                    break
                curr=curr.next

    def find(self,key):
        hashvalue=self.calcHash(key)
        curr=self.arr[hashvalue]
        while(curr!=None):
            if(curr.key==key):
                return "Found with count: "+(str)(curr.value)
            curr=curr.next
        return "Not Found"
    
    def printValues(self):
        for i in range(0,len(self.arr)):
            if(self.arr[i]!=None):
                print("Index: ",i)
                curr=self.arr[i]
                while(curr!=None):
                    print(curr.key+": ",curr.value,end=",")
                    curr=curr.next
                print()
    
    def delete(self,key):
        hashValue=self.calcHash(key)
        curr=self.arr[hashValue]
        if(curr.key==key):
            self.arr[hashValue]=curr.next
        while(curr.next!=None):
            if(curr.next.key==key):
                curr.next=curr.next.next
            curr=curr.next
    
    def findLengthCollisions(self):
        length=[]
        for i in range(0,self.m):
            curr=self.arr[i]
            cnt=0
            while(curr!=None):
                cnt+=1
                curr=curr.next
            length.append(cnt)
        
        return length
    
    def saveTofile(self):
        s=''
        for i in range(0,len(self.arr)):
            node=self.arr[i]
            s=s+"Index: "+(str)(i)+"\n"
            while(node!=None):
                s=s+(str)(node.key)+": "+(str)(node.value)+"\n"
                node=node.next
        file_path = 'output.txt'

        # Open the file in write mode ('w') and write the string to it
        with open(file_path, 'w') as file:
            file.write(s)        

        
file_path = 'AliceInWonderland.txt'
with open(file_path, 'r', encoding='ISO-8859-1') as file:
    text = file.read()

# Remove punctuation and split the text into words
l = text.replace('\n', ' ').replace('\r', '').split()
l = [word.strip('.,!?;:"()[]{}') for word in l]

obj=HashMap(30)
for i in l:
    obj.insert(i,1)


obj2=HashMap(300)
for i in l:
    obj2.insert(i,1)


obj3=HashMap(1000)
for i in l:
    obj3.insert(i,1)

print(obj.find("Alice"))
obj.delete("Alice")
print(obj.find("Alice"))
obj.saveTofile()
'''
collisionsObj=obj.findLengthCollisions()
plt.figure(figsize=(10, 6))
plt.bar(range(len(collisionsObj)), collisionsObj, edgecolor='black')
plt.title(f'Bar Plot of Collision List Lengths for MAXHASH = {30}')
plt.xlabel('Index')
plt.ylabel('Length of Collision Lists')
plt.grid(axis='y')
file_name = f'barplot_maxhash_{30}.png'
plt.savefig(file_name)
plt.close()
print("Variance for Hashmap of size 30 is: ",statistics.variance(collisionsObj))
print("N/M for 30 is: ",sum(collisionsObj)/30)
collisionsObj.sort(reverse=True)
print("Top 10 percent: ",collisionsObj[:3])

collisionsObj2=obj2.findLengthCollisions()
plt.figure(figsize=(10, 6))
plt.bar(range(len(collisionsObj2)), collisionsObj2, edgecolor='black')
plt.title(f'Bar Plot of Collision List Lengths for MAXHASH = {300}')
plt.xlabel('Index')
plt.ylabel('Length of Collision Lists')
plt.grid(axis='y')
file_name = f'barplot_maxhash_{300}.png'
plt.savefig(file_name)
plt.close()
print("Variance for Hashmap of size 300 is: ",statistics.variance(collisionsObj2))
print("N/M for 300 is: ",sum(collisionsObj2)/300)
collisionsObj2.sort(reverse=True)
print("Top 10 percent: ",collisionsObj2[:30])

collisionsObj3=obj3.findLengthCollisions()
plt.figure(figsize=(10, 6))
plt.bar(range(len(collisionsObj3)), collisionsObj3, edgecolor='black')
plt.title(f'Bar Plot of Collision List Lengths for MAXHASH = {1000}')
plt.xlabel('Index')
plt.ylabel('Length of Collision Lists')
plt.grid(axis='y')
file_name = f'barplot_maxhash_{1000}.png'
plt.savefig(file_name)
plt.close()
print("Variance for Hashmap of size 300 is: ",statistics.variance(collisionsObj3))
print("N/M for 1000 is: ",sum(collisionsObj3)/1000)
collisionsObj3.sort(reverse=True)
print("Top 10 percent: ",collisionsObj3[:100])

l=[]
for i in range(0,500):
    N = random.randint(1, 10)
    res = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                for i in range(N))    
    l.append(res)
print(l)

obj=HashMap()
for i in l:
    obj.insert(i,1)

obj.printValues()
'''