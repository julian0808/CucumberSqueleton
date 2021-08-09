from behave import *
from functions.functions import myFunctions

use_step_matcher("re")


@given("test squeleton class")
def step_impl(context):
    myFunctions.sum(context)


@then("sumo el resultado \+ (.*)")
def step_impl(context, numero):
    myFunctions.resultSum(context, int(numero))

