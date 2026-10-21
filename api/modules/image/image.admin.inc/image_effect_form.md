# image_effect_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 404–445 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L404-L445)
- **Module/theme:** image
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function image_effect_form($form, &$form_state, $style, $effect)
```

## Documentation

```text
Form builder; Form for adding and editing image effects.

This form is used universally for editing all image effects. Each effect adds
its own custom section to the form by calling the form function specified in
hook_image_effects().

@param $form_state
  An associative array containing the current state of the form.
@param $style
  An image style array.
@param $effect
  An image effect array.

@ingroup forms
@see hook_image_effects()
@see image_effects()
@see image_resize_form()
@see image_scale_form()
@see image_rotate_form()
@see image_crop_form()
@see image_effect_form_submit()
```

## Code

```php
function image_effect_form($form, &$form_state, $style, $effect) {
  if (!empty($effect['data'])) {
    $title = t('Edit %label effect', array('%label' => $effect['label']));
  }
  else{
    $title = t('Add %label effect', array('%label' => $effect['label']));
  }
  drupal_set_title($title, PASS_THROUGH);

  $form_state['image_style'] = $style;
  $form_state['image_effect'] = $effect;

  // If no configuration for this image effect, return to the image style page.
  if (!isset($effect['form callback'])) {
    drupal_goto('admin/config/media/image-styles/edit/' . $style['name']);
  }

  $form['#tree'] = TRUE;
  $form['#attached']['css'][drupal_get_path('module', 'image') . '/image.admin.css'] = array();
  if (function_exists($effect['form callback'])) {
    $form['data'] = call_user_func($effect['form callback'], $effect['data']);
  }

  // Check the URL for a weight, then the image effect, otherwise use default.
  $form['weight'] = array(
    '#type' => 'hidden',
    '#value' => isset($_GET['weight']) ? intval($_GET['weight']) : (isset($effect['weight']) ? $effect['weight'] : count($style['effects'])),
  );

  $form['actions'] = array('#tree' => FALSE, '#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => isset($effect['ieid']) ? t('Update effect') : t('Add effect'),
  );
  $form['actions']['cancel'] = array(
    '#type' => 'link',
    '#title' => t('Cancel'),
    '#href' => 'admin/config/media/image-styles/edit/' . $style['name'],
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
