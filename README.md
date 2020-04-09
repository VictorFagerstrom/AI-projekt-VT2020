# AI-projekt-VT2020
Repository för AI-projektet vi har jobbat med under vårterminen.

## Vad har jag gjort?

Jag har gjort en Reddit-bot som tar posts från subredditen r/Stories och genom en AI skapar nya posts som aldrig har funnits. Den ska även ladda upp de nya posterna på en ny subreddit. 

## Hur har jag gjort?

webscrape.py

Det första steget är att hämta data som AIn kan arbeta med. Som sagt tar den datan från subredditen r/Stories. För att hämta datan från reddit använder jag ett bibliotek till python som heter Praw. För att kunna använda Praw måste du installera det tillhörande biblioteket.
Det jag gör sedan är att med hjälp av Praw hämta data från reddit som jag sedan lägger i en ny textfil. Jag tar de 1000 högst rankade posterna på subredditen. När jag lägger över datan i den nya filen separerar jag även de enskilda posterna för att det ska bli enkare för AIn att skapa en bra post.
Koden för detta ligger i filen webscrape.py. För att kunna köra den filen behöver du också ladda ned json.

lol.py

Det här är huvudfilen där AIn körs. Men innan man kan köra den var jga tvungen att träna en AI. Det gjorde jag i den google colab-sidan som jag länkar här: 

https://colab.research.google.com/drive/1Eoyl3dkj_csNsy7-KcMIE0rvewf2ZWHm#scrollTo=VHdTL8NDbAh3.

För att kunna köra filen där du skapar texter behöver du importera följande bibliotek:

import gpt_2_simple as gpt2

import time

import random

import tarfile

import requests

import os

from datetime import datetime, timedelta

import praw

Det som händer i koden sen är att vi hämtar en .tar-fil från våran google drive som vi har länkat till colaben. Den innehåller checkpointen som skapades när AIn tränades. Sedan extractar vi den så att vi kan använda den. Nu har vi kommit till det att vi ska skapa en ny post. 
AIn kommer att skapa många posts men vi lägger alla i en array och väljer att använda den första posten. Sedan vill vi posta den nyskrivna posten och för det använder vi återigen Praw. Både skapa posten och uploada den har vi i en while-loop så vi kan lägga upp koden på heroku så att den kan göra detta om och omo igen.
Till sist säger vi att koden ska "sova" i ett visst tidsintervall så att vi inte skickar för många posts till reddit.

## Problem jag har haft

Som alltid med programmeringsprojekt stötte jag även med detta på småproblem som relativt snabbt gick att lösa. Det var allt ifrån att lära sig hur Praw fungerade till hur man bäst skulle forma datan så AIn kan göra ett så bra jobb som möjligt. Men det stora problemet kom precis i slutet när jag skulle göra så att koden själv
hämtade checkpointen så att den skulle kunna köra av sig själv. Jag fick då ett fel där den inte hittade rätt sökväg när den skulle använda checkpointen. Jag hittade inget smidigt sätt att lösa detta på så det jag gjorde var att träna om en ny checkpoint och döpde den till det namn som koden letade efter. Detta gjorde dock att 
själva AIn inte blev perfekt tränad vilket påverkade texterna den skapade.

## Andra tankar om projektet

Överlag är jag väl nöjd med projektet men som sagt är själva AIn långt ifrån perfekt. Den kan skriva texter men de kan tyvärr vara något osammanhängande ibland. Däremot funkar allt annat superbra, till exempel datainsamling och uppladdning till reddit. Men skulle jag göra om projektet skulle jag försöka göra AIn mycket bättre än vad jag lyckades med den här gången. 