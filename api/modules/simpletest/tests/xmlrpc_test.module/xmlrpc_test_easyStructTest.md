# xmlrpc_test_easyStructTest()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 23–25 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L23-L25)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_easyStructTest($array)
```

## Documentation

_No docblock in source._

## Code

```php
function xmlrpc_test_easyStructTest($array) {
  return $array["curly"] + $array["moe"] + $array["larry"];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
