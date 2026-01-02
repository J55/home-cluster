# Cilium

## UniFi BGP

```sh
router bgp 64513
  bgp router-id 192.168.20.1
  no bgp ebgp-requires-policy

  neighbor k8s peer-group
  neighbor k8s remote-as 64514

  neighbor 192.168.20.20 peer-group k8s
  neighbor 192.168.20.21 peer-group k8s
  neighbor 192.168.20.22 peer-group k8s
  neighbor 192.168.20.30 peer-group k8s
  neighbor 192.168.20.31 peer-group k8s
  neighbor 192.168.20.32 peer-group k8s
  neighbor 192.168.20.33 peer-group k8s

  address-family ipv4 unicast
    neighbor k8s next-hop-self
    neighbor k8s soft-reconfiguration inbound
  exit-address-family
exit
```
