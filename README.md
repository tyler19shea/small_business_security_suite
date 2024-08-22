# small_business_security_suite


## Setting up Grafana Dashboard for Monitoring
### Install Grafana on Linux
#### Step 1: Add Grafana APT Repository
Install dependencies:
```
sudo apt-get install -y software-properties-common
```
Add the Grafana APT repository:
```
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
```
Add Grafana’s GPG key:
```
sudo wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```
Update your package lists:
```
sudo apt-get update
```
#### Step 2: Install Grafana

```
sudo apt-get install grafana
```
#### Step 3: Start and Enable Grafana Service
```
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```
#### Step 4: Verify Grafana Installation

Open your browser and navigate to http://localhost:3000.
You should see the Grafana login page. The default login is admin for both the username and password.

### Install Prometheus on Linux Machine

https://medium.com/@abdullah.eid.2604/prometheus-installation-on-linux-ubuntu-c4497e5154f6

### Install Windows Exporter on all machines to monitor via Grafana
navigate to this page and download the exe file and run it. Ensure to configure the Exporter to prometheus server running on your linux machine. 

https://github.com/prometheus-community/windows_exporter/releases

This will server the metrics on http://localhost:9182/metrics. If you navigate to the page and it doesnt display a page with various metrics ensure windows_exporter.exe is running and ensure that you have administrative permissions to install and run the exporter.

Ensure the firewall on the Windows machine allows trafiic on port 9182. On another machine on the same network type http://"WindowsMachineIP":9182/metircs


### Connect Grafana to Prometheus
Create a new dashboard and while choosing the data source select prometheus, specifically your prometheus server. Typically will be http://localhost:9090.


