import socket

class Servidor():
    """
    Classe Servidor - Calculadora Remota - API Socket
    """
    def __init__(self, host, port):
        """
        Construtor da Classe Servidor
        """
        self._host = host
        self._port = port
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    def start(self):
        """"
        Inicia a execução do serviço
        """
        endpoint = (self._host,self._port)
        try:
            self._tcp.bind(endpoint)
            self._tcp.listen(1)
            print("Servidor foi iniciado em ", self._host, ":", self._port)
            while True:
                con, client = self._tcp.accept()
                self._service(con, client) 
        except Exception as e:
            print("Erro ao inicalizar o servidor", e.args)

    def _service(self, con, client):
        """
        Método que implementa o serviço de calculadora remota
        :param con: objeto socket usado para enviar e receber os dados
        :param client: é o endereço e porta do cliente
        """
        print("Atendendo o cliente ", client)
        operadores = ['+','-','*','/']
        while True:
            try:
                msg = con.recv(1024)
                msg_s = str(msg.decode('ascii')) #op1opop2 - 15+10 
                for x in operadores:
                    if msg_s.find(x) > 0:
                        op = x
                        msg_s = msg_s.split(op) #['15','10']
                        break
                if op == '+':
                    resp = float(msg_s[0]) + float(msg_s[1])
                elif op == '-':
                    resp = float(msg_s[0]) - float(msg_s[1])
                elif op == '*':
                    resp = float(msg_s[0]) * float(msg_s[1])
                elif op == '/':
                    resp = float(msg_s[0]) / float(msg_s[1])
                else:
                    resp = "Operação Inválida"
            
                con.send(bytes(str(resp),'ascii'))
                print(client, "-> requisição atendida")

            except OSError as e:
                print("Erro na conexão ", client, ": ", e.args)
                return 
            except Exception as e:
                print("Erro nos dados recebidos pelo Cliente ", client, ": ", e.args)
                con.send(bytes("Erro", 'ascii'))


