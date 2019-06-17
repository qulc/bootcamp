from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from .models import Question, Answer


class QuestionsMethodTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='john',
            email='lennon@thebeatles.com',
            password='johnpassword'
        )
        self.question = Question.objects.create(
            user=user,
            title='test title',
            description='test decorators',
        )
        Answer.objects.create(
            user=user,
            question=self.question,
            description='test answers decorators',
            is_accepted=True,
        )

    def test_get_answers(self):
        answers = self.question.get_answers()
        self.assertIsInstance(answers, QuerySet)

        answers_count = self.question.get_answers_count()
        self.assertIsInstance(answers_count, int)

        accept_answer = self.question.get_accepted_answer()
        self.assertIsInstance(accept_answer, Answer)

    def test_get_description(self):
        description_markdown = self.question.get_description_as_markdown()
        self.assertEqual(description_markdown, '<p>test decorators</p>')

        description_preview = \
            self.question.get_description_preview_as_markdown()
        self.assertEqual(description_preview, '<p>test decorators</p>')

    def test_get_favorites(self):
        favorites_count = self.question.calculate_favorites()
        self.assertEqual(favorites_count, 0)

        favoriters = self.question.get_favoriters()
        self.assertIsInstance(favoriters, list)

    def test_tags(self):
        tags = 'Python Tornado Async'
        self.question.create_tags(tags)

        tag_list = self.question.get_tags()
        self.assertIsInstance(tag_list, QuerySet)

        expect_tag = ('python', 'tornado', 'async')
        for tag in tag_list:
            self.assertIn(tag.tag, expect_tag)


class AnswerMethodTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='john_1',
            email='lennon_1@thebeatles.com',
            password='johnpassword'
        )
        question = Question.objects.create(
            user=user,
            title='test title 1',
            description='test decorators 1',
        )
        self.answer = Answer.objects.create(
            user=user,
            question=question,
            description='test answers decorators 1',
            is_accepted=True,
        )

    def test_get_vote(self):
        self.answer.accept()

        votes_count = self.answer.calculate_votes()
        self.assertIsInstance(votes_count, int)

        up_voters = self.answer.get_up_voters()
        self.assertIsInstance(up_voters, list)

        down_voters = self.answer.get_down_voters()
        self.assertIsInstance(down_voters, list)

        expect_markdown = '<p>test answers decorators 1</p>'
        description_markdown = self.answer.get_description_as_markdown()
        self.assertEqual(description_markdown, expect_markdown)
