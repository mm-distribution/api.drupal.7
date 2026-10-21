# options_field_widget_info()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 41–66 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L41-L66)
- **Module/theme:** options
- **Implements:** [hook_field_widget_info()](../../../field.api.php/hook_field_widget_info.md)
- **Implements:** [hook_options_list()](../options.api.php/hook_options_list.md)

## Signature

```php
function options_field_widget_info()
```

## Documentation

```text
Implements hook_field_widget_info().

Field type modules willing to use those widgets should:
- Use hook_field_widget_info_alter() to append their field own types to the
  list of types supported by the widgets,
- Implement hook_options_list() to provide the list of options.
See list.module.
```

## Code

```php
function options_field_widget_info() {
  return array(
    'options_select' => array(
      'label' => t('Select list'),
      'field types' => array(),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_CUSTOM,
      ),
    ),
    'options_buttons' => array(
      'label' => t('Check boxes/radio buttons'),
      'field types' => array(),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_CUSTOM,
      ),
    ),
    'options_onoff' => array(
      'label' => t('Single on/off checkbox'),
      'field types' => array(),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_CUSTOM,
      ),
      'settings' => array('display_label' => 0),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
