from behave import given, when, then
from src.package.samourai import Samourai
from src.package.dog import Dog

@given('a samourai named "{samourai_name}"')
def step_given_samourai(context, samourai_name):
    context.samourai = Samourai(samourai_name)

@given('a dog named "{dog_name}"')
def step_given_dog(context, dog_name):
    context.dog = Dog(dog_name)


@when('the samourai feeds the dog with {food}')
def step_then_samourai_feeds_dog_with_various_foods(context, food):
    context.samourai.setDog(context.dog)
    context.samourai.feedDog(food)

@then('the dog should be satisfied')
def step_then_dog_should_be_satisfied(context):
    assert context.dog.is_satisfied(), f"{context.dog.name} is not satisfied after being fed."

@then('the dog eat "{samourai_name}"')
def step_then_dog_should_be_satisfied(context, samourai_name):
    context.samourai.feedDog(samourai_name)
