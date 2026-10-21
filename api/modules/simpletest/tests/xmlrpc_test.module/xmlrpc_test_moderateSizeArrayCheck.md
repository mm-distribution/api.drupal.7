# xmlrpc_test_moderateSizeArrayCheck()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 36–38 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L36-L38)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_moderateSizeArrayCheck($array)
```

## Documentation

_No docblock in source._

## Code

```php
function xmlrpc_test_moderateSizeArrayCheck($array) {
  return array_shift($array) . array_pop($array);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
