# xmlrpc_test_nestedStructTest()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 40–42 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L40-L42)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_nestedStructTest($array)
```

## Documentation

_No docblock in source._

## Code

```php
function xmlrpc_test_nestedStructTest($array) {
  return $array["2000"]["04"]["01"]["larry"] + $array["2000"]["04"]["01"]["moe"] + $array["2000"]["04"]["01"]["curly"];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
