from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User

from bootcamp.activities.models import Activity


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    favorites = models.IntegerField(default=0)
    has_accepted_answer = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('-update_date',)

    def __str__(self):
        return self.title

    @staticmethod
    def get_unanswered():
        return Question.objects.filter(has_accepted_answer=False)

    @staticmethod
    def get_answered():
        return Question.objects.filter(has_accepted_answer=True)

    def get_answers(self):
        return Answer.objects.filter(question=self)

    def get_answers_count(self):
        return Answer.objects.filter(question=self).count()

    def get_accepted_answer(self):
        return Answer.objects.get(question=self, is_accepted=True)

    def get_description_as_markdown(self):
        return self.description

    def get_description_preview(self):
        preview_len = 255

        if len(self.description) > preview_len:
            return f'{self.description[:preview_len]}...'

        return self.description

    def get_description_preview_as_markdown(self):
        return self.get_description_preview()

    def calculate_favorites(self):
        favorites = Activity.objects.filter(
            question=self.pk,
            activity_type=Activity.FAVORITE
        ).count()

        self.favorites = favorites
        self.save()
        return self.favorites

    def get_favoriters(self):
        favorites = Activity.objects.filter(
            question=self.pk,
            activity_type=Activity.FAVORITE
        )

        favoriters = [favorite.user for favorite in favorites]
        return favoriters

    def create_tags(self, tags):
        tags = tags.strip()
        tag_list = tags.split(' ')

        for tag in tag_list:
            Tag.objects.get_or_create(tag=tag.lower(), question=self)

    def get_tags(self):
        return Tag.objects.filter(question=self)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True)
    votes = models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ('-is_accepted', '-votes', 'create_date',)

    def __str__(self):
        return self.description

    def accept(self):
        answers = Answer.objects.filter(question=self.question)

        for answer in answers:
            answer.is_accepted = False
            answer.save()

        self.is_accepted = True
        self.save()
        self.question.has_accepted_answer = True
        self.question.save()

    def calculate_votes(self):
        up_votes = Activity.objects.filter(
            answer=self.pk,
            activity_type=Activity.UP_VOTE,
        ).count()

        down_votes = Activity.objects.filter(
            answer=self.pk,
            activity_type=Activity.DOWN_VOTE,
        ).count()

        self.votes = up_votes - down_votes
        self.save()
        return self.votes

    def get_up_voters(self):
        votes = Activity.objects.filter(answer=self.pk,
                                        activity_type=Activity.UP_VOTE,)
        voters = [vote.user for vote in votes]
        return voters

    def get_down_voters(self):
        votes = Activity.objects.filter(answer=self.pk,
                                        activity_type=Activity.DOWN_VOTE)
        voters = [vote.user for vote in votes]
        return voters

    def get_description_as_markdown(self):
        return self.description


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

        constraints = [
            models.UniqueConstraint(fields=('tag', 'question'), name='unique_question_tag')
        ]

    def __str__(self):
        return self.tag
