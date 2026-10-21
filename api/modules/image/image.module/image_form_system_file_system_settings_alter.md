# image_form_system_file_system_settings_alter()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 252–254 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L252-L254)
- **Module/theme:** image
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function image_form_system_file_system_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function image_form_system_file_system_settings_alter(&$form, &$form_state) {
  $form['#submit'][] = 'image_system_file_system_settings_submit';
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
