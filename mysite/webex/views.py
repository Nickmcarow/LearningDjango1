from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):


    chr = """
<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
<h1 style="padding-left: 30px;">&nbsp;</h1>
<h1 style="padding-left: 30px;">&nbsp;</h1>
<h1 style="padding-left: 30px;"><span style="color: #333399; background-color: #ffffff;">Доброе утро, Андрюха&nbsp;<img src="https://image.flaticon.com/icons/svg/2307/2307690.svg" alt="" width="62" height="62" /></span></h1>
<h1 style="padding-left: 30px;"><span style="color: #333399;"><span style="font-size: 14px;">Сегодня мы должны сделать много разных дел:</span></span></h1>
<ol style="list-style: none; font-size: 14px; line-height: 32px; font-weight: bold;">
<li style="clear: both;"><img style="float: left;" src="https://upload-icon.s3.us-east-2.amazonaws.com/uploads/icons/png/12069381451556105347-512.png" alt="html cleaner" width="45" />&nbsp;Досмотреть Дудя&nbsp;</li>
<li style="clear: both;"><img style="float: left;" src="https://upload-icon.s3.us-east-2.amazonaws.com/uploads/icons/png/9237367661579060834-512.png" alt="Word to html" width="45" />&nbsp;Позавтракать</li>
<li style="clear: both;"><img style="float: left;" src="https://upload-icon.s3.us-east-2.amazonaws.com/uploads/icons/png/11589334141553681877-512.png" alt="replace text" width="45" />&nbsp;Погулять с френком</li>
<li style="clear: both;"><img style="float: left;" src="https://upload-icon.s3.us-east-2.amazonaws.com/uploads/icons/png/9878678521537856850-512.png" alt="gibberish" width="45" />&nbsp;Посмотреть Tableu и другие BI инструменты</li>
<li style="clear: both;"><img style="float: left;" src="https://upload-icon.s3.us-east-2.amazonaws.com/uploads/icons/png/18567034741542284594-512.png" alt="html table div" width="45" />&nbsp;Диванить</li>
</ol>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p>&nbsp;</p>
<p><strong>&nbsp;</strong></p>
    """


    return HttpResponse(chr)