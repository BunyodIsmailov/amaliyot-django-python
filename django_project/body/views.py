from django.shortcuts import render
from django.http import HttpResponse

def body_funk(request):
    return HttpResponse("""<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Gimn</title>
  </head>
  <body style="background-color:gray; text-align:center;">

<h1 style="color:DodgerBlue;">O'zbekiston Gimni</h1>

<!--#ishonch055-->
 <pre style="color:green;font-family:verdana;">
Serquyosh, hur o‘lkam, elga baxt, najot,
Sen o‘zing do‘stlarga yo‘ldosh, mehribon!
Yashnagay to abad ilmu fan, ijod,
Shuhrating porlasin toki bor jahon!</pre>


<pre>Oltin bu vodiylar — jon O‘zbekiston,
Ajdodlar mardona ruhi senga yor!
Ulug‘ xalq qudrati jo‘sh urgan zamon,
Olamni mahliyo aylagan diyor!


Bag‘ri keng o‘zbekning o‘chmas iymoni,
Erkin, yosh avlodlar senga zo‘r qanot!
Istiqlol mash’ali, tinchlik posboni,
Haqsevar, ona yurt, mangu bo‘l obod!


Oltin bu vodiylar — jon O‘zbekiston,
Ajdodlar mardona ruhi senga yor!
Ulug‘ xalq qudrati jo‘sh urgan zamon,
Olamni mahliyo aylagan diyor!</pre>


<pre style="text-align: right;">
  Mutal Burxonov musiqasi
Abdulla Oripov she’ri</pre>
<hr>""")
    # return HttpResponse("<h1>What is Lorem Ipsum?</h1>\n<h2>Lorem Ipsum </h2><h3>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</h3>")
def about_funk(request):
    return HttpResponse("""<html>
    <head>
    <style>* {
    paddiing: 0;
    margin: 0;
    box-sizing: border-box;
}

@font-face {
    font-family: "Iceland";
    font-style: normal;
    font-weight: 400;
}

body {
    background-color: #222;
}

.flag {
    width: 50rem;
    height: 25rem;
    border: solid 1px #000;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 4px 8px 16px 0, inset 0 8rem 0 blue, inset 0 8.5rem 0 red, inset 0 16.5rem 0 white, inset 0 17rem 0 red, inset 0 25rem 0 green;
    padding: 0.5rem 4rem;
}

.flag::before {
    content: " ";
    width: 7rem;
    height: 7rem;
    border-radius: 50%;
    position: absolute;
    box-shadow: inset 0.8rem 0.1rem white;
}

.flag::after {
    content: "\2605";
    position: absolute;
    color: white;
    font-weight: 1.8rem;
    line-height: 100%;
    top: 5.9rem;
    left: 9rem;
    text-shadow: 2.5rem 0 0, 5rem 0 0, 7.5rem 0 0, 10rem 0 0, 2.5rem -2.8rem 0, 5rem -2.8rem 0, 7.5rem -2.8rem 0, 10rem -2.8rem 0, 5rem -5.6rem 0, 7.5rem -5.6rem 0, 10rem -5.6rem 0;
}

p {
    text-align: center;
    position: absolute;
    top: 15%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 50px;
}

a {
    text-decoration: none;
    transition: all 0.5s;
}

p a {
    font-size: 1.5rem;
    color: #228dff;
    font-family: Iceland;
}

p:hover {
    color: #fff;
    animation: animationuz;
}

@keyframes animationuz {
    from {
        text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #228dff, 0 0 70px #228dff, 0 0 80px #228dff, 0 0 100px #228dff, 0 0 150px #228dff, ;
    }
    to {
        0 0 5px #fff,
        0 0 10px #fff,
        0 0 15px #fff,
        0 0 20px #228dff,
        0 0 35px #228dff,
        0 0 40px #228dff,
        0 0 50px #228dff,
        0 0 150px #228dff,
        ;
        ;
    }
}</style>
    <meta charset="UTF-8">

    <title>Document</title>
</head>

<body>



    <div class="flag"></div>
    <p>Jonim Fido O'zbekistonim </p>
</body>

</html>""")
def home_funk(request):
    return HttpResponse("""
    <html lang="en">

<head>

    <title>klub</title>
    <style>* {
    margin: 0;
    padding: 0;
    font-family: consolas;
    box-sizing: border-box;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    flex-direction: column;
    background: #050801;
}

a {
    position: relative;
    display: inline-block;
    padding: 25px 30px;
    margin: 40px 0;
    color: #03e9f4;
    font-size: 24px;
    text-decoration: none;
    text-transform: uppercase;
    overflow: hidden;
    transition: 0.5s;
    letter-spacing: 4px;
    -webkit-box-reflect: below 1px linear-gradient(transparent, #0005);
}

a:nth-child(1) {
    filter: hue-rotate(290deg);
}

a:nth-child(3) {
    filter: hue-rotate(110deg);
}

a:hover {
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4, 0 0 200px #03e9f4;
}

a span {
    position: absolute;
    display: block;
}

a span:nth-child(1) {
    top: 0;
    left: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate1 1s linear infinite;
}

@keyframes animate1 {
    0% {
        left: -100%;
    }
    50%,
    100% {
        left: 100%;
    }
}

a span:nth-child(2) {
    top: -100%;
    right: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}

@keyframes animate2 {
    0% {
        top: -100%;
    }
    50%,
    100% {
        top: 100%;
    }
}

a span:nth-child(3) {
    bottom: 0;
    right: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(270deg, transparent, #03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.5s;
}

@keyframes animate3 {
    0% {
        right: -100%;
    }
    50%,
    100% {
        right: 100%;
    }
}

a span:nth-child(4) {
    bottom: -100%;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(270deg, transparent, #03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}

@keyframes animate4 {
    0% {
        bottom: -100%;
    }
    50%,
    100% {
        bottom: 100%;
    }
}</style>
</head>

<body>
    <a href="#">
        <span></span>
        <span></span>
        <span></span>
        <span></span> ISHONCH </a>
    <a href="#">
        <span></span>
        <span></span>
        <span></span>
        <span></span> ISHONCH
    </a>
    <a href="#">
        <span></span>
        <span></span>
        <span></span>
        <span></span> ISHONCH
    </a>
</body>

</html>""")
def yurak_funk(request):
    return HttpResponse("""
<!--❤️ISHONCH❤️-->

<!DOCTYPE html>
<html>

<head>
    <title>animation in heart</title>
    <link rel="stylesheet" href="style.css">
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <style>/*❤️ISHONCH❤️*/

body {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 90vh;
    background-color: black;
}

.heart {
    position: relative;
    height: 200px;
    width: 200px;
    background: #ff1010;
    transform: rotate(45deg);
    box-shadow: 2px 2px 60px #ff66cc;
    animation: heart 1s ease-in-out infinite;
}

@keyframes heart {
    0% {
        transform: rotate (45deg) scale(0.8);
    }
    20% {
        transform: rotate(45deg) scale(0.9);
    }
    60% {
        transform: rotate(45deg) scale(1);
    }
    80% {
        transform: rotate(45deg) scale(0.9);
    }
    100% {
        transform: rotate(45deg) scale(1);
    }
}

.heart::before {
    content: '';
    position: absolute;
    height: 100px;
    width: 200px;
    background: #ff1010;
    top: -100px;
    border-top-left-radius: 100px;
    border-top-right-radius: 100px
}

.heart::after {
    content: '';
    position: absolute;
    height: 200px;
    width: 100px;
    background: #ff1010;
    left: -100px;
    border-top-left-radius: 100px;
    border-bottom-left-radius: 100px;
}</style>
</head>

<body>
    <div class="heart"></div>
</body>

</html>""")