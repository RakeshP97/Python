#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:49:01 2019
"""

annual_salary = float(input("Enter your annual salary: "))
percentage_savings = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_house = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: ")) 
current_savings=0
portion_down_payment=0.25 * cost_house
number_of_month=0
invest_ret = 0.04
monthy_income = (annual_salary/12)
while current_savings < portion_down_payment:
    current_savings += (current_savings * (invest_ret/12)) + (monthy_income * percentage_savings)
    number_of_month +=1
    if number_of_month%6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)
        monthy_income = (annual_salary/12)
print("Number of months: ",number_of_month)