from gpiozero import PWMLED
from signal import pause

# 핀 번호 설정
LED_PIN = 17

# PWMLED 객체 생성
led = PWMLED(LED_PIN)

# LED를 pulse 모드로 동작
led.pulse()

# 프로그램이 종료되지 않도록 대기
pause()
