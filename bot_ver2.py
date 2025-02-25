from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import talk_phb as tk
import gemini
from dotenv import load_dotenv
import os

load_dotenv()
# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TOKEN = os.getenv("TELEGRAM_TOKEN")

# TRIGGER_WORDS = {
#     "안녕" : "안녕하세요!🍕",
#     "정보" : "어떤 정보가 필요하세요?🧋",
#     "기분" : "그냥 그래요😑",
#     "다" : "🐈🐈🐈🐈‍⬛🐈‍⬛",
#     "!" : "🎉🎉🎉🎉🎉",
#     "ㅋㅋㅋ" : "ㅋㅋㅋ"
# }

async def start(update, context):
    await update.message.reply_text("안녕하세요!🧋🧋🧋")

async def send_photo(update, context):
    photo_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTAxMDJfMTYy%2FMDAxNzM1ODA4Nzc2NzE0.IyxMLY2no8Ox_8z_5h7faoECjAwi9kc3oJakKgBKnWkg.k_AmiBDklS-yzibSQ7VGjYS5-oBKime5i6mSTGWT5vsg.JPEG%2F%25B4%25D9%25BF%25EE%25B7%25CE%25B5%25E5%25C6%25C4%25C0%25CF%25A3%25DF20240919%25A3%25DF144903.jpg&type=sc960_832"
    await update.message.reply_photo(photo=photo_url,caption="이미지를 로딩했습니다‼️📩")

async def monitor_chat(update, context):
    user_text = update.message.text # 감지된 메세지들 (택배 알맹이라고 생각하면됨)
    chat_id = update.message.chat_id
    # 메세지가 온 채팅방 (택배주소지라고 생각하면됨) 이게 없으면 봇이 a채팅방에서 대답하고있을때(고정) b채팅방에서 질문해도 응답을 안 하는 경우가 발생할 수 있음

    if "딩딩" in user_text:
        res = gemini.aiai(user_text.replace("딩딩",""))
        await context.bot.send_message(chat_id=chat_id,text=res)
    elif "영화정보" in user_text: pass
        # await 영화정보크롤링()함수를 실행
    elif "사진 줘" in user_text:
        await send_photo(update,context)
    else:    
        for key, res in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await context.bot.send_message(chat_id=chat_id,text=res)
                break # 한개의 키워드에만 반응  
        
def main():
    app = Application.builder().token(TOKEN).build()

    # 명령어 핸들러 추가
    app.add_handler(CommandHandler("start",start))

    # 응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat)) # & ~fileters.COMMAND연산자 뒤에 오는 말은 뒤에꺼 처리하지말라는 뜻
    
    print("텔레그램 봇이 실행중입니다. 모니터링 중....")
    app.run_polling()

if __name__ == "__main__":
    main()