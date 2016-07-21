from system.core.controller import *



class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('Courses')

    def index(self):
        all_courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html')

    def create(self):
        course_details = {
            'name' : request.form['name']
            'description' : request.form['description']

        }
        self.models['Course'].add_course(course_details)
        return redirect('/')

     def show_confirm(self, id):
        one_course = self.models['Course'].get_course_by_id(id)
        return self.load_view('destroy.html', course=course)


     def destroy(self, course_id):
         self.models['Course'].destroy(course_id)
         return redirect('/')