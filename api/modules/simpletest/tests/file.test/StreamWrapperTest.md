# StreamWrapperTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 2981–3116 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2981-L3116)
- **Module/theme:** batch_test

## Signature

```php
class StreamWrapperTest extends DrupalWebTestCase
```

## Documentation

```text
Tests stream wrapper functions.
```

## Properties

### $scheme

```php
protected $scheme = 'dummy';
```

### $classname

```php
protected $classname = 'DrupalDummyStreamWrapper';
```

## Methods (derived index)

- [getInfo()](StreamWrapperTest/getInfo.md)
- [setUp()](StreamWrapperTest/setUp.md)
- [tearDown()](StreamWrapperTest/tearDown.md)
- [testGetClassName()](StreamWrapperTest/testGetClassName.md) — Test the getClassName() function.
- [testGetInstanceByScheme()](StreamWrapperTest/testGetInstanceByScheme.md) — Test the file_stream_wrapper_get_instance_by_scheme() function.
- [testUriFunctions()](StreamWrapperTest/testUriFunctions.md) — Test the URI and target functions.
- [testGetValidStreamScheme()](StreamWrapperTest/testGetValidStreamScheme.md) — Test the scheme functions.
- [testPharStreamWrapperRegistration()](StreamWrapperTest/testPharStreamWrapperRegistration.md) — Tests that phar stream wrapper is registered as expected.
- [testPharFile()](StreamWrapperTest/testPharFile.md) — Tests that only valid phar files can be used.

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
