# _tracker_user_access()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 166–168 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L166-L168)
- **Module/theme:** tracker

## Signature

```php
function _tracker_user_access($account)
```

## Documentation

```text
Access callback for user/%user/track.
```

## Code

```php
function _tracker_user_access($account) {
  return user_view_access($account) && user_access('access content');
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
