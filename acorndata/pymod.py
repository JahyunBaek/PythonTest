from pymodbus.client import ModbusTcpClient
from pymodbus.client import AsyncModbusTcpClient
import func

# asyncClient = AsyncModbusTcpClient(host='gjl2.iptime.org',port=504,unit_id=1)

client = ModbusTcpClient(host='gjl2.iptime.org',port=504,unit_id=1)   # Create client object
client.connect()                           # connect to device, reconnect automatically
#client.write_coil(1, True, slave=1)        # set information in device
result = client.read_holding_registers(40009, 1)  # get information from device
print(result.registers)                      # use information

client.close()                             # Disconnect device



