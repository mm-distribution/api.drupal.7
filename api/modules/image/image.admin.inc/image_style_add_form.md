# image_style_add_form()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 242–268 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L242-L268)
- **Module/theme:** image
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function image_style_add_form($form, &$form_state)
```

## Documentation

```text
Form builder; Form for adding a new image style.

@ingroup forms
@see image_style_add_form_submit()
```

## Code

```php
function image_style_add_form($form, &$form_state) {
  $form['label'] = array(
    '#type' => 'textfield',
    '#title' => t('Style name'),
    '#default_value' => '',
    '#required' => TRUE,
  );
  $form['name'] = array(
    '#type' => 'machine_name',
    '#description' => t('The name is used in URLs for generated images. Use only lowercase alphanumeric characters, underscores (_), and hyphens (-).'),
    '#size' => '64',
    '#required' => TRUE,
    '#machine_name' => array(
      'exists' => 'image_style_add_form_name_exists',
      'source' => array('label'),
      'replace_pattern' => '[^0-9a-z_\-]',
      'error' => t('Please only use lowercase alphanumeric characters, underscores (_), and hyphens (-) for style names.'),
    ),
  );

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Create new style'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
