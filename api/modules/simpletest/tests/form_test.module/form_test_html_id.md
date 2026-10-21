# form_test_html_id()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 2007–2018 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L2007-L2018)
- **Module/theme:** batch_test

## Signature

```php
function form_test_html_id($form, &$form_state)
```

## Documentation

```text
Builds a simple form to test duplicate HTML IDs.
```

## Code

```php
function form_test_html_id($form, &$form_state) {
  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => 'name',
    '#required' => TRUE,
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Save',
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
