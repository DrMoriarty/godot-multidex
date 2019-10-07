def can_build(env, platform):
	if platform == "android":
		return True
	return False

def configure(env):
	if (env['platform'] == 'android'):
		env.android_add_to_attributes("android/AndroidManifestAttributeChunk.xml")
		env.android_add_dependency("implementation 'androidx.multidex:multidex:2.0.0'")
		env.android_add_default_config("multiDexEnabled true")
		env.disable_module()

