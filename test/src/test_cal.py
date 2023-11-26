from app.src.cal import calculator

cal=calculator()

def test_divide():
    assert cal.add(1,1)==2
#    assert cal.divide(1,0)==0
    assert cal.divide(3,1)==3
