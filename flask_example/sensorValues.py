# Leitura de sensores grove
# Criado por Murilo Ferraz - 02/2016 - @muriloferraz125


import pyupm_grove as upm


def upm_light():
	light = upm.GroveLight(0) #Analog port A0
	upm_light = light.value()

	return upm_light


# Esta funcao retorna a temperatura
def upm_temp():

  temp = upm.GroveTemp(1) # Analog Port A1
	upm_temp = temp.value()
	upm_fahr = upm_temp * 9.0/5.0 + 32.0;

	return upm_temp
	#return upm_fahr;

#del light
#del temp
