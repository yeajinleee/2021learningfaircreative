#변수 선언
hello = "어서오세요. 00분식집입니다.\n"
menu = '*메뉴판* \n1.일반김밥:2000원 \n2.참치김밥:3000원 \n3.치즈김밥: 3100원\n4.돈까스김밥: 3500원'
what = '주문하실 메뉴를 숫자로 입력해주세요 :'
more = '\n 계속해서 주문하시려면 1번 \n 결제하시려면 2번을 눌러주세요 :'
totalMoney = '총 금액은 '

name = ['일반김밥', '참치김밥', '치즈김밥', '돈까스김밥']
price = [2000, 3000, 3100, 3500]

order = [] #주문서
cash = [10000] #나의현금
total = 0 #총 가격
change = 0 #거스름돈


print(hello)
while True:
    print(menu) #메뉴출력
    choice = int(input(what))
    ##일반김밥 
    if choice == 1:
        order. append('일반김밥')  #append함수:리스트 제일 뒤에 항목 추가
        total += price[0]   #price[0]=2000(원)
        while True:
            #변수의 재사용(choice)
            choice = int(input(more)) #int: 사용자로부터 입력받은 값 정수로 변환
            if choice == 1:
                choice = int(input(what))#주문할 메뉴 숫자로 입력받기
                #일반김밥
                if choice == 1:
                    order.append('일반김밥')
                    total += price[0]# => total=total + price[0]
                    continue
                #참치김밥
                elif choice == 2:
                    order.append('참치김밥')
                    total += price[1] #price[1]=3000(원)
                    continue
                #치즈김밥
                elif choice == 3:
                    order.append('치즈김밥')
                    total += price[2] #price[2]=3100(원)
                    continue
                #돈까스김밥
                else :
                    order.append('돈까스김밥')
                    total += price[3] #price[3]=3500(원)
                    continue
               
            #주문을 더 안할 경우 계산하는 곳으로
            else:
                break
            
    ##참치김밥
    elif choice == 2:
        order.append('참치김밥')
        total += price[1]
        while True:
            #변수의 재사용(choice)
            choice = int(input(more))
            if choice == 1:
                choice = int(input(what))
                #일반김밥
                if choice == 1:
                    order.append('일반김밥')
                    total += price[0]
                    continue
                #참치김밥
                elif choice == 2:
                    order.append('참치김밥')
                    total += price[1]
                    continue
                #치즈김밥
                elif choice == 3:
                    order.append('치즈김밥')
                    total += price[2]
                    continue
                #돈까스김밥
                else :
                    order.append('돈까스김밥')
                    total += price[3]
                    continue
              
        
            #주문을 더 안할 경우 계산하는 곳으로
            else:
                break

    ##치즈김밥
    elif choice == 3:
        order.append('치즈김밥')
        total += price[2]
        while True:
            #변수의 재사용(choice)
            choice = int(input(more))
            if choice == 1:
                choice = int(input(what))
                #일반김밥
                if choice == 1:
                    order.append('일반김밥')
                    total += price[0]
                    continue
                #참치김밥
                elif choice == 2:
                    order.append('참치김밥')
                    total += price[1]
                    continue
                #치즈김밥
                elif choice == 3:
                    order.append('치즈김밥')
                    total += price[2]
                    continue
                #돈까스김밥
                else :
                    order.append('돈까스김밥')
                    total += price[3]
                    continue
               
            #주문을 더 안할 경우 계산하는 곳으로
            else:
                break
    ##돈까스김밥
    elif choice == 4:
        order.append('돈까스김밥')
        total += price[3]
        while True:
            #변수의 재사용(choice)
            choice = int(input(more))
            if choice == 1:
                choice = int(input(what))
                #일반김밥
                if choice == 1:
                    order.append('일반김밥')
                    total += price[0]
                    continue
                #참치김밥
                elif choice == 2:
                    order.append('참치김밥')
                    total += price[1]
                    continue
                #치즈김밥
                elif choice == 3:
                    order.append('치즈김밥')
                    total += price[2]
                    continue
                #돈까스김밥
                else: 
                    order.append('돈까스김밥')
                    total += price[3]
                    continue
              
            #주문을 더 안할 경우 계산하는 곳으로
            else:
                break
            

 # break후 계산하기

    print('\n' + totalMoney + str(total) + '원 입니다.') #\n: 줄바꿈, str:문자열로 변환
    change = cash[0] - total #거스름돈= 10000원에서 주문금액 뺀 값
    if change < 0:
        print("금액이부족합니다.\n주문이 취소되었습니다..")
        total = 0
        order = []
        continue #break가 아닌 continue를 사용해서 처음 화면 (메뉴판)으로 돌아가기
    else:
        print("주문 내역은", end = " ")
        print(order)
        print('10000원을 받았습니다. 거스름돈은 ' + str(change) + '원 입니다.')
        break
