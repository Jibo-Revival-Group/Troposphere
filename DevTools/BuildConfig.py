# ========================================== #
# Troposphere Build config
#

# System Files

Include_Init_dir = True

# System patches
Include_Faster_Boot_Configs = True

# Really leave this as is pls

Include_stdlib = True
Include_TroposphereLib = True

# Root Mout Endpoints
Mount_Bind = [
        "dev/pts:STD",
        "tmpfs:ALL",
        "dev/shm:STD",
        "dev:STD",
        
        ]


# Device Cofig:
Mount_Devices = [
        "tmpfs:ALL"
        ]





