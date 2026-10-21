# filter_install()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 117–149 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L117-L149)
- **Module/theme:** filter
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function filter_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function filter_install() {
  // All sites require at least one text format (the fallback format) that all
  // users have access to, so add it here. We initialize it as a simple, safe
  // plain text format with very basic formatting, but it can be modified by
  // installation profiles to have other properties.
  $plain_text_format = array(
    'format' => 'plain_text',
    'name' => 'Plain text',
    'weight' => 10,
    'filters' => array(
      // Escape all HTML.
      'filter_html_escape' => array(
        'weight' => 0,
        'status' => 1,
      ),
      // URL filter.
      'filter_url' => array(
        'weight' => 1,
        'status' => 1,
      ),
      // Line break filter.
      'filter_autop' => array(
        'weight' => 2,
        'status' => 1,
      ),
    ),
  );
  $plain_text_format = (object) $plain_text_format;
  filter_format_save($plain_text_format);

  // Set the fallback format to plain text.
  variable_set('filter_fallback_format', $plain_text_format->format);
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
