<html>
<body>
<h2>Vehicles List</h2>
<hr/>
<table>
% for item in vehicles:
  <tr>
  <td>{{str(item['name'])}}</td>
  <td>{{str(item['description'])}}</td>
  <td>{{str(item['owner_name'])}}</td>
  <td><a href="/vehicle-update/{{str(item['id'])}}">update</a></td>
  <td><a href="/vehicle-delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/vehicle-add">Add a new item</a>
<hr/>
</body>
</html>