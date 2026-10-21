# forum_uri()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 240–244 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L240-L244)
- **Module/theme:** forum

## Signature

```php
function forum_uri($forum)
```

## Documentation

```text
Implements callback_entity_info_uri().

Entity URI callback used in forum_entity_info_alter().
```

## Code

```php
function forum_uri($forum) {
  return array(
    'path' => 'forum/' . $forum->tid,
  );
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
