"""Views for WillPress.

"An Excellent Blog Engine"

Copyright (c) 2021 by William Ellison.  This program is licensed under
the terms of the Do What the Fuck You Want To Public License, version 2
or later, as described in the COPYING file at the root of this
distribution.

William Ellison
<waellison@gmail.com>
October 2021
"""


SITE_NAME = "WillPress Test Site"
POSTS_PER_PAGE = 7

BASIC_SCAFFOLD = """
<!DOCTYPE html>
<html>
  <head>
    <title>{title}</title>
  </head>
  <body>
    <h1>{site_name}</h1>  
    <nav>
      <menu>
        <li>
          <a href='/'>Home</a>
        </li>
      </menu>
    </nav>
    <main>
      {body_html}
    </main>
    <footer>
      <p>
        Copyright &copy; 2021 by William Ellison, all rights reserved.
        Proudly served with <a href='//github.com/tnwae/willpress'>WillPress</a>.
      </p>
    </footer>
  </body>
</html>
"""


def wep_erect(scaffold=BASIC_SCAFFOLD, **kwargs):
    return scaffold.format(site_name=SITE_NAME, **kwargs)
