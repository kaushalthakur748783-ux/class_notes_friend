[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK version
android.ndk = 25b

# (int) Android NDK API
android.ndk_api = 21

# Accept SDK license automatically
android.accept_sdk_license = True

# Bootstrap
p4a.bootstrap = sdl2

# Python version
android.python_version = 3.11

# Debug / Release artifact type
android.debug_artifact = apk
android.release_artifact = apk

[buildozer]

# Log level (2 = debug)
log_level = 2

# Warn if run as root
warn_on_root = 1
