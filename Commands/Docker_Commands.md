
#########################################################

## Docker :

# Install @Ubuntu :

sudo apt-get remove docker docker-engine docker.io
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSl https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce

docker run hello-world // Give your environment a quick test run to make sure you are all set up

## Pour pouvoir enlever les "sudo" devant docker :

sudo groupadd docker
sudo usermod -aG docker $USER
Normalement c'est bon après ça

# Build command :

docker build -t friendlyhello .

# Run command :
docker run -p 4000:80 friendlyhello
==> open web browser and into address URL : localhost:4000

# Tag the image
docker tag friendlyhello myfriendlyhello

# Publish the image
docker push username/repository:tag

# Pull & Run the image from the remote repository
docker run -p 4000:80 username/repository:tag


# Dockerfile :
==> Defines what goes on in the environment inside your container.


sudo docker ps -a // Visualiser tous les containers actuels

docker image ls // Show all built images (in your machine's local Docker imagery registry)

sudo docker rm `sudo docker ps -aq` // Supprimer tous les containers actuels