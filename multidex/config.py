def can_build(env, platform):
	if platform == "android":
		return True
	return False

def configure(env):
	if (env['platform'] == 'android'):
		env.android_add_to_attributes("android/AndroidManifestAttributeChunk.xml")
		env.android_add_dependency("compile 'com.android.support:multidex:1.0.1'")
		env.android_add_default_config("multiDexEnabled true")
		#env.android_add_default_config("applicationId 'free.games.match.three.puzzle.galactic.adventure_2.android'")
		env.disable_module()

