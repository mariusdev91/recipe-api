from django.urls import reverse
from django.utils.html import format_html, format_html_join
from django.core.cache import cache


class ReviewLinkDisplay:
    @staticmethod
    def get_review_links(obj):
        cache_key = f'reviews_for_recipe_{obj.pk}'
        links_html = cache.get(cache_key)

        if links_html is not None:
            return links_html

        reviews = obj.reviews.only('id').all()
        if not reviews:
            links_html = "No reviews for this recipe"
        else:
            links_html = format_html(
                "<div style='height:100px;overflow:auto;'>{}</div>",
                format_html_join(
                    '\n', "<a href='{}'>{}</a><br>",
                    (
                        (reverse('admin:app_review_change',
                                 args=(review.id,)),
                         f'Review {review.id}')
                        for review in reviews
                    )
                )
            )

        cache.set(cache_key,
                  links_html,
                  timeout=3600)  # Cache for 1 hour, adjust as needed
        return links_html
