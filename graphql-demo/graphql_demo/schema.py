import graphene
import graphql_demo.movies.schema

##
## Both of these are passive, simply inheriting functionality from our app schemas
##

class Query(graphql_demo.movies.schema.Query, graphene.ObjectType):
    pass

class Mutation(graphql_demo.movies.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)