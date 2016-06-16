#!/usr/bin/python
import sys

level_to_priority = {
    'V': 0,
    'D': 1,
    'I': 2,
    'W': 3,
    'E': 4,
    'F': 5
}

exclude = {
    'E': [
        'WifiStateMachine',
        'WifiAutoJoinController',
        'WifiConfigStore',
        'WifiTrafficPoller',
        'WifiMonitor',
        'MtpServer',
        'ctxmgr',
        'Sensors',

        'LockPatternUtils',
        'GsmCellLocation',
        'CellLocation',
        'PhoneUtils',
        'NetworkTimeUpdateService',

        'SCREENCOLOR_JNI',
        'DropBox',
        'com.miui.',
        'com.facebook.',
        'Miui',
        'YellowPage',

        'MPlugin',
        'NativeCrypto',
        'MNLD',

        # prefixes
        'Audio',
        'Proximity',
        'Bluetooth',
        'Media',
        'usb',

    ],


    'W': [
        'Watchdog',
        'AlarmManager',
        'ADB_SERVICES',
        'ContextImpl',
        'BroadcastQueueInjector',
        'PushService',
        'ResourcesManager',
        'NetworkStatsRecorder',
        'ActivityManager',
        'PhoneNumberUtil',
        'fpc_hal',
        'fpcCORE',
        'fpc_tac',
        'fpc_lib',
        'FingerprintFPCImpl',
        'GAv4-SVC',
        'OldPhoneNumberUtils(',
        'Tethering(',
        'InputMethodManagerService(',

        'ProgressBarDelegate',
        'ProgressBar',
        'MtkAgpsNative',


        'InputDispatcher',
        'libdecode',
        'AEE',


        'System.out',
        'System.err',
    ],

    'V': [
        'AlarmManager',
        'LocationPolicy',
        'SettingsInterface',
        'MiCloudSyncStateService',
        'GoogleSignatureVerifier('
    ],

    'I': [
        'ANRManager', 
        'thermal_repeater',
        'memtrack_graphic',
        'WifiNotificationController',
        'wifiJNI',
        'XiaomiFirewall',
        'UploadManager',
        'Netd',
        'wpa_supplicant',
        'BufferQueueProducer',
        'SurfaceFlinger',
        'libPerfService',
        'ClearcutLoggerApiImpl',
        'EventLogChimeraService',
        'PerfService',
        'AP_PROF',
        'RenderThread',
        'ProcessStatsService',
        'WindowManager',
        'BufferQueueConsumer',
        'DisplayManagerService',
        'LocalDisplayAdapter',
        'SurfaceView',
        'InputMethodManager',
        'DisplayPowerController',
        'DisplayFeatureManager',
        'PowerManagerService',
        'UsageStatsService',
        'NetworkPolicy',
        'hwcomposer',
        'KeyLayoutMap',
        'KeyEvent',
        'Timeline',
        'SettingsInterface',
        'OpenGLRenderer',
        'WindowState',
        'WifiManager',
        'Beacon',
        'LocationManagerService',



        'BufferQueue',

        'art',


    ],

    'D': [
        'WifiController',
        'WifiService',
        'PowerManagerService',
        'InputReader',
        'NetworkManagementService'
        'SocketClient',
        'MNLD',
        'gps_mtk',
        'BatteryService',
        'NetworkManagementService',
        'SocketClient',
        'WifiDisplayAdapter',
        'PowerManagerNotifier',
        'ActivityThread',
        'DisplayPowerController',
        'libc-netbsd',
        'ccci_fsd',
        'PhoneInterfaceManager',
        'ListView',
        'SizeAdaptiveLayout',
        'WifiHW',
        'UsbDeviceManager',
        'LocationFilter',
        'AES',
        'FrameworkListener',
        'StatusBar.NetworkController',
        'SupplicantStateTracker',
        'Tethering',
        'WifiWatchdogStateMachine',
        '[BT3.0+HS]PAL',
        'SensorService',
        'Accel',
        'wifi2agps',
        'agps',
        'SQLiteDatabase',
        'NativeCrypto',
        'DisplayManagerService',
        'DisplayPowerState',
        'lights',
        'AbsListView',
        'PerfServiceManager',
        'CountryDetector',
        'SettingsProvider',
        'ConnectivityManager.CallbackHandler',
        'PhoneApp',
        'Nat464Xlat',
        'AALService',
        'LightsService',
        'WallpaperService',
        'FingerprintService',
        'PhoneStatusBar',
        'IMGSRV',
        'GraphicBuffer',
        'ScreenElementRoot',
        'Hwmsen_sensors',
        'PROXIMITY',
        'Hwmsen_sensors',
        'NetworkStats',
        'StatusBarManagerService',
        'GpsLocationProvider',
        'ColorDrawable',
        'PowerKeeper',
        'WhetstoneService',
        'LifecycleResourceManager',
        'FancyDrawable',
        'MultipleRenderable',
        'RendererCore',
        'Posix',
        'nlp_service',
        'mnl_linux',
        'MtkAudioLoud',
        'MtkAudioBitConverter',
        'NVRAM',
        'NotificationService',
        'ZenLog',

        'PreferenceGroup(',
        'Preference(',
        'PreferenceActivity(',

        'skia',
        'BitmapRegionDecoder',

        'OpenGL',


    ],

}

for line in sys.stdin:
    try:
        skip = False
    
        line_priority = level_to_priority[line[0]]

        for level, items in exclude.iteritems():
            priority = level_to_priority[level]

            if line_priority <= priority:
                for item in items:
                    if line.startswith(item, 2): skip = True

    except KeyError as e:
        skip = False        # just print as is

    if not skip:
        sys.stdout.write(line)




