


from system.core.model import Model
class CourseModel(Model):
    def __init__(self):
        super(CourseModel, self).__init__()

    def add_course(self, course):
      # Build the query first and then the data that goes in the query
      query = "INSERT INTO courses (title, description, created_at) VALUES (:title, :description, NOW())"
      data = { 'title': course['title'], 'description': course['description'] }
      return self.db.query_db(query, data)

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_course_by_id(self, course_id):
        # pass data to the query like so
        query = "SELECT * FROM courses WHERE id = :course_id"
        data = { 'course_id': course_id}
        return self.db.query_db(query, data)


    def destroy(self, course_id):
      query = "DELETE FROM courses WHERE id = :course_id"
      data = { "course_id": course_id }
      return self.db.query_db(query, data)