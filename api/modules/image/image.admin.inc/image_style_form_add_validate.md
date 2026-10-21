# image_style_form_add_validate()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 173–177 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L173-L177)
- **Module/theme:** image

## Signature

```php
function image_style_form_add_validate($form, &$form_state)
```

## Documentation

```text
Validate handler for adding a new image effect to an image style.
```

## Code

```php
function image_style_form_add_validate($form, &$form_state) {
  if (!$form_state['values']['new']) {
    form_error($form['effects']['new']['new'], t('Select an effect to add.'));
  }
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
