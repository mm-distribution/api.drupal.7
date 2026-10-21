# _filter_html_settings()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1277–1298 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1277-L1298)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_html_settings($form, &$form_state, $filter, $format, $defaults)
```

## Documentation

```text
Implements callback_filter_settings().

Filter settings callback for the HTML content filter.
```

## Code

```php
function _filter_html_settings($form, &$form_state, $filter, $format, $defaults) {
  $filter->settings += $defaults;

  $settings['allowed_html'] = array(
    '#type' => 'textfield',
    '#title' => t('Allowed HTML tags'),
    '#default_value' => $filter->settings['allowed_html'],
    '#maxlength' => 1024,
    '#description' => t('A list of HTML tags that can be used. JavaScript event attributes, JavaScript URLs, and CSS are always stripped.'),
  );
  $settings['filter_html_help'] = array(
    '#type' => 'checkbox',
    '#title' => t('Display basic HTML help in long filter tips'),
    '#default_value' => $filter->settings['filter_html_help'],
  );
  $settings['filter_html_nofollow'] = array(
    '#type' => 'checkbox',
    '#title' => t('Add rel="nofollow" to all links'),
    '#default_value' => $filter->settings['filter_html_nofollow'],
  );
  return $settings;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
