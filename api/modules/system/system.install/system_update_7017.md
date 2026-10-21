# system_update_7017()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2232–2253 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2232-L2253)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7017()
```

## Documentation

```text
Change the theme setting 'toggle_node_info' into a per content type variable.
```

## Code

```php
function system_update_7017() {
  // Get the global theme settings.
  $settings = variable_get('theme_settings', array());
  // Get the settings of the default theme.
  $settings = array_merge($settings, variable_get('theme_' . variable_get('theme_default', 'garland') . '_settings', array()));

  $types = _update_7000_node_get_types();
  foreach ($types as $type) {
    if (isset($settings['toggle_node_info_' . $type->type])) {
      variable_set('node_submitted_' . $type->type, $settings['toggle_node_info_' . $type->type]);
    }
  }

  // Unset deprecated 'toggle_node_info' theme settings.
  $theme_settings = variable_get('theme_settings', array());
  foreach ($theme_settings as $setting => $value) {
    if (substr($setting, 0, 16) == 'toggle_node_info') {
      unset($theme_settings[$setting]);
    }
  }
  variable_set('theme_settings', $theme_settings);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
