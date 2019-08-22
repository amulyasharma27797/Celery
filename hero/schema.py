import graphene
from graphene_django import DjangoObjectType

from .models import Hero


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class Query(graphene.ObjectType):
    heroes = graphene.Field(HeroType)

    def resolve_heroes(self, info, **kwargs):
        return Hero.objects.all()


class CreateHero(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        gender = graphene.String(required=True)
        movie = graphene.String(required=True)

    hero = graphene.Field(lambda: HeroType)

    def mutate(self, info, name, gender, movie):
        new_hero = Hero.objects.create(name=name, gender=gender, movie=movie)
        return CreateHero(hero=new_hero)


class DeleteHero(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        del_hero = Hero.objects.filter(id=id)
        del_hero.delete()
        return DeleteHero(ok=True)


class UpdateHero(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        gender = graphene.String(required=True)
        movie = graphene.String(required=True)

    hero = graphene.Field(lambda: HeroType)

    def mutate(self, info, id, **kwargs):
        update_hero = Hero.objects.get(id=id)
        for key, val in kwargs.items():
            setattr(update_hero, key, val)
        update_hero.save()

        return UpdateHero(update_hero)
