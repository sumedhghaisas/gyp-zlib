{
  'variables': { 'target_arch%': 'ia32' },

  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },
    'include_dirs': [
       # platform and arch-specific headers
       '../config/<(OS)/<(target_arch)'
     ],
  },

  "targets": [
        {
            "target_name": "zlib",
	    #'product_prefix': 'lib',
            "type": "static_library",
            "include_dirs": [
                "../zlib"
            ],
             'sources': [
				'../zlib/adler32.c',
				'../zlib/compress.c',
				'../zlib/crc32.c',
				'../zlib/deflate.c',
				'../zlib/gzclose.c',
				'../zlib/gzlib.c',
				'../zlib/gzread.c',
				'../zlib/gzwrite.c',
				'../zlib/infback.c',
				'../zlib/inffast.c',
				'../zlib/inflate.c',
				'../zlib/inflate.h',
				'../zlib/inftrees.c',
				'../zlib/trees.c',
				'../zlib/uncompr.c',
				'../zlib/zutil.c',
			],
        }
    ]
}
