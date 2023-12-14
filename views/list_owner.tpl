<html>
<body>
<h2>Owners List</h2>
<hr/>
<table>
% for item in owners:
  <tr>
  <td>{{str(item['name'])}}</td>
  <td>{{str(item['location'])}}</td>
  <td><a href="/owner-update/{{str(item['id'])}}">update</a></td>
  <td><a href="/owner-delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/owner-add">Add a new owner</a>
<a href="/vehicle-add">Add a new vehicle</a>
<hr/>
</body>
</html>