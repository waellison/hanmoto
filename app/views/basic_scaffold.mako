<%
    from flask import url_for
%>
<!DOCTYPE html>
<html>
  <head>
    <title>
      ${title}
    </title>
    <link rel="stylesheet" type="text/css" href="${url_for('static', filename='assets/style.css')}">
  </head>
  <body>
    <h1>${site_name}</h1>
    <nav>
      <menu>
        <li>
          <a href='/'>Home</a>
        </li>
        <li>
          % if user is None:
            <a href="/login">Login</a>
          % else:
            <img src="${user['avatar']}" class="profile-picture">
            Welcome, <a href="/users/${user['user_id']}">
              ${user['username']}</a> (<a href="/logout">Logout</a>)
          % endif
        </li>
      </menu>
    </nav>
    <main>
      ${body_html}
    </main>
    <footer>
      <p>
        Copyright &copy; 2021 by William Ellison, all rights reserved.
        Proudly served with <a href='//github.com/tnwae/willpress'>WillPress</a>.
      </p>
    </footer>
  </body>
</html>