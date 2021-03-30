import pandas as pd
from tkinter import *
import wikipedia as wiki
window = Tk()
window.geometry('300x800')
window.title("Chemistry App")
label = Label(text="Please Input the Element", fg="white", bg="black")
label.grid(column=0,row=0)
entry = Entry(fg="white", bg="black", width=50)
entry.grid(column=0,row=1)
label_result = Label(text='', bg='black', fg='white')
label_result.grid(column=0,row=3)
label_result_wikipedia = Label(text='', bg='black', fg='white')
label_result_wikipedia.grid(column=1,row=3)


def get_entry():
    element = entry.get()
    return element
def get_element():
        x = get_entry()
        attributes = []
        result = []
        index = 0
        elements = []
        final_text_result = ''

        data = pd.read_csv("Elements.csv")
        name_of_elements_pandas_series = data["Element"]

        for i in range(118):
            elements.append(name_of_elements_pandas_series[i])

        for atribute in data:
            attributes.append(atribute)

        index = elements.index(x)
        print(index)

        for i in range(len(attributes)):
            text_to_add_1 = str(attributes[i])
            text_to_add_2 = str(data[attributes[i]][index])
            text_to_add = text_to_add_1 + ": " + text_to_add_2
            result.append(text_to_add)

        for i in range(len(result)):
            final_text_result+=result[i]+"\n"


        label_result.configure(text=final_text_result)
        return result
def get_wikipedia_summary():
    x = get_entry()
    final_wikipedia_result = ''
    result_of_wikipedia = wiki.summary(x,sentences=20)
    result_of_wikipedia = result_of_wikipedia.split()

    length_of_wiki_responce = len(result_of_wikipedia)
    times = length_of_wiki_responce//7
    mod = length_of_wiki_responce % 7
    for i in range(length_of_wiki_responce-mod):
        print(times*7)
        if i % 7 ==0:
            print(result_of_wikipedia[i])
            result_of_wikipedia[i] +='\n'
        else:
            result_of_wikipedia[i]+=' '




        final_wikipedia_result+=result_of_wikipedia[i]


    label_result_wikipedia.configure(text=final_wikipedia_result)












button = Button(window,text= "Get Element Info",command=get_element)
button.grid(column=0,row=2)
button_wikipedia = Button(window,text = "Get Wikipedia Summary", command=get_wikipedia_summary)
button_wikipedia.grid(column=1,row=2)



window.mainloop()