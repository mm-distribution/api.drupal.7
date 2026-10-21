# image_style_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 36–168 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L36-L168)
- **Module/theme:** image
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function image_style_form($form, &$form_state, $style)
```

## Documentation

```text
Form builder; Edit an image style name and effects order.

@param $form_state
  An associative array containing the current state of the form.
@param $style
  An image style array.
@ingroup forms
@see image_style_form_submit()
```

## Code

```php
function image_style_form($form, &$form_state, $style) {
  $title = t('Edit %name style', array('%name' => $style['label']));
  drupal_set_title($title, PASS_THROUGH);

  // Adjust this form for styles that must be overridden to edit.
  $editable = (bool) ($style['storage'] & IMAGE_STORAGE_EDITABLE);

  if (!$editable && empty($form_state['input'])) {
    drupal_set_message(t('This image style is currently being provided by a module. Click the "Override defaults" button to change its settings.'), 'warning');
  }

  $form_state['image_style'] = $style;
  $form['#tree'] = TRUE;
  $form['#attached']['css'][drupal_get_path('module', 'image') . '/image.admin.css'] = array();

  // Show the thumbnail preview.
  $form['preview'] = array(
    '#type' => 'item',
    '#title' => t('Preview'),
    '#markup' => theme('image_style_preview', array('style' => $style)),
  );

  // Show the Image Style label.
  $form['label'] = array(
    '#type' => 'textfield',
    '#title' => t('Image style name'),
    '#default_value' => $style['label'],
    '#disabled' => !$editable,
    '#required' => TRUE,
  );

  // Allow the name of the style to be changed, unless this style is
  // provided by a module's hook_default_image_styles().
  $form['name'] = array(
    '#type' => 'machine_name',
    '#size' => '64',
    '#default_value' => $style['name'],
    '#disabled' => !$editable,
    '#description' => t('The name is used in URLs for generated images. Use only lowercase alphanumeric characters, underscores (_), and hyphens (-).'),
    '#required' => TRUE,
    '#machine_name' => array(
      'exists' => 'image_style_load',
      'source' => array('label'),
      'replace_pattern' => '[^0-9a-z_\-]',
      'error' => t('Please only use lowercase alphanumeric characters, underscores (_), and hyphens (-) for style names.'),
    ),
  );

  // Build the list of existing image effects for this image style.
  $form['effects'] = array(
    '#theme' => 'image_style_effects',
  );
  foreach ($style['effects'] as $key => $effect) {
    $form['effects'][$key]['#weight'] = isset($form_state['input']['effects']) ? $form_state['input']['effects'][$key]['weight'] : NULL;
    $form['effects'][$key]['label'] = array(
      '#markup' => $effect['label'],
    );
    $form['effects'][$key]['summary'] = array(
      '#markup' => isset($effect['summary theme']) ? theme($effect['summary theme'], array('data' => $effect['data'])) : '',
    );
    $form['effects'][$key]['weight'] = array(
      '#type' => 'weight',
      '#title' => t('Weight for @title', array('@title' => $effect['label'])),
      '#title_display' => 'invisible',
      '#default_value' => $effect['weight'],
      '#access' => $editable,
    );

    // Only attempt to display these fields for editable styles as the 'ieid'
    // key is not set for styles defined in code.
    if ($editable) {
      $form['effects'][$key]['configure'] = array(
        '#type' => 'link',
        '#title' => t('edit'),
        '#href' => 'admin/config/media/image-styles/edit/' . $style['name'] . '/effects/' . $effect['ieid'],
        '#access' => $editable && isset($effect['form callback']),
      );
      $form['effects'][$key]['remove'] = array(
        '#type' => 'link',
        '#title' => t('delete'),
        '#href' => 'admin/config/media/image-styles/edit/' . $style['name'] . '/effects/' . $effect['ieid'] . '/delete',
        '#access' => $editable,
      );
    }
  }

  // Build the new image effect addition form and add it to the effect list.
  $new_effect_options = array();
  foreach (image_effect_definitions() as $effect => $definition) {
    $new_effect_options[$effect] = check_plain($definition['label']);
  }
  $form['effects']['new'] = array(
    '#tree' => FALSE,
    '#weight' => isset($form_state['input']['weight']) ? $form_state['input']['weight'] : NULL,
    '#access' => $editable,
  );
  $form['effects']['new']['new'] = array(
    '#type' => 'select',
    '#title' => t('Effect'),
    '#title_display' => 'invisible',
    '#options' => $new_effect_options,
    '#empty_option' => t('Select a new effect'),
  );
  $form['effects']['new']['weight'] = array(
    '#type' => 'weight',
    '#title' => t('Weight for new effect'),
    '#title_display' => 'invisible',
    '#default_value' => count($form['effects']) - 1,
  );
  $form['effects']['new']['add'] = array(
    '#type' => 'submit',
    '#value' => t('Add'),
    '#validate' => array('image_style_form_add_validate'),
    '#submit' => array('image_style_form_submit', 'image_style_form_add_submit'),
  );

  // Show the Override or Submit button for this style.
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['override'] = array(
    '#type' => 'submit',
    '#value' => t('Override defaults'),
    '#validate' => array(),
    '#submit' => array('image_style_form_override_submit'),
    '#access' => !$editable,
  );
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Update style'),
    '#access' => $editable,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
