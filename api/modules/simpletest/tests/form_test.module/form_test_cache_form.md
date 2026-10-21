# form_test_cache_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 924–937 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L924-L937)
- **Module/theme:** batch_test

## Signature

```php
function form_test_cache_form($form, &$form_state)
```

## Documentation

```text
A simple form for testing form caching.
```

## Code

```php
function form_test_cache_form($form, &$form_state) {
  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => 'Title',
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
