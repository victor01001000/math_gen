#!/usr/bin/env python3

class Polynomial():

    def __init__(self, generated_eq):
        self.terms_list = generated_eq


    def get_equation(self):
        constructed_eq = ''
        for i in range(len(self.terms_list)):
            element = self.terms_list[i]

            if int(element.coefficient) < 0:
                constructed_eq += element.get_function()
            else:
                if(i == 0):
                    constructed_eq += element.get_function()
                else:
                    constructed_eq += '+' + element.get_function()

        return constructed_eq