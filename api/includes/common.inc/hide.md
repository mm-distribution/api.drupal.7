# hide()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6355–6358 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6355-L6358)

## Signature

```php
function hide(&$element)
```

## Documentation

```text
Hides an element from later rendering.

The first time render() or drupal_render() is called on an element tree,
as each element in the tree is rendered, it is marked with a #printed flag
and the rendered children of the element are cached. Subsequent calls to
render() or drupal_render() will not traverse the child tree of this element
again: they will just use the cached children. So if you want to hide an
element, be sure to call hide() on the element before its parent tree is
rendered for the first time, as it will have no effect on subsequent
renderings of the parent tree.

@param $element
  The element to be hidden.

@return
  The element.

@see render()
@see show()
```

## Code

```php
function hide(&$element) {
  $element['#printed'] = TRUE;
  return $element;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
