# _comment_per_page()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2446–2448 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2446-L2448)
- **Module/theme:** comment

## Signature

```php
function _comment_per_page()
```

## Documentation

```text
Return an array of "comments per page" settings from which the user
can choose.
```

## Code

```php
function _comment_per_page() {
  return drupal_map_assoc(array(10, 30, 50, 70, 90, 150, 200, 250, 300));
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
