# XMLRPCMessagesTestCase::testAlterListMethods()

- **Type:** Method
- **File:** [`modules/simpletest/tests/xmlrpc.test`](../_file.md), lines 232–247 · [local source](../../../../../../source/modules/simpletest/tests/xmlrpc.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test#L232-L247)
- **Class:** [XMLRPCMessagesTestCase](../XMLRPCMessagesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function testAlterListMethods()
```

## Documentation

```text
Ensure that hook_xmlrpc_alter() can hide even builtin methods.
```

## Code

```php
  protected function testAlterListMethods() {

    // Ensure xmlrpc_test_xmlrpc_alter() is disabled and retrieve regular list of methods.
    variable_set('xmlrpc_test_xmlrpc_alter', FALSE);
    $url = url(NULL, array('absolute' => TRUE)) . 'xmlrpc.php';
    $methods1 = xmlrpc($url, array('system.listMethods' => array()));

    // Enable the alter hook and retrieve the list of methods again.
    variable_set('xmlrpc_test_xmlrpc_alter', TRUE);
    $methods2 = xmlrpc($url, array('system.listMethods' => array()));

    $diff = array_diff($methods1, $methods2);
    $this->assertTrue(is_array($diff) && !empty($diff), 'Method list is altered by hook_xmlrpc_alter');
    $removed = reset($diff);
    $this->assertEqual($removed, 'system.methodSignature', 'Hiding builting system.methodSignature with hook_xmlrpc_alter works');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc.test) · Licensed GPL-2.0-or-later (see LICENSE)._
