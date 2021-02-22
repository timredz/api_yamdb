from api.permissions import IsAuthorOrIsAdminOrReadOnly, IsGetOrIsAdmin
from api.models.title import Title
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from api.models import Comment, Review, Title
from api.models.title import Title
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorOrIsAdminOrReadOnly,
        # IsGetOrIsAdmin,
        IsAuthenticatedOrReadOnly,
        # IsAuthenticated
    ]
    # pagination_class = PageNumberPagination
    # http_method_names = ('GET', 'POST')

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        review = get_object_or_404(
            Review,
            title=title,
            id=self.kwargs.get("review_id")
        )
        return review.comments.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        review = get_object_or_404(
            Review,
            title=title,
            id=self.kwargs.get("review_id")
        )
        serializer.save(review=review, author=self.request.user)

    # def perform_update(self, serializer):
    #    title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
    #    review = get_object_or_404(
    #        Review,
    #        title=title,
    #        id=self.kwargs.get("review_id")
    #    )
    #    comment = get_object_or_404(
    #        Comment,
    #        review=review,
    #       id=self.kwargs.get("comment_id")
    #    )
    #    serializer.save(comment=comment, author=self.request.user)

# ---------------------Не использовать-----------------------------------
# class Comment_IDViewSet(viewsets.ModelViewSet):
#    queryset = Comment.objects.all()
#    serializer_class = CommentSerializer
#    permission_classes = [
#        IsAuthenticatedOrReadOnly,
#        IsAuthorOrIsAdminOrReadOnly
#    ]
#    pagination_class = PageNumberPagination
#    http_method_names = ('GET', 'PATCH', 'DELETE')
#
#    def get_queryset(self):
#        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
#        review = get_object_or_404(
#            Review,
#            title=title,
#            id=self.kwargs.get("review_id"),
#        )
#        comment = get_object_or_404(
#            Comment,
#            review=review,
#            id=self.kwargs.get("comment_id")
#        )
#        return comment
#
#    def perform_update(self, serializer):
#        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
#        review = get_object_or_404(
#            Review,
#            title=title,
#            id=self.kwargs.get("review_id")
#        )
#        comment = get_object_or_404(
#            Comment,
#            review=review,
#            id=self.kwargs.get("comment_id")
#        )
#        serializer.save(comment=comment, author=self.request.user)
