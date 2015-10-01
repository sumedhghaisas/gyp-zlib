{    
    'targets': [
    {
      'target_name': 'zlib_test',
      'dependencies': [
        '../bindings/zlib.gyp:zlib'
      ],
      'sources': [
         'example.c',
      ],
      "include_dirs": [
        "../zlib",
	"../config/<(OS)/<(target_arch)"
      ],
    }
  ]
}
