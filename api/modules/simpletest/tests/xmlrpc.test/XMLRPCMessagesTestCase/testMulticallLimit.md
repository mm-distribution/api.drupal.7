# XMLRPCMessagesTestCase::testMulticallLimit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 252–282 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L252-L282)
- **Class:** [XMLRPCMessagesTestCase](../XMLRPCMessagesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMulticallLimit()
```

## Documentation

```text
Test limits on system.multicall that can prevent brute-force attacks.
```

## Code

```php
  function testMulticallLimit() {
    $url = url(NULL, array('absolute' => TRUE)) . 'xmlrpc.php';
    $multicall_args = array();
    $num_method_calls = 10;
    for ($i = 0; $i < $num_method_calls; $i++) {
      $struct = array('i' => $i);
      $multicall_args[] = array('methodName' => 'validator1.echoStructTest', 'params' => array($struct));
    }
    // Test limits of 1, 5, 9, 13.
    for ($limit = 1; $limit < $num_method_calls + 4; $limit += 4) {
      variable_set('xmlrpc_multicall_duplicate_method_limit', $limit);
      $results = xmlrpc($url, array('system.multicall' => array($multicall_args)));
      $this->assertEqual($num_method_calls, count($results));
      for ($i = 0; $i < min($limit, $num_method_calls); $i++) {
        $x = array_shift($results);
        $this->assertTrue(empty($x->is_error), "Result $i is not an error");
        $this->assertEqual($multicall_args[$i]['params'][0], $x);
      }
      for (; $i < $num_method_calls; $i++) {
        $x = array_shift($results);
        $this->assertFalse(empty($x->is_error), "Result $i is an error");
        $this->assertEqual(-156579, $x->code);
      }
    }
    variable_set('xmlrpc_multicall_duplicate_method_limit', -1);
    $results = xmlrpc($url, array('system.multicall' => array($multicall_args)));
    $this->assertEqual($num_method_calls, count($results));
    foreach ($results as $i => $x) {
      $this->assertTrue(empty($x->is_error), "Result $i is not an error");
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
