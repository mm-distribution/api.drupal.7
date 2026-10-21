# image_style_form_override_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 204–207 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L204-L207)
- **Module/theme:** image

## Signature

```php
function image_style_form_override_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for overriding a module-defined style.
```

## Code

```php
function image_style_form_override_submit($form, &$form_state) {
  drupal_set_message(t('The %style style has been overridden, allowing you to change its settings.', array('%style' => $form_state['image_style']['label'])));
  image_default_style_save($form_state['image_style']);
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
