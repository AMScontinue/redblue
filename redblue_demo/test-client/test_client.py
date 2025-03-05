"""
This module contains a test client script for the redblue_demo application.

The script creates multiple instances of the `Client` class and performs various operations 
such as deposit, interest calculation, withdrawal, 
and checking account balance on different servers.
"""

import sys
import time
from typing import List
from redblue_demo.client.client import Client


def case1(rpc_clients: List[Client]):
    """
    Executes a series of operations on the specified RPC clients for account 20.
    server 0: deposit 1000
    server 1: deposit 1100
    server 0: interest
    server 1: withdraw 2500

    Args:
        rpc_clients (List[Client]): A list of RPC clients.

    Returns:
        None
    """
    
    start_time = time.perf_counter()

    print("------------test case 1-------------")
    res = rpc_clients[0].request({"cmd": "DEPOSIT", "aid": 20, "amount": 1000})
    print(f"[account 20] DEPOSIT server 0 (+ 1000): {res}")
    res = rpc_clients[1].request({"cmd": "DEPOSIT", "aid": 20, "amount": 1100})
    print(f"[account 20] DEPOSIT server 1 (+ 1100): {res}")
    res = rpc_clients[0].request({"cmd": "INTEREST", "aid": 20})
    print(f"[account 20] DEPOSIT server 0 (rate 0.04): {res}")
    res = rpc_clients[1].request({"cmd": "WITHDRAW", "aid": 20, "amount": 2500})
    print(f"[account 20] WITHDRAW server 1 (- 2500): {res}")
    time.sleep(0.3)
    print("-----------------")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 20})
    print(f"[account 20] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 20})
    print(f"[account 20] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 20})
    print(f"[account 20] CHECK server 2: {res}")

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"test case 1 耗时: {elapsed_time:.6f} 秒")

def case2(rpc_clients: List[Client]):
    """
    Executes a test case for withdrawing funds from account 21 using multiple RPC clients.
    server 0: withdraw 800
    server 1: withdraw 800

    Args:
        rpc_clients (List[Client]): A list of RPC clients.

    Returns:
        None
    """
    
    start_time = time.perf_counter()
    
    print("------------test case 2-------------")
    res = rpc_clients[0].request({"cmd": "WITHDRAW", "aid": 21, "amount": 800})
    print(f"[account 21] WITHDRAW server 0 (- 800): {res}")
    res = rpc_clients[1].request({"cmd": "WITHDRAW", "aid": 21, "amount": 800})
    print(f"[account 21] WITHDRAW server 1 (- 800): {res}")
    time.sleep(0.3)
    print("-----------------")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 21})
    print(f"[account 21] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 21})
    print(f"[account 21] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 21})
    print(f"[account 21] CHECK server 2: {res}")
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"test case 2 耗时: {elapsed_time:.6f} 秒")

def case3(rpc_clients: List[Client]):
    """
    Executes a test case for withdrawing funds from account 21 using multiple RPC clients.
    server 0: withdraw 800
    server 1: withdraw 800

    Args:
        rpc_clients (List[Client]): A list of RPC clients.

    Returns:
        None
    """
    
    print("------------test case 3-------------")
    print(f"Time:0.0")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.1")
    start_time = time.perf_counter()
    res = rpc_clients[0].request({"cmd": "DEPOSIT", "aid": 22, "amount": 1000})
    print(f"[account 22] DEPOSIT server 0 (+ 1000): {res}")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"DEPOSIT 耗时: {elapsed_time:.6f} 秒")
    
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.2")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.3")
    # res = rpc_clients[1].request({"cmd": "INTEREST", "aid": 22})
    # print(f"[account 22] INTEREST server 1 (rate 0.04): {res}")
    
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.4")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.5")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.6")
    start_time = time.perf_counter()
    res = rpc_clients[0].request({"cmd": "WITHDRAW", "aid": 22, "amount": 100})
    print(f"[account 22] WITHDRAW server 0 (- 100): {res}")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"WITHDRAW 耗时: {elapsed_time:.6f} 秒")
    
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.7")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.8")
    res = rpc_clients[1].request({"cmd": "INTEREST", "aid": 22})
    print(f"[account 22] INTEREST server 1 (rate 0.04): {res}")
    
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:0.9")
    res = rpc_clients[0].request({"cmd": "WITHDRAW", "aid": 22, "amount": 100})
    print(f"[account 22] WITHDRAW server 1 (- 100): {res}")
    
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:1.0")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:1.1")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:1.2")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:1.3")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
    time.sleep(0.1)
    print(f"Time:1.4")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 22})
    print(f"[account 22] CHECK server 2: {res}")
    
def case4(rpc_clients: List[Client]):
    
    print("------------test case 4-------------")
    print(f"Time:0")
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    res = rpc_clients[2].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 2: {res}")
    
    time.sleep(1)
    print(f"Time:1")
    res = rpc_clients[0].request({"cmd": "DEPOSIT", "aid": 23, "amount": 20})
    print(f"[account 23] DEPOSIT server 0 (+ 20): {res}")
    res = rpc_clients[1].request({"cmd": "INTEREST", "aid": 23})
    print(f"[account 23] INTEREST server 1 (rate 0.05): {res}")
    
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:2")
    # res = rpc_clients[1].request({"cmd": "INTEREST", "aid": 23})
    # print(f"[account 23] INTEREST server 1 (rate 0.05): {res}")
    
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    
    time.sleep(1)
    print(f"Time:3")
    res = rpc_clients[1].request({"cmd": "WITHDRAW", "aid": 23, "amount": 60})
    print(f"[account 23] WITHDRAW server 1 (- 60): {res}")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:4")
    res = rpc_clients[0].request({"cmd": "WITHDRAW", "aid": 23, "amount": 70})
    print(f"[account 23] WITHDRAW server 0 (- 70): {res}")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:5")
    res = rpc_clients[1].request({"cmd": "DEPOSIT", "aid": 23, "amount": 10})
    print(f"[account 23] WITHDRAW server 1 (+ 10): {res}")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:6")
    res = rpc_clients[0].request({"cmd": "WITHDRAW", "aid": 23, "amount": 40})
    print(f"[account 23] WITHDRAW server 0 (- 40): {res}")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:7")
    res = rpc_clients[1].request({"cmd": "WITHDRAW", "aid": 23, "amount": 30})
    print(f"[account 23] WITHDRAW server 1 (- 30): {res}")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:8")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:9")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    
    time.sleep(1)
    print(f"Time:10")
      
    res = rpc_clients[0].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 0: {res}")
    res = rpc_clients[1].request({"cmd": "CHECK", "aid": 23})
    print(f"[account 23] CHECK server 1: {res}")
    


if __name__ == "__main__":
    clients = []
    for i in range(len(sys.argv) - 1):
        clients.append(Client(sys.argv[i + 1]))

    # case1(clients)
    # case2(clients)
    # case3(clients)
    case4(clients)
