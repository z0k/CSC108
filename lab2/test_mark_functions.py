import mark_functions as mf

print ('Calling mark_functions.percentage(15, 20)')
print ('Expected 75.0, returned', mf.percentage(15, 20), '\n')

print ('Calling mark_functions.percentage(4.5, 4.5)')
print ('Expected 100.0, returned', mf.percentage(4.5, 4.5), '\n')

print ('Calling mark_functions.contribution(100, 7)')
print ('Expected 7.0, returned', mf.contribution(100, 7), '\n')

print ('Calling mark_functions.raw_contribution(13.5, 15, 10)')
print ('Expected 9.0, returned', mf.raw_contribution(13.5, 15, 10), '\n')

print ('Calling mark_functions.assignments_contribution(32, 30)')
print ('Expected 15.5, returned', mf.assignments_contribution(32, 30), '\n')
    
print ('Calling mark_functions.exercises_contribution(10, 10, 5, 10)')
print ('Expected 10.5, returned',
       mf.exercises_contribution(10, 10, 5, 10), '\n')

print ('Calling mark_functions.test_contribution(21)')
print ('Expected 11.76, returned', mf.test_contribution(21), '\n')

print ('Calling mark_functions.term_work_mark(16, 10.5, 4, 5, 12)')
print ('Expected 47.5, returned', mf.term_work_mark(16, 10.5, 4, 5, 12), '\n')

print ('Calling mark_functions.exam_required(47, 80)')
print ('Expected 75.0, returned', mf.exam_required(47, 80), '\n')
