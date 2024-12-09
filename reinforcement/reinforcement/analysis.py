# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9 
    # answerNoise = 0.2

    # TRIAL AND ERROR?
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    # Prefer the close exit (+1), risking the cliff (-10)  

    # high: focus on more inmediate rewards 
    answerDiscount = 0.9
    # low: ensures the agent can take a risky path confidently
    answerNoise = 0.2
    # negative: discourages unnecessarily long paths
    answerLivingReward = -3
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    # Prefer the close exit (+1), but avoiding the cliff (-10)

    # focus on getting the exit (little less) fast 
    answerDiscount = 0.2
    # low: agent avoids high-risk paths
    answerNoise = 0.1
    # safe but shorter path
    answerLivingReward = 0

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    # Prefer the distant exit (+10), risking the cliff (-10)

    # high: values high payoff over inmediate rewards
    answerDiscount = 0.9
    # low: confidently navigate risky paths
    answerNoise = 0
    # slightly negative: discourage detours
    answerLivingReward = -0.5

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    # Prefer the distant exit (+10), avoiding the cliff (-10)

    # high: prioritizes the distant exit payoff
    answerDiscount = 0.9
    # low: avoids risky paths but seeks distant goal
    answerNoise = 0.2
    # 0: encourages a longer path
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    # Avoid both exits and the cliff (so an episode should never terminate)

    # 0: no future rewards, avoiding exits entirely
    answerDiscount = 0
    # 0: agent doesn't need to aim for any specific path
    answerNoise = 0
    # high:  encourages the agent to stay in the grid indefinitely
    answerLivingReward = 0.9
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
