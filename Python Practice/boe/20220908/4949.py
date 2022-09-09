

while True:
    st=[]
    p = 1
    n = input()
    if n != '.':
        for i in n:
            if i == '(':
                st.append('(')
            elif i == ')':
                if st:
                    a = st.pop()

                    if a != '(':
                        p = 2
                else:
                    p = 2
            elif i == '[':
                st.append('[')
            elif i == ']':
                if st:
                    b = st.pop()

                    if b != '[':
                        p = 2
                else:
                    p = 2
        if p == 1 and not st:
            print('yes')
        else:
            print('no')
    else:
        break