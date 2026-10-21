# XMLRPCBasicTestCase::testMethodSignature()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 47–52 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L47-L52)
- **Class:** [XMLRPCBasicTestCase](../XMLRPCBasicTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function testMethodSignature()
```

## Documentation

```text
Ensure that system.methodSignature returns an array of signatures.
```

## Code

```php
  protected function testMethodSignature() {
    $url = url(NULL, array('absolute' => TRUE)) . 'xmlrpc.php';
    $signature = xmlrpc($url, array('system.methodSignature' => array('system.listMethods')));
    $this->assert(is_array($signature) && !empty($signature) && is_array($signature[0]),
      'system.methodSignature returns an array of signature arrays.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
