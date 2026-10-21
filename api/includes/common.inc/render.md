# render()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6322–6332 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6322-L6332)

## Signature

```php
function render(&$element)
```

## Documentation

```text
Renders an element.

This function renders an element using drupal_render(). The top level
element is shown with show() before rendering, so it will always be rendered
even if hide() had been previously used on it.

@param $element
  The element to be rendered.

@return
  The rendered element.

@see drupal_render()
@see show()
@see hide()
```

## Code

```php
function render(&$element) {
  if (is_array($element)) {
    show($element);
    return drupal_render($element);
  }
  else {
    // Safe-guard for inappropriate use of render() on flat variables: return
    // the variable as-is.
    return $element;
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
