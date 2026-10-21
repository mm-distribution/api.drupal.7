# _options_properties()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 184–239 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L184-L239)
- **Module/theme:** options

## Signature

```php
function _options_properties($type, $multiple, $required, $has_value)
```

## Documentation

```text
Describes the preparation steps required by each widget.
```

## Code

```php
function _options_properties($type, $multiple, $required, $has_value) {
  $base = array(
    'filter_xss' => FALSE,
    'strip_tags' => FALSE,
    'strip_tags_and_unescape' => FALSE,
    'empty_option' => FALSE,
    'optgroups' => FALSE,
  );

  $properties = array();

  switch ($type) {
    case 'select':
      $properties = array(
        // Select boxes do not support any HTML tag.
        'strip_tags_and_unescape' => TRUE,
        'optgroups' => TRUE,
      );
      if ($multiple) {
        // Multiple select: add a 'none' option for non-required fields.
        if (!$required) {
          $properties['empty_option'] = 'option_none';
        }
      }
      else {
        // Single select: add a 'none' option for non-required fields,
        // and a 'select a value' option for required fields that do not come
        // with a value selected.
        if (!$required) {
          $properties['empty_option'] = 'option_none';
        }
        elseif (!$has_value) {
          $properties['empty_option'] = 'option_select';
        }
      }
      break;

    case 'buttons':
      $properties = array(
        'filter_xss' => TRUE,
      );
      // Add a 'none' option for non-required radio buttons.
      if (!$required && !$multiple) {
        $properties['empty_option'] = 'option_none';
      }
      break;

    case 'onoff':
      $properties = array(
        'filter_xss' => TRUE,
      );
      break;
  }

  return $properties + $base;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
