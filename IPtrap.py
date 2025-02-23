from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# 添加 ProxyFix 中间件来处理反向代理头
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
def hello_world():
    # 获取访问者的真实 IP 地址
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    
    # 打印访问者的 IP 地址
    print(f"Visitor IP: {user_ip}")
    
    # 将 IP 地址记录到文件中
    with open("ip_logs.txt", "a") as file:
        file.write(f"IP: {user_ip}\n")
    
    return f"Hello, World! Your IP address is {user_ip}"

if __name__ == '__main__':
    # 启动Flask应用并绑定到0.0.0.0，这样其他设备也能访问
    app.run(debug=True, host='0.0.0.0', port=5000)
