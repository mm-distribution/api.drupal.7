# color_form_system_theme_settings_alter()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 39–52 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L39-L52)
- **Module/theme:** color
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function color_form_system_theme_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function color_form_system_theme_settings_alter(&$form, &$form_state) {
  if (isset($form_state['build_info']['args'][0]) && ($theme = $form_state['build_info']['args'][0]) && color_get_info($theme) && function_exists('gd_info')) {
    $form['color'] = array(
      '#type' => 'fieldset',
      '#title' => t('Color scheme'),
      '#weight' => -1,
      '#attributes' => array('id' => 'color_scheme_form'),
      '#theme' => 'color_scheme_form',
    );
    $form['color'] += color_scheme_form($form, $form_state, $theme);
    $form['#validate'][] = 'color_scheme_form_validate';
    $form['#submit'][] = 'color_scheme_form_submit';
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
