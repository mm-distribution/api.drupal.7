# XMLRPCBasicTestCase::testListMethods()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 19–42 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L19-L42)
- **Class:** [XMLRPCBasicTestCase](../XMLRPCBasicTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function testListMethods()
```

## Documentation

```text
Ensure that a basic XML-RPC call with no parameters works.
```

## Code

```php
  protected function testListMethods() {
    // Minimum list of methods that should be included.
    $minimum = array(
      'system.multicall',
      'system.methodSignature',
      'system.getCapabilities',
      'system.listMethods',
      'system.methodHelp',
    );

    // Invoke XML-RPC call to get list of methods.
    $url = url(NULL, array('absolute' => TRUE)) . 'xmlrpc.php';
    $methods = xmlrpc($url, array('system.listMethods' => array()));

    // Ensure that the minimum methods were found.
    $count = 0;
    foreach ($methods as $method) {
      if (in_array($method, $minimum)) {
        $count++;
      }
    }

    $this->assertEqual($count, count($minimum), 'system.listMethods returned at least the minimum listing');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
