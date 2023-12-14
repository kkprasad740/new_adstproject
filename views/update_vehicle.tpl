<html>
<body>
<hr/>
<form action="/vehicle-update" method="post">
  <input type="hidden" name="id" value="{{str(item['id'])}}"/>
  <p>Name:<input name="name" value="{{item['name']}}"/></p>
  <p>Description:<input name="description" value="{{item['description']}}"/></p>
  <P>Owner:
    <select name="ownerId">
      % for item in owners:
        <option value="{{item['id']}}">{{item['name']}}</option>
      % end
    </select>
  </p>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>