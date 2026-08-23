import socket


def MakeParam(P):
    PStr = ""
    if (isinstance(P, list)):
        oTable = list(P)
        NoOfRows = len(oTable)
        NoOfCols = len(oTable[0])
        RowsJoined = [""] * (NoOfRows+1)
        RowsJoined[0] = "||" + "$list$"
        for i in range(NoOfRows):
            ColsJoined = [""] * (NoOfCols + 0 )
            for j in range(NoOfCols):
                if (isinstance(oTable[i][j], bool)):
                    ColsJoined[j] = "$bool$" + str(oTable[i][j])
                elif (isinstance(oTable[i][j], float) or isinstance(oTable[i][j], int)):
                    ColsJoined[j] = "$float$" + str(oTable[i][j])
                else:
                    ColsJoined[j] = str(oTable[i][j])
            RowsJoined[i + 1] = "§_§".join(ColsJoined);
        PStr = "§__§".join(RowsJoined);


    elif (isinstance(P, str)):
        PStr = "||" + "$string$" + str(P);
    elif (isinstance(P, float) or isinstance(P, int)):
        PStr = "||" + "$float$" + str(P);
    elif (isinstance(P, bool)):
        PStr = "||" + "$bool$" + str(P);
    return PStr


##def GetTypedData(Param):
##    ResultFinal = None
##    if Param.startswith("$float$"):
##        ResultFinal = float(Param[7:])
##    elif Param.startswith("$string$"):
##        ResultFinal = str(Param[8:])
##    elif Param.startswith("$list$"):
##        ResultFinal = String2List(Param)
##    elif Param.startswith("$bool$"):
##        if Param == "$bool$True": ResultFinal = True
##        else: ResultFinal = False
##    return ResultFinal;



def String2List(instr):
    globallist = []
    t = instr.split("§__§")
    #print(t)
    for i in range(1, len(t)):
        #print( "\n", t[i])
        ts = t[i].split("§_§")
        #print(ts)
        for j in range(len(ts)):
            #print(ts[j])
            if ts[j].startswith("$float$"):
                ts[j] = float(ts[j][7:])
            elif ts[j].startswith("$datetime$"):
                ts[j] = float(ts[j][10:])
            elif ts[j].startswith("$bool$"):
                if ts[j] == "$bool$True": ts[j] = True
                else: ts[j] = False
            #print(ts[j], type(ts[j]))
        #print(ts)
        globallist.append(ts)
    return globallist






def client_program(SnippetToSend):
    host = socket.gethostname()
    port = 11958  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    client_socket.send(SnippetToSend.encode())  # send message
    DataReceived = client_socket.recv(1024).decode()  # receive response
    client_socket.close()  # close the connection
    return DataReceived


def DemoClient():
    #SnippetToSend = 'result = mpm.cos(25 + 4)'

    P1 = [["A","B","C"], [True,False,True], [811,8812,9913]]
    SnippetToSend = "result = P1" + MakeParam(P1)

    DataReceived = client_program(SnippetToSend)
    print('Received from server: ' + DataReceived)

    Result = String2List(DataReceived)
    print('Result: ', Result)



def DemoMakeParam():
    P1 = "MyDataString"
    P1 = 45E23
    P1 = True
    P1 = [["A","B","C"], [True,False,True], [811,8812,9913]]
    PStr = MakeParam(P1)
    print(PStr)


try:
    if __name__ == '__main__':
        DemoClient()
        #DemoMakeParam()


except Exception:
    import traceback
    print(traceback.format_exc())

