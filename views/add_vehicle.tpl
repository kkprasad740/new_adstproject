<html>
<body>
<hr/>
<form action="/vehicle-add" method="post">
  <p>Name:<input name="name"/></p>
  <p>Description:<input name="description"/></p>
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