#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2011 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.  Any Red Hat
# trademarks that are incorporated in the source code or documentation are not
# subject to the GNU General Public License and may only be used or replicated
# with the express permission of Red Hat, Inc. 
#
__all__ = ["F17Handler"]

from pykickstart import commands
from pykickstart.base import BaseHandler
from pykickstart.version import F17

class F17Handler(BaseHandler):
    version = F17

    commandMap = {
        "auth": commands.authconfig.FC3_Authconfig,
        "authconfig": commands.authconfig.FC3_Authconfig,
        "autopart": commands.autopart.F17_AutoPart,
        "autostep": commands.autostep.FC3_AutoStep,
        "bootloader": commands.bootloader.F17_Bootloader,
        "btrfs": commands.btrfs.F17_BTRFS,
        "cdrom": commands.cdrom.FC3_Cdrom,
        "clearpart": commands.clearpart.F17_ClearPart,
        "cmdline": commands.displaymode.FC3_DisplayMode,
        "device": commands.device.F8_Device,
        "deviceprobe": commands.deviceprobe.FC3_DeviceProbe,
        "dmraid": commands.dmraid.FC6_DmRaid,
        "driverdisk": commands.driverdisk.F14_DriverDisk,
        "fcoe": commands.fcoe.F13_Fcoe,
        "firewall": commands.firewall.F14_Firewall,
        "firstboot": commands.firstboot.FC3_Firstboot,
        "graphical": commands.displaymode.FC3_DisplayMode,
        "group": commands.group.F12_Group,
        "halt": commands.reboot.FC6_Reboot,
        "harddrive": commands.harddrive.FC3_HardDrive,
        "ignoredisk": commands.ignoredisk.F14_IgnoreDisk,
        "install": commands.upgrade.F11_Upgrade,
        "iscsi": commands.iscsi.F17_Iscsi,
        "iscsiname": commands.iscsiname.FC6_IscsiName,
        "keyboard": commands.keyboard.FC3_Keyboard,
        "lang": commands.lang.FC3_Lang,
        "logging": commands.logging.FC6_Logging,
        "logvol": commands.logvol.F17_LogVol,
        "mediacheck": commands.mediacheck.FC4_MediaCheck,
        "method": commands.method.F14_Method,
        "monitor": commands.monitor.F10_Monitor,
        "multipath": commands.multipath.FC6_MultiPath,
        "network": commands.network.F16_Network,
        "nfs": commands.nfs.FC6_NFS,
        "part": commands.partition.F17_Partition,
        "partition": commands.partition.F17_Partition,
        "poweroff": commands.reboot.FC6_Reboot,
        "raid": commands.raid.F15_Raid,
        "reboot": commands.reboot.FC6_Reboot,
        "repo": commands.repo.F15_Repo,
        "rescue": commands.rescue.F10_Rescue,
        "rootpw": commands.rootpw.F8_RootPw,
        "selinux": commands.selinux.FC3_SELinux,
        "services": commands.services.FC6_Services,
        "shutdown": commands.reboot.FC6_Reboot,
        "skipx": commands.skipx.FC3_SkipX,
        "sshpw": commands.sshpw.F13_SshPw,
        "text": commands.displaymode.FC3_DisplayMode,
        "timezone": commands.timezone.FC6_Timezone,
        "updates": commands.updates.F7_Updates,
        "upgrade": commands.upgrade.F11_Upgrade,
        "url": commands.url.F14_Url,
        "user": commands.user.F12_User,
        "vnc": commands.vnc.F9_Vnc,
        "volgroup": commands.volgroup.F16_VolGroup,
        "xconfig": commands.xconfig.F14_XConfig,
        "zerombr": commands.zerombr.F9_ZeroMbr,
        "zfcp": commands.zfcp.F14_ZFCP,
    }

    dataMap = {
        "BTRFSData": commands.btrfs.F17_BTRFSData,
        "DriverDiskData": commands.driverdisk.F14_DriverDiskData,
        "DeviceData": commands.device.F8_DeviceData,
        "DmRaidData": commands.dmraid.FC6_DmRaidData,
        "FcoeData": commands.fcoe.F13_FcoeData,
        "GroupData": commands.group.F12_GroupData,
        "IscsiData": commands.iscsi.F17_IscsiData,
        "LogVolData": commands.logvol.F17_LogVolData,
        "MultiPathData": commands.multipath.FC6_MultiPathData,
        "NetworkData": commands.network.F16_NetworkData,
        "PartData": commands.partition.F17_PartData,
        "RaidData": commands.raid.F15_RaidData,
        "RepoData": commands.repo.F15_RepoData,
        "SshPwData": commands.sshpw.F13_SshPwData,
        "UserData": commands.user.F12_UserData,
        "VolGroupData": commands.volgroup.F16_VolGroupData,
        "ZFCPData": commands.zfcp.F14_ZFCPData,
    }
