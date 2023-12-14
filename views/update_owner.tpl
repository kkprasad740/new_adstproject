<html>
<body>
<hr/>
<form action="/owner-update" method="post">
  <input type="hidden" name="id" value="{{str(item['id'])}}"/>
  <p>Name:<input name="name" value="{{item['name']}}"/></p>
  <p>Location:<input name="location" value="{{item['location']}}"/></p>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>