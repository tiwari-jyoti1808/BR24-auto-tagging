# BR24-auto-tagging

BR24 is an online German news platform, which has a collection of approx. 40,000 manually tagged articles. For a large scale news broadcaster like BR24, operating with a small team of editors, manually tagging hundreds of articles on a daily basis is a cumbersome and tedious overhead. Auto tagging will help reduce the time and effort required to publish articles, as well as, streamline the entire process of tag selection.

Here, we aim to build an auto-tagging service which can be incorporated in the BR24 content management system (CMS) easily. 

### /auto-tagging/
contains the source code for the service

### /data/ 
contains all data files required for running and executing the jupyter notebooks

### /images/ 
contains images displayed in the notebooks

### /notebooks/ 
contains all jupyter notebooks in a numbered format. The numbers represents the order in which they can be followed. All data analysis, baseline system creation, testing and evaluation of in-text and out-of-text tagging approaches are done in these notebooks. Each notebook works on a .pkl data file and saves the results to a different .pkl file. The names of the .pkl files are mentioned in the notebooks itself


Follow the below steps to install and execute the auto-tagging service:
- clone the BR24-auto-tagging repo

All source code is available in /auto-tagging/src. 
check.py and main.py are modules to test the service.

The auto-tagging service can be tested in 3 ways:

1. Test locally without docker and without server.
    * Run the file check.py by giving command 'python check.py' in the terminal. Text for the article can be specified in the placeholder [TEXT], in the check.py file.
    
2. Test locally without docker but with server.
    * Run the file main.py by giving command 'python main.py' in the terminal. 
    * While the server starts in the current terminal, open a new terminal and enter 'python'. This activates the pythom environment and enter 'import requests' to start exchange with the server. 
    * Enter 'r = requests.post('http://127.0.0.1:5000/predict', json={'id':1234, 'data':'[TEXT]'})' in the terminal to send a message request to the server of the service. Replace the placeholder '[TEXT]' with the text of the article for which tags need to be predicted.
    * You can check if the message request was successful by the command 'r.status_code', which should return 200.
    * Results from the service can be obtained by giving the 'r.json()' command.
    
3. Test locally with docker and with server.
    * Docker command to start container: docker-compose up --build --remove-orphans 
    * Docker command to inspect Docker Network: docker network inspect [NETWORK NAME] | grep IPv4
    
    * While the container starts in the current terminal, open a new terminal and enter 'python'. This activates the pythom environment and enter 'import requests' to start exchange with the server. 
    * Enter 'r = requests.post('http://172.19.0.2:8007/predict', json={'id':1234, 'data':'[TEXT]'})' in the terminal to send a message request to the server of the service. Replace the placeholder '[TEXT]' with the text of the article for which tags need to be predicted. The IPv4 address may be vary and the correct address can be obtained by inspecting the docker network.
    * You can check if the message request was successful by the command 'r.status_code', which should return 200.
    * Results from the service can be obtained by giving the 'r.json()' command.