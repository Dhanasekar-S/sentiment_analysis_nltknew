import nltk
import tkinter as tk

class myapp(tk.Tk):
   def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.entry.pack()
        close_button = tk.Button(self, text="Close", command=self.close)
        close_button.pack()
        run_button=tk.Button(self,text="Analyze",command=self.analyze)
        run_button.pack()
        l1=tk.Label(text="Positive")
        l1.pack()
        self.entry1=tk.Entry(self.getvalue1())
        self.entry1.pack()
        l2=tk.Label(text="Negative")
        l2.pack()
        self.entry2=tk.Entry(self.getvalue2())
        self.entry2.pack()
        self.string = ""

   def analyze(self):
        self.string = self.entry.get()
        val=self.string
        process(val)
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry1.insert(0,myvalue1())
        self.entry2.insert(0,myvalue2())



   def close(self):
        global result
        self.string = self.entry.get()
        self.destroy()

   def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string

   def getvalue1(self):
       return myvalue1()

   def getvalue2(self):
       return myvalue2()

pos_fact=0
neg_fact=0
def get_words_in_tweets(tweets):
    all_words=nltk.word_tokenize(tweets)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    print(wordlist)
    word_features = wordlist.keys()
    return word_features

def process(senten):
    sentence=senten
    tweets = []
    positive_count=0
    negative_count=0
    word_features = get_words_in_tweets(sentence)
    print(word_features)
    file_content = open("positive").read()
    positive_words=nltk.word_tokenize(file_content)
    file_content = open("negative").read()
    negative_words=nltk.word_tokenize(file_content)
    for i in word_features:
      for j in positive_words:
          if(i==j):
             positive_count+=1
    for i in word_features:
         for j in negative_words:
           if(i==j):
             negative_count+=1
    global pos_fact
    global neg_fact
    pos_fact=positive_count/(positive_count+negative_count)
    neg_fact=negative_count/(positive_count+negative_count)
    print(pos_fact)
    print(neg_fact)

def myvalue1():
    global pos_fact
    return pos_fact
def myvalue2():
    global neg_fact
    return neg_fact

print ("enter a string in the GUI")
app = myapp()
result = app.mainloop()
process(result)
print ("you entered:", result)