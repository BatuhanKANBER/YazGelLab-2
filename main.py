import time
from tkinter import *
from tkinter import ttk
import random


root = Tk()
root.title('201307048 - 201307044 - 201307063')
root.geometry('1920x1080')
root.config(bg='darkgray')

algo_var = StringVar()
graph_var=StringVar()
srch = StringVar()
data = []
count=0

#_____________________________________________ Draw data ___________________________________________________#


def drdata(data, clr):
    canva.delete('all')
    ch = 380
    cw = 800
    xw = cw / (len(data) + 1)
    ofs = 30
    sp = 10
    n = [i / max(data) for i in data]
    for i, h in enumerate(n):
        x0 = i * xw + ofs + sp
        y0 = ch - h * 320
        x1 = (i + 1) * xw + ofs
        y1 = ch

        canva.create_rectangle(x0, y0, x1, y1, fill=clr[i])
        canva.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

#__________________________________________________ Draw data ___________________________________________________#

#__________________________________________________  Generate  ________________________________________________#


def gen(): 
    global data
    minv = int(minen.get())
    maxv = int(maxen.get())
    size = int(sizen.get())
    data = []
    for i in range(size):
        data.append(random.randrange(minv, maxv + 1))
    drdata(data, ['black' for i in range(len(data))])


#__________________________________________________  Generate  ________________________________________________#
#_________________________________________________ Merge Sort ____________________________________________________#


def mergesort(data, drdata, speed):
    merge_sort(data, 0, len(data) - 1, drdata, speed)


def merge_sort(data, l, r, drdata, speed):
    if l < r:
        mid = (l + r) // 2
        merge_sort(data, l, mid, drdata, speed)
        merge_sort(data, mid + 1, r, drdata, speed)
        merge(data, l, mid, r, drdata, speed)


def merge(data, l, mid, r, drdata, speed):
    drdata(data, clrar(len(data), l, mid, r))
    time.sleep(speed)
    left_data = data[l:mid + 1]
    right_data = data[mid + 1:r + 1]

    li = ri = 0
    for i in range(l, r + 1):
        if li < len(left_data) and ri < len(right_data):
            if left_data[li] <= right_data[ri]:
                data[i] = left_data[li]
                li += 1
            else:
                data[i] = right_data[ri]
                ri += 1
        elif li < len(left_data):
            data[i] = left_data[li]
            li += 1
        else:
            data[i] = right_data[ri]
            ri += 1

    drdata(data, ['white' if l <= c <= r else 'white' for c in range(len(data))])
    time.sleep(speed)


def clrar(n, l, mid, r):
    clr = []
    for i in range(n):
        if l <= i <= r:
            if l <= i <= mid:
                clr.append('darkgrey')
            else:
                clr.append('gray')
        else:
            clr.append('white')

    return clr


#_________________________________________________ Merge Sort ____________________________________________________#

#_________________________________________________ Quick Sort ____________________________________________________#


def partition(data, start, end, drdata, speed):
    pivot = data[end]

    drdata(data, getlcr(len(data), start, end, start, start))
    time.sleep(speed)

    for i in range(start, end):
        if data[i] < pivot:
            drdata(data, getlcr(len(data), start, end, start, i, True))
            time.sleep(speed)

            data[i], data[start] = data[start], data[i]
            start += 1
        drdata(data, getlcr(len(data), start, end, start, i))
        time.sleep(speed)

    drdata(data, getlcr(len(data), start, end, start, end, True))
    time.sleep(speed)
    data[end], data[start] = data[start], data[end]
    return start


def quicksort(data, start, end, drdata, speed):
    if start < end:
        pi = partition(data, start, end, drdata, speed)
        quicksort(data, start, pi - 1, drdata, speed)
        quicksort(data, pi + 1, end, drdata, speed)


def getlcr(n, start, end, s, ci, iswap=False):
    clr = []
    for i in range(n):
        if start <= i <= end:
            clr.append('gray')
        else:
            clr.append('white')
        if i == end:
            clr[i] = 'gray'
        elif i == s:
            clr[i] = 'black'
        elif i == ci:
            clr[i] = 'white'
        if iswap:
            if i == s or i == ci:
                clr[i] = 'white'
    return clr


#_________________________________________________ Quick Sort ____________________________________________________#

#_________________________________________________ Selection Sort ____________________________________________________#


def selectionSort(data, drdata, speed):
    for i in range(len(data)):
        mini = i
        for j in range(i + 1, len(data)):
            if data[mini] > data[j]:
                mini = j
                drdata(data, ['gray' if c == mini or c == i else 'black' for c in range(len(data))])
                time.sleep(speed)
        data[i], data[mini] = data[mini], data[i]
        drdata(data, ['white' if c == i or c == mini else 'black' for c in range(len(data))])
        time.sleep(speed)
    drdata(data, ['white' for i in range(len(data))])

#_________________________________________________ Selection Sort ____________________________________________________#


def insertion_sort(data, drdata, speed):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
        data[k] = temp
        drdata(data, ['white' if x == k or x == i else 'black' for x in range(len(data))])
        time.sleep(speed)
        
    drdata(data, ['black' for x in range(len(data))])

#_________________________________________________ Bubble Sort ____________________________________________________#


def bubbleSort(data, drdata, speed):
    count=0
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drdata(data, ['white' if c == j or c == j + 1 else 'black' for c in range(len(data))])
                time.sleep(speed)
                count+=1
    drdata(data, ['white' for i in range(len(data))])


#_________________________________________________ Bubble Sort ____________________________________________________#

#_________________________________________________ Start Button ____________________________________________________#


def strt():
    global data

    if algo_var.get() == 'Hızlı':
        quicksort(data, 0, len(data) - 1, drdata, speed.get())
        drdata(data, ['white' for i in range(len(data))])

    elif algo_var.get() == 'Kabarcık':
        bubbleSort(data, drdata, speed.get())

    elif algo_var.get() == 'Birleştirmeli':
        mergesort(data, drdata, speed.get())
        drdata(data, ['white' for i in range(len(data))])

    elif algo_var.get() == 'Seçmeli':
        selectionSort(data, drdata, speed.get())
         
    elif algo_var.get() == 'Eklemeli':
        insertion_sort(data, drdata, speed.get())


#_________________________________________________ Start Button ____________________________________________________#

#_________________________________________________ GUI ____________________________________________________#


uif = Frame(root, width=200, height=720, bg='grey')
uif.grid(row=0, column=0, padx=10, pady=5)

canva = Canvas(root, width=1000, height=720, bg='white')
canva.grid(row=0, column=1, padx=10, pady=5)

Label(uif, text="Algoritmalar: ", bg='grey', fg='black', font=('arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
alg = ttk.Combobox(uif, textvariable=algo_var, values=['Kabarcık', 'Hızlı', 'Birleştirmeli', 'Seçmeli','Eklemeli'])
alg.grid(row=1, column=0, padx=25, pady=5)
alg.current(0)

Label(uif, text="Grafikler: ", bg='grey', fg='black', font=('arial', 12)).grid(row=2, column=0, padx=5, pady=5, sticky=W)
graph = ttk.Combobox(uif, textvariable=graph_var, values=['Scatter', 'Bar', 'Stem'])
graph.grid(row=3, column=0, padx=25, pady=5)
graph.current(0)

speed = Scale(uif, from_=5.0, to=0.1, length=200, digits=2, resolution=0.1, orient=HORIZONTAL,
              label='Hız')
speed.grid(row=4, column=0, padx=5, pady=5)

sizen = Scale(uif, from_=3, to=50, length=200, resolution=1, orient=HORIZONTAL, label='Boyut')
sizen.grid(row=5, column=0, padx=5, pady=5, sticky=W)

minen = Scale(uif, from_=1, to=10, length=200,resolution=1, orient=HORIZONTAL, label='Minimum Değer')
minen.grid(row=6, column=0, padx=5, pady=5, sticky=W)

maxen = Scale(uif, from_=10, to=100,length=200, resolution=1, orient=HORIZONTAL, label='Maximum Değer')
maxen.grid(row=7, column=0, padx=5, pady=5, sticky=W)

Button(uif, text='Oluştur', command=gen,width=20, bg='White').grid(row=8, column=0, padx=5, pady=5)
Button(uif, text='Başlat', command=strt,width=20, bg='black', fg='white').grid(row=9, column=0, padx=5, pady=5)

root.mainloop()


#_________________________________________________ GUI ____________________________________________________#