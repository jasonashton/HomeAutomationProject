print("ESP Running!")
wifi.setmode(wifi.STATION)
wifi.sta.config("Ashton Wireless","ashton0919")

gpio.mode(3,gpio.OUTPUT)
-- create a server
sv=net.createServer(net.TCP, 30)    -- 30s time out for a inactive client
print("Starting Server")
-- server listen on 23, if data received, print data to console, and send "hello world" to remote.
sv:listen(23,function(c)
    --c:send("Connection Successful\n")
    c:on("receive", function(c, payload) print(payload)
    pinstate = tostring(payload) 
    --c:send("You said: " .. pinstate .. "\n")
    
    if pinstate == "on" then gpio.write(3,gpio.HIGH) elseif pinstate == "off" then gpio.write(3,gpio.LOW) end
    end)
    end)
