
def wobbly_table(rows, header=None, enable_bars=True):
    if not rows: return

    header = header or rows[0]
    column_starts = []
    starter, spacer, row = '| ', '   ', ''

    for column_name in header:
        column_starts.append(len(row))
        row += starter
        row += column_name
        row += spacer

    print(row)

    for row in rows[1:]:
        for i, column in enumerate(row):
            if enable_bars:
                out = (' ' * (column_starts[i] - (i * len(starter)))) + starter + column
                for j in range(i):
                    out = out[:column_starts[j]] + starter + out[column_starts[j]:]
            else:
                out = (' ' * column_starts[i]) + starter + column
            print(out)


if __name__ == '__main__':
    wobbly_table([
        ['Repository', 'Tag', 'Image ID', 'Created', 'Size'],
        ['gcr.io/k8s-minikube/kicbase', 'v0.0.39', '67a4b1138d2d', '5 weeks ago', '1.05GB'],
        ['hubproxy.docker.internal:5000/docker/desktop-kubernetes', 'kubernetes-v1.25.4-cni-v1.1.1-critools-v1.25.0-cri-dockerd-v0.2.6-1-debian', '2511e1796e7d', '5 months ago', '398MB'],
        ['registry.k8s.io/kube-apiserver', 'v1.25.4', '00631e54acba', '6 months ago', '128MB'],
        ['registry.k8s.io/kube-controller-manager', 'v1.25.4', '8f59f6dfaed6', '6 months ago', '117MB'],
        ['registry.k8s.io/kube-scheduler', 'v1.25.4', 'e2d17ec744c1', '6 months ago', '50.6MB'],
        ['registry.k8s.io/kube-proxy', 'v1.25.4', '2c2bc1864279', '6 months ago', '61.7MB'],
        ['registry.k8s.io/etcd', '3.5.5-0', '4694d02f8e61', '7 months ago', '300MB'],
        ['registry.k8s.io/pause', '3.8', '4873874c08ef', '11 months ago', '711kB'],
        ['registry.k8s.io/coredns/coredns', 'v1.9.3', '5185b96f0bec', '11 months ago', '48.8MB'],
        ['docker/desktop-vpnkit-controller', 'v2.0', '8c2c38aa676e', '2 years ago', '21MB'],
        ['docker/desktop-storage-provisioner', 'v2.0', '99f89471f470', '2 years ago', '41.9MB'],
    ], enable_bars=False)
