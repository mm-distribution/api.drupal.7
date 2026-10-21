# _drupal_default_html_head()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 319–347 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L319-L347)

## Signature

```php
function _drupal_default_html_head()
```

## Documentation

```text
Returns elements that are always displayed in the HEAD tag of the HTML page.
```

## Code

```php
function _drupal_default_html_head() {
  // Add default elements. Make sure the Content-Type comes first because the
  // IE browser may be vulnerable to XSS via encoding attacks from any content
  // that comes before this META tag, such as a TITLE tag.
  $elements['system_meta_content_type'] = array(
    '#type' => 'html_tag',
    '#tag' => 'meta',
    '#attributes' => array(
      'http-equiv' => 'Content-Type',
      'content' => 'text/html; charset=utf-8',
    ),
    // Security: This always has to be output first.
    '#weight' => -1000,
  );
  // Show Drupal and the major version number in the META GENERATOR tag.
  // Get the major version.
  list($version, ) = explode('.', VERSION);
  $elements['system_meta_generator'] = array(
    '#type' => 'html_tag',
    '#tag' => 'meta',
    '#attributes' => array(
      'name' => 'Generator',
      'content' => 'Drupal ' . $version . ' (http://drupal.org)',
    ),
  );
  // Also send the generator in the HTTP header.
  $elements['system_meta_generator']['#attached']['drupal_add_http_header'][] = array('X-Generator', $elements['system_meta_generator']['#attributes']['content']);
  return $elements;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
