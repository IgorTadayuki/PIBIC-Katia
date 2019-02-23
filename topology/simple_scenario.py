#!/usr/bin/python

"""
This example creates a multi-controller network from semi-scratch by
using the net.add*() API and manually starting the switches and controllers.

This is the "mid-level" API, which is an alternative to the "high-level"
Topo() API which supports parametrized topology classes.

Note that one could also create a custom switch class and pass it into
the Mininet() constructor.
"""

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

"""Create simple scenario

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=simple_scenario_topo' from the command line.
"""

from mininet.topo import Topo


class SimpleScenarioTopo(Topo):

    def __init__(self):
        """
        Create custom topo to lab 08.
        """

        # Initialize topology
        Topo.__init__(self)

        # protocols = "OpenFlow10"

        net = Mininet(switch=OVSSwitch)

        info("*** Creating (reference) controllers\n")
        c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6633)

        info("*** Creating switches\n")
        s1 = net.addSwitch('s1')
        s2 = net.addSwitch('s2')

        info("*** Creating hosts\n")
        h1 = net.addHost(name='h1', ip='10.0.0.1', defaultHost='')
        h2 = net.addHost(name='h2', ip='10.0.0.2', defaultHost='')

        info("*** Creating links\n")
        net.addLink(h1, s1)
        net.addLink(s1, s2)
        net.addLink(h2, s2)

        info("*** Creating network\n")
        net.build()
        s1.start([c1])
        net.start()
        net.staticArp()
        CLI(net)
        net.stop()


topos = {'simple_scenario_topo': (lambda: SimpleScenarioTopo())}


# def SimpleScenario():
#     "Create a network from semi-scratch with multiple controllers."
#
#     net = Mininet(controller=Controller, switch=OVSSwitch)
#
#     info("*** Creating (reference) controllers\n")
#     c1 = net.addController('c1', port=6633)
#     c2 = net.addController('c2', port=6634)
#
#     info("*** Creating switches\n")
#     s1 = net.addSwitch('s1')
#     s2 = net.addSwitch('s2')
#
#     info("*** Creating hosts\n")
#     hosts1 = [net.addHost('h%d' % n) for n in (3, 4)]
#     hosts2 = [net.addHost('h%d' % n) for n in (5, 6)]
#
#     info("*** Creating links\n")
#     for h in hosts1:
#         net.addLink(s1, h)
#     for h in hosts2:
#         net.addLink(s2, h)
#     net.addLink(s1, s2)
#
#     info("*** Starting network\n")
#     net.build()
#     c1.start()
#     c2.start()
#     s1.start([c1])
#     s2.start([c2])
#
#     info("*** Testing network\n")
#     net.pingAll()
#
#     info("*** Running CLI\n")
#     CLI(net)
#
#     info("*** Stopping network\n")
#     net.stop()
#
#
# if __name__ == '__main__':
#     setLogLevel('info')  # for CLI output
#     SimpleScenario()
