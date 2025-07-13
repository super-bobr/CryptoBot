from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import config, crypto, users
from keyboards import main_menu

router = Router()

@router.message(F.text == "/start")
async def start_handler(msg: Message):
    await msg.answer("Привет! Выбери действие:", reply_markup=main_menu()) #часть отвечающая за подписки и рассылку

@router.callback_query(F.data.in_(["price", "subscribe", "unsubscribe"]))
async def menu_handler(query: CallbackQuery):
    action = query.data
    chat_id = query.message.chat.id

    if action == "price":
        texts = []
        for symbol in config.DEFAULT_CRYPTOS:
            try:
                price = crypto.get_price(symbol)
                texts.append(f"{symbol}: {price:.2f} USD")
            except:
                texts.append(f"{symbol}: ошибка!")
        await query.message.edit_text("💵\n" + "\n".join(texts), reply_markup=main_menu())

    elif action == "subscribe":
        users.subscribe(chat_id)
        await query.message.edit_text("✅ Подписан на рассылку", reply_markup=main_menu())

    elif action == "unsubscribe":
        users.unsubscribe(chat_id)
        await query.message.edit_text("❌ Отписан от рассылки", reply_markup=main_menu())

    await query.answer()
