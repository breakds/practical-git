def RunMyLedger():
    balance = 0.0

    # 2018-01-01, Red Packet from Tony
    balance += 3.0

    # 2018-01-04, Red Packet to Miao
    balance -= 50.0

    print("My total balance: {}".format(balance))

if __name__ == "__main__":
    RunMyLedger()
