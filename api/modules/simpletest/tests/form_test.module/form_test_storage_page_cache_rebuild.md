# form_test_storage_page_cache_rebuild()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 917–919 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L917-L919)
- **Module/theme:** batch_test

## Signature

```php
function form_test_storage_page_cache_rebuild($form, &$form_state)
```

## Documentation

```text
Form submit callback: Rebuild the form and continue.
```

## Code

```php
function form_test_storage_page_cache_rebuild($form, &$form_state) {
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
