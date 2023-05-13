# wobbly_table

> Print tables more compactly in the terminal

Turns this way too long table:

```
REPOSITORY                                                TAG                                                                          IMAGE ID       CREATED         SIZE
gcr.io/k8s-minikube/kicbase                               v0.0.39                                                                      67a4b1138d2d   5 weeks ago     1.05GB
hubproxy.docker.internal:5000/docker/desktop-kubernetes   kubernetes-v1.25.4-cni-v1.1.1-critools-v1.25.0-cri-dockerd-v0.2.6-1-debian   2511e1796e7d   5 months ago    398MB
registry.k8s.io/kube-apiserver                            v1.25.4                                                                      00631e54acba   6 months ago    128MB
registry.k8s.io/kube-proxy                                v1.25.4                                                                      2c2bc1864279   6 months ago    61.7MB
registry.k8s.io/kube-scheduler                            v1.25.4                                                                      e2d17ec744c1   6 months ago    50.6MB
registry.k8s.io/kube-controller-manager                   v1.25.4                                                                      8f59f6dfaed6   6 months ago    117MB
registry.k8s.io/etcd                                      3.5.5-0                                                                      4694d02f8e61   7 months ago    300MB
registry.k8s.io/pause                                     3.8                                                                          4873874c08ef   11 months ago   711kB
registry.k8s.io/coredns/coredns                           v1.9.3                                                                       5185b96f0bec   11 months ago   48.8MB
docker/desktop-vpnkit-controller                          v2.0                                                                         8c2c38aa676e   2 years ago     21MB
docker/desktop-storage-provisioner                        v2.0                                                                         99f89471f470   2 years ago     41.9MB
```

Into this more compact one:

```python
from wobbly_table import wobbly_table

headers = ['a', 'b', 'c', ...]
rows = [[...], [...], [...], ...]
wobbly_table(rows, headers, enable_bars=True)
```

```
| Repository   | Tag   | Image ID   | Created   | Size
| gcr.io/k8s-minikube/kicbase
|              | v0.0.39
|              |       | 67a4b1138d2d
|              |       |            | 5 weeks ago
|              |       |            |           | 1.05GB
| hubproxy.docker.internal:5000/docker/desktop-kubernetes
|              | kubernetes-v1.25.4-cni-v1.1.1-critools-v1.25.0-cri-dockerd-v0.2.6-1-debian
|              |       | 2511e1796e7d
|              |       |            | 5 months ago
|              |       |            |           | 398MB
| registry.k8s.io/kube-apiserver
|              | v1.25.4
|              |       | 00631e54acba
|              |       |            | 6 months ago
|              |       |            |           | 128MB
| registry.k8s.io/kube-controller-manager
|              | v1.25.4
|              |       | 8f59f6dfaed6
|              |       |            | 6 months ago
|              |       |            |           | 117MB
| registry.k8s.io/kube-scheduler
|              | v1.25.4
|              |       | e2d17ec744c1
|              |       |            | 6 months ago
|              |       |            |           | 50.6MB
| registry.k8s.io/kube-proxy
|              | v1.25.4
|              |       | 2c2bc1864279
|              |       |            | 6 months ago
|              |       |            |           | 61.7MB
| registry.k8s.io/etcd
|              | 3.5.5-0
|              |       | 4694d02f8e61
|              |       |            | 7 months ago
|              |       |            |           | 300MB
| registry.k8s.io/pause
|              | 3.8
|              |       | 4873874c08ef
|              |       |            | 11 months ago
|              |       |            |           | 711kB
| registry.k8s.io/coredns/coredns
|              | v1.9.3
|              |       | 5185b96f0bec
|              |       |            | 11 months ago
|              |       |            |           | 48.8MB
| docker/desktop-vpnkit-controller
|              | v2.0
|              |       | 8c2c38aa676e
|              |       |            | 2 years ago
|              |       |            |           | 21MB
| docker/desktop-storage-provisioner
|              | v2.0
|              |       | 99f89471f470
|              |       |            | 2 years ago
|              |       |            |           | 41.9MB
```

Optionally you can disable the repeated bars. This is helpful for even smaller
terminals.


```python
wobbly_table(rows, headers, enable_bars=False)
```

```
| Repository   | Tag   | Image ID   | Created   | Size
| gcr.io/k8s-minikube/kicbase
               | v0.0.39
                       | 67a4b1138d2d
                                    | 5 weeks ago
                                                | 1.05GB
| hubproxy.docker.internal:5000/docker/desktop-kubernetes
               | kubernetes-v1.25.4-cni-v1.1.1-critools-v1.25.0-cri-dockerd-v0.2.6-1-debian
                       | 2511e1796e7d
                                    | 5 months ago
                                                | 398MB
| registry.k8s.io/kube-apiserver
               | v1.25.4
                       | 00631e54acba
                                    | 6 months ago
                                                | 128MB
| registry.k8s.io/kube-controller-manager
               | v1.25.4
                       | 8f59f6dfaed6
                                    | 6 months ago
                                                | 117MB
| registry.k8s.io/kube-scheduler
               | v1.25.4
                       | e2d17ec744c1
                                    | 6 months ago
                                                | 50.6MB
| registry.k8s.io/kube-proxy
               | v1.25.4
                       | 2c2bc1864279
                                    | 6 months ago
                                                | 61.7MB
| registry.k8s.io/etcd
               | 3.5.5-0
                       | 4694d02f8e61
                                    | 7 months ago
                                                | 300MB
| registry.k8s.io/pause
               | 3.8
                       | 4873874c08ef
                                    | 11 months ago
                                                | 711kB
| registry.k8s.io/coredns/coredns
               | v1.9.3
                       | 5185b96f0bec
                                    | 11 months ago
                                                | 48.8MB
| docker/desktop-vpnkit-controller
               | v2.0
                       | 8c2c38aa676e
                                    | 2 years ago
                                                | 21MB
| docker/desktop-storage-provisioner
               | v2.0
                       | 99f89471f470
                                    | 2 years ago
                                                | 41.9MB
```
