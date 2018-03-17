import random

correct=0
wrong=0
a="Name of the screen that recognizes touch input is :\n\n1.)Recog screen\n2.)Point Screen\n3.)Touch Screen\n4.)Android Screen"
b="Identify the device through which data and instructions are entered into a computer?\n\n1.)Software\n2.)Output device\n3.)Input device\n4.)Memory"
c="Computer Moniter is also known as :\n\n1.)DVU\n2.)UVD\n3.)VDU\n4.)CCTV"
d="Arrange in ascending order the units of memory TB, KB, GB, MB\n\n1.)TB>MB>GB>KB\n2.)MB>GB>TB>KB\n3.)TB>GB>MB>KB\n4.)GB>MB>KB>TB"
e="Which one of these stores more data than a DVD ? \n\n1.)CD Rom\n2.)Blue Ray Disk\n3.)Floppy\n4.)Red Ray Disk"
f="The output shown on the computer monitor is called \n\n1.)VDU\n2.)Hard Copy\n3.)Screen Copy\n4.)Soft Copy"
g="Eight Bits make up a\n\n1.)byte\n2.)megabyte\n3.)kilobyte\n4.)None"
h="Which one is the result of the output given by a computer \n\n1.)Data\n2.Instruction)\n3.)Information\n4.)Excursion"
i="Which one of these also known as read/write memory ? \n\n1.)ROM\n2.)RAM\n3.)DVD\n4.)Hard Disk"
j="The printed output from a computer is called \n\n1.)Copy\n2.)Hard Copy\n3.)Soft Copy\n4.)Paper"

l=[a,b,c,d,e,f,g,h,i,j]
random.shuffle(l)
d={a:3,b:3,c:3,d:3,e:2,f:4,g:1,h:3,i:2,j:2}
print("***************  Quiz  ***************\n\n")
print("\t\t\t\tFor each Correct Answer:+4 marks\n")
print("\t\t\t\tFor each Wrong Answer: -1 marks\n\n")    
for i in range(0,10):
    print(i+1,end="")
    print(".)",end=" ")
    print(l[i])
    ans=int(input("\nSelect option\t"))
    print("\n")
    if(ans==d[l[i]]):
        correct=correct+1;
    else:
        wrong=wrong+1;
marks=(correct*4)-(wrong*1)
print("\n\nCorrect Answers:",correct)
print("\n\nWrong Answers:",wrong)
print("\nMarks:",marks)
                                                            
