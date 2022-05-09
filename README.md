# 🍿TTS-Korean-Dubbing-Project
Google Text To Speech API를 이용하여 한국어음성파일을 만들고 moviepy를 이용하여 영상파일과 병합하여 한국어더빙영상을 만드는 프로젝트입니다.


### 기능구현(python 기반)
+ SSML파일(subtitles.ssml)을 읽어서 Google Text To Speech API를 이용하여 한국어음성파일(dubbing.mp3)로 변환하여 저장합니다.
+ Moviepy 라이브러리를 이용하여 한국어음성파일(dubbing.mp3)과 원본영상파일(movie.mp4) 및 원본음성파일(background.mp3)을 결합하여 하나의 영상파일(result.mp4)을 생성합니다.
+ ImageMagick를 이용하여 생성한 영상파일(result.mp4)과 자막파일(subtitles.srt)을 결합하여 최종적인 영상파일(final.mp4)를 생성합니다.
 
### 결과화면
![final](https://user-images.githubusercontent.com/102117360/167414247-d9a569b0-0702-4f9d-954a-923af69eb927.gif)

