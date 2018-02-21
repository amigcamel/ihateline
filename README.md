# ihateline

A life-saver for helping you sending LINE message automatically, and more.

---


Tired of sending greetings via LINE to your parents or relatives each and every day?  
Well, `ihateline` could be your best friend!



## Prerequisites

### `credentials.conf`

Save your account and password in `credentials.conf`.

    [main]
    email = youremail@whatever.swag
    password = yourpasswordhere

Pack your LINE Chrome extension and put it in ` src`.

    src/Extensions/ophjlpahpchlmihnnnihgmmeilfjmjjc/2.1.0_0.crx


## Environments
+ Python 3.6+  
+ docker
+ docker-compose


## Documentation

### Deploy

    docker-compose up -d

You have to enter the "verification code" on your mobile every time you start the service. To get the verification code:

    docker-compose logs -f ihateline

### Add your craontabs

`cron/crontabs`

    * */5 * * * python client.py python cli.py -f johndoe -m hello --random-offset 180

If there's any change of the file, do not forget to restart the `cron` service:

    docker-compose restart cron
