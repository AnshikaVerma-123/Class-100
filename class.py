class Biodata ():
  def __init__( self, name, age, grade, school, favouriteSubjects, favouriteFruit):
    self.name = name
    self.age= age
    self.grade= grade
    self.school= school
    self.favouriteSubjects =favouriteSubjects
    self.favouriteFruit =favouriteFruit

object1 = Biodata ("Anshika", 12, 8 , "CMS" , "Computer", "Apple")
print(object1.name)
print(object1.favouriteFruit)


