Coding task
===

#### Notes

For really long strings conversion there is no `<long>` type, since Python 3, interpreter handles big integers internally.

Constructing parametrized tests in `unittest` library involves hacking with decorators and method patching that will probably lead to writing tests for my tests. I didn't know whether I may use a `pytest` lib, so there are no neat "PASSED" status output for each subtest (only traceback for "FAILED").
