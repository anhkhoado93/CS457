import sys
from time import time
import struct
HEADER_SIZE = 12

class RtpPacket:	
	header = bytearray(HEADER_SIZE)
	
	def __init__(self):
		pass
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields
		
		# header[0] = ...
		# ...
		header[0] = 2 << 7
		header[1] = 26
		header[2] = seqnum & int('ff00', 16)
		header[3] = seqnum & int('00ff', 16)
		header[4] = time() & int('ff000000', 16)
		header[5] = time() & int('00ff0000', 16)
		header[6] = time() & int('0000ff00', 16)
		header[7] = time() & int('000000ff', 16)
		header[8] = ssrc & int('ff000000', 16)
		header[9] = ssrc & int('00ff0000', 16)
		header[10] = ssrc & int('0000ff00', 16)
		header[11] = ssrc & int('000000ff', 16)


		
		# Get the payload from the argument
		# self.payload = ...
		
	def decode(self, byteStream):
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		"""Return payload."""
		return self.payload
		
	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload