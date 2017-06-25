def can_build(plat):
	return plat=="android"

def configure(env):
	if (env['platform'] == 'android'):
		#env.android_add_java_dir("android/src/")
		env.android_add_to_attributes("android/AndroidManifestAttributeChunk.xml")
		env.android_add_dependency("compile 'com.android.support:multidex:1.0.1'")
		env.android_add_default_config("multiDexEnabled true")
		env.disable_module()

