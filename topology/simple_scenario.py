#!/usr/bin/python

from mininet.cli import CLI
from mininet.log import info
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController

"""
Create simple scenario

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=simple_scenario_topo' from the command line.
"""

from mininet.topo import Topo


class SimpleScenarioTopo(Topo):

    def __init__(self):
        """
        Create custom topo SimpleScenarioTopo.
        """

        # Initialize topology
        Topo.__init__(self)

        info("*** Using Openflow 1.3 \n")
        protocols = "OpenFlow13"

        net = Mininet(switch=OVSSwitch)

        info("*** Creating (reference) controllers\n")
        c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6633)

        info("*** Creating switches\n")
        s1 = net.addSwitch('s1', protocols=protocols)
        s2 = net.addSwitch('s2', protocols=protocols)

        info("*** Creating hosts\n")
        h1 = net.addHost(name='h1', ip='10.0.0.1', mac='00:00:00:00:00:01', defaultHost='')
        h2 = net.addHost(name='h2', ip='10.0.0.2', mac='00:00:00:00:00:02', defaultHost='')
        # h3 = net.addHost(name='h3', ip='10.0.0.3', mac='00:00:00:00:00:03', defaultHost='')

        info("*** Creating links\n")
        net.addLink(h1, s1)
        net.addLink(s1, s2)
        net.addLink(h2, s2)
        # net.addLink(h3, s2)

        info("*** Creating network\n")
        net.build()
        s1.start([c1])
        net.start()
        net.staticArp()
        CLI(net)
        net.stop()


topos = {'simple_scenario_topo': (lambda: SimpleScenarioTopo())}
