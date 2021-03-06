"""
d_plugins
    use example
    plugin: {
        "object": "", 
        "method": [],
        "property": [],
        "event": [],  
    }

"""

d_plugins = {
    # // We get the initial value when the promise resolves ...
    # navigator.getBattery().then(function(battery) {
    # console.log(battery.level);
    # // ... and any subsequent updates.
    # battery.onlevelchange = function() {
    #     console.log(this.level);
    # };
    # });
    "battery": {
        "object": "navigator.getBattery",
        "method": [],
        "property": [],
        "event": [],
    },
    # navigator.camera.getPicture(cameraSuccess, cameraError, cameraOptions);
    "camera": {
        "object": "navigator.camera",
        "method": ["getPicture", "cleanup", "onError", "onSuccess", "CameraOptions"],
        "property": [],
        "event": [],
    },
    # var string = device.platform;
    "device": {
        "object": "device",
        "method": [],
        "property": [
            "cordova",
            "model",
            "platform",
            "uuid",
            "version",
            "manufacturer",
            "isVirtual",
            "serial",
        ],
        "event": [],
    },
    "dialogs": {
        "object": "navigator.notification",
        "method": [
            "alert",
            "confirm",
            "prompt",
            "beep",
            "dismissPrevious",
            "dismissAll",
        ],
        "property": [],
        "event": [],
    },
    # document.addEventListener("deviceready", onDeviceReady, false);
    # function onDeviceReady() {
    #     console.log(cordova.file);
    # }
    # TODO - Android file 
    "file": {
        "object": "cordova.file",
        "method": [
            "resolveLocalFileSystemURL",
            "applicationDirectory",
            "applicationStorageDirectory",
            "dataDirectory",
            "cacheDirectory",
            "externalApplicationStorageDirectory",
            "externalDataDirectory",
            "externalCacheDirectory",
            "externalRootDirectory",
            "tempDirectory",
            "syncedDataDirectory",
            "documentsDirectory",
            "sharedDirectory",
        ],
        "property": [],
        "event": [],
    },
    # navigator.geolocation.getCurrentPosition(geolocationSuccess, [geolocationError], [geolocationOptions]);
    "geolocation": {
        "object": "navigator.geolocation",
        "method": ["getCurrentPosition", "watchPosition", "clearWatch"],
        "property": [],
        "event": [],
    },
    # var ref = cordova.InAppBrowser.open('http://apache.org', '_blank', 'location=yes');
    # var iab = cordova.InAppBrowser;
    # iab.open('local-url.html'); // loads in the Cordova WebView
    "InAppBrowser": {
        "object": "cordova.InAppBrowser",
        "method": ["open"],
        "property": [],
        "event": [],
    },
    # var my_media = new Media(src, onSuccess, onError);
    # my_media.startRecord();
    "media": {
        "object": "Media",
        "method": [
            "getCurrentAmplitude",
            "getCurrentPosition",
            "getDuration",
            "play",
            "pause",
            "pauseRecord",
            "release",
            "resumeRecord",
            "seekTo",
            "setVolume",
            "startRecord",
            "stopRecord",
            "stop",
            "setRate",
        ],
        "property": [],
        "event": [],
    },
    # navigator.device.capture.captureVideo(captureSuccess, captureError, {limit:2});
    "media-capture": {
        "object": "navigator.device.capture",
        "method": ["captureAudio", "captureImage", "captureVideo"],
        "property": [],
        "event": [],
    },
    # var networkState = navigator.connection.type;
    "network-information": {
        "object": "navigator.connection",
        "method": [],
        "property": ["type"],
        "event": [],
    },
    # // set to either landscape
    # screen.orientation.lock('landscape');
    # // allow user rotate
    # screen.orientation.unlock();
    # // access current orientation
    # console.log('Orientation is ' + screen.orientation.type);
    "screen-orientation": {
        "object": "screen.orientation",
        "method": ["lock", "unlock"],
        "property": ["type"],
        "event": [],
    },
    # setTimeout(function() {
    #   navigator.splashscreen.hide();
    # }, 2000);
    "splashscreen": {
        "object": "navigator.splashscreen",
        "method": ["show", "hide"],
        "property": [],
        "event": [],
    },
    # StatusBar.overlaysWebView(true);
    # if (StatusBar.isVisible) {
    # // do something
    # }
    "statusbar": {
        "object": "StatusBar",
        "method": [
            "overlaysWebView",
            "styleDefault",
            "styleLightContent",
            "styleBlackTranslucent",
            "styleBlackOpaque",
            "backgroundColorByName",
            "backgroundColorByHexString",
            "hide",
            "show",
        ],
        "property": ["isVisible"],
        "event": ["statusTap"],
    },
    # document.addEventListener("deviceready", onDeviceReady, false);
    # function onDeviceReady() {
    #     console.log(navigator.vibrate);
    # }
    "vibration": {
        "object": "navigator.vibrate",
        "method": [],
        "property": [],
        "event": [],
    },
}

# TODO - Redesign get event, method, object


def get_func():
    # return all functions(["method", "property", "event"]) of all plugins as one list
    # [plugin1.function1, plugin1.function2, ..., ]
    l_func = []
    values = ["method", "property", "event"]
    for funcs in d_plugins.values():
        plugin_obj = funcs["object"]
        for v in values:
            for func in funcs[v]:
                l_func.append[f"{plugin_obj}.{func}"]
    return l_func


def get_plugin():
    # return all plugins as a list
    # [plugin1, plugin2, ]
    return d_plugins.keys()

def get_object():
    # return object of API call as a list:
    return [v["object"] for v in d_plugins.values()]

def get_plugin_func():
    # return all functions(method, propert, event) and plugins as one list
    # [plugin1_function1, plugin1_function2, ..., plugin1, ... plugin]
    l_plugins_func = []
    for plugin, funcs in d_plugins.items():
        l_plugins_func.extend(funcs)
        l_plugins_func.append(plugin)
    return l_plugins_func


def get_func_plugin_dict():
    # Todo - some plugin might have the same function name
    # return a dict of func and plugin pair
    # {function: plugin}
    d_func_plugin = {
        func: plugin for plugin, funcs in d_plugins.items() for func in funcs
    }
    return d_func_plugin