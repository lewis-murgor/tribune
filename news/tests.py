from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.lewis= Editor(first_name = 'Lewis', last_name ='Murgor', email ='kiplagatlewis29@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lewis,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.lewis.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class TagTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.champions= tags(name = 'The Uefa Champions League')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.champions,tags))

class ArticleTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        # Creating a new editor and saving it
        self.editor_lewis = Editor(first_name = 'Lewis', last_name ='Murgor', email ='kiplagatlewis29@gmail.com')
        self.editor_lewis.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Champions League', post = 'The quater finals of the champions league to be played soon.', editor = self.editor_lewis)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    
    # Testing  instance
    def test_check_instance_variables(self):
        self.assertEqual(self.new_article.title, 'Champions League')
        self.assertEqual(self.new_article.post, 'The quater finals of the champions league to be played soon.')
        self.assertEqual(self.new_article.editor, self.editor_lewis)

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
