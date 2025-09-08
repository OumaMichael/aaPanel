# coding: utf-8
# +-------------------------------------------------------------------
# | aaPanel Telemetry Module
# +-------------------------------------------------------------------
# | Copyright (c) 2015-2099 aaPanel(www.aapanel.com) All rights reserved.
# +-------------------------------------------------------------------
# | Author: AI Assistant
# +-------------------------------------------------------------------

import psutil
import json
import time
import os
import public
from datetime import datetime


class Telemetry:
    def __init__(self):
        self.start_time = time.time()

    def get_system_info(self):
        """Get basic system information"""
        try:
            return {
                'cpu_count': psutil.cpu_count(),
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory_total': psutil.virtual_memory().total,
                'memory_used': psutil.virtual_memory().used,
                'memory_percent': psutil.virtual_memory().percent,
                'disk_total': psutil.disk_usage('/').total,
                'disk_used': psutil.disk_usage('/').used,
                'disk_percent': psutil.disk_usage('/').percent,
                'uptime': int(time.time() - psutil.boot_time()),
                'load_average': os.getloadavg() if hasattr(os, 'getloadavg') else None
            }
        except Exception as e:
            return {'error': str(e)}

    def get_panel_info(self):
        """Get aaPanel specific information"""
        try:
            panel_info = {
                'version': self.get_panel_version(),
                'sites_count': public.M('sites').count(),
                'databases_count': public.M('databases').count(),
                'ftp_count': public.M('ftps').count(),
                'tasks_count': public.M('task_list').count(),
                'plugins_count': len(self.get_installed_plugins()),
                'server_time': datetime.now().isoformat()
            }
            return panel_info
        except Exception as e:
            return {'error': str(e)}

    def get_panel_version(self):
        """Get aaPanel version"""
        try:
            version_file = '/www/server/panel/version.pl'
            if os.path.exists(version_file):
                with open(version_file, 'r') as f:
                    return f.read().strip()
            return 'unknown'
        except:
            return 'unknown'

    def get_installed_plugins(self):
        """Get list of installed plugins"""
        try:
            plugin_dir = '/www/server/panel/plugin'
            if os.path.exists(plugin_dir):
                return [d for d in os.listdir(plugin_dir) if os.path.isdir(os.path.join(plugin_dir, d))]
            return []
        except:
            return []

    def get_network_info(self):
        """Get network interface information"""
        try:
            network_info = {}
            for interface, stats in psutil.net_if_addrs().items():
                network_info[interface] = {
                    'addresses': [{'address': addr.address, 'netmask': addr.netmask, 'broadcast': addr.broadcast}
                                for addr in stats if addr.address]
                }
            return network_info
        except Exception as e:
            return {'error': str(e)}

    def get_process_info(self):
        """Get process information for key services"""
        try:
            processes = []
            key_processes = ['nginx', 'apache', 'mysql', 'php', 'redis', 'mongodb', 'postgresql']

            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    if any(key in proc.info['name'].lower() for key in key_processes):
                        processes.append({
                            'pid': proc.info['pid'],
                            'name': proc.info['name'],
                            'cpu_percent': proc.info['cpu_percent'],
                            'memory_percent': proc.info['memory_percent']
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            return processes[:10]  # Limit to top 10 processes
        except Exception as e:
            return {'error': str(e)}

    def collect_telemetry_data(self):
        """Collect all telemetry data"""
        return {
            'timestamp': datetime.now().isoformat(),
            'system': self.get_system_info(),
            'panel': self.get_panel_info(),
            'network': self.get_network_info(),
            'processes': self.get_process_info(),
            'collection_time': time.time() - self.start_time
        }

    def get_telemetry_report(self, get=None):
        """Generate telemetry report"""
        try:
            data = self.collect_telemetry_data()

            # Format the response
            result = {
                'status': True,
                'data': data,
                'message': 'Telemetry data collected successfully'
            }

            return public.getJson(result)
        except Exception as e:
            return public.returnJson(False, 'Failed to collect telemetry data: ' + str(e))

    def export_telemetry_data(self, get=None):
        """Export telemetry data to file"""
        try:
            data = self.collect_telemetry_data()
            filename = f'/tmp/telemetry_report_{int(time.time())}.json'

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)

            return public.returnJson(True, f'Telemetry data exported to {filename}')
        except Exception as e:
            return public.returnJson(False, 'Failed to export telemetry data: ' + str(e))
