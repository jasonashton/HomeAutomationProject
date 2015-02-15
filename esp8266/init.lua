print("ESP Running!")
wifi.setmode(wifi.STATION)
wifi.sta.config("Ashton Wireless","ashton0919")

pin = 5

gpio.mode(pin,gpio.OUTPUT)
gpio.write(pin,gpio.HIGH)
tmr.delay(500000)
gpio.write(pin,gpio.LOW)

-- create a server
sv=net.createServer(net.TCP, 30)    -- 30s time out for a inactive client
print("Starting Server")
-- server listen on 23, if data received, print data to console, and send "hello world" to remote.
sv:listen(23,function(c)
    c:send("Connection Successful\n")
    c:on("receive", function(c, payload) print(payload)
    pinstate = tostring(payload) 
    c:send("You said: " .. pinstate .. "\n")
    
    if pinstate == "on" then gpio.write(pin,gpio.HIGH) elseif pinstate == "off" then gpio.write(pin,gpio.LOW) end
    end)
    end)
