from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
# import talk_phb as tk
import gemini
from dotenv import load_dotenv
import os
import random
import wish
import randomwish

load_dotenv()
# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TOKEN = os.getenv("TELEGRAM_TOKEN")

# TRIGGER_WORDS = {
#     "정보" : "어떤 정보가 필요하세요?🧋",
# }

async def start(update, context):
    await update.message.reply_text("안녕하세요!🧋🧋🧋")
            
    

async def monitor_chat(update, context):
    user_text = update.message.text # 감지된 메세지들 (택배 알맹이라고 생각하면됨)
    chat_id = update.message.chat_id
    # 메세지가 온 채팅방 (택배주소지라고 생각하면됨) 이게 없으면 봇이 a채팅방에서 대답하고있을때(고정) b채팅방에서 질문해도 응답을 안 하는 경우가 발생할 수 있음

    if "딩딩" in user_text or "딩딩이" in user_text or "딩딩아" in user_text:
        res = gemini.aiai(user_text.replace("딩딩","").replace("딩딩이","").replace("딩딩아",""))
        await context.bot.send_message(chat_id=chat_id,text=res)
    # elif "영화정보" in user_text: pass
    #     # await 영화정보크롤링()함수를 실행
    elif "ㄹㅋㅅㅈ" in user_text:
        await wish.send_riku(update,context)
    elif "ㅅㅇㅅㅈ" in user_text:
        await wish.send_sion(update,context)
    elif "ㅇㅇㅅㅅㅈ" in user_text:
        await wish.send_yushi(update,context)
    elif "ㅅㅋㅇㅅㅈ" in user_text:
        await wish.send_sakuya(update,context)
    elif "ㄹㅅㅈ" in user_text:
        await wish.send_ryo(update,context)
    elif "ㄷㅇㅅㅈ" in user_text:
        await wish.send_jaehee(update,context)
    elif "ㅇㅅㅅㅈ" in user_text:
        await randomwish.send_wish(update,context) 
    # else:    
    #     for key, res in tk.TRIGGER_WORDS.items():
    #         if key in user_text:
    #             await context.bot.send_message(chat_id=chat_id,text=res)
    #             break # 한개의 키워드에만 반응  
        
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