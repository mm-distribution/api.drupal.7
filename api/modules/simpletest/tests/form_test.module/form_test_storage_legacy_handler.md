# form_test_storage_legacy_handler()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 820–833 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L820-L833)
- **Module/theme:** batch_test

## Signature

```php
function form_test_storage_legacy_handler($form_build_id)
```

## Documentation

```text
Emulate legacy AHAH-style ajax callback.

Drupal 6 AHAH callbacks used to operate directly on forms retrieved using
form_get_cache and stored using form_set_cache after manipulation. This
callback helps testing whether form_set_cache prevents resaving of immutable
forms.
```

## Code

```php
function form_test_storage_legacy_handler($form_build_id) {
  $form_state = array();
  $form = form_get_cache($form_build_id, $form_state);

  drupal_json_output(array(
    'form' => $form,
    'form_state' => $form_state,
  ));

  $form['#poisoned'] = TRUE;
  $form_state['poisoned'] = TRUE;

  form_set_cache($form_build_id, $form, $form_state);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
