# FieldInfo::prepareInstanceDisplay()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 609–634 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L609-L634)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function prepareInstanceDisplay($display, $field_type)
```

## Documentation

```text
Adapts display specifications to the current run-time context.

@param $display
  Display specifications as found in $instance['display']['a_view_mode'].
@param $field_type
  The field type.

@return
  The display properties completed for the current runtime context.
```

## Code

```php
  public function prepareInstanceDisplay($display, $field_type) {
    $field_type_info = field_info_field_types($field_type);

    // Fill in default values.
    $display += array(
      'label' => 'above',
      'settings' => array(),
      'weight' => 0,
    );
    if (empty($display['type'])) {
      $display['type'] = $field_type_info['default_formatter'];
    }
    if ($display['type'] != 'hidden') {
      $formatter_type_info = field_info_formatter_types($display['type']);
      // Fall back to default formatter if formatter type is not available.
      if (!$formatter_type_info) {
        $display['type'] = $field_type_info['default_formatter'];
        $formatter_type_info = field_info_formatter_types($display['type']);
      }
      $display['module'] = $formatter_type_info['module'];
      // Fill in default settings for the formatter.
      $display['settings'] += field_info_formatter_settings($display['type']);
    }

    return $display;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
