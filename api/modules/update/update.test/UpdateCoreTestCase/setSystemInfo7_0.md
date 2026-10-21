# UpdateCoreTestCase::setSystemInfo7_0()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 268–275 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L268-L275)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
protected function setSystemInfo7_0()
```

## Documentation

```text
Sets the version to 7.0 when no project-specific mapping is defined.
```

## Code

```php
  protected function setSystemInfo7_0() {
    $setting = array(
      '#all' => array(
        'version' => '7.0',
      ),
    );
    variable_set('update_test_system_info', $setting);
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
