st="1"*203
M=-22
for i in range(204):
    st = "1" * 203
    st=st[:i]+"2"+ st[i:]
    while "111" in st or "222" in st:
        st=st.replace("111","22",1)
        st=st.replace("222","11",1)
    if len(st)>M:
        M=len(st)
        p=st
    st=st[:i]+st[i+1:]
    print(st)
print(p)