# ModuleInstallTestCase::testDrupalWriteRecord()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 307–313 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L307-L313)
- **Class:** [ModuleInstallTestCase](../ModuleInstallTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalWriteRecord()
```

## Documentation

```text
Test that calls to drupal_write_record() work during module installation.

This is a useful function to test because modules often use it to insert
initial data in their database tables when they are being installed or
enabled. Furthermore, drupal_write_record() relies on the module schema
information being available, so this also checks that the data from one of
the module's hook implementations, in particular hook_schema(), is
properly available during this time. Therefore, this test helps ensure
that modules are fully functional while Drupal is installing and enabling
them.
```

## Code

```php
  function testDrupalWriteRecord() {
    // Check for data that was inserted using drupal_write_record() while the
    // 'module_test' module was being installed and enabled.
    $data = db_query("SELECT data FROM {module_test}")->fetchCol();
    $this->assertTrue(in_array('Data inserted in hook_install()', $data), 'Data inserted using drupal_write_record() in hook_install() is correctly saved.');
    $this->assertTrue(in_array('Data inserted in hook_enable()', $data), 'Data inserted using drupal_write_record() in hook_enable() is correctly saved.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
