#!/usr/bin/env python
# coding: utf-8

# In[24]:


#one
active_program = ['time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident']
#print the list
print(active_program)


# In[25]:


#print first 3 items
print(active_program[0])
print(active_program[1])
print(active_program[2])


# In[26]:


#print last 5 items
print(active_program[3])
print(active_program[4])
print(active_program[5])
print(active_program[6])
print(active_program[7])


# In[28]:


#add items to the end of list
active_program = ['time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'look at tutorials' , 'watch movies about programmers']
print(active_program)


# In[29]:


#add items to the beginning of list
active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'look at tutorials' , 'watch movies about programmers']
print(active_program)


# In[30]:


#replace items to the from the of list
active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'watch tutorials online' , 'watch movies about programmers']
print(active_program)


# In[31]:


#remove items to the from the of list
active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'watch tutorials online']
print(active_program)


# In[32]:


#remove items to the from the of list
active_program = ['commitment to learning' , 'time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'watch tutorials online']
print(active_program)


# In[33]:


#retrieve most relevant action for learning
#remove items to the from the of list
active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'watch tutorials online']
print(active_program[0])


# In[34]:


#remove items to the from the of list
active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'watch tutorials online']
print(active_program)


# In[37]:


#slice the list
active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'self responsibility' , 'studying' , 'syntax' , 'practice' , 'start your own projects' , 'ask for help' , 'be confident' , 'watch tutorials online']
print(active_program[0:3])


# In[38]:


#slice the list
active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'practice' , 'start your own projects']
print(active_program)


# In[41]:


active_program = ['desire to learn' , 'commitment to learning' , 'time management' , 'practice' , 'start your own projects']
print(active_program)
# string in the list
if 'commitment to learning' in active_program:
    print('It is present in the list')

# string not in the list
if 'commitment to learning' not in active_program:
    print('It is not present in the list')


# In[42]:


#create two lists
Course_ID = ['100' , '108' , '124' , '131' , '171' , '197']
Course_Topic = ['Information in the 21st Century' , ' Programming for Problem Solving' , 'Cybersecurity Basics' , 'Introduction to Data Analytics' , ' eSports & Digital Gaming Ecosystem ' , ' Mini Special Topic in Informatics']


# In[46]:


#sort in numerical order
Course_ID = ['100' , '108' , '124' , '131' , '171' , '197']
Course_ID.sort()
print(Course_ID)


# In[49]:


#sort in alphabetical order
Course_Topic = ['Information in the 21st Century' , 'Programming for Problem Solving' , 'Cybersecurity Basics' , 'Introduction to Data Analytics' , 'eSports & Digital Gaming Ecosystem' , 'Mini Special Topic in Informatics']
Course_Topic.sort()
print(Course_Topic)


# In[50]:


#reverse the sort for course id
Course_ID = ['100' , '108' , '124' , '131' , '171' , '197']
print(Course_ID)


# In[51]:


#reverse the sort for course topic
Course_Topic = ['Information in the 21st Century' , ' Programming for Problem Solving' , 'Cybersecurity Basics' , 'Introduction to Data Analytics' , ' eSports & Digital Gaming Ecosystem ' , ' Mini Special Topic in Informatics']
print(Course_Topic)


# In[53]:


#print the IDs that correspond with the course
Course_ID = ['100' , '108' , '124' , '131' , '171' , '197']
Course_Topic = ['Information in the 21st Century' , ' Programming for Problem Solving' , 'Cybersecurity Basics' , 'Introduction to Data Analytics' , ' eSports & Digital Gaming Ecosystem ' , ' Mini Special Topic in Informatics']
print(Course_ID[0],Course_Topic[0])
print(Course_ID[1],Course_Topic[1])
print(Course_ID[2],Course_Topic[2])
print(Course_ID[3],Course_Topic[3])
print(Course_ID[4],Course_Topic[4])
print(Course_ID[5],Course_Topic[5])


# In[60]:


#create a tuple for the IDs and Courses and write a script
idtuple = ('100' , '108' , '124' , '131' , '171' , '197')
coursetuple = ('Information in the 21st Century' , ' Programming for Problem Solving' , 'Cybersecurity Basics' , 'Introduction to Data Analytics' , ' eSports & Digital Gaming Ecosystem ' , ' Mini Special Topic in Informatics')
print('Welcome to CINF' + idtuple[0], coursetuple[0] + '!')
print('Welcome to CINF' + idtuple[1], coursetuple[1] + '!')
print('Welcome to CINF' + idtuple[2], coursetuple[2] + '!')
print('Welcome to CINF' + idtuple[3], coursetuple[3] + '!')
print('Welcome to CINF' + idtuple[4], coursetuple[4] + '!')
print('Welcome to CINF' + idtuple[5], coursetuple[5] + '!')


# In[61]:


#add cinf200
idtuple = ('100' , '108' , '124' , '131' , '171' , '197' , '200')
coursetuple = ('Information in the 21st Century' , ' Programming for Problem Solving' , 'Cybersecurity Basics' , 'Introduction to Data Analytics' , ' eSports & Digital Gaming Ecosystem ' , ' Mini Special Topic in Informatics' , ' Research Methods for Informatics ')
print('Welcome to CINF' + idtuple[0], coursetuple[0] + '!')
print('Welcome to CINF' + idtuple[1], coursetuple[1] + '!')
print('Welcome to CINF' + idtuple[2], coursetuple[2] + '!')
print('Welcome to CINF' + idtuple[3], coursetuple[3] + '!')
print('Welcome to CINF' + idtuple[4], coursetuple[4] + '!')
print('Welcome to CINF' + idtuple[5], coursetuple[5] + '!')
print('Welcome to CINF' + idtuple[6], coursetuple[6] + '!')


# In[63]:


#remove cinf197 and then print the rest so they match
idtuple = ('100' , '108' , '124' , '131' , '171' , '200')
coursetuple = ('Information in the 21st Century' , ' Programming for Problem Solving' , 'Cybersecurity Basics' , 'Introduction to Data Analytics' , ' eSports & Digital Gaming Ecosystem ' , ' Research Methods for Informatics ')
print('Welcome to CINF' + idtuple[0], coursetuple[0] + '!')
print('Welcome to CINF' + idtuple[1], coursetuple[1] + '!')
print('Welcome to CINF' + idtuple[2], coursetuple[2] + '!')
print('Welcome to CINF' + idtuple[3], coursetuple[3] + '!')
print('Welcome to CINF' + idtuple[4], coursetuple[4] + '!')
print('Welcome to CINF' + idtuple[5], coursetuple[5] + '!')


# In[ ]:


## very confused on the last two parts of this lab. I dont know how to do the dictionary but I understand everything else

