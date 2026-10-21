# XMLRPCBasicTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 8–14 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L8-L14)
- **Class:** [XMLRPCBasicTestCase](../XMLRPCBasicTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name'  => 'XML-RPC basic',
      'description'  => 'Perform basic XML-RPC tests that do not require additional callbacks.',
      'group' => 'XML-RPC',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
