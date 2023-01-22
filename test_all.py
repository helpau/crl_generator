from main import gen_crl
import hashlib

def test_1_cert():
    res_lst=gen_crl(n=1,start_id=1,exp="250120103948Z",rev="250120103949Z")
    sha256_result=hashlib.sha256(str(res_lst).encode()).hexdigest()
    assert sha256_result=="a948d9b565b48b0b86196b9859a4b1925473763d4b34d1e43228beeb6ed4d70a"

def test_10_certs():
    res_lst=gen_crl(n=10,start_id=1,exp="250120103948Z",rev="250120103949Z")
    sha256_result=hashlib.sha256(str(res_lst).encode()).hexdigest()
    assert sha256_result=="d2189a6236b3f1d17ec10d1260278e117f71bf9a51fe3f0a3c51b4a3cb1bd48a"
