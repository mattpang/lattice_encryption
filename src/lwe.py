# learning with errors. 
# impart a small sampled error into a set of equations. sigma=2 for k=4 seems fine 


import random 
from collections import defaultdict

def make_equations(s:list[int],mod_value:int=69,seed:int=42,size=10):
    # Given some polynomial and modulo; generate a set of equations. and add some errors to it. 
    random.seed(seed)
    eqns = []
    for j in range(size):
        b=0
        terms = {} 
        for i,p in enumerate(s):
            a_i = random.randint(-50,50)
            terms[f'p_{i}'] = a_i
            b += a_i*p
        error_term = int(random.gauss(0,sigma=2))
        b+=error_term
        
        terms['ans'] = b%mod_value
        eqns.append(terms)
    return eqns


def encode(eqn,message,mod_val,size:int):
    # randomally pick N[size] eqns, and return the sum of all values along with the message.
    sampled_eqn = random.sample(eqn,k=size)
    total = defaultdict(int)

    for e in sampled_eqn:
        for k,v in e.items():
            total[k]+=v

    total['ans'] += mod_val//2 * message   
    # total['ans'] = total['ans'] % mod_val
    
    # print('---')
    # print(sampled_eqn)
    # print(total)
    # print(message)
    # print('---')
    # this part seems to be working
    return total

def decode(payload:list[defaultdict[int]],s:list[int],mod_val:int=69):
    results = [] 
    for line in payload:
        ans = line.pop('ans')
        tmp_ans = 0
        for i,x in enumerate(s):
            tmp_ans += line[f'p_{i}']*x
        tmp_ans=tmp_ans%mod_val
        
        # print(tmp_ans,ans, (tmp_ans-ans)%mod_val)
        # is it closer to mod_val//2 or 0? 
        if 3*(mod_val//4) > (ans-tmp_ans)%mod_val > mod_val//4:
            results.append('1')
        else:
            results.append('0')

    # every 8 block, we turn into an int and chr it. 
    message = ''
    s = []

    for r in results:
        s.append(r)
        if len(s)==8:
            num = int(''.join(s),2)
            print(''.join(s),num)
            try:
                message += chr(num)
            except ValueError:
                print('fucked',num)
                message+='*'
            s = [] 

    return message

def communicate(message='Hello world',mod_val=69):
    # simulate communication between Alice and Bob
    # Alice has her private key, the int vector s.
    # Her public key is the set of the eqauations and answers (+plus some random errors)
    #
    # Bob picks at random a set of the equations, and adds them up. 
    # He adds 0 or 1 accordingly in each sample of eqns, at either 0 or modulo//2
    # 
    # Alice will decrypt using her private key. and the errors should be small (and sum to zero anyway) compared the mod//2 value

    eqns = make_equations(s=[1,2,3],size=100,mod_value=mod_val)

    # encode message to binary.
    payload = [] 
    sent = ''
    for char in message:
        m = bin(ord(char))
        print(str(m),ord(char),char)
        bstring = str(m)[2:]
        if bstring!=8:
            # prepend so they are all length 8
            bstring = '0'*(8-len(bstring)) + bstring
            sent+=bstring
            for b in bstring:
                payload.append(encode(eqns,int(b),mod_val,size=4))
    # print(payload)
    print(sent)

    # Now for Alice to try and decode this. 
    # take every 8th as a byte int, and then to a char
    recv = decode(payload, s=[1,2,3], mod_val=mod_val)
    print(recv)
    # chr(23)

if __name__=='__main__':
    # e = make_equations(s=[1,2,3])
    # print(e)

    communicate()
    
