from nfc import reader
from i2c import lcddriver
from database import fetch_user
from led import led_functions

display = lcddriver.lcd()

while True:

    tag_id = reader.card_reader()
    fetch_data = fetch_user.fetch_balance(tag_id)
    user_status = fetch_data[0]

    if user_status:
        user_name = fetch_data[1][0]
        user_balance = fetch_data[1][1]
        led_functions.led_action('green', 3, 0.07)
        display.lcd_clear()
        display.lcd_display_string("User:"+user_name,1)
        display.lcd_display_string("Balance:" + str(user_balance),2)

    else:
        led_functions.led_action('red',3, 0.07)
        display.lcd_clear()
        display.lcd_display_string("User Not Found",1)
        display.lcd_display_string("****************", 2)







