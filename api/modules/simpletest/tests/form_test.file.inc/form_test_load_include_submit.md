# form_test_load_include_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.file.inc`](_file.md), lines 35–37 · [local source](../../../../../source/modules/simpletest/tests/form_test.file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.file.inc#L35-L37)
- **Module/theme:** batch_test

## Signature

```php
function form_test_load_include_submit($form, $form_state)
```

## Documentation

```text
Submit callback for the form API file inclusion test forms.
```

## Code

```php
function form_test_load_include_submit($form, $form_state) {
  drupal_set_message('Submit callback called.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.file.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
