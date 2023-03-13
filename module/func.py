from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,AudioSendMessage,VideoSendMessage,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,PostbackTemplateAction,ConfirmTemplate,CarouselTemplate,CarouselColumn,ImageCarouselTemplate,ImageCarouselColumn
from linebot.models import ImagemapSendMessage, BaseSize, MessageImagemapAction, ImagemapArea, URIImagemapAction

from linebot.models import TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN) 

def sendButton(event):
    try:
        message = TemplateSendMessage(
            alt_text='賣場介紹',
            template=ButtonsTemplate(
                thumbnail_image_url='https://imgur.com/thmnrNy.png',
                title='YMTODAY賣場介紹 & 快速通道 ',
                text='請選擇:',
                actions=[
                    MessageTemplateAction(
                        label='賣場介紹 ♡',
                        text='@賣場介紹 ♡'
                    ),
                    URITemplateAction(
                        label='IG網址',
                        uri='https://www.instagram.com/ymtoday/?hl=zh-tw'
                    ),
                    URITemplateAction(
                        label='蝦皮網址',
                        uri='https://shopee.tw/ymtoday?v=70f&smtt=0.0.4'
                    ),    
                 ]
            )
        )   
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
        
def sendYM(event):
    try:
        message = TextSendMessage(
            text = '歡迎來到YMTODAY，\n有喜歡的東西請盡情選購(如IG有喜歡的商品可以小盒子唷)，\n如有任何問題可以私訊蝦皮聊聊或IG小盒子唷 ♡ \n再次謝謝您喜歡我們 ♡'   
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendYM1(event):
    try:
        message = TextSendMessage(
            text = '換貨須知 \n ▴更換尺寸/商品服務為避免濫用，買方寄件及原訂單的運費不予以退費，此規範售前皆附註告知。\n 此為本店提供的額外售後服務，更換後再寄回運費由我方吸收。（無提供超商代碼退貨及換貨，勿再次詢問）\n退貨須知\n▴若為退貨相關 務必於七日內聯絡Line@客服(以上規範皆適用)\n▴超過鑑賞期後告知，等同放棄退換貨服務，一律不接受任何理由申請退換貨。\n(寄回郵資需自行負擔） '   
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendYM2(event):
    try:
        message = TextSendMessage(
            text = 'Ｑ請問要如何訂購？\n若您不會使用購物網站或者不知如何下訂，歡迎私訊IG小盒子任一帳號專員下單\n( IG:主帳ymtoday)'   
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
def sendYM3(event):
    try:
        message = TextSendMessage(
            text = '商品若是現貨則會於48小時內完成出貨，如為預購則須等待7~14個工作天(故不收集單唷)，還請仙女們耐心等待，造成不便請見諒感謝您的配合 ♡'   
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
def sendYM4(event):
    try:
        message = TextSendMessage(
            text = '1.若收到商品為下水、香味過重(認定為穿出遊過)、商品吊牌拆除等相關商品不完整，將不予退貨。\n2.換貨需酌收寄回運費，請務必尊重買賣交易規則感謝您的配合與愛護支持。\n3.注意！！同一張訂單只限一次退貨或是換貨。\n4.不受理二次退換請注意如附胸墊背心/小可愛屬個人貼身衣物，基於衛生考量不適用退換貨政策，售出恕不退換。'   
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
        
def sendVideo(event): #傳送影片
    try:
        message = TextSendMessage(
            text = '最新優惠折扣碼( YMTOBOT01 ):\n https://shopee.tw/ymtoday?v=70f&smtt=0.0.4',
        )     
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
        
                 
def sendImgCarousel(event):
    try:
        message = TemplateSendMessage(
            alt_text='熱門商品',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://imgur.com/HtFfyDM.jpg',
                        action=MessageTemplateAction(
                            label='刺繡簡約文字T恤',
                            text=' 簡約T搭配基本牛仔長短褲、或像闆娘一樣搭配燈芯絨褲，況造出休閒的簡約感 \n https://shopee.tw/product/116960037/2047275880?smtt=0.0.9'
                        )
                    ),
                    ImageCarouselColumn(   
                        image_url='https://imgur.com/PnrUX1b.jpg',
                        action=MessageTemplateAction(
                            label='搞怪動物短袖T',
                            text='搭配牛仔裙加上牛皮感的手表與小白鞋可以創造出清新的感覺 \n  https://shopee.tw/product/116960037/2053446293?smtt=0.0.9'
                        )   
                    ),
                    ImageCarouselColumn(
                        image_url='https://imgur.com/UOUYfKy.jpg',
                        action=MessageTemplateAction(
                            label='不規則雙鈕扣牛仔短褲',
                            text='不規則牛仔褲搭配露肚小背心，雖然是牛仔短褲卻有不一樣的剪裁形狀，簡單中卻有小驚喜\n  https://shopee.tw/product/116960037/2222279313?smtt=0.0.9'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
                        
                        
def SendQuickreply(event):
    try:
        message = TextSendMessage(
            text = '請選擇一個常見QA ♡',  
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="退換貨須知",text="@退換貨或須知")
                     ),
                    QuickReplyButton(
                        action=MessageAction(label="如何下訂單",text="@如何下訂單")
                     ),
                    QuickReplyButton(
                        action=MessageAction(label="何時出貨",text="@何時出貨")
                     ),
                    QuickReplyButton(
                        action=MessageAction(label="重要須知",text="@重要須知")
                     ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))                   

def sendConfirm(event):
    try:
        message = TemplateSendMessage(
            alt_text='量身推薦',
            template=ConfirmTemplate(
                text='請問您的身高高於165公分嗎?',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='@高挑女孩'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@小隻女孩'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
def sendYes(event):
    try:
        message = TextSendMessage(
            text=' 高挑女孩也適合的OVERSIZE長版上衣(料質非常舒服唷~)\n https://www.instagram.com/p/BwM7A57lpQS/?igshid=8mr6oqg5m46v',        
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
def sendNo(event):
    try:
        message = TextSendMessage(
            text='小隻女孩最適合的顯腿長的不規則高腰短褲 \n ttps://www.instagram.com/p/Bymdt8WHKkn/?igshid=1hz73bv2a5bh7 ',        
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
        
        
def sendImgmap(event): #圖片地圖
    try:
        image_url = ' https://imgur.com/7C9BQPX.jpg ' #圖片位址
        imgwidth = 1040 #原始圖片寬度一定要1040
        imgheight = 400
        message = ImagemapSendMessage(
            base_url = image_url,
            alt_text = "圖片地圖範例",
            base_size = BaseSize(height = imgheight, width = imgwidth),
            actions = [
                MessageImagemapAction( #顯示文字訊息
                    text = '單品上裝 \n https://shopee.tw/product/116960037/2053446293?v=559&smtt=0.0.4',
                    area = ImagemapArea( #設定圖片範圍:左方1/4區域
                        x = 0,
                        y = 0,
                        width = imgwidth*0.33,
                        height = imgheight
                    )
                ),
                MessageImagemapAction( #顯示文字訊息
                    text = '單品下裝 \n https://shopee.tw/product/116960037/2222279313?v=b27&smtt=0.0.4',
                    area = ImagemapArea(
                        x = imgwidth*0.33,
                        y = 0,
                        width = imgwidth*0.33,
                        height = imgheight
                    )
                ),
                MessageImagemapAction( #顯示文字訊息
                    text = '下裝包包 \n https://shopee.tw/product/116960037/1985792506?v=c34&smtt=0.0.4',
                    area = ImagemapArea( #設定圖片範圍:左方1/4區域
                        x = imgwidth*0.66,
                        y = 0,
                        width = imgwidth*0.33,
                        height = imgheight
                    )
                ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))