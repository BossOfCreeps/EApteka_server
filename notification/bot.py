# http://t.me/invalid_syntax_eapteka_Bot
import telegram

telegram_bot = telegram.Bot("1813927589:AAGFJAN96LQXE4n190Akzn4V9SJ9azYwsdw")


def tg_send(user, text):
    if user.telegram_id:
        telegram_bot.send_message(user.telegram_id, text, parse_mode="markdown")


def tg_storage_rules(user, order):
    if user.telegram_id:
        text = "Здравствуйте. Вы только что купили товары в ЕАптеке. Мы бы хотели рассказать вам о правилах их " \
               "хранения, чтобы они не испортились и не навредили вашему здоровью.\n\n"
        for order_product in order.order_products.all():
            text += f"*{order_product.product.base}*: \n{order_product.product.base.storage}\n\n"

        tg_send(user, text)


def tg_notification(user, product):
    if user.telegram_id:
        text = f"Здравствуйте. Напоминаем принять вам *{product.product}* \n" \
               f"Способ: {product.set.reception_method.name.lower()}, " \
               f"{product.set.get_reception_time_display().lower()}"
        tg_send(user, text)
