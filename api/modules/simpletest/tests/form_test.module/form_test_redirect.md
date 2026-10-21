# form_test_redirect()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1860–1880 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1860-L1880)
- **Module/theme:** batch_test

## Signature

```php
function form_test_redirect($form, &$form_state)
```

## Documentation

```text
Form builder to detect form redirect.
```

## Code

```php
function form_test_redirect($form, &$form_state) {
  $form['redirection'] = array(
    '#type' => 'checkbox',
    '#title' => t('Use redirection'),
  );
  $form['destination'] = array(
    '#type' => 'textfield',
    '#title' => t('Redirect destination'),
    '#states' => array(
      'visible' => array(
        ':input[name="redirection"]' => array('checked' => TRUE),
      ),
    ),
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
