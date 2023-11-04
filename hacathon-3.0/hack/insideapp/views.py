from django.shortcuts import render,redirect


from .models import workeraccountregister,useraccountregister 
from .models import order
from django.contrib.auth.models import User
from django.contrib.auth.models import auth

# Create your views here.

def loginpage(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)  
        
        if user is not None:
          auth.loginpage(request,user)
          return redirect("/")
        return redirect('insi')

        
    return render(request,"index.html")

   
def register(request):
    if request.method=="POST":
        first_name=request.POST.get('firstname','')
        last_name=request.POST.get('lastname','')
        username=request.POST.get('firstname','')
        address_name=request.POST.get('address','')
        Gender=request.POST.get('gender','')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        pincode=request.POST.get('pincode','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        pn=useraccountregister(Firstname=first_name,Lasttname=last_name, Username=username,Address=address_name, Gender=Gender, State=state,city=city, pincode=pincode,email=email, phone=phone, password=password)
        pn.save()

    return render(request,"user_registration.html")


def adminpage(request):
    return render(request,"")

def center(request,cno):
    if request.method == 'POST':
          order_no=request.POST.get('order_id','')
          block=request.POST.get('delivery_guy','')
          order.objects.filter(order_number=order_no).update(current_b=block,current_center=None)

    order_list=order.objects.filter(current_center=cno)     
    return render(request,"Block_page.html",{'orders':order_list})

def worker_reg(request):
    if request.method=="POST":
        first_name=request.POST.get('firstname','')
        last_name=request.POST.get('lastname','')
        user_name=request.POST.get('firstname','')
        address_name=request.POST.get('address','')
        Gender=request.POST.get('gender','')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        pincode=request.POST.get('pincode','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        en=workeraccountregister(Firstname=first_name,Lasttname=last_name, Username=user_name,Address=address_name, Gender=Gender, State=state,city=city, pincode=pincode,email=email, phone=phone, password=password)
        en.save()
    return render(request,"worker_registration.html")

def user(request, uno):
    if request.method == 'POST':
        name='abcd'
        adress1=request.POST.get('address_1','')
        adress2=request.POST.get('address_2','')
        start_b=1
        end_block=12
        way=[1,2,7,12]
        way_str=''
        for i in way:
            way_str= way_str + str(i)
        order1=order(customer_name=name,adress1=adress1,adress2=adress2,start_b=start_b,final_b=end_block,path=way_str, current_b=start_b,current_status='pending')   
        order1.save()
        # worker1=workeraccountregister.objects.get(worker_id=start_b) 
    order_list=order.objects.filter(customer_name='abcd')
    print(order_list)
    return render(request,"dashboard.html",{'recent_orders':order_list})

def worker(request, wno):

    if request.method== 'POST':
        order_no=request.POST.get('order_number','')
        customer_name=request.POST.get('customer_name','')
        delivery_name=request.POST.get('delivery_address','')
        if delivery_name in ['1','2','3','4','5','6']:
              d= int(delivery_name)
              order.objects.filter(order_number=order_no).update(current_center=d, current_b=None)
        else:      
            order.objects.filter(order_number=order_no).update(current_status='deliverd',current_b=None)
        
    order_list=order.objects.filter(current_b=wno)
        
    return render(request,"dashbord_worker.html",{'orders':order_list})
              

              
              



    

    

from typing import List
from sys import maxsize
from collections import deque

def add_edge(adj: List[List[int]],
			src: int, dest: int) -> None:
	adj[src].append(dest)
	adj[dest].append(src)

# Function which finds all the paths
# and stores it in paths array
def find_paths(paths: List[List[int]], path: List[int],
			parent: List[List[int]], n: int, u: int) -> None:
	# Base Case
	if (u == -1):
		paths.append(path.copy())
		return

	# Loop for all the parents
	# of the given vertex
	for par in parent[u]:

		# Insert the current
		# vertex in path
		path.append(u)

		# Recursive call for its parent
		find_paths(paths, path, parent, n, par)

		# Remove the current vertex
		path.pop()

# Function which performs bfs
# from the given source vertex
def bfs(adj: List[List[int]],
		parent: List[List[int]], n: int,
		start: int) -> None:

	# dist will contain shortest distance
	# from start to every other vertex
	dist = [maxsize for _ in range(n)]
	q = deque()

	# Insert source vertex in queue and make
	# its parent -1 and distance 0
	q.append(start)
	parent[start] = [-1]
	dist[start] = 0

	# Until Queue is empty
	while q:
		u = q[0]
		q.popleft()
		for v in adj[u]:
			if (dist[v] > dist[u] + 1):

				# A shorter distance is found
				# So erase all the previous parents
				# and insert new parent u in parent[v]
				dist[v] = dist[u] + 1
				q.append(v)
				parent[v].clear()
				parent[v].append(u)

			elif (dist[v] == dist[u] + 1):

				# Another candidate parent for
				# shortes path found
				parent[v].append(u)

# Function which prints all the paths
# from start to end
def print_paths(adj: List[List[int]], n: int,
				start: int, end: int) -> None:
	paths = []
	path = []
	parent = [[] for _ in range(n)]

	# Function call to bfs
	bfs(adj, parent, n, start)

	# Function call to find_paths
	find_paths(paths, path, parent, n, end)
	last=paths[0]
	return(last)
	

def getway():
    n = 27

    adj = [[] for _ in range(n)]

	# Given Graph
    add_edge(adj, 1, 2)
    add_edge(adj, 1, 5)
    add_edge(adj, 1, 6)
    add_edge(adj, 2, 3)
    add_edge(adj, 2, 7)
    add_edge(adj, 2, 6)
    add_edge(adj, 2, 5)
    add_edge(adj, 3, 6)
    add_edge(adj, 3, 7)
    add_edge(adj, 3, 8)
    add_edge(adj, 4, 7)
    add_edge(adj, 4, 8)
    add_edge(adj, 5, 6)
    add_edge(adj, 5, 10)
    add_edge(adj, 5, 9)
    add_edge(adj, 6, 9)
    add_edge(adj, 6, 10)
    add_edge(adj, 6, 11)
    add_edge(adj, 6, 7)
    add_edge(adj, 7, 8)
    add_edge(adj, 7, 12)
    add_edge(adj, 7, 11)
    add_edge(adj, 7, 10)
    add_edge(adj, 8, 11)
    add_edge(adj, 8, 12)
    add_edge(adj, 9, 10)
    add_edge(adj, 10, 11)
    add_edge(adj, 11, 12)
    
    src =1
    des=12

	