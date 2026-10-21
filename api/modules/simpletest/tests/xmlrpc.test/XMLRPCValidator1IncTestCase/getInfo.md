# XMLRPCValidator1IncTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 84–90 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L84-L90)
- **Class:** [XMLRPCValidator1IncTestCase](../XMLRPCValidator1IncTestCase.md)
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
      'name' => 'XML-RPC validator',
      'description' => 'See <a href="http://www.xmlrpc.com/validator1Docs">the xmlrpc validator1 specification</a>.',
      'group' => 'XML-RPC',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
