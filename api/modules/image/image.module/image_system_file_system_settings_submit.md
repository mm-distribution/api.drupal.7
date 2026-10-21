# image_system_file_system_settings_submit()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 262–266 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L262-L266)
- **Module/theme:** image

## Signature

```php
function image_system_file_system_settings_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for system_file_system_settings().

Adds a menu rebuild after the public file path has been changed, so that the
menu router item depending on that file path will be regenerated.
```

## Code

```php
function image_system_file_system_settings_submit($form, &$form_state) {
  if ($form['file_public_path']['#default_value'] !== $form_state['values']['file_public_path']) {
    variable_set('menu_rebuild_needed', TRUE);
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
