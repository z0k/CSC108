# a simple gui that we could use in Lab 3 for students to 
# try with their mark calculator solutions
# Michelle Craig
# July 9, 2012

try:
    import mark_functions as mf
    imported_correctly = True
except ImportError:
    imported_correctly = False
    
from tkinter import *

def functions_implemented():
    ''' () -> bool
    Do a simple check to see if the required functions are there in the 
    required module. It would have already failed if the module wasn't 
    found and will fail later if the functions have incompatible signatures.
    '''
    functions_needed = ['exam_required', 'term_work_mark', 'percentage',
                        'assignments_contribution', 'exercises_contribution', 'test_contribution']
    for fun in functions_needed:
        if fun not in mf.__dict__:
            return False
    return True
    

class Application(Frame):

    def recalculate_percentages(self, event):
        for work in self.term_work_items:
            new_val = mf.percentage(self.raw[work].get(),
                                                self.max_mark[work])
            self.percent[work]["text"] = "(%.2f percent)"%(new_val)

    def recalculate_exam_goal(self):
        self.calc_term()
        self.exam_goal = mf.exam_required(self.term_work,
                          self.goal_mark.get())
        new_text = '''To acheive %.0f on the course with this term mark
you would need a %d percent on the final exam'''%(self.goal_mark.get(),
        self.exam_goal)
        self.exam_goal_label['text'] = new_text
 

    def post_no_import_message(self):
        self.create_quit_button()
        message = '''You do not have the required module called mark_functions.py.

Go back and look at the lab instructions.'''
        message_label = Label(text=message)
        message_label.pack({"padx":10})

    def post_message(self):
        self.create_quit_button()
        message = '''You have the required  module called mark_functions.py but it
needs to contain all the functions listed in the lab handout before this code will
work properly.  Go back and look at the lab instructions.'''
        message_label = Label(text=message)
        message_label.pack({"padx":10})

    def create_labelled_entry(self, item):
        my_frame = Frame(self)
        max_score = self.max_mark[item] 
        self.labels[item] = Label(my_frame, text="%s out of %.1f"%(item,max_score))
        self.labels[item].pack({"side":"left"})
        raw_enterbox = Entry(my_frame)
        raw_enterbox.pack({"side":"left"})
        raw_enterbox["textvariable"] = self.raw[item]
        percent = mf.percentage(self.raw[item].get(), max_score)
        self.percent[item] = Label(my_frame, text="%.2f percent"%(percent))
        self.percent[item].pack({"side":"left"})
        raw_enterbox.bind('<Key-Return>', self.recalculate_percentages)
        raw_enterbox.bind('<Key-Tab>', self.recalculate_percentages)
        my_frame.pack()

    def calc_term(self):
        # call the functions in mark_functions to calculate term work
        ass = mf.assignments_contribution(self.raw['a1'].get(), 
                                                      self.raw['a2'].get()) 
        ex = mf.exercises_contribution(self.raw['e1'].get(), 
               self.raw['e2'].get(), self.raw['e3'].get(), self.raw['e4'].get())
        labs = self.raw['labs'].get()
        prep = self.raw['prep'].get()
        test = mf.test_contribution(self.raw['midterm'].get())
        self.term_work = mf.term_work_mark(ass, ex, labs, prep, test)

        # in case the user hasn't hit enter or tab on the entries for term work,
        # do the recalculations here
        self.recalculate_percentages(None)

        # update the label
        if self.term_work_total == None:
          self.term_work_total = Label(self, 
             text="Term work total is %.2f out of 56."%(self.term_work))
          self.term_work_total.pack({"side": "top"})
        else:
          self.term_work_total["text"] = "Term work total is %.2f out of 56."%(self.term_work)
          
     
    def create_goal_button(self):
        my_frame = Frame(self)
        goal_button = Button(my_frame)
        goal_button["text"] = "Click to see your exam mark goal"
        goal_button["command"] = self.recalculate_exam_goal
        goal_button.pack()
        my_text = '''To acheive %.0f on the course with this term mark
you would need a %d percent on the final exam'''%(self.goal_mark.get(),
        self.exam_goal)
        self.exam_goal_label = Label(my_frame, text=my_text)
        self.exam_goal_label.pack()
        my_frame.pack({"side":"bottom"})

    def create_desired_mark_entry(self):
        my_frame = Frame(self)
        label = Label(my_frame, text="Enter the mark you would like to get on this course.")
        label.pack({"side":"left"})
        enterbox = Entry(my_frame)
        enterbox.pack({"side":"left"})
        enterbox["textvariable"] = self.goal_mark
        my_frame.pack({"side":"bottom"})
 
    def create_quit_button(self):
        QUIT = Button(self)
        QUIT["text"] = "QUIT"
        QUIT["command"] = self.quit
        QUIT.pack({"padx":20, "pady":10, "side": "top"})

    def create_term_work_button(self):
        term_work = Button(self)
        term_work["text"] = "Click to (re)calculate term work mark"
        term_work["command"] = self.calc_term
        term_work.pack()

    def create_widgets(self):

        self.create_quit_button()
        message = '''Enter the raw marks you have earned so far (or an estimate)
        and this calculator will use your functions to determine how you must do
        on the final exam, to achieve your desired course grade.'''
        message_label = Label(text=message)
        message_label.pack({"side": "top"})

        for work in self.term_work_items:
            self.raw[work] = DoubleVar()
            self.create_labelled_entry(work)

        self.create_term_work_button()
        self.create_goal_button()
        self.create_desired_mark_entry()

    def __init__(self, master=None):
        self.term_work_items = ['a1', 'a2', 'e1', 'e2', 'e3', 'e4', 
                                'labs', 'prep', 'midterm']
        self.max_mark = {'a1':40, 'a2':40, 
                          'e1':10, 'e2':10, 'e3':10, 'e4':10,
                          'labs':4.5, 'prep': 5.5, 'midterm':25}
        self.term_work_total = None
        self.goal_mark = DoubleVar()
        self.exam_goal = 0.0
        self.labels = {}
        self.raw = {}
        self.percent = {}
       
        Frame.__init__(self, master)
        if imported_correctly and functions_implemented():
            self.create_widgets()
        elif imported_correctly:
            self.post_message()
        else:
            self.post_no_import_message()
        self.pack()

root = Tk()
app = Application(master=root)
app.master.title("Simple Marks Calculator Using Functions from Week 3 Lab")
app.mainloop()
root.destroy()
