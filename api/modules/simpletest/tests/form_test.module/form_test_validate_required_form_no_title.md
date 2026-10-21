# form_test_validate_required_form_no_title()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 447–455 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L447-L455)
- **Module/theme:** batch_test

## Signature

```php
function form_test_validate_required_form_no_title($form, &$form_state)
```

## Documentation

```text
Form constructor to test the #required property without #title.
```

## Code

```php
function form_test_validate_required_form_no_title($form, &$form_state) {
  $form['textfield'] = array(
    '#type' => 'textfield',
    '#required' => TRUE,
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => 'Submit');
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
