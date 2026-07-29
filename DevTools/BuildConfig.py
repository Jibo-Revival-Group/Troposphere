# ========================================== #
# Troposphere Build config
#

# System General

Include_Init_dir = False#Includes a Init configuration with pre set files... Can break some older versions
Include_JiboPackageManager = False#Bundle Jibo package manager (Grabs from git)
Include_JiboBinaryWrappers = False#Bundle Wrappers for the jibo binaries inside the chroot

Troposphere_Splash = "%/splash_0.png" #Set the Troposphere boot splash
Setup_Init_Entry = True #If you wanna do everything manually leave this off
Setup_Init_Startup_Entry = True #If you want troposphere to start with the system


# System patches
Include_Faster_Boot_Configs = True #Change with patches to make startup times faster & async!

# Really leave this as is pls

Include_stdlib = True #Installs standard libraries on first boot
Include_TroposphereLib = True #Bundles Troposphere lib

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


# Init.d Files to replace (Under Faster Boot Configs):

Staged_Init_FBC = [
        "S09wifi-enable",
        "S18udev",
        "S36sshd",
        "rcS"
        ]

if Include_JiboBinaryWrappers:
    Staged_Jibo_Binary_Wrappers = []

