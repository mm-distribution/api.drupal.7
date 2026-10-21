# theme_forum_form()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 134–136 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L134-L136)
- **Module/theme:** forum
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_forum_form($variables)
```

## Documentation

```text
Returns HTML for a forum form.

By default this does not alter the appearance of a form at all, but is
provided as a convenience for themers.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_forum_form($variables) {
  return drupal_render_children($variables['form']);
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
