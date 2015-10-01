'use strict';
var zlib = require('./build/Release/zlib_test');
var expect = require('chai').expect;

describe('functionality', function() {

    describe('zlib_func_test', function() {

        it('should be able to compress the test string', function() {
            var result = zlib.zlibTest();
            expect(result).to.eql(0);
        });
    });
});