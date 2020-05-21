from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import RpcError
from jnpr.junos.utils.config import Config
from lxml import etree as etree

host_ip_list = ['192.168.1.35','192.168.1.36']
Router_Phy = ['42.7.1.1/24','42.7.1.2/24']
Router_loop = ['42.7.10.1/24','42.7.20.1/24']

for i in range(2):
	device = Device(host=host_ip_list[i], user='labuser', password='Labuser', normalize=True)
	if_config = {'ge-0/0/1': Router_Phy[i],'lo0':Router_loop[i]}
	if_config_check = {'ge-0/0/1': '','lo0' : 'passive' }

	

	var_dict = {'if_config':if_config, 'if_config_check': if_config_check}
                             
	try:
		device.open()
		device.bind(conf=Config)
		device.conf.load(template_path='template_rip.conf', template_vars = var_dict, merge = True)
		if host_ip_list[i] == "192.168.1.35":
			device.conf.load(template_path='template_ffw.conf', template_vars = var_dict, merge = True)
		
		success = device.conf.commit()
		print("Success : {}".format(success))
		
	except (RpcError, ConnectError) as err:
		print("\nError: " + repr(err))

	finally:
		device.close()






