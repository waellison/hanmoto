<% from flask import url_for %>
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
          % if google_data is None:
            <a href="/login">Login</a>
          % else:
            <img src="${google_data['picture']}" class="profile-picture">
            Welcome, <a href="/users/${google_data['id']}">
              ${google_data['given_name']}</a> (<a href="/logout">Logout</a>)
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