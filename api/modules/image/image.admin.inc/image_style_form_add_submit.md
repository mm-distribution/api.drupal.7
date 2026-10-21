# image_style_form_add_submit()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 182–199 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L182-L199)
- **Module/theme:** image

## Signature

```php
function image_style_form_add_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for adding a new image effect to an image style.
```

## Code

```php
function image_style_form_add_submit($form, &$form_state) {
  $style = $form_state['image_style'];
  // Check if this field has any configuration options.
  $effect = image_effect_definition_load($form_state['values']['new']);

  // Load the configuration form for this option.
  if (isset($effect['form callback'])) {
    $path = 'admin/config/media/image-styles/edit/' . $form_state['image_style']['name'] . '/add/' . $form_state['values']['new'];
    $form_state['redirect'] = array($path, array('query' => array('weight' => $form_state['values']['weight'])));
  }
  // If there's no form, immediately add the image effect.
  else {
    $effect['isid'] = $style['isid'];
    $effect['weight'] = $form_state['values']['weight'];
    image_effect_save($effect);
    drupal_set_message(t('The image effect was successfully applied.'));
  }
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
