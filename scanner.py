import nmap
import json
from datetime import datetime

def scan_target(target):
    nm = nmap.PortScanner()
    
    print(f"[+] Scanning {target} ... this may take a moment")
    nm.scan(target, arguments='-sV')
    

    scan_result = {
        "target": target,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hosts": []
    }
    
    for host in nm.all_hosts():
        host_data = {
            "ip": host,
            "hostname": nm[host].hostname(),
            "state": nm[host].state(),
            "protocols": {}
        }
        
        for proto in nm[host].all_protocols():
            ports_list = []
            ports = nm[host][proto].keys()
            
            for port in sorted(ports):
                port_info = {
                    "port": port,
                    "state": nm[host][proto][port]['state'],
                    "service": nm[host][proto][port]['name'],
                    "version": nm[host][proto][port].get('version', ''),
                    "product": nm[host][proto][port].get('product', '')
                }
                ports_list.append(port_info)
            
            host_data["protocols"][proto] = ports_list
        
        scan_result["hosts"].append(host_data)
    
    return scan_result


if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    result = scan_target(target)
    
    
    print("\n--- SCAN SUMMARY ---")
    print(json.dumps(result, indent=4))
    
    
    filename = f"scan_result_{target.replace('.', '_')}.json"
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4)
    
    print(f"\n[+] Results saved to {filename}")