import ftplib
max_attempts = 5
for i in range(1, max_attempts + 1):
    try:
        with ftplib.FTP(ROS_MGMT_ADDR, self.username, self.password) as session:
            with open(CONFIG_FILE, "rb") as file:  # file to send
                session.storbinary("STOR config.auto.rsc", file)
    except:
        pass

for i in range(1, max_attempts + 1):
    try:
        with ftplib.FTP_TLS(ROS_MGMT_ADDR, self.username, self.password) as session:
            with open(CONFIG_FILE, "rb") as file:  # file to send
                session.storbinary("STOR config.auto.rsc", file)
    except:
        pass