# -*- coding: utf-8 -*-
import requests,sys,os
import yaml
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton
from PyQt5.QtGui import QIcon

SLACK_TOKEN = os.environ['SLACK_TOKEN']
API_URL = 'https://{0}/api/users.profile.set'.format(os.environ['SLACK_DOMAIN'])

def change_status(icon,message):
    message = '"status_text":"{0}"'.format(message)
    payload = {
        'token' : SLACK_TOKEN,
        'profile' : '{"status_emoji":":%s:",%s}' % (icon,message)
    }
    res = requests.post(API_URL,params=payload)

def click_ok():
    change_status('ok','話しかけても大丈夫です！')

def click_busy():
    change_status('warning','集中して作業中！火急の要件でなければ暫く後にしてください。')

def click_ng():
    change_status('x','本番作業中！障害以外は後にしてください。')

def click_sm():
    change_status('smoking','屋上にいます。')

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))
    w = QWidget()
    w.setWindowTitle("Status for slack")
    w.setGeometry(300, 300, 200, 150)
    w.setMinimumHeight(100)
    w.setMinimumWidth(250)
    w.setMaximumHeight(100)
    grid = QGridLayout()
    w.setLayout(grid)
    button_ok = QPushButton('OK')
    button_busy = QPushButton('Busy')
    button_sm = QPushButton('Smoking')
    button_ng = QPushButton('NG')
    button_ok.clicked.connect(click_ok)
    button_busy.clicked.connect(click_busy)
    button_sm.clicked.connect(click_sm)
    button_ng.clicked.connect(click_ng)
    grid.addWidget(button_ok, 0,0)
    grid.addWidget(button_ng, 0,1)
    grid.addWidget(button_busy, 1,0)
    grid.addWidget(button_sm, 1,1)
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
