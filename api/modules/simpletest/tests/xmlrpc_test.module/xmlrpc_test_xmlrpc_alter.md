# xmlrpc_test_xmlrpc_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 70–86 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L70-L86)
- **Module/theme:** batch_test
- **Implements:** [hook_xmlrpc_alter()](../../../system/system.api.php/hook_xmlrpc_alter.md)

## Signature

```php
function xmlrpc_test_xmlrpc_alter(&$services)
```

## Documentation

```text
Implements hook_xmlrpc_alter().

Hide (or not) the system.methodSignature() service depending on a variable.
```

## Code

```php
function xmlrpc_test_xmlrpc_alter(&$services) {
  if (variable_get('xmlrpc_test_xmlrpc_alter', FALSE)) {
    $remove = NULL;
    foreach ($services as $key => $value) {
      if (!is_array($value)) {
        continue;
      }
      if ($value[0] == 'system.methodSignature') {
        $remove = $key;
        break;
      }
    }
    if (isset($remove)) {
      unset($services[$remove]);
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
