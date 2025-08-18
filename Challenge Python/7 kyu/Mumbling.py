def accum(st):
    st_ = list(st)
    new_st = []

    for x in st_:
        new_st.append(x.upper() + x.lower)

    return new_st

print(accum('abcd'))
