import random
from burp import IBurpExtender, IntruderPayloadGeneratorFactory, IIntruderPayloadGenerator
from java.util import List, ArrayList

def banner():
print "###   Burp Fuzzer p79   ###"

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
	def registerExtenterCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		callbacks.registerIntruderPayloadGeneratorFactory(self)
		return

	def getGeneratorName(self):
		return "[***]   Payload Generator   [***]"

	def createNewInstance(self, attack):
		return BHPFuzzer(self, attack)

class BHPFuzzer(IIntruderPayloadGenerator):
	def __init__(self, extender, attack):
		self._extender = extender
		self._helpers = extender._helpers
		sefl._attack = attack
		self.max_payloads = 10
		self.num_iterations = 0
		return

	def hasMorePayloads(self):
		if self.num_iterations == self.max_payloads:
			return False
		else:
			return True

	def getNextPayload(self, current_payload):
		payload = "".join(chr(x) for x in current_payload)
		self.num_iterations +=1
		return payload

	def reset(self):
		self.num_iterations = 0
		return

	def mutate_payload(self, original_payload):
		picker = random.randint(1,3)
		offset = random.randint(0,len(original_payload)-1)
		payload = original_payload[:offset]
		if picker == 1:
			payload += "'"							#Insert SQL injection attempt
		if picker == 2:
			payload += "<script>alert('Goteem');</script>"		#insert XSS attempt
		if picker == 3:
			chunk_length = random.randint(leng(payload[offset:]),len(payload)-1)
			repeater = random.randint(1,10)
			for i in range(repeater):
				payload += original_payload[offset:offset+chunk_length]
		payload += original_payload[offset:]
		return payload


	

