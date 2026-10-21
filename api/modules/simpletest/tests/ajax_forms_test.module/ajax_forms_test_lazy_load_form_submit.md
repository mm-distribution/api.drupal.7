# ajax_forms_test_lazy_load_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 502–509 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L502-L509)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_lazy_load_form_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler: Adds JavaScript and CSS that wasn't on the original form.
```

## Code

```php
function ajax_forms_test_lazy_load_form_submit($form, &$form_state) {
  if ($form_state['values']['add_files']) {
    drupal_add_js(array('ajax_forms_test_lazy_load_form_submit' => 'executed'), 'setting');
    drupal_add_css(drupal_get_path('module', 'system') . '/system.admin.css');
    drupal_add_js(drupal_get_path('module', 'system') . '/system.js');
  }
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
