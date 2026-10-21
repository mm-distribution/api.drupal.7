# system_image_toolkit_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1867–1898 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1867-L1898)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_image_toolkit_settings()
```

## Documentation

```text
Form builder; Configure site image toolkit usage.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_image_toolkit_settings() {
  $toolkits_available = image_get_available_toolkits();
  $current_toolkit = image_get_toolkit();

  if (count($toolkits_available) == 0) {
    variable_del('image_toolkit');
    $form['image_toolkit_help'] = array(
      '#markup' => t("No image toolkits were detected. Drupal includes support for <a href='!gd-link'>PHP's built-in image processing functions</a> but they were not detected on this system. You should consult your system administrator to have them enabled, or try using a third party toolkit.", array('!gd-link' => url('http://php.net/gd'))),
    );
    return $form;
  }

  if (count($toolkits_available) > 1) {
    $form['image_toolkit'] = array(
      '#type' => 'radios',
      '#title' => t('Select an image processing toolkit'),
      '#default_value' => variable_get('image_toolkit', $current_toolkit),
      '#options' => $toolkits_available
    );
  }
  else {
    variable_set('image_toolkit', key($toolkits_available));
  }

  // Get the toolkit's settings form.
  $function = 'image_' . $current_toolkit . '_settings';
  if (function_exists($function)) {
    $form['image_toolkit_settings'] = $function();
  }

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
