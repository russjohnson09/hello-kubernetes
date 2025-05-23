

Hello kubernetes

https://kubernetes.io/docs/tutorials/hello-minikube/

# Windows

https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download




https://kubernetes.io/docs/tasks/tools/#kubectl
https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/



https://kubernetes.io/docs/tutorials/hello-minikube/



minikube start

minikube dashboard

virtualbox VM interface


A Kubernetes Pod is a group of one or more Containers



Use the kubectl create command to create a Deployment that manages a Pod. The Pod runs a Container based on the provided Docker image.


kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080



kubectl get deployments


kubectl get pods


https://www.reddit.com/r/devops/comments/qfotkk/ecs_fargate_vs_eks/

Use Fargate until you outgrow it.

The last thing you need as a startup is "challenging" when you should be focusing on growing the product. If you're not having issues with Fargate, don't layer on Kubernetes until you run into some problem it actually solves and is worth the engineering effort and the price tag that comes with.


With AWS Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.

EC2

We were on EC2 instances but moved to using ECS with Fargate

We were on ECS but then moved to 


AWS

EC2 - Elastic Compute Cloud

EKS - Elastic Kubernetes Service
ECS - Elastic Constainer Service


First it was every business had its own server room.

Then it was a group of businesses that would all do business with someone in their state.

Then it was AWS with their EC2 instances.

Then docker was introduced which made infrastructure as code and continuous deployments much easier. 
Tools like jenkins and code coverage tools made releases easier. There is more of a one time setup from devops to get things going.

Docker + Kubernetes is great because they are both open source and so you aren't necessarily tied to running things on AWS.

You can make your own server rooms if you really want to come back full circle.



Then it was business worked with other local bussinesses that specialized in servers


EC2
ECS
EKS

Fargate with docker images.


You give up some control and you tie yourself more closely with AWS.

But the work to migrate off of AWS if you wanted to wouldn't be too much work. Most of the more complex parts are handled by the docker images?


https://www.cloudzero.com/blog/ecs-vs-eks/



SQS


terraform



https://hub.docker.com/_/perl


mariadb


https://dev.to/zakame/a-few-tips-for-perl-on-docker-and-kubernetes-29bg




windows subsystem for linux 
wsl


https://hub.docker.com/_/mariadb


https://www.reddit.com/r/mysql/comments/y5u1au/exactly_how_free_mysql_is/


https://code.visualstudio.com/docs/containers/overview


https://docs.docker.com/desktop/setup/install/windows-install/


test123