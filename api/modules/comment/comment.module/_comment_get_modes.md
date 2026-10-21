# _comment_get_modes()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2435–2440 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2435-L2440)
- **Module/theme:** comment

## Signature

```php
function _comment_get_modes()
```

## Documentation

```text
Return an array of viewing modes for comment listings.

We can't use a global variable array because the locale system
is not initialized yet when the comment module is loaded.
```

## Code

```php
function _comment_get_modes() {
  return array(
    COMMENT_MODE_FLAT => t('Flat list'),
    COMMENT_MODE_THREADED => t('Threaded list')
  );
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
