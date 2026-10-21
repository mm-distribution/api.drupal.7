# theme_link()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1738–1740 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1738-L1740)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_link($variables)
```

## Documentation

```text
Returns HTML for a link.

All Drupal code that outputs a link should call the l() function. That
function performs some initial preprocessing, and then, if necessary, calls
theme('link') for rendering the anchor tag.

To optimize performance for sites that don't need custom theming of links,
the l() function includes an inline copy of this function, and uses that
copy if none of the enabled modules or the active theme implement any
preprocess or process functions or override this theme implementation.

@param array $variables
  An associative array containing the keys:
  - text: The text of the link.
  - path: The internal path or external URL being linked to. It is used as
    the $path parameter of the url() function.
  - options: (optional) An array that defaults to empty, but can contain:
    - attributes: Can contain optional attributes:
      - class: must be declared in an array. Example: 'class' =>
        array('class_name1','class_name2').
      - title: must be a string. Example: 'title' => 'Example title'
      - Others are more flexible as long as they work with
        drupal_attributes($variables['options']['attributes]).
    - html: Boolean flag that tells whether text contains HTML or plain
      text. If set to TRUE, the text value will not be sanitized so the
      calling function must ensure that it already contains safe HTML.
  The elements $variables['options']['attributes'] and
  $variables['options']['html'] are used in this function similarly to the
  way that $options['attributes'] and $options['html'] are used in l().
  The link itself is built by the url() function, which takes
  $variables['path'] and $variables['options'] as arguments.

@see l()
@see url()
```

## Code

```php
function theme_link($variables) {
  return '<a href="' . check_plain(url($variables['path'], $variables['options'])) . '"' . drupal_attributes($variables['options']['attributes']) . '>' . ($variables['options']['html'] ? $variables['text'] : check_plain($variables['text'])) . '</a>';
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
