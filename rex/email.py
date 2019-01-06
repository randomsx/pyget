import re

def is_valid_email(addr):
    email = re.compile(r'[\w+\.\w]+@[\w+\.\w]+')
    if email.match(addr):
        return True
    else:
        return False


if __name__ == '__main__':
    # 测试:
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
    assert not is_valid_email('bob#example.com')
    assert not is_valid_email('mr-bob@example.com')
    print('ok')