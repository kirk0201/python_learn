# 외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

# print(test_dict)
# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))
