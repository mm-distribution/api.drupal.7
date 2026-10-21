# _field_extra_fields_pre_render()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 714–739 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L714-L739)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function _field_extra_fields_pre_render($elements)
```

## Documentation

```text
Pre-render callback to adjust weights and visibility of non-field elements.
```

## Code

```php
function _field_extra_fields_pre_render($elements) {
  $entity_type = $elements['#entity_type'];
  $bundle = $elements['#bundle'];

  if (isset($elements['#type']) && $elements['#type'] == 'form') {
    $extra_fields = field_info_extra_fields($entity_type, $bundle, 'form');
    foreach ($extra_fields as $name => $settings) {
      if (isset($elements[$name])) {
        $elements[$name]['#weight'] = $settings['weight'];
      }
    }
  }
  elseif (isset($elements['#view_mode'])) {
    $view_mode = $elements['#view_mode'];
    $extra_fields = field_extra_fields_get_display($entity_type, $bundle, $view_mode);
    foreach ($extra_fields as $name => $settings) {
      if (isset($elements[$name])) {
        $elements[$name]['#weight'] = $settings['weight'];
        // Visibility: make sure we do not accidentally show a hidden element.
        $elements[$name]['#access'] = isset($elements[$name]['#access']) ? ($elements[$name]['#access'] && $settings['visible']) : $settings['visible'];
      }
    }
  }

  return $elements;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
