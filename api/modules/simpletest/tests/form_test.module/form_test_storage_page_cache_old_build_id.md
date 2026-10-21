# form_test_storage_page_cache_old_build_id()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 907–912 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L907-L912)
- **Module/theme:** batch_test

## Signature

```php
function form_test_storage_page_cache_old_build_id($form)
```

## Documentation

```text
Form element #after_build callback: output the old form build-id.
```

## Code

```php
function form_test_storage_page_cache_old_build_id($form) {
  if (isset($form['#build_id_old'])) {
    $form['test_build_id_old']['#markup'] = check_plain($form['#build_id_old']);
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
