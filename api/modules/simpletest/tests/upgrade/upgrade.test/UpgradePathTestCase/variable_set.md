# UpgradePathTestCase::variable_set()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 176–194 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L176-L194)
- **Class:** [UpgradePathTestCase](../UpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function variable_set($name, $value)
```

## Documentation

```text
Specialized variable_set() that works even if the child site is not upgraded.

@param $name
  The name of the variable to set.
@param $value
  The value to set. This can be any PHP data type; these functions take care
  of serialization as necessary.
```

## Code

```php
  protected function variable_set($name, $value) {
    db_delete('variable')
      ->condition('name', $name)
      ->execute();
    db_insert('variable')
      ->fields(array(
        'name' => $name,
        'value' => serialize($value),
      ))
      ->execute();

    try {
      cache_clear_all('variables', 'cache');
      cache_clear_all('variables', 'cache_bootstrap');
    }
    // Since cache_bootstrap won't exist in a Drupal 6 site, ignore the
    // exception if the above fails.
    catch (Exception $e) {}
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
