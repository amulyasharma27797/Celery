import graphene
import hero.schema


class Query(hero.schema.Query, graphene.ObjectType):
    pass


class HeroMutation(graphene.ObjectType):
    create_hero = hero.schema.CreateHero.Field()
    del_hero = hero.schema.DeleteHero.Field()
    update_hero = hero.schema.UpdateHero.Field()


schema = graphene.Schema(query=Query, mutation=HeroMutation)
