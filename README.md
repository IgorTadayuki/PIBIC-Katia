# PIBIC-Katia


### Install the dependencies

Install mininet
```
pip install git+https://github.com/mininet/mininet.git
```

Install all dependencies
```
pip install -r requirements.txt
```

### Debugging the code
To debug the application, run the app.py file as the main application
```
python app.py
```
or configure to use your IDE: 
1. https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
2. https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html

## Simple Scenario (scenario1)

Mininet simple scenario (scenario1) in figure:
```
mn --custom topology/simple_scenario.py --topo=simple_scenario_topo
```