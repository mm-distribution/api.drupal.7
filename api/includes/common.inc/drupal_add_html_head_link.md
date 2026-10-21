# drupal_add_html_head_link()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3004–3019 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3004-L3019)

## Signature

```php
function drupal_add_html_head_link($attributes, $header = FALSE)
```

## Documentation

```text
Adds a LINK tag with distinct attributes to the page's HEAD.

This function can be called as long the HTML header hasn't been sent, which
on normal pages is up through the preprocess step of theme('html'). Adding
a link will overwrite a prior link with the exact same 'rel', 'href' and
'hreflang' attributes.

@param $attributes
  Associative array of element attributes including 'href' and 'rel'.
@param $header
  Optional flag to determine if a HTTP 'Link:' header should be sent.
```

## Code

```php
function drupal_add_html_head_link($attributes, $header = FALSE) {
  $element = array(
    '#tag' => 'link',
    '#attributes' => $attributes,
  );
  $href = $attributes['href'];

  if ($header) {
    // Also add a HTTP header "Link:".
    $href = '<' . $attributes['href'] . '>;';
    unset($attributes['href']);
    $element['#attached']['drupal_add_http_header'][] = array('Link',  $href . drupal_http_header_attributes($attributes), TRUE);
  }

  drupal_add_html_head($element, 'drupal_add_html_head_link:' . $attributes['rel'] . ':' . (isset($attributes['hreflang']) ? "{$attributes['hreflang']}:" : '') . $href);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
