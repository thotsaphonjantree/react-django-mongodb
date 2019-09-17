from mongoengine import Document, EmbeddedDocument, fields
 
# class Major(EmbeddedDocument):
#     major_name = fields.StringField(required=True)


class Student(Document):
    student_code = fields.StringField(required=True)
    first_name = fields.StringField(required=True)
    last_name = fields.StringField(required=True)
    Major = fields.ReferenceField("Major",required=True)

class Major(Document):
    major_name = fields.StringField(required=True)






