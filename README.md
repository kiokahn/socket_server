# Socket Server

- 클라이언트의 Request 확인을 위한 소켓서버
- 클라이언트 요청을 그대로 "request"폴더 하위에 "년-월-일-시-분-초.bin" 파일명을 가진 이진파일로 저장함


## 테스트

Test for HTTP multipart by [CURL](https://curl.se)

```bash
curl -X POST -S -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" -F "author=1" -H 'Accept: application/json' -F "title=curl 테스트" -F "text=API curl로 작성된 AP 테스트 입력 입니다." -F "created_date=2024-06-10T18:34:00+09:00" -F "published_date=2024-06-10T18:34:00+09:00" -F "image=@/Users/kiokahn/Pictures/53297865145_aca24097c7_k.jpg;type=image/jpg" http://127.0.0.1:8000/api_root/Post/
```



## 제작

By Kiok Ahn, kiokahn@gazzi.ai
2024-06-05
