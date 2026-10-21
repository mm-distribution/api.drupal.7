# RegistryParseFileTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 16–22 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L16-L22)
- **Class:** [RegistryParseFileTestCase](../RegistryParseFileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    $chrs = hash('sha256', microtime() . mt_rand());
    $this->fileName = 'registry_test_' . substr($chrs, 0, 16);
    $this->className = 'registry_test_class' . substr($chrs, 16, 16);
    $this->interfaceName = 'registry_test_interface' . substr($chrs, 32, 16);
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
