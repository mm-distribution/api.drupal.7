# ajax_forms_test_lazy_load_form_ajax()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 518–520 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L518-L520)
- **Module/theme:** batch_test

## Signature

```php
function ajax_forms_test_lazy_load_form_ajax($form, &$form_state)
```

## Documentation

```text
AJAX callback for the ajax_forms_test_lazy_load_form() form.

This function returns nothing, because all we're interested in testing is
ajax_render() adding commands for JavaScript and CSS added during the page
request, such as the ones added in ajax_forms_test_lazy_load_form_submit().
```

## Code

```php
function ajax_forms_test_lazy_load_form_ajax($form, &$form_state) {
  return NULL;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
