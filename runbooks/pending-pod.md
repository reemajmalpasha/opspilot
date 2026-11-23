# Kubernetes pod stuck in Pending
A Pending pod has not been scheduled onto a node yet.
1. Run kubectl get pods to confirm the status.
2. Run kubectl describe pod NAME and read the Events section at the bottom.
3. Common causes: insufficient CPU or memory on nodes, node taints without a toleration, nodeSelector or affinity that matches no node, a PersistentVolumeClaim that is not bound, or no nodes in Ready state.
4. Check nodes with kubectl get nodes, kubectl describe node NAME and kubectl top nodes.
5. Fix the cause, for example reduce resource requests, add nodes, add a toleration or fix the PVC. The pod then schedules by itself.
