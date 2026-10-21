# xmlrpc_test_arrayOfStructsTest()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 3–11 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L3-L11)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_arrayOfStructsTest($array)
```

## Documentation

_No docblock in source._

## Code

```php
function xmlrpc_test_arrayOfStructsTest($array) {
  $sum = 0;
  foreach ($array as $struct) {
    if (isset($struct['curly'])) {
      $sum += $struct['curly'];
    }
  }
  return $sum;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
