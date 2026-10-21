# _options_prepare_options()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 268–290 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L268-L290)
- **Module/theme:** options

## Signature

```php
function _options_prepare_options(&$options, $properties)
```

## Documentation

```text
Sanitizes the options.

The function is recursive to support optgroups.
```

## Code

```php
function _options_prepare_options(&$options, $properties) {
  foreach ($options as $value => $label) {
    // Recurse for optgroups.
    if (is_array($label)) {
      _options_prepare_options($options[$value], $properties);
    }
    else {
      // The 'strip_tags' option is deprecated. Use 'strip_tags_and_unescape'
      // when plain text is required (and where the output will be run through
      // check_plain() before being inserted back into HTML) or 'filter_xss'
      // when HTML is required.
      if ($properties['strip_tags']) {
        $options[$value] = strip_tags($label);
      }
      if ($properties['strip_tags_and_unescape']) {
        $options[$value] = decode_entities(strip_tags($label));
      }
      if ($properties['filter_xss']) {
        $options[$value] = field_filter_xss($label);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
