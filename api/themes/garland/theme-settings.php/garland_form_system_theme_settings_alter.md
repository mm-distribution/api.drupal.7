# garland_form_system_theme_settings_alter()

- **Type:** Function
- **File:** [`themes/garland/theme-settings.php`](_file.md), lines 16–30 · [local source](../../../../source/themes/garland/theme-settings.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/theme-settings.php#L16-L30)
- **Module/theme:** garland
- **Implements:** [hook_form_FORM_ID_alter()](../../../modules/system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function garland_form_system_theme_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

@param $form
  The form.
@param $form_state
  The form state.
```

## Code

```php
function garland_form_system_theme_settings_alter(&$form, &$form_state) {

  $form['garland_width'] = array(
    '#type' => 'radios',
    '#title' => t('Content width'),
    '#options' => array(
      'fluid' => t('Fluid width'),
      'fixed' => t('Fixed width'),
    ),
    '#default_value' => theme_get_setting('garland_width'),
    '#description' => t('Specify whether the content will wrap to a fixed width or will fluidly expand to the width of the browser window.'),
    // Place this above the color scheme options.
    '#weight' => -2,
  );
}
```

---
_Drupal 7.103 · [themes/garland/theme-settings.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/theme-settings.php) · Licensed GPL-2.0-or-later (see LICENSE)._
