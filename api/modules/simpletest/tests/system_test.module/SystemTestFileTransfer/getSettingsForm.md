# SystemTestFileTransfer::getSettingsForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/system_test.module`](../_file.md), lines 486–493 · [local source](../../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L486-L493)
- **Class:** [SystemTestFileTransfer](../SystemTestFileTransfer.md)
- **Module/theme:** batch_test

## Signature

```php
public function getSettingsForm()
```

## Documentation

_No docblock in source._

## Code

```php
  public function getSettingsForm() {
    $form = array();
    $form['system_test_username'] = array(
      '#type' => 'textfield',
      '#title' => t('System Test Username'),
    );
    return $form;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
