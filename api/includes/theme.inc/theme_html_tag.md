# theme_html_tag()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2317–2335 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2317-L2335)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_html_tag($variables)
```

## Documentation

```text
Returns HTML for a generic HTML tag with attributes.

@param $variables
  An associative array containing:
  - element: An associative array describing the tag:
    - #tag: The tag name to output. Typical tags added to the HTML HEAD:
      - meta: To provide meta information, such as a page refresh.
      - link: To refer to stylesheets and other contextual information.
      - script: To load JavaScript.
    - #attributes: (optional) An array of HTML attributes to apply to the
      tag.
    - #value: (optional) A string containing tag content, such as inline
      CSS.
    - #value_prefix: (optional) A string to prepend to #value, e.g. a CDATA
      wrapper prefix.
    - #value_suffix: (optional) A string to append to #value, e.g. a CDATA
      wrapper suffix.
```

## Code

```php
function theme_html_tag($variables) {
  $element = $variables['element'];
  $attributes = isset($element['#attributes']) ? drupal_attributes($element['#attributes']) : '';
  if (!isset($element['#value'])) {
    return '<' . $element['#tag'] . $attributes . " />\n";
  }
  else {
    $output = '<' . $element['#tag'] . $attributes . '>';
    if (isset($element['#value_prefix'])) {
      $output .= $element['#value_prefix'];
    }
    $output .= $element['#value'];
    if (isset($element['#value_suffix'])) {
      $output .= $element['#value_suffix'];
    }
    $output .= '</' . $element['#tag'] . ">\n";
    return $output;
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
