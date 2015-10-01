#include <iostream>
#include <string>

#include <v8.h>
#include <node.h>

using namespace std;
using namespace v8;

extern "C" int zlib_test();

void zlib_test_wrap(const FunctionCallbackInfo<v8::Value>& args)
{
  v8::Isolate* isolate;
  isolate = args.GetIsolate();
  int status = zlib_test();
  Local<Number> out = Number::New(isolate, status);
  args.GetReturnValue().Set(out);
}

void init(Handle<Object> exports)
{
  Isolate* isolate = v8::Isolate::GetCurrent();
  exports->Set(String::NewFromUtf8(isolate, "zlibTest", v8::String::kInternalizedString),
      FunctionTemplate::New(isolate, zlib_test_wrap)->GetFunction());
}

NODE_MODULE(zlib_test, init)

