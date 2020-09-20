
from bangtal import *

scene1 = Scene("방", "이미지/방.png")
scene2 = Scene("버정1", "이미지/버정1.png")
scene3 = Scene("매장","이미지/애플매장.png")
scene4 = Scene("버정2","이미지/버정2.png")

closed1 = True
arived1 = False
arived2 = False
buy = False

door1 = Object('이미지/방문-닫힘.png')
door1.locate(scene1, 880, 205)
door1.show()

wallet = Object('이미지/지갑.png')
wallet.locate(scene1, 415, 335)
wallet.show()

sign1 = Object('이미지/표지판1.png')
sign1.locate(scene2, 900, 171)
sign1.show()

bus1 = Object('이미지/버스1.png')
bus1.locate(scene2, 230, 155)

macbook = Object('이미지/맥북.png')
macbook.locate(scene3, 600, 286)
macbook.show()

exit = Object('이미지/나가기.png')
exit.setScale(0.5)
exit.locate(scene3, 250, 20)
exit.show()

sign2 = Object('이미지/표지판2.png')
sign2.locate(scene4, 300, 171)
sign2.show()

bus2 = Object('이미지/버스2.png')
bus2.locate(scene4, 500, 155)

end = Object('이미지/종료.png')
end.locate(scene1, 420, 400)


def door1_onMouseAction(x, y, action):
    global closed1

    if closed1 == True:
        door1.setImage('이미지/방문-열림.png')
        closed1 = False

    else:
        scene2.enter()
        door1.setImage('이미지/방문-닫힘.png')
        closed1 = True

door1.onMouseAction = door1_onMouseAction


def wallet_onMouseAction(x, y, action):
    wallet.pick()
        
wallet.onMouseAction = wallet_onMouseAction

def sign1_onMouseAction(x, y, action):
    global arived1

    if arived1 == False:
        bus1.show()
        arived1 = True

sign1.onMouseAction = sign1_onMouseAction

def bus1_onMouseAction(x, y, action):
    global arived1

    if arived1 == True:
        scene3.enter()
        showMessage('맥북을 결제하자')
        arived1 = False
        bus1.hide()

bus1.onMouseAction = bus1_onMouseAction

def exit_onMouseAction(x, y, action):
    scene4.enter()

exit.onMouseAction = exit_onMouseAction

def sign2_onMouseAction(x, y, action):
    global arived2

    if arived2 == False:
        bus2.show()
        arived2 = True

sign2.onMouseAction = sign2_onMouseAction

def bus2_onMouseAction(x, y, action):
    global arived2

    if arived2 == True and not macbook.inHand():
        scene1.enter()
        arived2 = False
        bus2.hide()

    elif arived2 == True and macbook.inHand():
        scene1.enter()
        showMessage('맥북을 사왔다 기분 좋아')
        end.show()

bus2.onMouseAction = bus2_onMouseAction

def macbook_onMouseAction(x, y, action):
    global buy

    if buy == False and wallet.inHand():
        showKeypad('3690000', macbook)


    else:
        showMessage('헉 지갑을 안 가져 왔다')

macbook.onMouseAction = macbook_onMouseAction


def macbook_onKeypad():
        showMessage('맥북을 구매했다')
        buy = True
        macbook.pick()
        macbook.hide()

macbook.onKeypad = macbook_onKeypad

def end_onMouseAction(x, y, action):
    endGame()

end.onMouseAction = end_onMouseAction


startGame(scene1)

