# _filter_url_settings()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1430–1444 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1430-L1444)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_url_settings($form, &$form_state, $filter, $format, $defaults)
```

## Documentation

```text
Implements callback_filter_settings().

Provides settings for the URL filter.

@see filter_filter_info()
```

## Code

```php
function _filter_url_settings($form, &$form_state, $filter, $format, $defaults) {
  $filter->settings += $defaults;

  $settings['filter_url_length'] = array(
    '#type' => 'textfield',
    '#title' => t('Maximum link text length'),
    '#default_value' => $filter->settings['filter_url_length'],
    '#size' => 5,
    '#maxlength' => 4,
    '#field_suffix' => t('characters'),
    '#description' => t('URLs longer than this number of characters will be truncated to prevent long strings that break formatting. The link itself will be retained; just the text portion of the link will be truncated.'),
    '#element_validate' => array('element_validate_integer_positive'),
  );
  return $settings;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
