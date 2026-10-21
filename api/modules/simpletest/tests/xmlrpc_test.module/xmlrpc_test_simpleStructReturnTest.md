# xmlrpc_test_simpleStructReturnTest()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 44–46 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L44-L46)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_simpleStructReturnTest($number)
```

## Documentation

_No docblock in source._

## Code

```php
function xmlrpc_test_simpleStructReturnTest($number) {
  return array("times10" => ($number*10), "times100" => ($number*100), "times1000" => ($number*1000));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
