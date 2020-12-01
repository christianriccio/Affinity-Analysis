''' 
the basic idea is that when two things appear historically togheter, then they are more likely to appear 
togheter in the future, so if the user made the choice X she/he is more likely to made the choice y
'''
import numpy as np
from collections import defaultdict 

def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print(f"""Rule: If a person buys {premise_name} then she/he will buy {conclusion_name}
        Support: {support[(premise,conclusion)]}
        Confidence: {np.round(confidence[(premise, conclusion)], 5)}""")

name = 'affinity_dataset.txt'

df = np.loadtxt(name)

rows, cols = df.shape

features = ["bread", "milk", "cheese", "apples", "bananas"]

#let's print the first fine rows of the df 
print(df[:5])

'''
each row of the df represent the items purchased in the first transaction and so forth with the
other rows
each column represent every of the items
we have: bread, milk, cheese, apples, bananas
'''

'''
LET'S IMPLEMENT THE RULE WHERE IF A PERSONE BUY THE PRODUCT X SHE/HE IS MORE LIKELY TO BUY Y
to implement the rule we considere premise and conclusion 
is the momento to perform the rules for all the relations insiede the dataset.
i will create two dictionaries:
1) valide rules 
2) invalid rules
in each dictionary i will store a tuple for the rule
given the premise, if the conclusion is equal to it then the rule is valid, and while the premise is 
given and the conclusion is not satisfied then the rule does not exist
'''
apples_buy=0
for el in df:
    if el[3] == 1:
        apples_buy+=1

print(f'{apples_buy} apples has been buyed')
print()
valid_rules=0
invalid_rules=0
for el in df:
    if el[4]==1:
        if el[2]==1:
            valid_rules+=1
        else:
            invalid_rules+=1

print("People that have bouhht bananas and milk are:", valid_rules)
print("people for which is not valid the association is:", invalid_rules)
print()
print()
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurences = defaultdict(int)

for el in df:
    for premise in range(cols):
        if el[premise] == 0: 
            continue
        num_occurences[premise] += 1
        for conclusion in range(cols):
            if premise == conclusion: 
                continue
            if el[conclusion] == 1:
                valid_rules[(premise, conclusion)] +=1
            else:
                invalid_rules[(premise, conclusion)]+=1

support = valid_rules 
confidence =dict()

for premise, conclusion in valid_rules.keys():
    rule= (premise, conclusion)
    confidence[rule]= valid_rules[rule]/num_occurences[premise]

for premise, conclusion in confidence:
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print(f"Rule: If a person buys {premise_name} they will also buy {conclusion_name}")
    print(f" - Confidence: {np.round(confidence[(premise, conclusion)],5)}")
    print(f" - Support: {support[(premise, conclusion)]}")
    print()

'''
i have now i dictionary with the support and confidence for each rule
'''
premise=1
conclusion = 3
print_rule(premise, conclusion, support, confidence, features)
# The best Rules
'''
here I perform a rank to find the best rules
'''
print()
print()
print(confidence)
print()
sorted_confidence= sorted([(np.round(v,5), np.array(k)) for k, v in confidence.items()], reverse=True)
print(sorted_confidence)
print()
print()
print()
sorted_support=sorted([(v, k) for k, v in support.items()], reverse=True)
print(sorted_support)
print()
for i in range(5):
    print(f'''Rule {i}''')
    premise, conclusion =sorted_support[i][1]
    print_rule(premise, conclusion, support, confidence, features)
    print()
print()
for i in range(5):
    print(f"Rule {i}")
    premise, conclusion = sorted_confidence[i][1]
    print_rule(premise, conclusion, support, confidence, features)


