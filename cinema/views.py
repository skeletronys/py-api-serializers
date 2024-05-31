from rest_framework import viewsets

from cinema.models import (
    Movie,
    MovieSession,
    Actor,
    CinemaHall,
    Genre
)
from cinema.serializers import (
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionListSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieSerializer,
    MovieSessionSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self) -> list[Movie]:
        queryset = self.queryset

        if self.action == "list":
            queryset = queryset.prefetch_related("actors", "genres")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return self.serializer_class


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> list[MovieSession]:
        queryset = self.queryset

        if self.action == "list":
            return queryset.select_related("movie", "cinema_hall")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return self.serializer_class
