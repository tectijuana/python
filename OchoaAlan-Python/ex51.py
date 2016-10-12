import web

urls = (
  '/hello', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        form = web.input(name="Nobody")
        greeting = "Hello, %s" % form.name

        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()


    <html>
        <head>
            <title>Sample Web Form</title>
        </head>
    <body>

    <h1>Fill Out This Form</h1>

    <form action="/hello" method="POST">
        A Greeting: <input type="text" name="greet">
        <br/>
        Your Name: <input type="text" name="name">
        <br/>
        <input type="submit">
    </form>

    </body>
    </html>


    import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()


    $def with (greeting)

    $if greeting:
        I just wanted to say <em style="color: green; font-size: 2em;">$greeting</em>.
    $else:
        <em>Hello</em>, world!



        <h1>Fill Out This Form</h1>

      <form action="/hello" method="POST">
          A Greeting: <input type="text" name="greet">
          <br/>
          Your Name: <input type="text" name="name">
          <br/>
          <input type="submit">
      </form>


      $def with (content)

<html>
<head>
    <title>Gothons From Planet Percal #25</title>
</head>
<body>

$:content

</body>
</html>



from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):

    assert status in resp.status, "Expected response %r not in %r" % (status, resp.status)

    if status == "200":
        assert resp.data, "Response data is empty."

    if contains:
        assert contains in resp.data, "Response does not contain %r" % contains

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Response does not match %r" % matches

    if headers:
        assert_equal(resp.headers, headers)





        from nose.tools import *
        from bin.app import app
        from tests.tools import assert_response

        def test_index():
            # check that we get a 404 on the / URL
            resp = app.request("/")
            assert_response(resp, status="404")

            # test our first GET request to /hello
            resp = app.request("/hello")
            assert_response(resp)

            # make sure default values work for the form
            resp = app.request("/hello", method="POST")
            assert_response(resp, contains="Nobody")

            # test that we get expected values
            data = {'name': 'Zed', 'greet': 'Hola'}
            resp = app.request("/hello", method="POST", data=data)
            assert_response(resp, contains="Zed")


            
