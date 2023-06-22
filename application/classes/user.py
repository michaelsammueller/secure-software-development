class User():
   pass

   def __init__(self, name, dob):
      self.__name = name
      self.__dob = dob

   def get_name(self):
      return self.__name

class Employee(User):
   pass

   def __init__(self, name, dob):

      User.__init__(self, name, dob)

   def request_holiday(self, date, ndays):
      self.holiday = Holiday(date, ndays, self)

      return self.holiday

class Manager(User):
   pass

   def __init__(self, name, dob):

      User.__init__(self, name, dob)

   def approve_holiday(self, holiday):
      self.holiday = holiday
      self.holiday.approved = True
      return self.holiday
