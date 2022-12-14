#! /usr/env/python

import sys


def add_to_score(q_bool, score_in):
    if q_bool:
        score_in = score_in + 1
    return score_in

def get_response(prompt):
    q = prompt + input(prompt) + "\n\n"
    return q

def run_q0():
    q0_prompt = "Question 0: What does the command 'cd ~' do on the command line?\n"
    q0 = get_response(q0_prompt)
    return q0

def run_q1():
    q1_prompt = "Question 1: What does the command 'ls' do on the command line?\n"
    q1 = get_response(q1_prompt)
    return q1

def run_q2():
    q2_prompt = "Question 2: What are the symbols '#' used for in bash and python?\n"
    q2 = get_response(q2_prompt)
    return q2

def run_q3():
    q3_prompt = "Question 3: What is a python package? Are you familiar with any python packages?\n"
    q3 = get_response(q3_prompt)
    return q3

def run_q4():
    q4_prompt = "Question 4: What is a SNP? (hint: this is a biology question, not a computer science question)\n"
    q4 = get_response(q4_prompt)
    return q4

def run_q5():
    q5_prompt = "Question 5: What is high-throughput (next generation) sequencing? What types of high-throughput sequencing have you heard of? How do they work?\n"
    q5 = get_response(q5_prompt)
    return q5

def run_q6():
    q6_prompt = "Question 6: What is read mapping?\n"
    q6 = get_response(q6_prompt)
    return q6

def run_q7():
    q7_prompt = "Question 7: What is variant calling?\n"
    q7 = get_response(q7_prompt)
    return q7

def run_q8():
    q8_prompt = "Question 8: What are your post-graduation plans (if you have any- it's okay if you don't!)\n"
    q8 = get_response(q8_prompt)
    return q8

def run_q9():
    q9_prompt = "Question 9: What have you enjoyed learning about in CS/bioinformatics courses?\n"
    q9 = get_response(q9_prompt)
    return q9

def run_q10():
    q10_prompt = "Question 10: Is there anything in particular you want to learn before you graduate?\n"
    q10 = get_response(q10_prompt)
    return q10

def run_q11():
    q11_prompt = "Question 11: On a scale of 0-9, how comfortable are you using the command line?\n"
    q11 = get_response(q11_prompt)
    return q11

def run_q12():
    q12_prompt = "Question 12: On a scale of 0-9, how comfortable are you coding in bash?\n"
    q12 = get_response(q12_prompt)
    return q12

def run_q13():
    q13_prompt = "Question 13: On a scale of 0-9, how comfortable are you coding in python?\n"
    q13 = get_response(q13_prompt)
    return q13

def run_q14():
    q14_prompt = "Question 14: In computer science, what is a variable?\n"
    q14 = get_response(q14_prompt)
    return q14

def run_q15():
    q15_prompt = "Question 15: In computer science, what is a function?\n"
    q15 = get_response(q15_prompt)
    return q15

def run_q16():
    q16_prompt = "Question 16: What is a for loop? What is a while loop?\n"
    q16 = get_response(q16_prompt)
    return q16

def run_q17():
    q17_prompt = "Question 17: What is parallelization? Is running commands in-parallel more efficient than running them in a loop?\n"
    q17 = get_response(q17_prompt)
    return q17


if __name__ == "__main__":
    with open("test_results.txt", 'w') as outfile:
        for i in range(0,18):
            run_code = "run_q" + str(i) + "()"
            outfile.write(eval(run_code))

