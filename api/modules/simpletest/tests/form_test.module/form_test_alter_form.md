# form_test_alter_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 271–276 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L271-L276)
- **Module/theme:** batch_test

## Signature

```php
function form_test_alter_form($form, &$form_state)
```

## Documentation

```text
Form builder for testing hook_form_alter() and hook_form_FORM_ID_alter().
```

## Code

```php
function form_test_alter_form($form, &$form_state) {
  // Elements can be added as needed for future testing needs, but for now,
  // we're only testing alter hooks that do not require any elements added by
  // this function.
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
