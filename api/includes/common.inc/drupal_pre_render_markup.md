# drupal_pre_render_markup()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6040–6043 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6040-L6043)

## Signature

```php
function drupal_pre_render_markup($elements)
```

## Documentation

```text
#pre_render callback to append contents in #markup to #children.

This needs to be a #pre_render callback, because eventually assigned
#theme_wrappers will expect the element's rendered content in #children.
Note that if also a #theme is defined for the element, then the result of
the theme callback will override #children.

@param $elements
  A structured array using the #markup key.

@return
  The passed-in elements, but #markup appended to #children.

@see drupal_render()
```

## Code

```php
function drupal_pre_render_markup($elements) {
  $elements['#children'] = $elements['#markup'];
  return $elements;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
