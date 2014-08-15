import _bcm2835 as soc
##import libbcm2835._bcm2835 as soc

PIN=17
soc.bcm2835_set_debug(1)
##soc.bcm2835_init()

##soc.bcm2835_gpio_fsel(PIN, soc.BCM2835_GPIO_FSEL_OUTP)

# // Turn it on
##soc.bcm2835_gpio_write(PIN, 1);
#// wait a bit
#soc.bcm2835_delay(500);
#// turn it off
##soc.bcm2835_gpio_write(PIN, 0);
#// wait a bit
#soc.bcm2835_delay(500);

##soc.bcm2835_close();

##print(soc.BCM2835_I2C_REASON_OK)
