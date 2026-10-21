# show()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6384–6387 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6384-L6387)

## Signature

```php
function show(&$element)
```

## Documentation

```text
Shows a hidden element for later rendering.

You can also use render($element), which shows the element while rendering
it.

The first time render() or drupal_render() is called on an element tree,
as each element in the tree is rendered, it is marked with a #printed flag
and the rendered children of the element are cached. Subsequent calls to
render() or drupal_render() will not traverse the child tree of this element
again: they will just use the cached children. So if you want to show an
element, be sure to call show() on the element before its parent tree is
rendered for the first time, as it will have no effect on subsequent
renderings of the parent tree.

@param $element
  The element to be shown.

@return
  The element.

@see render()
@see hide()
```

## Code

```php
function show(&$element) {
  $element['#printed'] = FALSE;
  return $element;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
