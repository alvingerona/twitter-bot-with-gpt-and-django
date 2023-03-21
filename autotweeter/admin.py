from django.contrib import admin
from django.forms import ValidationError
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from . import models
from .services import makeCompletion

# Custom admin views


@staff_member_required
def generateTweets(request):

    makeCompletion()

    messages.add_message(request, messages.INFO,
                         'New tweets has been generated, check the entries with status "For Review"')

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'body_summary', 'character_len',
                    'status', 'is_twitted_label', 'created_at']
    list_editable = ['status']

    def get_urls(self):
        urls = super(TweetAdmin, self).get_urls()
        custom_urls = [
            # add custom URL for generating tweet
            path("generate-tweets/", generateTweets)
        ]
        return custom_urls + urls

    def body_summary(self, tweet):

        if len(tweet.body) > 75:
            return tweet.body[:75] + "..."

        return tweet.body

    @admin.display(ordering='tweeted_at', description="Tweeted?")
    def is_twitted_label(self, tweet):
        if(tweet.tweeted_at):
            return "Yes"

        return "No"

    @admin.display(description="Length")
    def character_len(self, tweet):
        """
        Compute number of character same as tweet character counter
        """

        return len(tweet.body)


# Register models in admin
admin.site.register(models.Tweet, TweetAdmin)
