{
  "targets": [
    {
      "target_name": "fasttext",
      "sources": [
        "fastText/src/args.cc",
        "fastText/src/args.h",
        "fastText/src/dictionary.cc",
        "fastText/src/dictionary.h",
        "fastText/src/fasttext.cc",
        "fastText/src/fasttext.h",
        "fastText/src/matrix.cc",
        "fastText/src/matrix.h",
        "fastText/src/model.cc",
        "fastText/src/model.h",
        "fastText/src/productquantizer.cc",
        "fastText/src/productquantizer.h",
        "fastText/src/qmatrix.cc",
        "fastText/src/qmatrix.h",
        "fastText/src/real.h",
        "fastText/src/utils.cc",
        "fastText/src/utils.h",
        "fastText/src/vector.cc",
        "fastText/src/vector.h",
        "src/classifier.h",
        "src/classifierWorker.cc",
        "src/query.h",
        "src/nnWorker.cc",
        "src/wrapper.cc",
        "src/fasttext.cc"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      "cflags_cc": ['-O3', '-Wall', '-pedantic', '-std=c++11', '-fexceptions', '-DUSE_SSE', '-DUSE_SSE2'],
      "conditions": [
            ["OS==\"mac\"", {
                "xcode_settings": {
                    "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
                }
            }]
        ],
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": ["<(module_name)"],
      "copies": [{
          "files": ["<(PRODUCT_DIR)/<(module_name).node"],
          "destination": "<(module_path)"
      }]
    }
  ]
}