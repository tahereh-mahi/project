import tornado.web
import tornado


class TestHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('test.html', name='', fname='ali')

    def post(self, *args, **kwargs):
        name = self.get_argument('name', None)

        self.write('khosh amadin !!!')
        print "************************" + name
