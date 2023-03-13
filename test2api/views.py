from django.conf import settings
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError,LineBotApiError
from linebot.models import MessageEvent,TextMessage,PostbackEvent

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
from module import func
from urllib.parse import parse_qsl

@csrf_exempt
def callback(request):
    if request.method =='POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        
        try:
            events = parser.parse(body,signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        
        for event in events:
            if isinstance(event,MessageEvent):
                if isinstance(event.message, TextMessage):

                    strText = event.message.text
                    if strText == '@賣場介紹':
                        func.sendButton(event)
                    elif strText == '@賣場介紹 ♡':
                        func.sendYM(event)
                    elif strText == '@最新優惠':
                        func.sendVideo(event)
                    elif strText == '@熱門商品':
                        func.sendImgCarousel(event)
                    elif strText == '@穿搭指南':
                        func.sendImgmap(event)
                    elif strText == '@常見QA':
                        func.SendQuickreply(event)
                    elif strText == '@退換貨或須知':
                        func.sendYM1(event)
                    elif strText == '@如何下訂單':
                        func.sendYM2(event)
                    elif strText == '@何時出貨':
                        func.sendYM3(event)
                    elif strText == '@重要須知':
                        func.sendYM4(event)
                    elif strText == '@量身推薦':
                        func.sendConfirm(event)
                        
                    elif strText == '@高挑女孩':
                        func.sendYes(event)
                        
                    elif strText == '@小隻女孩':
                        func.sendNo(event)

                        
            if isinstance(event, PostbackEvent):
               backdata = dict(parse_qsl(event.postback.data))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()      