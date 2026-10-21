# xmlrpc_test_manyTypesTest()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 31–34 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L31-L34)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_manyTypesTest($number, $boolean, $string, $double, $dateTime, $base64)
```

## Documentation

_No docblock in source._

## Code

```php
function xmlrpc_test_manyTypesTest($number, $boolean, $string, $double, $dateTime, $base64) {
  $timestamp = gmmktime($dateTime->hour, $dateTime->minute, $dateTime->second, $dateTime->month, $dateTime->day, $dateTime->year);
  return array($number, $boolean, $string, $double, xmlrpc_date($timestamp), xmlrpc_Base64($base64));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
