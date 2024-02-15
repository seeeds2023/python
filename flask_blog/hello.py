from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World 12345!'

@app.route('/table')
def table():
    return style() + static_table()

@app.route('/table')
def dtable():
    return style() + dynamic_table()

def style():
    return'''
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}

table.center {
  margin-left: auto; 
  margin-right: auto;
}
</style>
'''

def static_table():
    return '''
 <table class="center">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table> 
'''

def dynamic_table():
    return 'todo'