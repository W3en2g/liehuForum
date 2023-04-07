```sh
cd /home/pi/projects
. venv/bin/activate
cd /home/pi/projects/liehuForum/backend
export FLASK_APP=app
export FLASK_ENV=development
flask run --host=0.0.0.0
```



```sh
sudo chmod 777 development_setup.sh 
```





```sh
screen -L -Logfile /home/pi/projects/backend.log  -dmS backend /home/pi/projects/development_setup.sh
```

 