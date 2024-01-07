import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic


form_class = uic.loadUiType("C:\\Users\\user\\Desktop\\Delivery pr\\project_ui.ui")[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #계산하기 버튼 클릭시 이벤트
        self.pushButton.clicked.connect(self.buttonClicked)
               
    def textCheck(self,input):
        #입력칸에 숫자가 입력되었는지 확인
        text = input.text()
        if text.isdigit():
            return True
        else:
            return False
    
    def comboboxCheck(self,input):
        #쿠팡,요기요 수수료유형이 제대로 선택되었는지 확인
        text = input.currentText()
        if text=="  선택" or text=="     선택":
            return False
        else:
            return True

    def buttonClicked(self):
        if self.textCheck(self.materialCost)==False:
            QMessageBox.about(self, '오류', '재료비를 다시 입력해주세요.')
        elif self.textCheck(self.tax)==False:
            QMessageBox.about(self, '오류', '세금을 다시 입력해주세요.')
        elif self.textCheck(self.deliveryCost)==False:
            QMessageBox.about(self, '오류', '배달료 총액을 다시 입력해주세요.')
        elif self.textCheck(self.rent)==False:
            QMessageBox.about(self, '오류', '임대료를 다시 입력해주세요.')
        elif self.textCheck(self.utilityCost)==False:
            QMessageBox.about(self, '오류', '수도,가스,전기요금을 다시 입력해주세요.')
        elif self.textCheck(self.laborCost)==False:
            QMessageBox.about(self, '오류', '인건비를 다시 입력해주세요.')    
        elif self.textCheck(self.ultracallFlag)==False:
            QMessageBox.about(self, '오류', '배민울트라콜 깃발 개수를 다시 입력해주세요.')    
        elif self.textCheck(self.supplies)==False:
            QMessageBox.about(self, '오류', '소모품비용을 다시 입력해주세요.')   
        elif self.textCheck(self.etc)==False:
            QMessageBox.about(self, '오류', '기타비용을 다시 입력해주세요.')    
        elif self.textCheck(self.ultracallRevenue)==False:
            QMessageBox.about(self, '오류', '매출(배민 울트라콜)을 다시 입력해주세요.')
        elif self.textCheck(self.baemin1Revenue)==False:
            QMessageBox.about(self, '오류', '매출(배민1)을 다시 입력해주세요.')
        elif self.textCheck(self.coupangRevenue)==False:
            QMessageBox.about(self, '오류', '매출(쿠팡이츠)를 다시 입력해주세요.')        
        elif self.textCheck(self.yogiyoRevenue)==False:
            QMessageBox.about(self, '오류', '매출(요기요)을 다시 입력해주세요.')
        elif self.textCheck(self.ultracallOrder)==False:
            QMessageBox.about(self, '오류', '주문수(배민 울트라콜)를 다시 입력해주세요.')
        elif self.textCheck(self.baemin1Order)==False:
            QMessageBox.about(self, '오류', '주문수(배민1)를 다시 입력해주세요.')
        elif self.textCheck(self.coupangOrder)==False:
            QMessageBox.about(self, '오류', '주문수(쿠팡이츠)를 다시 입력해주세요.')
        elif self.textCheck(self.yogiyoOrder)==False:
            QMessageBox.about(self, '오류', '주문수(요기요)를 다시 입력해주세요.')
        elif self.comboboxCheck(self.coupangType)==False:
            QMessageBox.about(self, '오류', '쿠팡 수수료유형을 선택해주세요')
        elif self.comboboxCheck(self.yogiyoType)==False:
            QMessageBox.about(self, '오류', '요기요 중개수수료를 선택해주세요')
        else:
            #총 주문수
            self.orderSum = int(self.ultracallOrder.text()) + int(self.baemin1Order.text()) + int(self.coupangOrder.text()) + int(self.yogiyoOrder.text())
            
            #나머지 비용 총합
            self.otherCost = int(self.rent.text()) + int(self.utilityCost.text()) + int(self.laborCost.text()) + int(self.supplies.text()) + int(self.etc.text())
            
            #건당 평균 기타비용
            self.costPerCase = (self.otherCost) / (self.orderSum)
            
            #배민울트라콜,요기요 건당 평균배달료
            try:
                self.deliveryPerCase = int(self.deliveryCost.text()) / ( int(self.ultracallOrder.text()) + int(self.yogiyoOrder.text()) )
            except:
                self.deliveryPerCase = 0

            #플랫폼별 객단가
            try:
                self.ultracallAverage = int(self.ultracallRevenue.text()) / int(self.ultracallOrder.text())
            except:
                self.ultracallAverage = 0
            
            try:
                self.baemin1Average = int(self.baemin1Revenue.text()) / int(self.baemin1Order.text())
            except:
                self.baemin1Average = 0
            
            try:
                self.coupangAverage = int(self.coupangRevenue.text()) / int(self.coupangOrder.text())
            except:
                self.coupangA = 0
            
            try:
                self.yogiyoAverage = int(self.yogiyoRevenue.text()) / int(self.yogiyoOrder.text())
            except:
                self.yogiyoAverage = 0
            
            #플랫폼별 건당 순수익
            try:
                self.ultracallProfit = self.ultracallAverage * (1 - int(self.materialCost.text())/100 - int(self.tax.text())/100 ) - ( int(self.ultracallFlag.text()) * 88000 / int(self.ultracallOrder.text()) ) \
                - self.deliveryPerCase - self.costPerCase
            except:
                self.ultracallProfit = 0
            self.baemin1Profit = self.baemin1Average * (1 - int(self.materialCost.text())/100 - int(self.tax.text())/100 - 0.068) - self.costPerCase - 3000
            self.coupangProfitA = self.coupangAverage * (1 - int(self.materialCost.text())/100 - int(self.tax.text())/100 - 0.098) - self.costPerCase - 5400
            self.coupangProfitB = self.coupangAverage * (1 - int(self.materialCost.text())/100 - int(self.tax.text())/100 - 0.075) - self.costPerCase - 6000
            self.yogiyoProfit = self.yogiyoAverage * (1 - int(self.materialCost.text())/100 - int(self.tax.text())/100 - 0.125) - self.costPerCase - self.deliveryPerCase
            self.yogiyoProfitFranchise = self.yogiyoAverage * (1 - int(self.materialCost.text())/100 - int(self.tax.text())/100 - 0.08) - self.costPerCase - self.deliveryPerCase

            #플랫폼별 건당 순수익률                                     
            try:
                self.ultracall = round( self.ultracallProfit / self.ultracallAverage * 100, 2 )
                self.ultracall = str(self.ultracall) + ' %'
            except:
                self.ultracall = '매출이 없습니다.'

            try:
                self.baemin1 = round( self.baemin1Profit / self.baemin1Average * 100, 2 )
                self.baemin1 = str(self.baemin1) + ' %'
            except:
                self.baemin1 = '매출이 없습니다.'

            try:
                self.coupangA = round( self.coupangProfitA / self.coupangAverage * 100, 2 )
                self.coupangA = str(self.coupangA) + ' %'
            except:
                self.coupangA = '매출이 없습니다.'
            
            try:
                self.coupangB = round( self.coupangProfitB / self.coupangAverage * 100, 2 )
                self.coupangB = str(self.coupangB) + ' %'
            except:
                self.coupangB = '매출이 없습니다.'

            try:
                self.yogiyo = round( self.yogiyoProfit / self.yogiyoAverage * 100, 2 )
                self.yogiyo = str(self.yogiyo) + ' %'
            except:
                self.yogiyo = '매출이 없습니다.'

            try:
                self.yogiyoFranchise = round( self.yogiyoProfitFranchise / self.yogiyoAverage * 100, 2 )
            except:
                self.yogiyoFranchise = '매출이 없습니다.'

            if self.coupangType.currentText() == '    A':
                if self.yogiyoType.currentText() == '     개인':
                    self.ultracallResult.setText(self.ultracall)
                    self.baemin1Result.setText(self.baemin1)
                    self.coupangResult.setText(self.coupangA)
                    self.yogiyoResult.setText(self.yogiyo)
                else:
                    self.ultracallResult.setText(self.ultracall)
                    self.baemin1Result.setText(self.baemin1)
                    self.coupangResult.setText(self.coupangA)
                    self.yogiyoResult.setText(self.yogiyoFranchise)
            else:
                if self.yogiyoType.currentText() == '     개인':
                    self.ultracallResult.setText(self.ultracall)
                    self.baemin1Result.setText(self.baemin1)
                    self.coupangResult.setText(self.coupangB)
                    self.yogiyoResult.setText(self.yogiyo)
                else:
                    self.ultracallResult.setText(self.ultracall)
                    self.baemin1Result.setText(self.baemin1)
                    self.coupangResult.setText(self.coupangB)
                    self.yogiyoResult.setText(self.yogiyoFranchise)


app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
