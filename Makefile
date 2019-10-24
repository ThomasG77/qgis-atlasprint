# Name of the plugin, for the ZIP file
PLUGINNAME = atlasprint

help:
	$(MAKE) -C qgis_plugin_tools help

docker_test:
	$(MAKE) -C qgis_plugin_tools docker_test PLUGINNAME=$(PLUGINNAME)

docker_server_test:
	$(MAKE) -C qgis_plugin_tools docker_server_test PLUGINNAME=$(PLUGINNAME)

release_%:
	$(MAKE) -C qgis_plugin_tools release_$* PLUGINNAME=$(PLUGINNAME)