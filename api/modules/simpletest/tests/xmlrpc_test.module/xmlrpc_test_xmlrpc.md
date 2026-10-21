# xmlrpc_test_xmlrpc()

- **Type:** Function
- **File:** [`modules/simpletest/tests/xmlrpc_test.module`](_file.md), lines 51–63 · [local source](../../../../../source/modules/simpletest/tests/xmlrpc_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module#L51-L63)
- **Module/theme:** batch_test
- **Implements:** [hook_xmlrpc()](../../../system/system.api.php/hook_xmlrpc.md)

## Signature

```php
function xmlrpc_test_xmlrpc()
```

## Documentation

```text
Implements hook_xmlrpc().
```

## Code

```php
function xmlrpc_test_xmlrpc() {
  return array(
    'validator1.arrayOfStructsTest' => 'xmlrpc_test_arrayOfStructsTest',
    'validator1.countTheEntities' => 'xmlrpc_test_countTheEntities',
    'validator1.easyStructTest' => 'xmlrpc_test_easyStructTest',
    'validator1.echoStructTest' => 'xmlrpc_test_echoStructTest',
    'validator1.manyTypesTest' => 'xmlrpc_test_manyTypesTest',
    'validator1.moderateSizeArrayCheck' => 'xmlrpc_test_moderateSizeArrayCheck',
    'validator1.nestedStructTest' => 'xmlrpc_test_nestedStructTest',
    'validator1.simpleStructReturnTest' => 'xmlrpc_test_simpleStructReturnTest',
    'messages.messageSizedInKB' => 'xmlrpc_test_message_sized_in_kb',
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/xmlrpc_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/xmlrpc_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
