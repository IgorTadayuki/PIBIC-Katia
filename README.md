# PIBIC-Katia

### Install the dependencies

Install mininet
```
$ pip install git+https://github.com/mininet/mininet.git
```

Install all dependencies
```
$ pip install -r requirements.txt
```

### Debugging the code
To debug the application, run the app.py file as the main application
```
$ python app.py
```
or configure to use your IDE: 
1. https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
2. https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html


## Scenarios

![alt text](https://raw.githubusercontent.com/LABORA-INF-UFG/PIBIC-Katia/master/docs/topology.jpg)

**Obs.:** To each scenario use the **OpenFlow protocol version 1.3**

### Simple Scenario (scenario1)

Mininet simple scenario (scenario1):
```
$ mn --custom topology/simple_scenario.py --topo=simple_scenario_topo
```

Run in your host the following command to show all rules added on switch `s1`: 
```
$ ovs-ofctl dump-flows s1 -O OpenFlow13
```
we hope to have two rules:
```
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x0, duration=58.695s, table=0, n_packets=3, n_bytes=294, priority=1,in_port=1,dl_dst=00:00:00:00:00:02 actions=output:2
 cookie=0x0, duration=58.688s, table=0, n_packets=3, n_bytes=294, priority=1,in_port=2,dl_dst=00:00:00:00:00:01 actions=output:1
 cookie=0x0, duration=66.593s, table=0, n_packets=18, n_bytes=1484, priority=0 actions=CONTROLLER:65535
```

and on switch `s2`:
```
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x0, duration=232.293s, table=0, n_packets=3, n_bytes=294, priority=1,in_port=1,dl_dst=00:00:00:00:00:02 actions=output:2
 cookie=0x0, duration=232.290s, table=0, n_packets=3, n_bytes=294, priority=1,in_port=2,dl_dst=00:00:00:00:00:01 actions=output:1
 cookie=0x0, duration=240.163s, table=0, n_packets=21, n_bytes=1694, priority=0 actions=CONTROLLER:65535
```

**Obs.:** Note that we have one rule for the output packet and one for the input packet, i.e., ping response (e.g. h1 ping h2). 
```
(h1 -> s1 -> s2 -> h2)
(h2 -> s2 -> s1 -> h1)
```

To see the number of each port on the switch, run:
```
$ ovs-ofctl show s1 -O OpenFlow13
```

```
OFPT_FEATURES_REPLY (OF1.3) (xid=0x2): dpid:0000000000000001
n_tables:254, n_buffers:256
capabilities: FLOW_STATS TABLE_STATS PORT_STATS GROUP_STATS QUEUE_STATS
OFPST_PORT_DESC reply (OF1.3) (xid=0x3):
 1(s1-eth1): addr:92:88:42:34:65:af
     config:     0
     state:      0
     current:    10GB-FD COPPER
     speed: 10000 Mbps now, 0 Mbps max
 2(s1-eth2): addr:d2:9e:ac:8d:50:9a
     config:     0
     state:      0
     current:    10GB-FD COPPER
     speed: 10000 Mbps now, 0 Mbps max
 LOCAL(s1): addr:be:4b:f6:45:be:47
     config:     PORT_DOWN
     state:      LINK_DOWN
     speed: 0 Mbps now, 0 Mbps max
OFPT_GET_CONFIG_REPLY (OF1.3) (xid=0x5): frags=normal miss_send_len=0
```

## Now, implement scenario1 in the file[./controller/simple_scenario.py](./controller/simple_scenario.py)

To do this, change line 12 of [app.py](./app.py) file to reference the file [./controller/simple_scenario.py](./controller/simple_scenario.py)


