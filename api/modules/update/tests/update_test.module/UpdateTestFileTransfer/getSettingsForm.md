# UpdateTestFileTransfer::getSettingsForm()

- **Type:** Method
- **File:** [`modules/update/tests/update_test.module`](../_file.md), lines 174–181 · [local source](../../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L174-L181)
- **Class:** [UpdateTestFileTransfer](../UpdateTestFileTransfer.md)
- **Module/theme:** aaa_update_test

## Signature

```php
public function getSettingsForm()
```

## Documentation

```text
Returns a settings form with a text field to input a username.
```

## Code

```php
  public function getSettingsForm() {
    $form = array();
    $form['udpate_test_username'] = array(
      '#type' => 'textfield',
      '#title' => t('Update Test Username'),
    );
    return $form;
  }
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
