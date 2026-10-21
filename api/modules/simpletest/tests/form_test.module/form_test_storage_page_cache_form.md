# form_test_storage_page_cache_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 874–902 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L874-L902)
- **Module/theme:** batch_test

## Signature

```php
function form_test_storage_page_cache_form($form, &$form_state)
```

## Documentation

```text
A simple form for testing form storage when page caching is enabled.
```

## Code

```php
function form_test_storage_page_cache_form($form, &$form_state) {
  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => 'Title',
    '#required' => TRUE,
  );

  $form['test_build_id_old'] = array(
    '#type' => 'item',
    '#title' => 'Old build id',
    '#markup' => 'No old build id',
  );

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Save',
  );

  $form['rebuild'] = array(
    '#type' => 'submit',
    '#value' => 'Rebuild',
    '#submit' => array('form_test_storage_page_cache_rebuild'),
  );

  $form['#after_build'] = array('form_test_storage_page_cache_old_build_id');
  $form_state['cache'] = TRUE;

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
