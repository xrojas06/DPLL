# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:29:21 2020

@author: ximen
"""
def complemento(p):
    neg = "-"
    if neg in p:
        return p[-1]
    else:
        x = "-"+p
        return x
def unitclause(S):
    for i in S:
        if len(i)==1 or (len(i)==2 and "-" in i):
            return True
    return False
def searchunit(S):
    if unitclause(S):
        for i in S:
            if len(i)==1 or (len(i)==2 and "-" in i):
                return i
def unitPropagate(S, I):
    empty = []
    while empty not in S and unitclause(S):
           i = searchunit(S)
           j = i[0]
           q = 0
           while q<len(S):
               x = S[q]
               if j in x:
                  S.remove(x)
                  q-=1
               if complemento(j) in x: 
                  x.remove(complemento(j))    
               q+=1
           if "-" in j:
               j2 = j[-1]
               I[j2] = 0
           else:
               I[j] = 1
    return S,I
def notassign(S,I):
    for i in S:
        for j in i:
            if j not in I and complemento(j) not in I:
                return j
def dpll(S,I):
    empty = []
    S, I = unitPropagate(S,I)
    if empty in S:
        return "INSATISFACIBLE",{}
    if len(S)==0:
        return "SATISFACIBLE",I
    lit = notassign(S,I)
    S1 = S.copy()
    q = 0
    while q<len(S1):
       p = complemento(lit)
       x = S1[q]
       if lit in x:
           S1.remove(x)
           q-=1
       if p in x: 
           y = []
           for i in x:
               if i!=p:
                   y.append(i)
           S1.remove(x)
           S1.append(y)
           q-=1
       q+=1
    I1 = I.copy()
    if "-" in lit:
        lit2 = lit[-1]
        I1[lit2] = 0
    else:
        I1[lit] = 1
    m, n = dpll(S1,I1)
    if m == "SATISFACIBLE":
        return m,n
    else:
        S2 = S
        w = 0
        while w<len(S2):
            x = S2[w]
            if complemento(lit) in x:
                S2.remove(x)
                w-=1
            if lit in x: 
                x.remove((lit)) 
            w+=1
        I2 = I
        if "-" in complemento(lit):
            I2[lit] = 0
        else:
            I2[complemento(lit)] = 1
        return dpll(S2,I2)

#S = [['p'],['-p','q'],['-q','r','s']]       
#S = [['p','-q','r'],['-p', 'q','-r'], ['-p','-q','r'],['-p','-q','-r']]
#S = [['p','q','r'],['-p','-q','-r'],['-p','q','r'],['-q','r'],['q','-r']]
#S = [['p','q','r','-s'],['p','t','s'],['-p','-q'],['p','r','-q','-s']]
#S = [['p','-q'],['-p','-q'],['q','r'],['-q','-r'],['-p','-r'],['p','-r']]
#S = [['p','q','-r'],['r','s','t'],['t'],['p','s'],['q','-p']]
S = [['r','p','s'],['-r','-p','-s'],['-r','p','s'],['p','-s']]
I = {}
# print (unitPropagate(S,I))
#print (dpll(S,I))
