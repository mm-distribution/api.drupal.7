# BootstrapGetFilenameWebTestCase::testRecursiveRebuilds()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 642–662 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L642-L662)
- **Class:** [BootstrapGetFilenameWebTestCase](../BootstrapGetFilenameWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testRecursiveRebuilds()
```

## Documentation

```text
Test that drupal_get_filename() does not break recursive rebuilds.
```

## Code

```php
  public function testRecursiveRebuilds() {
    // Ensure that the drupal_get_filename() call due to a missing module does
    // not break the data returned by an attempted recursive rebuild. The code
    // path which is tested is as follows:
    // - Call drupal_get_schema().
    // - Within a hook_schema() implementation, trigger a drupal_get_filename()
    //   search for a nonexistent module.
    // - In the watchdog() call that results from that, trigger
    //   drupal_get_schema() again.
    // Without some kind of recursion protection, this could cause the second
    // drupal_get_schema() call to return incomplete results. This test ensures
    // that does not happen.
    $non_existing_module = $this->randomName();
    variable_set('system_test_drupal_get_filename_test_module_name', $non_existing_module);
    $this->drupalGet('system-test/drupal-get-filename-with-schema-rebuild');
    $original_drupal_get_schema_tables = variable_get('system_test_drupal_get_filename_with_schema_rebuild_original_tables');
    $final_drupal_get_schema_tables = variable_get('system_test_drupal_get_filename_with_schema_rebuild_final_tables');
    $this->assertTrue(!empty($original_drupal_get_schema_tables));
    $this->assertTrue(!empty($final_drupal_get_schema_tables));
    $this->assertEqual($original_drupal_get_schema_tables, $final_drupal_get_schema_tables);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
