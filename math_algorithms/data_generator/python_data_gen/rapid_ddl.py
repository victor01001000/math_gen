import varchar_column
import integer_column

datatypes = {
  'int': {
     'parsing_values': ['integer', 'int', 'INT'],
     'min': -32768,
     'max': 32767
   },
  'varchar': {
     'parsing_values': ['varchar', 'VARCHAR'],
     'min': 0,
     'max': 10
   }
}


class RapidDDL:

  def __init__(self, ddl_file, number_of_rows):
    self.ddl_file = ddl_file
    self.number_of_rows = int(number_of_rows)

  def read_ddl(self):
    with open(self.ddl_file, "r") as ddl:
      line = ddl.readline()
      while line:
        nodes = line.split("(", 1)
        columns = str(nodes[1])[:-3].split(",")
        line = ddl.readline()
    return columns

  def generate_rows(self, columns):
    names = []
    types = []
    for i in columns:
      column_parts = i.strip().split()
      names.append(column_parts[0])
      if "CHAR" in column_parts[1]:
         types.append(column_parts[1].split("(")[0])
         datatypes['varchar']['max'] = int(column_parts[1].split("(")[1].strip("()"))
      else:
        types.append(column_parts[1])
    with open("data.csv", "w") as f:
      for x in range(self.number_of_rows):
        for i in types:
          if i in datatypes['int']['parsing_values']:
            data = integer_column.Integer16(datatypes['int']['min'], datatypes['int']['max']).generate_value()
            f.write(str(data) + ",")
          elif i in datatypes['varchar']['parsing_values']:
            data = varchar_column.Varchar(datatypes['varchar']['min'], datatypes['varchar']['max']).generate_value()
            f.write(str(data) + ",")
        f.write("\n")
      f.close()
