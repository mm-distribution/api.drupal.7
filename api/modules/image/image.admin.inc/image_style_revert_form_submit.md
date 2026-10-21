# image_style_revert_form_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 375–379 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L375-L379)
- **Module/theme:** image

## Signature

```php
function image_style_revert_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to convert an overridden style to its default.
```

## Code

```php
function image_style_revert_form_submit($form, &$form_state) {
  drupal_set_message(t('The %style style has been reverted to its defaults.', array('%style' => $form_state['image_style']['label'])));
  image_default_style_revert($form_state['image_style']);
  $form_state['redirect'] = 'admin/config/media/image-styles';
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
