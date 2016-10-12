import web

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()

    $def with (greeting)

    <html>
        <head>
            <title>Gothons Of Planet Percal #25</title>
        </head>
    <body>

    $if greeting:
        I just wanted to say <em style="color: green; font-size: 2em;">$greeting</em>.
    $else:
        <em>Hello</em>, world!

    </body>
    </html>

    import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
