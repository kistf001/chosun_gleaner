from pywinauto.application import Application
import pywinauto
import time

# 어플리케이션 모듈 선언
app = pywinauto.application.Application()

# pywinauto 목록생성
procs = pywinauto.findwindows.find_elements()
for proc in procs:
    print(proc)
    if  'Internet Explorer' in  proc.name:
        break

app = Application(backend="uia").connect(process=proc.process_id) # process 연결
app.top_window().set_focus()
#time.sleep(3)
# 어플리케이션 모듈 선언
#pywinauto.mouse.move(coords=(0,0))
pywinauto.mouse.click(coords=(224,394))
pywinauto.mouse.click(coords=(224,394))
pywinauto.mouse.click(coords=(224,394))
pywinauto.keyboard.send_keys('20195136')

pywinauto.mouse.click(coords=(224,414))
pywinauto.mouse.click(coords=(224,414))
pywinauto.mouse.click(coords=(224,414))
pywinauto.keyboard.send_keys('1545861De#')

pywinauto.mouse.click(coords=(324,405))
pywinauto.mouse.click(coords=(324,405))
pywinauto.mouse.click(coords=(324,405))

###############################################
time.sleep(3)
#수강신청칸 뜨는지 검토 필요
###############################################
pywinauto.mouse.click(coords=(137,249))
pywinauto.mouse.click(coords=(137,249))
pywinauto.mouse.click(coords=(137,249))

###############################################
time.sleep(3)
#수강신청 버튼 뜨는지 검토 필요
###############################################
pywinauto.mouse.click(coords=(910,247))
pywinauto.mouse.click(coords=(910,247))
pywinauto.mouse.click(coords=(910,247))

###############################################
time.sleep(3)
#웹페이지 메시지 버튼 뜨는지 검토 필요
###############################################
pywinauto.mouse.click(coords=(802,586))
pywinauto.mouse.click(coords=(802,586))
pywinauto.mouse.click(coords=(802,586))

###############################################
time.sleep(3)
#학과(부)  버튼 뜨는지 검토 필요
###############################################
pywinauto.mouse.click(coords=(222,190))
pywinauto.mouse.click(coords=(222,190))
pywinauto.mouse.click(coords=(222,190))

afdsf = [
    [751,194]#영어
    [751,211]#
    [751,529]#운영체제
    [751,544]#
    [751,562]#자바프로그래밍
    [751,574]#
]
for af in range(0,15):
    for ss in afdsf:
        time.sleep(1)
        pywinauto.mouse.double_click(coords=(ss[0],ss[1]))
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(521,486))
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(626,517))
        time.sleep(0.5)
        pywinauto.mouse.click(coords=(730,580))