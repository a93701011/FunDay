def num_teachers (value):
	#print(kwargs)
	#print("{Kenneth Love}".format(**kwargs))
	print(len(value.keys()))
	
def num_courses (value):
    course_total = 0
    for course in value.values():
        course_total += len(course)
    return course_total

def courses (value):
    courses_list = []
    for courses in value.values():
            courses_list.extend(courses)
    return courses_list

def most_courses (value):
    most_teacher = ''
    most_cours = 0
    for courses in value.keys():
        if len(value[courses]) > most_cours:
            most_cours = len(value[courses])
            most_teacher = courses
        else:
            pass
    return most_teacher

def stats (value):
    teacher_stats = []
    for courses in value.keys():
        teacher_courses = []
        teacher_courses.append (courses )
        teacher_courses.append (len(value[courses]))
        teacher_stats.append (teacher_courses)
    print( teacher_stats )
		
stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']})