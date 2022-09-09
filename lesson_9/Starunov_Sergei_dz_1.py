from time import sleep


class TrafficLight:
    __color = 'красный'

    def running(self):
        correct_job = (('красный', 7), ('желтый', 2), ('зеленый', 7))
        for color, delay in correct_job:
            reaction = {
                'красный': '(стой, не газуй)',
                'желтый': '(втыкай передачу)',
                'зеленый': f'(газ в палас, у тебя {delay} секунд)'
            }
            print(color, reaction[color], end=' ')
            for sec in range(delay, 0, -1):
                print(sec, end=' ')
                sleep(1)
            print()
        print('вы добрались до места')


if __name__ == '__main__':
    a = TrafficLight()
    a.running()
