# image_style_add_form_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 286–294 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L286-L294)
- **Module/theme:** image

## Signature

```php
function image_style_add_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for adding a new image style.
```

## Code

```php
function image_style_add_form_submit($form, &$form_state) {
  $style = array(
    'name' => $form_state['values']['name'],
    'label' => $form_state['values']['label'],
  );
  $style = image_style_save($style);
  drupal_set_message(t('Style %name was created.', array('%name' => $style['label'])));
  $form_state['redirect'] = 'admin/config/media/image-styles/edit/' . $style['name'];
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
