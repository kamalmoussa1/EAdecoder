'''

This is a simple application that decode Arabic letters into its English
opposites letters on the keyboard, and vice versa.

Author: Kamal Moussa
last edit: Dec 6 2016
'''


#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

from PyQt4 import QtGui,QtCore


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(250, 200, 900, 600)
        self.setMinimumSize(900, 600)
        self.setMaximumSize(900, 600)

        self.setWindowTitle('Arabic-English Decoder-Encoder')
        self.initUI()
        self.button.clicked.connect(self.getE)
        self.button2.clicked.connect(self.getA)


    def getE(self):
        text2 =str(self.textedit2.toPlainText().toUtf8())
        text2 = unicode((text2).decode('utf-8'))
        self.decode(text2,0)    # 0 means Arabic to english


    def getA(self):
        text1 =str(self.textedit.toPlainText().toUtf8())
        self.decode(text1,1)    # 0 means Arabic to english


    def initUI(self):


        welcomeLabel =QtGui.QLabel("Arabic-English Encoder-Decoder")
        welcomeLabel.setMinimumSize(300,100)
        welcomeLabel.setStyleSheet("font-size:25px")


        hLbox=QtGui.QHBoxLayout()
        hLbox.addStretch()
        hLbox.addWidget(welcomeLabel)
        hLbox.addStretch()


        leftheader =QtGui.QLabel("Decoded Words")
        # leftheader.setMinimumSize(300,100)
        leftheader.setStyleSheet("font-size:20px")

        rightheader =QtGui.QLabel("Decoded Words")
        # rightheader.setMinimumSize(300,100)
        rightheader.setStyleSheet("font-size:20px")


        hHbox = QtGui.QHBoxLayout()
        hHbox.addStretch()
        hHbox.addWidget(leftheader)
        hHbox.addStretch()

        hHbox.addWidget(rightheader)
        hHbox.addStretch()


        self.button=  QtGui.QPushButton("Execute A")
        self.button.setMinimumSize(250,50)
        self.button.setStyleSheet("border-radius: 10px; border: 3px solid #BADA55; background: white;font-size:22px")

        self.button2=  QtGui.QPushButton("Execute E")
        self.button2.setMinimumSize(250,50)
        self.button2.setStyleSheet("border-radius: 10px; border: 3px solid #BADA55; background: white;font-size:22px")

        self.textedit= QtGui.QTextEdit()
        self.textedit.setMinimumSize(400,50)
        self.textedit2= QtGui.QTextEdit()
        self.textedit2.setMinimumSize(400,50)

        self.textedit2.setStyleSheet("border-radius: 10px; border: 3px solid #BADA55; background: white;font-size:22px")
        self.textedit.setStyleSheet("border-radius: 10px; border: 3px solid #BADA55; background: white; font-size:22px")

        self.HboxLine = QtGui.QHBoxLayout()
        self.HboxLine.addStretch()
        self.HboxLine.addWidget(self.textedit)
        self.HboxLine.addWidget(self.textedit2)
        self.HboxLine.addStretch()
        self.HboxLine.setContentsMargins(0,20,0,50)


        self.HboxButtons= QtGui.QHBoxLayout()
        self.HboxButtons.addStretch()
        self.HboxButtons.addWidget(self.button2)
        self.HboxButtons.addStretch()
        self.HboxButtons.addWidget(self.button)
        self.HboxButtons.addStretch()
        self.HboxButtons.setContentsMargins(0,10,0,50)


        self.Vbox = QtGui.QVBoxLayout()
        self.Vbox.addStretch()
        self.Vbox.addLayout(hLbox)
        # self.Vbox.addLayout(hHbox)
        self.Vbox.addLayout(self.HboxLine )
        self.Vbox.addLayout(self.HboxButtons)
        self.Vbox.addStretch()

        # self.show()

        self.setLayout(self.Vbox)



    def decode(self,text,x):

        #dict to hold all chars and thier opposites
        exampledict = {
        unicode(('ض').decode('utf-8')):'q',
        unicode(('ص').decode('utf-8')):'w',
        unicode(('ث').decode('utf-8')):'e',
        unicode(('ق').decode('utf-8')):'r',
        unicode(('ف').decode('utf-8')):'t',
        unicode(('غ').decode('utf-8')):'y',
        unicode(('ع').decode('utf-8')):'u',
        unicode(('ه').decode('utf-8')):'i',
        unicode(('خ').decode('utf-8')):'o',
        unicode(('ح').decode('utf-8')):'p',
        unicode(('ش').decode('utf-8')):'a',
        unicode(('س').decode('utf-8')):'s',
        unicode(('ي').decode('utf-8')):'d',
        unicode(('ب').decode('utf-8')):'f',
        unicode(('ل').decode('utf-8')):'g',
        unicode(('ا').decode('utf-8')):'h',
        unicode(('ت').decode('utf-8')):'j',
        unicode(('ن').decode('utf-8')):'k',
        unicode(('م').decode('utf-8')):'l',
        unicode(('ئ').decode('utf-8')):'z',
        unicode(('ء').decode('utf-8')):'x',
        unicode(('ؤ').decode('utf-8')):'c',
        unicode(('ر').decode('utf-8')):'v',
        unicode(('ﻻ').decode('utf-8')):'b',
        unicode(('ى').decode('utf-8')):'n',
        unicode(('ة').decode('utf-8')):'m',
        unicode(('و').decode('utf-8')):',',
        unicode(('ز').decode('utf-8')):'.',
        unicode((' ').decode('utf-8')):' ',
        unicode(('ط').decode('utf-8')):"'",
        unicode(('ك').decode('utf-8')):';',
        unicode(('ج').decode('utf-8')):'[',
        unicode(('ذ').decode('utf-8')):'~',
        unicode(('َ').decode('utf-8')):'Q',
        unicode(('ً').decode('utf-8')):'W',
        unicode(('ُ').decode('utf-8')):'E',
        unicode(('ٌ').decode('utf-8')):'R',
        unicode(('ﻹ').decode('utf-8')):'T',
        unicode(('إ').decode('utf-8')):'Y',
        unicode(('`').decode('utf-8')):'U',
        unicode(('÷').decode('utf-8')):'I',
        unicode(('×').decode('utf-8')):'O',
        unicode(('؛').decode('utf-8')):'P',
        unicode(('ِ').decode('utf-8')):'A',
        unicode(('ٍ').decode('utf-8')):'S',
        unicode((']').decode('utf-8')):'D',
        unicode(('[').decode('utf-8')):'F',
        unicode(('ﻷ').decode('utf-8')):'G',
        unicode(('أ').decode('utf-8')):'H',
        unicode(('ـ').decode('utf-8')):'J',
        unicode(('،').decode('utf-8')):'K',
        unicode(('/').decode('utf-8')):'L',
        unicode((':').decode('utf-8')):':',
        unicode(('"').decode('utf-8')):'"',
        unicode(('~').decode('utf-8')):'Z',
        unicode(('ْ').decode('utf-8')):'X',
        unicode(('{').decode('utf-8')):'C',
        unicode(('{').decode('utf-8')):'V',
        unicode(('ﻵ').decode('utf-8')):'B',
        unicode(('آ').decode('utf-8')):'N',
        unicode(("'").decode('utf-8')):'M',
        unicode((',').decode('utf-8')):'<',
        unicode(('.').decode('utf-8')):'>',
        unicode(('؟').decode('utf-8')):'?',
        unicode(('!').decode('utf-8')):'!',
        unicode(('@').decode('utf-8')):'@',
        unicode(('#').decode('utf-8')):'#',
        unicode(('$').decode('utf-8')):'$',
        unicode(('%').decode('utf-8')):'%',
        unicode(('^').decode('utf-8')):'^',
        unicode(('&').decode('utf-8')):'&',
        unicode(('*').decode('utf-8')):'*',
        unicode(('(').decode('utf-8')):'(',
        unicode((')').decode('utf-8')):')',
        unicode(('_').decode('utf-8')):'_',
        unicode(('+').decode('utf-8')):'+',
        unicode(('=').decode('utf-8')):'=',
        unicode(('-').decode('utf-8')):'-',
        unicode(('1').decode('utf-8')):'1',
        unicode(('2').decode('utf-8')):'2',
        unicode(('3').decode('utf-8')):'3',
        unicode(('4').decode('utf-8')):'4',
        unicode(('5').decode('utf-8')):'5',
        unicode(('6').decode('utf-8')):'6',
        unicode(('7').decode('utf-8')):'7',
        unicode(('8').decode('utf-8')):'8',
        unicode(('9').decode('utf-8')):'9',
        unicode(('0').decode('utf-8')):'0',
        unicode(('د').decode('utf-8')):']'}

        keys = exampledict.keys()
        values = exampledict.values()
        self.result =''
        if(x == 0):
            for let in text:
                for i in range(0,len(values)):
                    if(let == keys[i]):
                        self.result += values[i]
                        break

            self.textedit.setText(self.result)
        elif(x==1):

            for let in text:
                for i in range(0, len(values)):
                    if (let == values[i]):
                        self.result += keys[i]
                        break

            self.textedit2.setText(self.result)





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())