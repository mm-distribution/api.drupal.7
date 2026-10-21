# xmlrpc_test_countTheEntities()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 13–21 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L13-L21)
- **Module/theme:** batch_test

## Signature

```php
function xmlrpc_test_countTheEntities($string)
```

## Documentation

_No docblock in source._

## Code

```php
function xmlrpc_test_countTheEntities($string) {
  return array(
    'ctLeftAngleBrackets' => substr_count($string, '<'),
    'ctRightAngleBrackets' => substr_count($string, '>'),
    'ctAmpersands' => substr_count($string, '&'),
    'ctApostrophes' => substr_count($string, "'"),
    'ctQuotes' => substr_count($string, '"'),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
